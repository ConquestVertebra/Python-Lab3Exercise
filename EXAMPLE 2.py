"""EXAMPLE 2:
 The following pseudocode describes how to transform a string containing a ten-digit telephone number
 (such as "4155551212") into a more easily readable string, formatted in the U.S. style, such as "(415) 555-1212".
 I. Take the string consisting of the first three characters and surround it with round brackets (this is the prefix,
 called the "area code"); II. Concatenate the prefix with the string containing the next three characters, a dash and
 the string consisting of the last four characters you get the number in the required format. Translate this pseudocode
 into a Python program that stores a 10-digit telephone number in a string and then displays it in the format just
 described."""

def format_telephone_number(number):
    # prefix oluştur
    prefix = "(" + number[:3] + ")"

    # numarayı istenen formatına dönüştür
    formatted_number = prefix + " " + number[3:6] + "-" + number[6:]

    # numarayı döndür
    return formatted_number

# test et
print(format_telephone_number("4155551212"))  # (415) 555-1212
print(format_telephone_number("1234567890"))  # (123) 456-7890
print(format_telephone_number("9876543210"))  # (987) 654-3210
