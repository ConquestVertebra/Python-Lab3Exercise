"""EXAMPLE 5:
Write a program that translates a letter grade entered by the user into the corresponding numerical grade and prints it.
The letter grades are 'A', 'B', 'C', 'D' and 'F', possibly followed by a + or – sign. Their numerical values are, in
order, 4.0, 3.0, 2.0, 1.0 and 0.0. 'F+' and 'F–' grades do not exist. A + sign increases the numerical grade by 0.3,
while a – sign decreases it by the same amount. The 'A+' grade is equal to 4.0."""

def translate_grade(grade):
    # harf notunu sayısal nota çevir
    if grade[0] == "A":
        numeric_grade = 4.0
    elif grade[0] == "B":
        numeric_grade = 3.0
    elif grade[0] == "C":
        numeric_grade = 2.0
    elif grade[0] == "D":
        numeric_grade = 1.0
    else:
        numeric_grade = 0.0

    # + işareti varsa notu arttır
    if len(grade) > 1 and grade[1] == "+":
        numeric_grade += 0.3
    # - işareti varsa notu azalt
    elif len(grade) > 1 and grade[1] == "-":
        numeric_grade -= 0.3

    # sayısal notu döndür
    return numeric_grade

# test et
print(translate_grade("A"))  # 4.0
print(translate_grade("A+"))  # 4.3
print(translate_grade("A-"))  # 3.7
print(translate_grade("B+"))  # 3.3
print(translate_grade("B-"))  # 2.7
print(translate_grade("C+"))  # 2.3
