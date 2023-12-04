class1 = int(input("Введите количество учеников в первом классе: "))
class2 = int(input("Введите количество учеников во втором классе: "))
class3 = int(input("Введите количество учеников в третьем классе: "))

class1 = (class1 + 1) // 2
class2 = (class2 + 1) // 2
class3 = (class3 + 1) // 2

total_desks = class1 + class2 + class3

print(total_desks)