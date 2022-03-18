import socket
from time import sleep, time

HOST = '127.0.0.1'  
PORT = 50007         

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('working')

def listen(): # produces encoder values for the wheels. returns right wheel value, left wheel value.
    buffer = ""
    while not buffer:
        data = conn.recv(1)
        if data == b'*':
            data = conn.recv(1)
            buffer += data.decode(encoding='utf-8')
            while data != b'*':
                data = conn.recv(1)
                buffer += data.decode(encoding='utf-8')
    x = buffer.split('*')
    if len(x) > 1:
        x = x[-2]
    buffer = ""
    raw_vals = [float(i) for i in x.split(',')]
    RWV = int(raw_vals[0]*153)
    LWV = int(raw_vals[1]*153)
    return RWV, LWV # returned as a tuple!

def strait(mag,direction): #direction +1 or -1
    current = listen()
    target = current[0]+mag*direction
    while True:
        current = listen()
        print(current,target)
        if current[0]<= target and direction == +1 or current[0]>= target and direction == '-1':
            #print(f'{direction*-10},{direction*-10}')
            conn.send(bytes(f'{direction*-10},{direction*-10}','utf-8'))
        else:
            conn.send(bytes('0,0','utf-8'))
            return

while True:
    strait(int(input('Distance to travel: ')),+1)#int(input('enter direction: '))

