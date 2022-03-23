#Thomas Powell Horan
#population calculator
def main():
    #line break to make code more readable
    def line_break():
        print("###########################")

    #messages displayed to the user saved as global variables so I can easily re use them later
    msg_1 = "Enter the starting size of a population of organisms: "
    msg_2 = "Enter the average daily population increase (as a percentage): "
    msg_3 = "Enter the number of days the organisms will be left to multiply: "
    goodbye_msg = ("*** Thank you for using this population calculator ***")
    error_msg = "*** ERROR please type a number next time or type 0 to exit ***"

    #quick description of what the program does and how to use it
    print("This program will calculate the aproximate size of a population of organisms")

    #this checks the input to make sure it is not a string or the exit code "0"
    def valid_check(msg):
        msg = msg
        while True:
            try:
                check = int(input(f"{msg}"))
                if check <= 0: #checks if the user is trying to leave the program
                    print(goodbye_msg)
                    quit()
                if check * 0 == 0:# this checks if the input is a number because n * 0 is allways equal to 0
                    return check
            except ValueError:# allows the program to work even with a bad input
                print(error_msg)#promts the user to try again
                pass


    #start_pop = int(input(f'{msg_1}'))

    #this is used for formating the outputs to make them look nice
    width = 10
    padding = ""


    #this loop allows the program to run untill the user stops it.
    while True:
        print("When done, enter 0 or a negative number for any of the inputs.")
        start_pop = valid_check(msg_1)

        daily_inc = valid_check(msg_2)

        days = valid_check(msg_3)
        line_break()
        print(f'{"DAY":{padding}<{width}}{"POPULATION"}')
        for dias in range(1, days+1):
            if dias == 1:
                print(f'{dias:{padding}<{width}}{start_pop:.7f}')
                continue
            start_pop = start_pop * (daily_inc/100) + start_pop
            print(f'{dias:{padding}<{width}}{start_pop:.7f}')
        line_break()

if __name__ == '__main__':
     main()
