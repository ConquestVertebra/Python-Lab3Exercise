
"""Write a program that asks the user as input a wavelength value (real number, which
can be written in scientific notation, e.g., 1.23e-7), and displays the description of
the corresponding part of the electromagnetic spectrum, as shown in the table below"""

# Kullanıcıdan dalga boyu değerini isteyelim
dalga_boyu = float(input("Lütfen dalga boyu değerini girin: "))

# Elektromanyetik spektrumun parçasını bulalım
if dalga_boyu >= 1e-1:
    parça = "Radyo dalgaları"
elif 1e-3 <= dalga_boyu < 1e-1:
    parça = "Mikro dalga"
elif 7e-7 <= dalga_boyu < 1e-3:
    parça = "Kızılötesi"
elif 4e-7 <= dalga_boyu < 7e-7:
    parça = "Görülebilir ışık"
elif 1e-8 <= dalga_boyu < 4e-7:
    parça = "Ultraviyole"
elif 1e-11 <= dalga_boyu < 1e-8:
    parça = "X-ışınları"
else:
    parça = "Gama ışınları"

# Sonucu ekrana yazdıralım
print(f"{dalga_boyu:.2e} m dalga boyu, {parça}'a aittir.")