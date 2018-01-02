# -*- coding: utf-8 -*-
# Jamal Galette
# Prog Assignment 1
#Python UDP Client
import socket
import sys
from socket import *
serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.connect((serverName, serverPort))

while 1:
    message = raw_input('Enter your math equation: ')
    clientSocket.sendto(message,(serverName, serverPort))
    messageRes, serverAddress = clientSocket.recvfrom(2048)

    print "Calculated output = ", messageRes
if message == "0/0":
    clientSocket.close()
