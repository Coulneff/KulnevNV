# -- coding: utf-8 --
#Практическое занятие №3 У-213 Кульнев Н.В.
	
#1 
def Zadanue1(a, b): 
    if (a<=b): 
        print("Вывод всех чисел от A до B")
        for i in range(a, b + 1):
            print(i) 
    else:
        print("A >= B - решение невозможно") 
    print("\n")

#2
def Zadanue2(a, b): 
    if (a<b): 
        print("Вывод всех чисел от A до B в порядке возрастания")
        for i in range(a, b + 1):
            print(i) 
    else:
        print("Вывод всех чисел от A до B в порядке убывания")
        for i in range(a, b - 1,-1):
            print(i) 
    print("\n")

#3
def Zadanue3(a, b): 
    if (a>b): 
        print("Вывод всех нечетных чисел от A до B включительно в порядке убывания")
        for i in range(a, b - 1, -1):
            if i%2 != 0 :
                print(i) 
    
    print("\n")

#4
def Zadanue4(): 
    print(sum(int(input('Число: ')) for i in range(int(input('Количество чисел для for: '))))) 
    print("\n")

#5
def Zadanue5(n): 
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    print("Сумма по натуральному n (",n,") = ",sum,"\n")

#6
def Zadanue6(n): 
    otvet = 1
    for i in range(1, n + 1):
        otvet *= i 
    print("Факториал числа n (",n,") = ",otvet,"\n")

 #7
def Zadanue7(n): 
    sum = 0
    fact = 1
    for i in range(1, n + 1):
        fact *=i
        sum += fact 
    print("Сумма числа факториалов n (",n,") = ",sum,"\n")

#8
def Zadanue8(n):  
    if (n<=9):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, sep='', end='')
            print() 
    else:
        print("n больше 9")
    print("\n")

#9
def Zadanue9(n):   
    summ = 0
    (x, y) = (0, 1)
    for i in range(0,n):
        (x, y) = (y, x + y) 
        summ = summ + x

    print("Сумма", summ)
    print("\n")
 
#10
def Zadanue10(n,k):   
    summ = 0
    (x, y) = (0, 1)
    for i in range(0,n):
        (x, y) = (y, x + y)
        if (i >= k-1):
            summ = summ + x

    print("Сумма", summ)
    print("\n")
 

print("#Введите A и B для Задания 1")
Zadanue1(int(input()),int(input()))

print("#Введите A и B для Задания 2")
Zadanue2(int(input()),int(input()))

print("#Введите A и B для Задания 3")
Zadanue3(int(input()),int(input()))

print("#Введите N и N для Задания 4")
Zadanue4()

print("#Введите натуральное число n для Задания 5")
Zadanue5(int(input("Натуральное число: ")))

print("#Введите натуральное число n для нахождение его факториала в Задании 6")
Zadanue6(int(input("Натуральное число: ")))

print("#Введите натуральное число n для нахождение суммы его факториала в Задании 7")
Zadanue7(int(input("Натуральное число: ")))

print("#Введите n<=9 для вывода лесенки из ступенек в Задании 8")
Zadanue8(int(input()))

print("#Введите n - количество чисел из ряда Фибоначчи. в Задании 9")
Zadanue9(int(input()))

print("#Введите n - количество чисел из ряда Фибоначчи и k - порядковый номер в ряду. в Задании 10")
Zadanue10(int(input()),int(input()))