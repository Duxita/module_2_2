first = input('Введите первое число ')
second = input('Введите второе число ')
third = input('Введите третье число ')
if first == second and first == third:
    print(3)
elif second == first or second == third or third == first:
    print(2)
else:
    print(0)