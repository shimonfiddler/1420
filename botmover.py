import socket
from time import sleep, time

HOST = '127.0.0.1'  
PORT = 50007         

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('working')
    
def linemove(timedelay):
    conn.send(bytes('10,10','utf-8'))
    sleep(timedelay)
    conn.send(bytes('0,0','utf-8'))
    return

def curve(direction,timedelay):
    print(direction)
    if direction == 'L' or 'l':
        conn.send(bytes('10,0','utf-8'))
        sleep(timedelay)
        conn.send(bytes('0,0','utf-8'))
    elif direction == 'R' or 'r':
        conn.send(bytes('10,10','utf-8'))
        sleep(timedelay)
        conn.send(bytes('0,0','utf-8'))
    return

while True:
    direction = str(input('Input the direction: '))
    timedelay = int(input('Input the time in secconds the bot moves forward for: '))
    #linemove(timedelay)
    curve(direction,timedelay)