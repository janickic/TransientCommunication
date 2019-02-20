import zmq, time

port = "8081"

# Create REQ (request) socket connection
context = zmq.Context()
# Create PUB (publish) socket connection
socket = context.socket(zmq.PUB)
print "starting server ..."
# Bind socket to port
socket.bind("tcp://*:%s" % port)


while True:
    # Keep publishing current time
    message = socket.send(str(time.time()))