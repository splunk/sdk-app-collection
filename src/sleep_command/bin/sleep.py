import splunk.Intersplunk
import sys
import os

from time import sleep
from datetime import datetime, timedelta

DEFAULT = 10

# time.sleep on Windows ignores signals,
# and so prevents processes from being killed.
def safe_sleep(t):
    start = datetime.now()
    diff = timedelta(seconds=t)
    while datetime.now() - start < diff:
        sleep(0.05)


if len(sys.argv) > 1:
    try:
        safe_sleep(float(sys.argv[1]))
    except ValueError:
        safe_sleep(DEFAULT)
else:
    safe_sleep(DEFAULT)


results, u1, u2 = splunk.Intersplunk.getOrganizedResults()
splunk.Intersplunk.outputResults(results)
