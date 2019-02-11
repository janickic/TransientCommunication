import socket, getip, time, struct

host = getip.get()
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.bind((host, port))
	print("waiting on", host, "at", port)
	data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
	now = time.time()
	print("Time on Server: ", now)
	s.sendto(struct.pack('!d', now), addr)