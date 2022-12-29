"""EXAMPLE 7:
Given the numerical values of the grades explained in exercise 03.2.2, write a program that translates a number
between 0.0 and 4.0 into the literal grade closest to it. For example, the number 2.8 (which could be the average of
several grades) should be translated as 'B-'. Resolve cases of equality in favor of the better grade: for example,
2.85 should be translated as 'B'."""


def translate_grade(grade):
    # nota göre harf notu belirle
    if grade >= 3.85:
        letter_grade = "A"
    elif grade >= 3.5:
        letter_grade = "A-"
    elif grade >= 3.15:
        letter_grade = "B+"
    elif grade >= 2.85:
        letter_grade = "B"
    elif grade >= 2.5:
        letter_grade = "B-"
    elif grade >= 2.15:
        letter_grade = "C+"
    elif grade >= 1.85:
        letter_grade = "C"
    elif grade >= 1.5:
        letter_grade = "C-"
    elif grade >= 1.15:
        letter_grade = "D+"
    elif grade >= 0.85:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # harf notunu döndür
    return letter_grade


# test et
print(translate_grade(4.0))  # A
print(translate_grade(3.85))  # A
print(translate_grade(3.5))  # A-
print(translate_grade(3.15))  # B+
print(translate_grade(2.85))  # B
print(translate_grade(2.5))  # B-
print(translate_grade(2.15))  # C+
print(translate_grade(1.85))  # C
print(translate_grade(1.5))  # C-
print(translate_grade(1.15))  # D+
print(translate_grade(0.85))  # D
print(translate_grade(0.5))  # F
