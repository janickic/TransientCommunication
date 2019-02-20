import zmq, sys, time

# Check IP of server
if len(sys.argv) < 2:
    print("Please insert IP of server")
    sys.exit()
ip = sys.argv[1]
print 'Server ip:', ip

port = "5556"

# zmq Prepare context and socket
context = zmq.Context()
# Create REQ (request) socket connection
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:%s" % (ip, port))

# Get time before remote call
start = time.time()
# Call the remote server
socket.send(b"get server time")
serverTime = float(socket.recv())
# Get time after remote call
end = time.time()

# Calculate rtt
rtt = (end - start) / 2
updatedTime = serverTime + rtt
# Output results
print "Server time:\t", serverTime
print "RTT:\t\t", rtt
print "Updated time:\t", updatedTime