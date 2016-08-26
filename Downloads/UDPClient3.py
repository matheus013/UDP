import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
print "[+] New socket created\n"
print " - Target IP::", UDP_IP
print " - Target Port:", UDP_PORT

while True:
    MESSAGE = raw_input('\nInput Message:')

    if "/quit" in MESSAGE:
        break

    if MESSAGE == "LOOPTEST":
        while True:
            sock.sendto("LOOPTEST", (UDP_IP, UDP_PORT))
            modifiedMessage, serverAddress = sock.recvfrom(2048)
            print "[Server]: ", modifiedMessage

    if MESSAGE == "SPAMTEST":
        count = 0
        while MESSAGE == "SPAMTEST" and count < 100000:
            sock.sendto(str(count), (UDP_IP, UDP_PORT))
            modifiedMessage, serverAddress = sock.recvfrom(2048)
            print "[Server]: ", modifiedMessage
            count += 1
            if count == 100000:
                MESSAGE = raw_input("Input Message:")
                count = 0

    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    modifiedMessage, serverAddress = sock.recvfrom(2048)
    print "[Server]: ",  modifiedMessage