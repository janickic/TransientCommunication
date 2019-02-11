import zmq, time

port = "8081"

context = zmq.Context()
socket = context.socket(zmq.PUB)
print "starting server ..."
socket.bind("tcp://*:%s" % port)


while True:
    message = socket.send(str(time.time()))