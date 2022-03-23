def main():

    #line break to make code more readable
    def line_break():
        print("###########################")
    
    def validcheck(check):
        check = check
        if check <= 0:
            print("*** Thank you for using this population calculator ***")
            quit()
        else:
            pass
    
     
    print("This program will calculate the aproximate size of a population of organisms")

    while True:
        #this is used for formating the outputs to make them look nice
        width = 10
        padding = ""

        print("When done, enter 0 or a negative number for any of the inputs.")

        start_pop = int(input(f"Enter the starting size of a population of organisms: "))
        validcheck(start_pop)

        daily_inc = float(input(f'Enter the average daily population increase (as a percentage): '))
        validcheck(daily_inc)

        days = int(input(f'Enter the number of days the organisms will be left to multiply: '))
        validcheck(days)

        line_break()
        print(f'{"DAY":{padding}<{width}}{"POPULATION"}')
        for dias in range(1, days+1):
            if dias == 1:
                print(f'{dias:{padding}<{width}}{start_pop:.7g}')
                continue
            start_pop = start_pop * (daily_inc/100) + start_pop
            print(f'{dias:{padding}<{width}}{start_pop:.7g}')
        line_break()

if __name__ == '__main__':
     main()



    
    
