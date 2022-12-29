"""EXAMPLE 4:
 The matriculation of students at an Athenaeum consists of two parts: a letter and a sequence of numbers. Write a
 Python program that, starting with two matriculation codes, displays them on the screen in ascending order based only
 on the numeric part"""

def check_order(num1, num2, num3):
    # artan sırada mı
    if num1 < num2 < num3:
        print("increasing")
    # azalan sırada mı
    elif num1 > num2 > num3:
        print("decreasing")
    # hiçbiri değil
    else:
        print("neither")
# test et
check_order(1, 2, 3) # increasing
check_order(3, 2, 1) # decreasing
check_order(1, 2, 2) # neither
check_order(1, 1, 2) # neither
check_order(2, 1, 3) # neither
