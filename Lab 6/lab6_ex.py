months_list  = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
user_date = tuple(input("enter a date in mm/dd/yyyy format ").split("/"))

month=int(user_date[0])-1
day=int(user_date[1])
year=int(user_date[2])

month_len = len(user_date[0])
day_len = len(user_date[1])
year_len =len(user_date[2])

if month <= 11 and month >= 0 and month_len <= 2:
    if day < 32 and day > 0 and day_len <= 2:
        if year < 10000 and year > 0 and year_len <= 4:
            print(f'Valid date: {months_list[month]} {day}, {year}')
        else:
            print("Invaild year")
    else:
        print("Invaid Day")
else:
    print("invald month")


