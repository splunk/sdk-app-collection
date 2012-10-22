"""
sleep.py - Sleep command for use in the SDK test suites.

Testing job-related code in the SDKs often requires capturing
a job before it has reached ready or done. The sleep command
inserts fixed amounts of time into both the phase before ready
(by delaying the getinfo probe) and the phase before done (by
delaying the return of events).

Its syntax is::

    sleep [x|done=x] [ready=y]

where x and y are real numbers. This inserts y seconds before
ready and x seconds before done. Both arguments are optional.
If either is omitted, no additional time is inserted into that
phase.

NOTE: I have not confirmed that ready actually injects time
before the job is ready.
"""
import sys
import time
import traceback
import splunk.Intersplunk as I

def float_or_error(value, message):
    """Read a real number from *value* or send Splunk an error.
    
    *message* is the error to be sent to Splunk. If it contains
    ``%s``, then *value* will be interpolated into it before
    being sent to Splunk.

    :param value: Value to try reading a real number from.
    :type value: ``str``
    :param message: Error message to send to Splunk if parsing fails.
    :type message: ``str``

    **Examples**::

        float_or_error("4.3", "Parsing failed!")
        # returns 4.3
        float_or_error("boris", "Bad machine, bad: %s")
        # Send "Bad machine, bad: boris" to Splunk and
        # terminates the script.
    """
    try:
        return float(value)
    except ValueError:
        if "%s" in message:
            I.parseError(message % value)
        else:
            I.parseError(message)

def parse_arguments(args, kwargs):
    """Extract both sleep times from arguments to the script.

    If the arguments are invalid, sends a parse error to Splunk
    and terminates the script. Otherwise returns a dictionary::

        {'done': x, 'ready': y}

    where ``x`` and ``y`` are real numbers (or ``None``) giving the
    time to sleep in each phase. ``None`` should be taken as 0.
    """
    sleep_before_done = None
    sleep_before_ready = None
    if 'ready' in kwargs:
        sleep_before_ready = float_or_error(
            kwargs.pop('ready'),
            "Argument to ready must be a real number; found %s")
    if 'done' in kwargs:
        sleep_before_done = float_or_error(
            kwargs.pop('done'),
            "Argument to done must be a real number; found %s")
    if len(args) > 0:
        if sleep_before_done is not None:
            I.parseError("Cannot provide both a non-keyword sleep time and argument to done.")
        elif len(args) > 1:
            I.parseError("sleep takes at most one non-keyword argument.")
        else:
            sleep_before_done = float_or_error(
                args[0],
                "Time to sleep must be real number; found %s")
    if len(kwargs) > 0:
        I.parseError("Unrecognized arguments: %s", ", ".join("%s=%s" % (k,v) for k,v in kwargs.iteritems()))
    return {'ready': sleep_before_ready, 'done': sleep_before_done}

def main():
    # Parse the arguments passed in
    (isgetinfo, sys.argv) = I.isGetInfo(sys.argv)
    args, kwargs = I.getKeywordsAndOptions()
    sleep_times = parse_arguments(args, kwargs)

    if isgetinfo:
        if sleep_times['ready'] is not None:
            time.sleep(sleep_times['ready'])
        # Tell Splunk that this is a sane search command.
        I.outputInfo(
            streaming=False,
            generating=False,
            retevs=True,
            reqsop=False,
            preop=None,
            timeorder=True)
    else:
        if sleep_times['done'] is not None:
            time.sleep(sleep_times['done'])
        # Pass on all the results unchanged.
        results, u1, u2 = I.getOrganizedResults()
        I.outputResults(results)

try:
    main()
except Exception, e:
    I.generateErrorResults(traceback.format_exc())
