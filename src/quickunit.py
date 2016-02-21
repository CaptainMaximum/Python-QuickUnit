#!/usr/bin/python

import sys
import quickunitlib as quickunit

def quickunit_main():
    filename = sys.argv[1]
    modulename = ''.join(filename.split('.')[0:-1])
    modulename = '.'.join(modulename.split('/'))
    module = __import__(modulename)
    for test in quickunit.waitlist:
        test.test()
    quickunit.report()

if __name__ == "__main__":
    quickunit_main()

