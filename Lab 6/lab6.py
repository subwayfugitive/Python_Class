# Thomas Powell Horan Lab 6
# list of all the months

#default library that helps to check if a year is a leap year
from calendar import isleap

# list of months
months_list  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    user_date = tuple((x.strip())for x in input("please enter the date in mm/dd/yyyy format that you want to convert, include '/' to seperate month day and year ").split('/'))

    month = int(user_date[0])-1
    day = int(user_date[1])
    year = int(user_date[2])

    mm = len(user_date[0])
    dd = len(user_date[1])
    yy = len (user_date[2])

    correct_days = 0

    if month == 1 and day > 28 and isleap(year) == False:
        print(f'Invalid date, {year} is not a leap year, so {months_list[month]} only has 28 days!')
        correct_days +=1
    if month == 3 and day > 30:
        print(f'Invalid date, {months_list[month]} only has 30 days!')
        correct_days +=1
    if month == 5 and day > 30:
        print(f'Invalid date, {months_list[month]} only has 30 days!')
        correct_days +=1
    if month == 8 and day > 30:
        print(f'Invalid date, {months_list[month]} only has 30 days!')
        correct_days +=1
    if month == 10 and day > 30:
        print(f'Invalid date, {months_list[month]} only has 30 days!')
        correct_days +=1

    if correct_days <= 0:
        if month <= 11 and month >= 0 and mm == 2:
            if day < 32 and day > 0 and dd == 2:
                if year < 10000 and yy == 4:
                    print(f"Valid Date: {months_list[month]} {day}, {year}")
                else:
                    print("ERROR invalid year, please enter a year less than 10,0000 in YYYY format")
            else:
                print("ERROR invaild day, please enter a day lower than 32 and more than 0 in DD format") 
        else:
            print("ERROR invalid month, please enter a month 1-12 in MM format")

if __name__ == '__main__':
    main()