#!python

import datetime
import time

def timestamp():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    for i in range(80):
        print timestamp() + " The random number is still 42"
        time.sleep(1)
