from pythonping import ping, icmp
import sys

hostname = str(sys.argv[1])
count = int(str(sys.argv[2]))
if len(sys.argv) > 3 :
    verbose = bool(sys.argv[3])
else:
    verbose = False

test = ping(hostname, verbose=verbose, count=count)