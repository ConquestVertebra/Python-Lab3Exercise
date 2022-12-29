"""EXAMPLE 3:
 The matriculation of students at an Athenaeum consists of two parts: a letter and a sequence of numbers. Write a
 Python program that, starting with two matriculation codes, displays them on the screen in ascending order based only
 on the numeric part"""

def apply_(code1, code2):
    # sayısal kısımları ayıkla
    num1 = int(code1[1:])
    num2 = int(code2[1:])

    # sayısal kısımları karşılaştır ve sırala
    if num1 < num2:
        print(code1)
        print(code2)
    else:
        print(code2)
        print(code1)


# test et
apply_("A123", "B456")  # A123 B456
apply_("C789", "B456")  # B456 C789
apply_("D123", "D456")  # D123 D456
