first, second, third = input('Введите три целых числа, используя "пробел": ').split()
if first == second == third:
    print(3)
elif first == second:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
