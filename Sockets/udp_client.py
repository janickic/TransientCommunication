import socket, sys, time, struct

# Check IP of server
if len(sys.argv) < 2:
    print("Please insert IP of server")
    sys.exit()
host = sys.argv[1]
port = 65432
print('Server ip:', host)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((host, port))
    start = time.time()
    s.sendto(b'Get time', (host, port))
    data, addr = s.recvfrom(1024)
    end = time.time()
    rtt = (end - start)/2
    [server_time] = struct.unpack('!d', data)

updated_time = server_time + rtt
print('Estimated delay', rtt)
print('Updated time', updated_time)