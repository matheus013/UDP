import socket, datetime

UDP_IP = ''  # "127.0.0.1"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

log = []

print "\n[+] New server socket created\n"

f = open('/home/glins/Downloads/serverlog.txt', 'w')

while True:
    data, (ip, port) = sock.recvfrom(1024)  # buffer size is 1024 bytes
    if data == "SAVELOG":
        for item in log:
            f.write("\n".join(map(lambda x: str(x), log)) + "\n")
        f.close()

    print "Received addr:", (ip, port)
    log.append("["+datetime.datetime.now().time().__str__()+"] Message:" + data + " IP:"+ip)

    #  modifiedMessage = data.upper()
    sock.sendto("seus lixos absolutos", (ip, port))
    #  print "Sent message:", modifiedMessage
