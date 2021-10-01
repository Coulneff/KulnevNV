# -- coding: utf-8 --

	
#1 
print("-[Задание 1]-")
print("Введите число 1: ")
a = int(input())
print("Введите число 2: ")
b = int(input())
print("Введите число 3: ")
c = int(input())
print("Сумма введённых чисел: ",a+b+c)

#2
print("-[Задание 2]-")
print("Введите катет А: ")
a = int(input())
print("Введите катет Б: ")
b = int(input()) 
print("Площадь прямоугольного треугольника: ", 1/2*(a*b))

#3
print("-[Задание 3]-")
print("Введите число N: ")
n = int(input())
 
minute = (n % 60)
chas = ((n//60)%24)

print("Количество часов: ",chas)
print("Количество минут: ",minute)

#4 - mb переделать


def dlina_shnura(a,b,l,n):
    otv =  (2 * l + (2 * n - 1) * a + 2 * (n - 1) * b)
    return otv  


print("-[Задание 4]-")
print("Введите расстояние между рядами (a): ")
v1 = int(input())
print("Введите расстояние между дырочками (b): ")
v2 = int(input())
print("Введите количество дырочек (n): ")
v3 = int(input())
print("Введите длину свободного конца шнурка (l): ")
v4 = int(input())

print("Искомая длина шнура: ",dlina_shnura(v1,v2,v4,v3))
 
#5

def naumenshie(a,b,c):
    if b >= a <= c:
        buf = (a)
    elif a >= b <= c:
        buf = (b)
    else:
        buf = (c)

    return buf

print("-[Задание 5]-")
print("Введите число 1: ")
a = int(input())
print("Введите число 2: ")
b = int(input())
print("Введите число 3: ")
c = int(input())

print("Наименьший из 3 чисел: ",naumenshie(a,b,c))


#6

 

print("-[Задание 6]- \nВведите первую клетку(X,Y) и потом вторую (X,Y)")

a, b = ((int(input()) + int(input()) - 1) % 2 for _ in range(2))
print("Да, это чёрные клетки" if a == b else "Они различаются")

#7

print("-[Задание 7]- \nВведите Год")
 
year = int(input())
if (year % 4 == 0) :
    if (not (year % 100 == 0)) or (year % 400 == 0):
     print("Это високосный год")
else:    
    print("Это обычный год")

#8

print("-[Задание 8]- \nВведите 3 числа")
 
a = int(input())
b = int(input())
c = int(input())

rez = 0 
if  a == b == c:
    rez = 3
elif a == b or b == c or a == c: 
    rez = 2
else:
    rez = 0

print("Количество совпадений: ",rez)

#9

print("-[Задание 9]- \nВведите n*m долек шоколада и отлом от шоколадки на k долей")
 
n = int(input())
m = int(input())
k = int(input())
if k < n * m:
    if ((k % n == 0) or (k % m == 0)):
        print('Да, можно отломить от шоколадки часть')
    else:
        print('Нет, можно отломить от шоколадки часть')
