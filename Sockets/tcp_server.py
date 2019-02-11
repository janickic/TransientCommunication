import socket, getip, time, struct

host = getip.get()
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print("waiting on", host, "at", port)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            now = time.time()
            print("Time on Server: ", now)
            conn.sendall(struct.pack('!d', now))