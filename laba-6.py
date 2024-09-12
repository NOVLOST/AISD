"""
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
 Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
 на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.

ВАРИАНТ №15

Ассортимент магазина составляют  товары К артикулов (названий).
 Допускается к празднику на артикулы товаров (количество от Т до N) установить скидки.
 Сформировать все возможные варианты списков товаров для скидок. """


import time
import itertools
t = 2
n = 1
k = 0
choice=int(input("выбор сложности программы 0-простая 1-сложная\n"))
k = int ( input ( "Введите количество товаров К= " ) )
combi = []
premiumScore = 0
costScore = 0
display = []
class Tovar_premium:
    def __init__(self,prefix,id,cost):
        self.prefix = prefix
        self.id = id
        self.cost = cost

class Tovar_lowcost:
    def __init__(self,prefix,id,cost):
        self.prefix = prefix
        self.id = id
        self.cost = cost



""" ______________________________________________________________
    ||             первая часть через стандарт                 ||
    ||                                                         ||
    --------------------------------------------------------------"""


while t > n: #фильтрация т и n

    t = int ( input ( "\nНужно ввести диапазон товаров Введите от Т до N\n\n Введите Т " ) )
    n = int ( input( "\nВведите N " ) )
if choice==0:
    y = t
    start=time.time()

    while   y <= n: #идем от меньшего к большему

        for i in range(0, k): #добовляем числа по размеру списка определяемого y
            if len(combi) >= y:
                break
            else:
                combi.append(i)

        print(f'\n {combi}') #выводим первую комбинацию
        combi.append( k ) #нужны для определения момента выхода из цикла
        combi.append( 0 )

        while True:


            for i in range( len(combi) - 1 ):
                if combi[i] + 1 == combi[i + 1]: #если следующий элемент= предидущий + 1 то идем дальше присаваивая предидущиму значение его индекса

                    combi[i] = i

                else:

                    break

            if i < y: #если индекс элемента меньше размера комбинации то выводим комбинацю

                combi[i] += 1
                print(f"\n {combi[:-2]}")

            else:

                y += 1
                combi.clear()
                break


    end = time.time()
    print(f'\nВремя выполнения самописной функции {end-start}')


    """ ______________________________________________________________
        ||              вторая часть через библиотеку               ||
        ||                                                          ||
        --------------------------------------------------------------"""



    start=time.time()


    print("\n\nвторая часть через библиотеку itertools\n\n")
    combi=[i for i in range(0,k) ]


    for g in range(t,n+1):

        tmp=itertools.combinations(combi,g)
        print(f'\n{list(tmp)},\n комбинций из {g} элементов')

    end = time.time()
    print(f'\nВремя выполнения питон функции {end-start}')

if choice==1:
    """ ____________________________________________________________________________________________________________________
        || по новому условию функция расматривает класс товара и его цену и делает вывод по условию                      ||
        ||Колво-премиум товаров > y - t and (количество цен которые определяются по условию  (> (k - t) * 100) ) < k - t ||
        ||                                                                                                               ||
        ||                                                                                                               ||
        ||                                                                                                               ||
        -------------------------------------------------------------------------------------------------------------------"""

    pause=input("\n\n\n\n\nпо новому условию функция расматривает класс товара и его цену и делает вывод по условию   Колво-премиум товаров > y - t and (количество цен которые определяются по условию  (> (k - t) * 100) ) < k - t\n\nДЛЯ ПРОДОЛЖЕНИЯ ВВЕДИТЕ ЛЮБОЙ СИМВОЛ\n\n\n\n")
    y = t
    start=time.time()
    spisok = []
    while   y <= n: #идем от меньшего к большему



        for i in range(0, k):

            if i % 2 == 0 and len(spisok) < y :
                combi = Tovar_premium("PREMIUM", i, (i+1) * 100)
                spisok.append([combi.id, combi.prefix, combi.cost])
            elif len(spisok) < y:
                combi = Tovar_premium("LOWCOST", i, (i+1) * 10)
                spisok.append([combi.id, combi.prefix, combi.cost])
            else:
                break




        spisok.append( ( k,0,0)) #нужны для определения момента выхода из цикла
        spisok.append( (0, 0) )


        while True:



            for i in range( len(spisok) - 1  ):



                if spisok[i][0] + 1 == spisok[i+1][0]: #если следующий элемент= предидущий + 1 то идем дальше присаваивая предидущиму значение его индекса



                    for j in range(len(spisok)-1):
                        if spisok[j][1] == "PREMIUM":
                            premiumScore += 1

                        if spisok[j][2] > (k - t) * 100:
                            costScore += 1

                    if premiumScore > y - t and costScore < k - t:
                        print(f'новая комбинация на {y} элементов {spisok[:-2]} \n ')
                        premiumScore = 0
                        costScore = 0
                    else:
                        premiumScore = 0
                        costScore = 0


                    if spisok[i ][0] % 2 == 0:
                        spisok[i ][1] = "PREMIUM"
                        spisok[i ][2] = spisok[i ][0] * 100
                    else:
                        spisok[i ][1] = "LOWCOST"
                        spisok[i ][2] = spisok[i ][0] * 10

                else:



                    break



            if i < y:
                for j in range(len(spisok) - 1):
                    if spisok[j][1] == "PREMIUM":
                        premiumScore += 1

                    if spisok[j][2] > (k - t) * 100:
                        costScore += 1
                if premiumScore > y - t and costScore < k - t:
                    print(f'новая комбинация на {y} элементов {spisok[:-2]} \n ')
                    premiumScore = 0
                    costScore = 0
                else:
                    premiumScore = 0
                    costScore = 0


                spisok[i ][0] += 1



                if spisok[i ][0] % 2 ==0:
                    spisok[i ][1]= "PREMIUM"
                    spisok[i ][2] = spisok[i ][0] * 100
                    premiumScore = 0
                    costScore = 0
                else:
                    spisok[i ][1] = "LOWCOST"
                    spisok[i ][2] = spisok[i ][0] * 10
                    premiumScore = 0
                    costScore = 0

                for j in range(len(spisok) - 1):
                    if spisok[j][1] == "PREMIUM":
                        premiumScore += 1

                    if spisok[j][2] > (k - t) * 100:
                        costScore += 1
                if premiumScore > y - t and costScore < k - t:
                        print(f'новая комбинация на {y} элементов {spisok[:-2]} \n ')
                        premiumScore = 0
                        costScore = 0
                else:
                    premiumScore = 0
                    costScore = 0

            else:
                costScore = 0
                premiumScore = 0


                y += 1
                spisok.clear()
                break


    end = time.time()
    print(f'\nВремя выполнения самописной функции {end-start}')



    start=time.time()


    print("\n\nТЕПЕРЬ  через библиотеку itertools\n\n")
    for i in range(0, k):

        if i % 2 == 0:

            combi = Tovar_premium("PREMIUM", i, (i+1 ) * 100)
            spisok.append([combi.id, combi.prefix, combi.cost])
        else:

            combi = Tovar_premium("LOWCOST", i, (i+1 ) * 10)
            spisok.append([combi.id, combi.prefix, combi.cost])



    for g in range(t,n+1):

        tmp=[]
        tmp=list(itertools.combinations(spisok,g))
        for i in range(0,len(tmp)):


            if premiumScore > g - t and costScore < k - t:

                print(f'\n{list(tmp[i-1])},\n комбинций из {g} элементов')
                premiumScore = 0
                costScore = 0

            else:

                premiumScore = 0
                costScore = 0



            for j in range(0,len(tmp[0])):
                if tmp[i][j][1] == "PREMIUM":
                    premiumScore += 1

                if tmp[i][j][2] > (k - t) * 100:
                    costScore += 1

