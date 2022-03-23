#Celsius to Fahrenheit Temperature Converter
#Thomas Powell Horan 2/19/21

#first a quick description of the program then we require input
#store the input as a floating point number 
print('This program can convert Celsius temperatures into Fahrenheit')
celsius =float(input('please enter the Celsius temperature that you wish to convert: '))

#use the formula to convert temperature
fahrenheit= celsius * 9/5 +32

#print the answer rounded to two decimal places
print(f'{celsius:.2f} degrees Celsius is: {fahrenheit:.2f} degress Farenheit')
