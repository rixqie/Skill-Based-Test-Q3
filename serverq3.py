import random
import threading
import socket

quotes = ["“Do not go gentle into that good night” \n By Dylan Thomas", 
        "“Everybody is going to be dead one day,just give them time” \n By Neil Gaiman",
        "“The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time” \n By Mark Twain",
        "“I needed to put two critical ideas together: that I could both be mentally ill and lead a rich and satisfying life” \n By Elyn R.Saks",
        "“I have not failed. I’ve just found 10,000 ways that won’t work” \n By Thomas Alva Edison",
        "“I didn't want to wake up. I was having a much better time asleep. And that's really sad. It was almost like a reverse nightmare,like when you wake up from a nightmare you're so relieved. I woke up into a nightmare.” \n By Ned Vizzini"]
def function_quote(csocket):
    quote = random.choice(quotes)
    csocket.sendall(quote.encode())
    csocket.close()

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 8888))

    s.listen(5)
    print("[*] Listening on %s:%d for request" % ("127.0.0.1", 8888))

    while True:
        c, address = s.accept()
        print("[*] Accepted connection from %s" % str(address))
        cHandler = threading.Thread(target=function_quote, args=(c,))
        cHandler.start()
        
main()