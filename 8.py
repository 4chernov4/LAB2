n = float(input("Введите скорость машины в км/день: "))
m = float(input("Введите длину маршрута в км: "))

days = m // n

if m % n != 0:
    days += 1

print(days)