import sys, time

# for i in xrange(0, 101, 10):
#     print '\r>> You have finished %d%%' % i,
#     sys.stdout.flush()
#     time.sleep(2)
# print


class Fib:


    '''iterator that yields numbers in the Fibonacci sequence'''


def __init__(self, max):
    self.max = max


def __iter__(self):
    self.a = 0
    self.b = 1
    return self


def __next__(self):
    fib = self.a
    if fib > self.max:
        raise StopIteration
    self.a, self.b = self.b, self.a + self.b
    return fib


l = []
print len(l)
l.append(None)
print len(l)
print l
