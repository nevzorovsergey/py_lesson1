# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a > b:
    if b > c:
        mid = b
    elif a > c:
        mid = c
    else:
        mid = a
else:
    if b < c:
        mid = b
    elif a < c:
        mid = c
    else:
        mid = a
print('Среднее число ', mid)
