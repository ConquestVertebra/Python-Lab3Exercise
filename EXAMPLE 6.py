"""EXAMPLE 6:
The following algorithm (already seen in exercise 01.1.2) identifies the season (Spring, Summer, Fall or Winter,
i.e., spring, summer, fall or winter, respectively) to which a date belongs, given as month and day.
If month is 1, 2 or 3
season = “Winter”
Otherwise if month is 4, 5 or 6
season = “Spring”
Otherwise if month is 7, 8 or 9
season = “Summer”
Otherwise if month is 10, 11 or 12
season = “Fall”
If month is divisible by 3 and day >= 21
If season is “Winter”
season = “Spring”
Otherwise if season is “Spring”
season = “Summer”
Otherwise if season is “Summer”
season = “Fall”
Otherwise
season = “Winter”

Take back the analysis of the algorithm and then write a program that, by implementing it, asks the user for a month
and a day and, then, displays the season determined by this algorithm, verifying its correctness. """

def get_season(month, day):
    #mevsim belirleme
    if month in[1,2,3]:
        season = "Winter"
    elif month in [4,5,6]:
        season = "Spring"

    elif month in [7,8,9]:
        season = "Summer"

    else:
        season = "Fall"

    #21'den büyük veya eşit olan günler için mevsimi güncelle
    if month%3 == 0 and day >= 21:
        if season=="Winter":
            season = "Spring"
        elif season == "Spring":
            season="Summer"
        elif season == "Summer":
            season = "Fall"
        else:
            season="Winter"

    #mevsimi döndür
    return season

#kullanıcıdan ay ve gün iste
month = int (input("Enter mont (1-12): "))
day = int(input("Enter day (1-31): "))

#mevsimi bul ve ekrana yazdır
season= get_season(month,day)
print("Season", season)
