import socket, datetime

UDP_IP = ''  # "127.0.0.1"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

log = []
clients = []

print "[+] New server socket created\n"
print " - Server Port:"+ str(UDP_PORT)

while True:
    data, (ip, port) = sock.recvfrom(1024)  # buffer size is 1024 bytes

    if (ip, port) not in clients:
        clients.append((ip, port))

    if data.find("SAVELOG")==0:
        with open("serverlogs.txt", "w")as fp:
            for line in log:
                fp.write(line + "\n")
        fp.close()
        sock.sendto("Saved server logs successfully.", (ip, port))
        continue

    if data.find("CLEARLOG")==0:
        del log[:]
        sock.sendto("Cleared server logs successfully.", (ip, port))
        continue

    if data.find("WHOAMI")==0:
        sock.sendto("Client " + (clients.index((ip, port))+1).__str__(), (ip, port))
        continue

    print "[" + ip + "] Sent: " + data
    log.append("["+datetime.datetime.now().time().__str__()+"] Message:" + data + "\n - [IP:"+ip + "] Client " + (clients.index((ip, port))+1).__str__())

    #  modifiedMessage = data.upper()
    sock.sendto("Received \"" + data + "\"", (ip, port))
    #  print "Sent message:", modifiedMessage
