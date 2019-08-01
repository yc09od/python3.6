from pythonping import ping, icmp


test = ping('10.1.112.1', verbose=True, count=10)

print(test.rtt_avg_ms == 2000)