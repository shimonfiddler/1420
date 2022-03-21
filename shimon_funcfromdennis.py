import socket
from time import sleep

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

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

prev_vals = [0,0] # initialize a proper structure for values;
gap = 360 # example threshold for movement - this is how many encoder ticks the wheels will move for.

def forward(distance):
	current_vals = listen()
	goal = current_vals[0] + distance
	while current_vals[0] <= goal:
		conn.send(bytes("-10,-10", 'utf-8'))
		current_vals = listen()
		print(current_vals)
	conn.send(bytes("0,0", 'utf-8')) # stop the robot

def strait(mag,direction): #direction +1 or -1
    current = listen()
    target = current[0]+mag*direction
    while True:
        current = listen()
        print(current,target)
        if current[0]<= target and direction == +1 or current[0]>= target and direction == -1:
            #print(f'{direction*-10},{direction*-10}')
            speed = -10*direction #the multiplication seems to be the issue.
            # Processing would throw an error having read '0-10' for the speed.
            conn.send(bytes(f'{-10*direction},{-10*direction}','utf-8'))
        else:
            conn.send(bytes('0,0','utf-8'))
            return


while True: # keep everything looping, as if running on a microcontroller
	strait(100, 1)
	sleep(2)
	strait(100, -1)
	sleep(2)