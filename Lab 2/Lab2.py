#Roman Numeral Converter
#Thomas Powell Horan 2/23/21

#Description of what the program does and require input
print('This program will convert any interger between 1 and 10 into roman numerals')
user_number = int(input("Please enter the number that you wish to convert ")) 
#I saved the input as an interger so that I can easily use the correct the logical and mathematical operations to set up the condional statements for the loops
                                                                                
#here is a list of all the possible outputs for the program
roman_numerals = ("I","II","III","IV","V","VI","VII","VII","IX","X")

#following are the loops that make the program work 1st check if ths input is in range, then print the correct Roman numeral associated with the input
if user_number <= 0:
    print("This Number is out of range")#This makes sure that the user inputed number is larger than 0
if user_number >= 11:
    print("This Number is out of range")#This makes sure that the user inputed number is smaller than 11
elif user_number == user_number:  
    print(f'The Roman numeral for {user_number} is: {roman_numerals[(user_number-1)]}')

#the output of this program is acheived by printing a numeral from our list
#the index of the string that gets printed is calucalted by subtracting 1 from the user input variable sice our list starts at index 0 "I", 1 "II",3 "III" etc.   
