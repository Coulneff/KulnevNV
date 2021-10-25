# -- coding: utf-8 --
#Практическое занятие №3 У-213 Кульнев Н.В.
	
#1 
def Zadanue1_i(a): 
    print("Третий символ строки: ")
    print(a[2])

def Zadanue1_ii(a):
    print("Предпоследний символ строки: ")
    print(a[len(a)-2])

def Zadanue1_iii(a):
    print("Первые пять символов этой строки: ")
    st = a[:5]
    print(st)

def Zadanue1_iv(a):
    print("Вся строка, кроме последних двух символов: ")
    b = a[0:-2]
    print(b)

def Zadanue1_v(a):
    print("Только чётные: ")
    b = a[::2]
    print(b)

def Zadanue1_vi(a):
    print("Только нечётные: ")
    b = a[1::2] #Как было понятно - от 1 индекса (2 буквы) и до конца, с шагом 2, как в цикле.
    print(b)


def Zadanue1_vii(a):
    print("В обратном порядке: ")
    b = a[::-1]
    print(b)


def Zadanue1_viii(a):
    print("Вывести все символы через один в обратном порядке, начиная с последнего: ")
    b = a[::-2]
    print(b)


def Zadanue1_ix(a):
    print("Длина строки: ", len(a))
      


 



#2
def Zadanue2(stroka): 
    print(stroka.count(' ')+1, " слова")

#3
def Zadanue3(stroka): 
    chast1 = stroka[(len(stroka) + 1) // 2:]
    chast2 = stroka[:(len(stroka) + 1) // 2]
    print(chast1+chast2)

#4
def Zadanue4(stroka): 
    a = stroka[0:(stroka.find(' '))]
    b = stroka[stroka.find(' ')+1:len(stroka)]
    print(b+" "+a)

#5
def Zadanue5(stroka):  
    if stroka.count('f') == 1:
        print(stroka.find('f'))
    elif stroka.count('f') >1:
        print(stroka.find('f')," и ",stroka.rfind('f'))

#6
def Zadanue6(stroka): 
    if stroka.count('f') > 1:
        b = stroka.find('f')
        print(stroka.find('f',b+1,len(stroka)))
    elif stroka.count('f') == 1:
        print("-1")
    else: print("-2")

 #7
def Zadanue7(stroka): 
    buf = stroka.rfind('h')
    stroka = stroka[:(stroka.find('h'))]+stroka[buf+(buf != -1):]
    print(stroka)

#8
def Zadanue8(stroka):  
    buf = stroka[stroka.find('h'):stroka.rfind('h') + 1]
    print(stroka[:stroka.find('h')] +buf[::-1]+stroka[stroka.rfind('h') + 1:])

#9
def Zadanue9(stroka):   
    sim_yd = input()
    print(stroka.replace(sim_yd, ''))
 
 
 
 
Zadanue6(input("#Введите строку для задания 6: "))
 
Zadanue7(input("#Введите строку для задания 7: "))
 
Zadanue8(input("#Введите строку для задания 8: "))
 
Zadanue9(input("#Введите строку для задания 9: "))
 