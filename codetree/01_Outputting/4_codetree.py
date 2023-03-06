# 소수점 4째짜리까지 값을 반올림하여 출력하는 코드
# 1
a = 33.567268
print("%.4f" % a)
# 2
a = 33.567268
print("{0:.4f}".format(a))
# >> 33.5673

#1
a = 13
b = 0.165
print(a,"*", "%.6f"%b, "=", "{0:.6f}".format(a*b))
#2
a = 25.352
print("%.1f"%a)
#3
ft = 30.48 
mi = 160934
print("9.2ft = {0:.1f}cm".format(ft * 9.2))
print("1.3mi = {0:.1f}cm".format(mi * 1.3))
#4
a = 2.8437
print(f"{a:.2f}")
# >> 2.84