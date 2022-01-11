import math

a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
d = b * b - 4 * a * c
if d < 0:
    print("Нет корней")
    exit(0)
sqr_x = (-b + math.sqrt(d))/2
if sqr_x > 0:
    print(math.sqrt(sqr_x), ' ', -math.sqrt(sqr_x))
sqr_x = (-b - math.sqrt(d))/2
if sqr_x > 0:
    print(math.sqrt(sqr_x), ' ', -math.sqrt(sqr_x))
