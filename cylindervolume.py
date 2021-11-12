import math
Height = eval(input('Enter the height: '))
Diameter = eval(input('Enter the Diameter: '))
Volume = ((math.pi*(Diameter/2))**2)*Height
VolumeL=Volume/1000
print(Volume,'Cm\u00b3\n',VolumeL,'L')
