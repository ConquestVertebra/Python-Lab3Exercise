"""Write a program that calculates taxes according to the following scheme. The program
should acquire the value of the income from the user, and print the taxes due. It is not required to
print intermediate steps."""


def _taxes(income):
    # vergi oranları
    rates = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    # vergi miktarları
    amounts = [9275, 37650, 91150, 190150, 413350, 415050, float("inf")]

    # vergi miktarı
    tax = 0

    # vergi oranı ve vergi miktarı belirle
    for i in range(len(amounts)):
        if income > amounts[i]:
            tax += (income - amounts[i]) * rates[i]
            income = amounts[i]

    # vergi miktarını döndür
    return tax


# kullanıcıdan gelir miktarı iste
income = float(input("Enter income: "))

# vergi hesapla
tax = _taxes(income)

# vergi miktarını ekrana yaz
print("Taxes:", tax)
