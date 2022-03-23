def main():
    
    def line_break():
        print("###########################")
    
    def valid(check):
        if check <= 0:
            start_pop == 0
    
    while start_pop > 0:
            #this is used for formating the outputs to make them look nice
            width = 10
            padding = ""

            print("When done, enter 0 or a negative number for any of the inputs.")

            start_pop = int(input(f"Enter the starting size of a population of organisms: "))
            valid(start_pop)
            

            daily_inc = float(input(f'Enter the average daily population increase (as a percentage): '))
            valid(daily_inc)
        

            days = int(input(f'Enter the number of days the organisms will be left to multiply: '))
            valid(days)

            



            line_break()
            print(f'{"DAY":{padding}<{width}}{"POPULATION"}')
            for dias in range(1, days+1):
                if dias == 1:
                    print(f'{dias:{padding}<{width}}{start_pop:.07f}')
                    continue
                start_pop = start_pop * (daily_inc/100) + start_pop
                print(f'{dias:{padding}<{width}}{start_pop:.07f}')
            line_break()

if __name__ == '__main__':
    main()