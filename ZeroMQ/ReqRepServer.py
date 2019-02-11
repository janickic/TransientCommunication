import zmq, time

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.REP)
print "starting server ..."
# socket.connect("tcp://localhost:5560")
socket.bind("tcp://*:%s" % port)


while True:
    message = socket.recv()
    print "Received request: ", message
    now = time.time()

    socket.send(str(now))
