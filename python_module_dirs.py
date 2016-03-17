#!/usr/bin/env python

#
# Print a list of paths that contain python modules on this system.
#

import sys

print '=-' * 32

for dir in sys.path:
    print "  " + dir

print '=-' * 32
