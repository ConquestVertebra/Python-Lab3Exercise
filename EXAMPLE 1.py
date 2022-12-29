"""EXAMPLE 1:
Write a python program that stores a string in a variable and, starting from that variable, displays the first three
characters of the string, followed by three dots, and finally followed by the last three characters. For example,
if the string is initialized to the value "Mississippi", the program should display "Mis...ppi." What happens if the
string is shorter than 6 characters? What if it is shorter than 3 characters?"""

def truncate_string(s):
    # eğer string uzunluğu 6 veya daha küçükse, direkt olarak yazdır
    if len(s) <= 6:
        return s

    # ön ve son üç karakteri al
    first_three = s[:3]
    last_three = s[-3:]

    # ön ve son üç karakteri yazdır ve arasına "..." ekle
    return f"{first_three}...{last_three}"


# test et
print(truncate_string("Mississippi"))  # Mis...ppi
print(truncate_string("Hi"))  # Hi
print(truncate_string(""))  # ""
print(truncate_string("123456"))  # 123456
print(truncate_string("FetitoMakarnatte"))  # Fet...tte