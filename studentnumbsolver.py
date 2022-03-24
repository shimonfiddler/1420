import serial 
from time import sleep
studentnumb = 'M00713267'
Arduino = serial.Serial('/dev/ttyACM0')
sleep(2)
Arduino.write(studentnumb)
print(studentnumb)
returndata = Arduino.readline()
print(returndata)
offset = returndata[23:25]
offset = int(offset)
print(offset)
for i in range(8):
	j = i+27
	#print(returndata[j])
	chrdec = ord(returndata[j])
	chrdec = chrdec + offset
	chrenc = chr(chrdec)
	print(chrenc)

