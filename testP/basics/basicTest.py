

import sys, time

for i in xrange(0, 101, 10):
  print '\r>> You have finished %d%%' % i,
  sys.stdout.flush()
  time.sleep(2)
print