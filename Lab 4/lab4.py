#global constants for seat price
ClassA = 20
ClassB = 15
ClassC = 10

#here is a function that makes the code look nicer by seperating the output from the users input in the command line (makes it more readable)
# I made it a function so i could call it mulitiple times in the progam to 
def line_break():
     print('------------------------------------------')

#description of what the program will do
print('This program claculates the income generated from ticket sales.')

line_break()

#define main function
def main():
     #here we are letting the user know how much each seat costs and that there are different categories of seats
     print(f'Class A seats cost ${ClassA}')
     print(f'Class B seats cost ${ClassB}')
     print(f'Class C seats cost ${ClassC}')

     line_break()

     #here we are using the "get_seats" func to store the users input as intergers for the differnt types of seat. 
     tier_1 = get_seats("Class A")
     tier_2 = get_seats("Class B")
     tier_3 = get_seats("Class C")

     line_break()

     total_sales(tier_1,tier_2,tier_3)
     

#this function requres input from the user. It will ask for the number of tickets sold per class then return the input to the varible that calls it.
def get_seats(seat_type):
     number_seats = int(input(f"How many seats of {seat_type} were sold?: "))
     #this while loop validates the input(cannot have a nuber less than zero beacause one cannot sell a negative number of seats)
     while number_seats < 0:
          number_seats = int(input(f"How many seats of {seat_type} were sold?: "))
     else:
          return number_seats
          
     
#caluclates the total income from ticket sales and stores it in the variable "gross" then prints it out.
def total_sales(a,b,c):
     seat_a = a
     seat_b = b
     seat_c = c
     gross = (a* ClassA) + (b* ClassB) + (c* ClassC)
     print(f'The total income generated from ticket sales is ${gross}')
     
if __name__ == '__main__':
     main()

