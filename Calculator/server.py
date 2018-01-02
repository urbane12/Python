#coding: utf-8 -*-
# Jamal Galette
# Prog Assignment 1
#Python UDP Server
import socket
import sys

from socket import *
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
#serverSocket.listen(1)
print "The Server is ready to receive"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)

    if message == "0/0":
        break
    else:
        message = message.split(" ")

    i=0
    while i<3:
        if i!=1:
            message[i] = float(message[i])
            i+=1
        else:
            i+=1
    if message[1] == '+':
        final = (message[0] + message[2])
        print "Recieved question ", message
        print "Send back answer ", final
        serverSocket.sendto(str(final), clientAddress)


    elif message[1] == '-':
        final = (message[0] - message[2])
        print "Recieved question ", message
        print "Send back answer ", final
        serverSocket.sendto(str(final), clientAddress)

    elif message[1] == '*':
        final = (message[0] * message[2])
        print "Recieved question ", message
        print "Send back answer ", final
        serverSocket.sendto(str(final), clientAddress)

    elif message[1] == '/':
        final = (message[0] / message[2])
        print "Recieved question ", message
        print "Send back answer ", final
        serverSocket.sendto(str(final), clientAddress)

    else:
        print("Enter a valid input")


serverSocket.close()
