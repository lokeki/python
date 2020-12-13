from datetime import date
def DaysOfYear (*dates):

    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print(delta.days)


DaysOfYear(date(1999,1,15))
print('----------------')
DaysOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())


