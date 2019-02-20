import zmq, time

port = "5556"

# zmq Prepare context and socket
context = zmq.Context()
# Create REP (reply) socket connection
socket = context.socket(zmq.REP)
print "starting server ..."
# socket.connect("tcp://localhost:5560")
socket.bind("tcp://*:%s" % port)


while True:
    # Return server time when socket request received
    message = socket.recv()
    print "Received request: ", message
    now = time.time()
    print "Time on server: ", now
    socket.send(str(now))
