n = int(input("Введите количество минут, прошедших с начала суток: "))

hours = (n // 60) % 24
minutes = n % 60

print("Часы: ", hours)
print("Минуты: ", minutes)