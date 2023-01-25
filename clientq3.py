import socket

def main():
   
    csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csocket.connect(("127.0.0.1", 8888))

    quote = csocket.recv(1024)
    print("Quotes Of The Day! : \n %s" % quote.decode())

    csocket.close()

main()