# Lab 6 /
# list of all the months

months_list  = ["February", "March", "May", "June", "August", "April", "September", "January", "October", "November", "December","July"]

def main():
    user_date = tuple((x.strip())for x in input("please enter the date in mm/dd/yyyy format that you want to convert, include '/' to seperate month day and year ").split('/'))

    month = int(user_date[0])
    day = int(user_date[1])
    year = int(user_date[2])

    mm = len(user_date[0])
    dd = len(user_date[1])
    yy = len (user_date[2])
 
    if month <= 11 and month >= 0 and mm == 2:
        if day < 28 and day > 0 and dd == 2:
            if year < 10000 and year > 0 and yy == 4:
                print('#########################')
            else:
                print("##############")
        else:
            print("#################") 
    else:
        print("#########################")

if __name__ == '__main__':
    main()