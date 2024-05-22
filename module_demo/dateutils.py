
def is_leap_year(year):
    if  year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False

def days_in_month(month,year=1987):
    
    if month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30

def date_to_day(yy,mm,dd):
    w = week_day_number(yy,mm,dd)
    return day_name(2)


def date_value(yy,mm,dd):
    # find how many days passed till begining of current year yy
    py=yy-1

    dy= py*365 #approximately 365 days per year
    dy+= py//4 # every 4th year is a leap year. not // is int division
    dy-= py//100 # but every 100th year is not a leap year
    dy+= py//400 # but every 400th year is a leap year

    dm=0
    for m in range(1,mm): #excluding mm
        dm+=days_in_month(m,yy)

    return dy+dm+dd
    



def week_day_number(yy,mm,dd):
    ref_date_value = date_value(2001,1,1)
    value=date_value(yy,mm,dd)

    return (value-ref_date_value)%7

def month_name(month):
    months=("","Januaury","February","March","April","May","June","July","August", \
            "September","October","November","December","December")

    return months[month]

def day_name(day):

    days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    return days[day]

def print_calendar(year,month):
    
    print(f"{month_name(month)} {year}".center(49))
    for m in range(7):
        print(day_name(m)[:3].center(7),end="")
    print()
    print("-"*49)
    position= week_day_number(year,month,1)
    for spaces in range(position):
        print(' '*7,end='')

    for day in range(1, days_in_month(month,year)+1):
        print(f'{str(day).center(7)}',end='')
        position+=1
        if position==7:
            print()
            position=0

    print()
    print("-"*49)