'''
Nov 13 2017
Jamal Galette
'''
from socket import*
import datetime


data = ["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]
rdt_timer= 10000
servername ='localhost'
serverPort = 54054
clientSocket = socket()
clientSocket.connect(('localhost',serverPort))
clientSocket.settimeout(.2)
number="0"
time=0
i=0
starttime= datetime.datetime.now()
while time<rdt_timer:
    i = i%7
    clientSocket.send(data[i]+number)
    print("Sender sent a txt: " + data[i] + " " + number)
    while 1:
        case =0
        endtime=datetime.datetime.now()
        time = (endtime-starttime).microseconds
        try:
            
            newdata= clientSocket.recv(2048)
            case= int(newdata[1])
            recnumber = newdata[0]
            
        except timeout:
            print ('Still Waiting...')
            continue
        if case == 1:
            print("Sender received valid ACK of " + recnumber +" send next txt")
            if number =='0':
                newnumber ='1'
            elif number == '1':
                newnumber = '0'
            number = newnumber
            i=i+1
            break
        elif case == 2:
            print("Sender says nothing recieved, send nothing")
            break
        elif case ==3:
            print(" Sender has a corrupted ACK, more waiting")
            break
        elif case == 4:
            print("Sender received wrong ACK, even more waiting ")
            break
clientSocket.close()
        


