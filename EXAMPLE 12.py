"""EXAMPLE 7:
A 366-day year is called a leap year and is used to keep the calendar synchronized with the Sun, since the Earth
revolves around it once every 365.25 days or so. In reality, this number is not accurate, and for all dates after
1582 the Gregorian correction applies: usually years divisible by 4, such as 1996, are leap years, but years divisible
by 100, such as 1900, are not; as an exception to the exception, years divisible by 400, such as 2000, are leap years.
Write a program that asks the user for a year (greater than 1582) and determines whether it is a leap year using a
single if construct."""

def is_leap_year(year):
    # yıl artık yıl mı değil mi
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# kullanıcıdan yıl iste
year = int(input("Enter year: "))

# yıl artık yıl mı değil mi
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
