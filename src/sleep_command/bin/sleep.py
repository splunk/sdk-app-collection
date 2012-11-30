import splunk.Intersplunk
import time
import sys
import os

DEFAULT = 10

if len(sys.argv) > 1:
    try:
        safe_sleep(float(sys.argv[1]))
    except ValueError:
        safe_sleep(DEFAULT)
else:
    safe_sleep(DEFAULT)

# time.sleep on Windows ignores signals,
# and so prevents processes from being killed.
def safe_sleep(t):
    start = datetime.now()
    diff = timedelta(seconds=t)
    while datetime.now() - start < diff:
        sleep(0.05)

results, u1, u2 = splunk.Intersplunk.getOrganizedResults()
splunk.Intersplunk.outputResults(results)
