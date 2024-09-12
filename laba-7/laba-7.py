"""Ассортимент магазина составляют  товары К артикулов (названий)
.Допускается к празднику на артикулы товаров (количество от Т до N) установить скидки.
Сформировать все возможные варианты списков товаров для скидок.
по новому условию функция расматривает класс товара и его цену и делает вывод по условию

Колво-премиум товаров > y - t and (количество цен которые определяются по условию  (> (k - t) * 100) ) < k - t '

НАПИСАТЬ ДЛЯ ЗАДАЧИ ВЫШЕ^^^ ГРАФИЧЕСКИЙ ИНТЕРФЕЙС

"""

import tkinter as tk
from tkinter import ttk
import itertools
from tkinter.messagebox import showerror

win = tk.Tk()
h = 1200
w = 720
"""ПРЕФИКС ЭТО КАТЕГОРИЯ ТОВАРА(ДЕШЕВЫЙ/ДОРОГОЙ) ID ЭТО ИДЕКС ТОВАРА ,COST ЦЕНА"""
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
"""ФУНКЦИЯ ОЧИСТКИ ЭКРАНА"""
def delete_editor():

    editor.delete('1.0','end')


def combination():
    """ПОЛУЧАЕМ ЗАНЧЕНИЯ ОТ ЮЗЕРА"""
    t = int(entryT.get())
    n = int(entryN.get())
    k = int(entryK.get())

    y = t
    """ПРЕДУПРЕЖДЕНИЕ"""
    if k >= 20 and n>=7:
        tk.messagebox.showinfo(title="Информация", message="Приданных значениях программа может долго выполнять запрос")

    premiumScore = 0
    costScore = 0
    spisok = []
    while y <= n:  # идем от меньшего к большему

        for i in range(0, k):

            if i % 2 == 0 and len(spisok) < y:
                combi = Tovar_premium("PREMIUM", i, (i + 1) * 100)
                spisok.append([combi.id, combi.prefix, combi.cost])
            elif len(spisok) < y:
                combi = Tovar_premium("LOWCOST", i, (i + 1) * 10)
                spisok.append([combi.id, combi.prefix, combi.cost])
            else:
                break

        spisok.append((k, 0, 0))  # нужны для определения момента выхода из цикла
        spisok.append((0, 0))

        while True:

            for i in range(len(spisok) - 1):

                if spisok[i][0] + 1 == spisok[i + 1][0]:  # если следующий элемент= предидущий + 1 то идем дальше присаваивая предидущиму значение его индекса

                    for j in range(len(spisok) - 1):
                        if spisok[j][1] == "PREMIUM":
                            premiumScore += 1

                        if spisok[j][2] > (k - t) * 100:
                            costScore += 1

                    if premiumScore > y - t and costScore < k - t:
                        editor.insert("1.0",f'новая комбинация на {y} элементов {spisok[:-2]} \n\n\n\n')
                        premiumScore = 0
                        costScore = 0
                    else:
                        premiumScore = 0
                        costScore = 0

                    if spisok[i][0] % 2 == 0:
                        spisok[i][1] = "PREMIUM"
                        spisok[i][2] = spisok[i][0] * 100
                    else:
                        spisok[i][1] = "LOWCOST"
                        spisok[i][2] = spisok[i][0] * 10

                else:

                    break

            if i < y:
                for j in range(len(spisok) - 1):
                    if spisok[j][1] == "PREMIUM":
                        premiumScore += 1

                    if spisok[j][2] > (k - t) * 100:
                        costScore += 1
                if premiumScore > y - t and costScore < k - t:
                    editor.insert("1.0", f'новая комбинация на {y} элементов {spisok[:-2]} \n\n\n\n')
                    premiumScore = 0
                    costScore = 0
                else:
                    premiumScore = 0
                    costScore = 0

                spisok[i][0] += 1

                if spisok[i][0] % 2 == 0:
                    spisok[i][1] = "PREMIUM"
                    spisok[i][2] = spisok[i][0] * 100
                    premiumScore = 0
                    costScore = 0
                else:
                    spisok[i][1] = "LOWCOST"
                    spisok[i][2] = spisok[i][0] * 10
                    premiumScore = 0
                    costScore = 0

                for j in range(len(spisok) - 1):
                    if spisok[j][1] == "PREMIUM":
                        premiumScore += 1

                    if spisok[j][2] > (k - t) * 100:
                        costScore += 1
                if premiumScore > y - t and costScore < k - t:
                    editor.insert("1.0", f'новая комбинация на {y} элементов {spisok[:-2]} \n\n\n\n')
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






    editor.insert("1.0","\n\nТЕПЕРЬ  через библиотеку itertools\n\n")
    for i in range(0, k):

        if i % 2 == 0:

            combi = Tovar_premium("PREMIUM", i, (i + 1) * 100)
            spisok.append([combi.id, combi.prefix, combi.cost])
        else:

            combi = Tovar_premium("LOWCOST", i, (i + 1) * 10)
            spisok.append([combi.id, combi.prefix, combi.cost])

    for g in range(t, n + 1):

        tmp = []
        tmp = list(itertools.combinations(spisok, g))
        for i in range(0, len(tmp)):

            if premiumScore > g - t and costScore < k - t:

                editor.insert("1.0", f'новая комбинация на {y} элементов {spisok[:-2]} \n\n\n\n')
                premiumScore = 0
                costScore = 0

            else:

                premiumScore = 0
                costScore = 0

            for j in range(0, len(tmp[0])):
                if tmp[i][j][1] == "PREMIUM":
                    premiumScore += 1

                if tmp[i][j][2] > (k - t) * 100:
                    costScore += 1



"""ГРАФИЧЕСКИЙ ИНТЕРФЕЙС"""



win.title("Комбинации Товаров")
win.geometry(f"{h}x{w}+500+300")
win.resizable(False,False)

"""ОПИСАНИЕ ЗАДАЧИ"""
descrit = tk.Label(win, text='Ассортимент магазина составляют  товары К артикулов (названий)\n'
                             '.Допускается к празднику на артикулы товаров (количество от Т до N) установить скидки.\n'
                             ' Сформировать все возможные варианты списков товаров для скидок.\n'
                   '\n\nпо новому условию функция расматривает класс товара и его цену и делает вывод по условию \nКолво-премиум товаров > y - t and (количество цен которые определяются по условию  (> (k - t) * 100) ) < k - t '
                   ,fg = "orange",bg = '#381c1a',relief=tk.RAISED,bd='5' )
descrit.place(x=320,y=0)


"""Вводим количество товаров К"""
descritK = tk.Label(win, text='Введите К',fg = "orange",bg = '#381c1a',relief=tk.GROOVE,bd='5')
descritK.place(x=40, y=200)

entryK = tk.Entry(highlightthickness=2)
entryK.config(highlightbackground="orange", highlightcolor="red")
entryK.place(x=10,y=240)
"""Окно ввода переменной Т являюшийся началом комбинации"""
descritT = tk.Label(win, text='Введите T',fg = "orange",bg = '#381c1a',relief=tk.GROOVE,bd='5',)
descritT.place(x=40, y=280)

entryT = tk.Entry(highlightthickness=2)
entryT.config(highlightbackground="orange", highlightcolor="red")
entryT.place(x=10,y=320)


"""Окон ввода переменной N являюшийся границей кмбинации"""
descritN = tk.Label(win, text='Введите N',fg = "orange",bg = '#381c1a',relief=tk.GROOVE,bd='5',)
descritN.place(x=40,y=360)

entryN = tk.Entry(highlightthickness=2)
entryN.config(highlightbackground="orange", highlightcolor="red")
entryN.place(x=10,y=400)


"""Поле вывода работы программы"""
editor = tk.Text(width=120, height=35, bg="#5c5a5a",
            fg='orange',wrap="word")
editor.place(x=210, y=140)

"""Скрол"""
scroolY = ttk.Scrollbar(orient="vertical", command=editor.yview)

editor["yscrollcommand"]=scroolY.set
scroolY.place(x=1180,y=140,height=560)


"""кнопка запуска программы"""
startEngine = ttk.Button(win,text = "Запуск",cursor="pirate",command=combination)
startEngine.place(x=40,y=480)

"""кнопка очистки """
clean = ttk.Button(win,text = "Сброс",cursor="pirate",command=delete_editor)
clean.place(x=40,y=540)

"""ВЫВОД НА ЭКРАН"""
win.config(bg='#381c1a')
win.mainloop()
