import serial 
from time import sleep
studentnumb = 'M00713267'
Arduino = serial.Serial('/dev/ttyACM0')
sleep(2)
Arduino.write(studentnumb)
#print(studentnumb)
returndata = Arduino.readline()
print(returndata)
offset = returndata.split('*')
#offset = returndata[23:25] breaks with 1 digit codes
offset = offset[1]
offset = int(offset)
encmsg = returndata.split('*')
encmsg = encmsg[2]
encmsg.strip(' ')
#print(offset)
result = ''
for i in range(1,len(encmsg)-2):
	#j = i+27 #works with 2 digit codes
	#print(returndata[j])
	#chrdec = ord(returndata[j])
	chrdec = ord(encmsg[i])
	chrdec = chrdec + offset
	chrenc = chr(chrdec)
	#print(chrenc)
	result= result + chrenc
print(result)
