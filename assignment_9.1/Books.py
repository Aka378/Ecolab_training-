

def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30

def date_value(day ,month, year):
    value=0
    y=year-1
    # total days elapsed till the end of previous year
    value = y * 365 + y//4  - y//100 + y//400

    # add total days passed till previous month of this year
    m=1
    while m<month:
        #print(f'Adding {days_in_month(m,year)} for {m}/{year}')
        value+= days_in_month(m,year)
        m+=1

    #add days of this month
    value+=day
    return value

def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff


def print_calendar_horizontal(month,year):
    startDay=date_to_week_day(1,month,year)
    days=days_in_month(month,year)
    m=0
    n=0
    
    week=['Sun','Mon','Tue','wed','thu','fri','Sat']
    for i in range(7):
        print(week[i],end="\t")
        t=1
        
        if i< startDay:
            d=(7-startDay)+m
            print(" ", end="\t")
            for i in range(5):
             if d<days:
                print(d+1,end="\t")
                d+=7
            m=m+1    
        if i>=startDay:
            t=t+n
            for i in range(5):
             if t<=days:
              print(t,end="\t")
              t=t+7
            n=n+1  

        
                   
        print()    
    
        
print_calendar_horizontal(3,2023)    


def sum(a,b):
    return a+b