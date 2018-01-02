'''
Nov. 13 2017
Jamal Galette
'''
from socket import *
from random import *
serverport = 54054
servername = 'localhost'

serversocket = socket()
serversocket.bind(('',serverport))
serversocket.listen(3)
conn, addr = serversocket.accept()

while True:
    data=conn.recv(1024)
    try:
        number = data.strip()[-1]
        txt = data[:-1]
    except:
        print("Nothing recieved, closing connection...")
        serversocket.close()
    print("Receiver message confirmed: " + txt + " " + number)
    print("(1) Working ACK; (2) Corrupted ACK; (3) Send ACK; (4) Invalid ACK")
    option = randint(1,4)
    if option == 1:
        print("Receiver correctly responds with ACK " +number)
    if option == 2:
        print ("Error corrupted ACK recieved")
        
        try:
            conn.send(number + str(option))
            data=conn.recv(1024)
            number = data.strip()[-1]
            expectedseq = data.strip()[-1]
            txt = data[:-1]
        except:
            print("Nothing recieved, closing connection...")
            serversocket.close()
            break
        print ("Receiver got a duplicated txt: " + txt +" " + number)
    if option == 3:
        print("Receiver send no ACK")
        
        try:
            conn.send(number + str(option))
            number = data.strip()[-1]
            expectedseq = data.strip()[-1]
            txt = data[:-1]
        except:
            print("The Server did not receive anything, closing connection...")
            serversocket.close()
            break
        print("Receiver correctly responds with a duplicated txt: " + txt + " " + number)
    if option == 4:
        origninalseq =number
        if number == '0':
            newnumber = '1'
        if number =='1':
            newnumber = '0'
        number = newnumber
        print ("receiver incorrectly responds with Ack " + number)
        try:
            conn.send(number + str(option))
            number = data.strip()[-1]
            expectedseq = data.strip()[-1]
            txt = data[:-1]
        except:
            print("Nothing recieved, closing connection...")
            serversocket.close()
            break
        print ("Receiver correctly responds with a duplicated txt:" + txt + " " + number)
        print("Receiver responds with ACK " + origninalseq)
    try:
        conn.send(number + str(option))
    except:
        print ("Timer ran out...Closing Connection ...")
        serversocket.close()
        break;
    
    
