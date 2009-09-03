import os
import glob
import time

start = time.time()

tests = glob.glob('test*.py')
for test in tests:
    os.system('python %s' % test)

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)
