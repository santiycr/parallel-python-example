from subprocess import Popen
import glob
import time

start = time.time()

tests = glob.glob('testF*.py')
processes = []
for test in tests:
    processes.append(Popen('python %s' % test, shell=True))

for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)
