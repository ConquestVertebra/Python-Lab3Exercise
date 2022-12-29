
"""A supermarket rewards its customers with shopping vouchers whose amount depends on
the amount of money spent on food. For example, if you spend $50, you get a shopping
voucher equal to 8% of the amount you spent. The table below shows the percentage
used to calculate the shopping voucher relative to different amounts. Write a Python
program that calculates and displays the value of the shopping voucher given to the
customer, based on the amount of money he or she spent on the purchase of groceries."""

# kullanıcıdan harcadığı para miktarını isteyelim
para = float(input("Harcadığınız para miktarı: "))

# Ödül yüzdesini bulmak için harcadığı para miktarını kontrol edeceğimiz bir dizi
# oluşturalım
odul_yuzdeleri = [0,50,100,200,300]

# Ödül yüzesini belirleyecek if/elif yapısını oluşturalım
if para < 50:
    odul_yuzdesi = 0
elif para <100:
    odul_yuzdesi = 5
elif para < 200:
    odul_yuzdesi = 6
elif para < 300:
    odul_yuzdesi = 7
else:
    odul_yuzdesi = 8

# Ödül miktarını bulalım
odul_miktarı = para*odul_yuzdesi/100

# Ödül miktarını ekrana yazdıralım
print("Ödül miktarı: ", odul_miktarı)