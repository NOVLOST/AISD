"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
 Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
  Определить границы применимости рекурсивного и итерационного подхода.
   Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
15.	F(1) = 1; G(1) = 1; F(n) = (-1)n*(F(n–1) – G(n–1))/(n+5)!, G(n) = F(n–1) + sin(n), при n >=2"""


import math
import time
import matplotlib.pyplot as plt
from functools import lru_cache
"""n это переменная для значения n"""
n=-1
"""one это переменная для определения знака"""
one=1
"""k это переменная для выбора режима работы"""
k=-1
"""списки для замера времени"""
timer=[]
timer_rec=[]
"""ans это переменная для ответа пользователя """
ans=1
"""шаг графика"""
step=-1

"""рекурсия"""
@lru_cache(maxsize=None)
def factrial(x):
    if x == 1:
        return x
    else:
        return x * factrial(x - 1)


def rec_f(x,one):

    if x < 2:

        return 1
    else:
        one *= -1
        return one*(rec_f(x - 1,one) - rec_g(x-1,one)) // factrial(x+5)

def rec_g(x,one):
    if x < 2:
        return 1
    else:

        return  rec_f(x-1,one)+int(math.sin(x))

"""итерация"""
def it_f(x):
    cata_f=[1]*3
    cata_g=[1]*3
    one = 1
    for i in range(2,x+1):

        cata_g[1] = cata_f[0]   + int((math.sin(cata_f[-1]))) #либо cata_f[0]
        cata_f[-1] = one*( (cata_f[1] - cata_g[1]) // it_factorial(i + 5)) #либо Х
        cata_f[0], cata_f[1] = cata_f[1], cata_f[2]
        cata_g[0], cata_g[1] = cata_g[1], cata_g[2]
        one *= -1

    return cata_f[-1]
@lru_cache(maxsize=None)
def it_factorial(x):
    res=x
    for i in range(1,x):
        res = res * (i+1)
    return res


"""ввод числа n"""
while n < 1:
    print("Введите натуральное число от 1 ")
    n = int(input())
while step<1:
    step=int(input("Введите шаг графика от 1"))
graf = list(range(1, n + 1,step))


"""выбор режима работы программы 0-рекурсия 1-итерация 2-оба"""
while k != 0 and k != 1 and k != 2:
    print("Выберите режим работы 0-рекурсия 1-итерация 2-оба")
    k = int(input())

if (n >=  33 and (k == 0 or k == 2)) or (n >= 5000 and (k == 1 or k == 2)):
    print("работа программы может занять большое время ,вы хотите продолжить? \n 1=да 0=нет")
    ans = int(input())

    while ans != 1 and ans != 0:
        print("работа программы может занять большое время ,вы хотите продолжить? \n 1=да 0=нет")
        ans = int(input())


if k == 0 and ans == 1:
    for i in graf:
        start = time.time()
        res = rec_f(i,one)
        end = time.time()
        timer.append(end-start)
        rec_times = end - start
        print(i,"№Результат рекурсии ",res,"\nВремя выполнения",end-start,"\n\n")
    """графики"""
    plt.plot(graf, timer, label='рекурсионная функция.')
    plt.legend(loc=2)


if k == 1 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i)
        end = time.time()
        timer.append(end - start)
        iter_times = end - start
        print(i,"№Результат рекурсии ",result,"\nВремя выполнения",end-start,"\n\n")
    """графики"""
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.legend(loc=2)

if k == 2 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i)
        end = time.time()
        timer.append(end-start)
        start_rec = time.time()
        res = rec_f(i,one)
        end_rec = time.time()
        timer_rec.append(end_rec-start_rec)
        rec_times = end_rec-start_rec
        iter_times = end-start
        print("\n",i,"№результат рекурсии ", res,"---------результат итерации",result,"-----------время  РЕКУРСИИ ",end_rec-start_rec,"-------время  ИТЕРАЦИИ",end-start)
    """графики"""
    plt.plot(graf, timer, label='Итерационная функция.')
    plt.plot(graf, timer_rec, label='Рекусионная функция.')
    plt.legend(loc=2)



plt.xlabel('Значение n')
plt.ylabel('Время выполнения (c)')
plt.show()
