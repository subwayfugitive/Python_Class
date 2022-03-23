two_or_less = 1.50
two_less_six = 3.00
six_less_ten = 4.00
over_ten = 4.75


def main():
    #quick description of what the program does
    print("This program will calculate the shipping charges based on a package weight entered by the user")

    linebreak()

    #this is an instruction for how the program works, I saved it as a var that i can use later
    msg = "To exit the program, enter a weight of 0, or a negative weight"

    print(msg)

    #take input from user
    user_input = float(input("To calculate the shipping charges, enter the weight in lbs: "))

    #here we set up the program to run indefinely untill the user wants to stop
    while user_input > 0:
        #calculate the cost of shippping using the func we made earlier 
        final_cost = ship_calc(user_input)
        linebreak()
        print(f'Your shipping charges for {user_input} lbs is {final_cost:.02f} dollars.')
        linebreak()
        print(msg)
        user_input = float(input("To calculate the shipping charges, enter the weight in lbs: "))
    else:
        #display a message when the user is done
        linebreak()
        print("Thank you for using this shipping calculator")

#calculate func 
def ship_calc(calc):
    how_much = calc
    if how_much > 10:
        return how_much * over_ten
    if how_much > 6 and how_much <= 10:
        return how_much * six_less_ten
    if how_much > 2 and how_much <= 6:
        return how_much * two_less_six
    if how_much <= 2:
        return how_much * two_or_less

#simple line break to make output more readable
def linebreak():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == '__main__':
    main()