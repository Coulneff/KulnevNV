# -*- coding: utf-8 -*-
#1
print('"1" Курс Основы программирования начался')
#2
a = 16823*12302/3092
print('"2" Остаток от деления: ', a)
#3
age = 16 #Возраст
name = "НеИван" #Имя
if (age >= 16):
	print('"3" Поздравляем вы поступили в ВГУИТ') 
else:
	print('Cначала нужно окончить школу!')
	buf = 16-age
	print('"3c" Осталось учиться в школе: ',buf)
if (age > 0 and age<75):
		print('"3a" Ваш возраст в радиусе 0 до 75: ', age)
else: 
		print('"3a" Ваш возраст вне радиуса: ', age)	
if (name != "Иван"):
		print('"3b" Вы не Иван')
else:
		print('"3b" Вы Иван')
#4
a = 90400 #начальные секунды
seconds = a % 60
minute = (a//60) % 60
chas = ((a//3600)%24)
day = a // 86400
print('"4" Дни: ',day,' часы: ',chas,' минуты: ',minute,' секунды: ', seconds)
#5
n = "4"
nv = int(n)
rez = nv + nv**2+nv**3+nv**4+nv**5
print('"5" Результат выражения: ',rez)
#6
x = 3
y = 4
print('"6" До: x: ',x,' y: ',y)
baf = x
x = y
y = baf
print('"6" После: x: ',x,' y: ',y)
#7
chislo = '666'
if (type(chislo) == int) or (type(chislo) == float):
	print('"7" Переменная - число')
else:
	print('"7" Переменная - не число')

