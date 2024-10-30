
import requests as re
from bs4 import BeautifulSoup as bs
from time import sleep

import tkinter
from tkinter import *
from tkinter import ttk
import csv

# заголовки для обхода защиты сайта
header = {"User-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

# переменные окна
window = Tk()
height = 1280
width = 600
window.geometry(f"{height}x{width}")
window.resizable(False, False)
window.config(bg='#007241')
#списки марок и моделей
marks = ['lada','honda','bmw']
marks_var = Variable(value=marks)
honda_model = ['accord','fit','civic']
vaz_model = ['niva_legend','granta','2106']
bmw_model = ['x5','x1','x6']
#трансформация пременных для treeview
honda_model_var = Variable(value=honda_model)
vaz_model_var = Variable(value=vaz_model)
bmw_model_var = Variable(value=bmw_model)
model_list = vaz_model_var
#индекс выбранного пользователем марки/модели
index_marks = 0
index_models = 0
tab_header = ['название','цена','комплектация','город']
#выбранные пользователем марка/модель отправляемые парсеру
mark_for_parser = 'lada'
model_for_parser = 'niva_legend'

#------------------------
#ПАРСЕР: Формирует ссылку из переданных марки/модели затем делает запрос на сервер и обрабатывает HTML код(работает как генератор)
#-------------------------
def parser(mark,model):
    print("HELLO")
    for num in range(1,5):
        sleep(10) #задержка чтобы не нагружать сервер
        url = f"https://auto.drom.ru/{mark}/{model}/page{num}/"

        response = re.get(url, headers=header)

        print(response)#статус код

        soup = bs(response.text, "lxml")

        data = soup.find_all("div", class_="css-1f68fiz ea1vuk60")

        for i in data:
            complect_part_3 = ""

            try:
                name = i.find("h3", class_="css-16kqa8y efwtv890").text

                price = i.find("span", class_="css-46itwz e162wx9x0").text.replace('\xa0', '')

                link = i.find("a",class_="g6gv8w4 g6gv8w8 _1ioeqy90").get("href")

                complect_part_1 = i.find_all("span",class_='css-1l9tp44 e162wx9x0')

                town = i.find("span",class_="css-1488ad e162wx9x0").text
                for y in complect_part_1:
                    complect_part_2 = y.text
                    complect_part_3 += complect_part_2





                yield (name,f"{price}",f'{complect_part_3 }',f'{town}',f'{link}')
            except:
                continue

#
#ЗАПИСЬ В CSV ФАЙЛ И ТАБЛИЦУ:делает вызов парсера с передачей ему марки/модели и полученную от него строку записывает в
#csv файл и таблицу
#
def excel(mark,model):
    global start
    start['state'] = tkinter.DISABLED
    with open('Servers.csv', 'a') as file:  # формируем csv файл
        CSwriter = csv.writer(file, dialect='excel')

        for i in parser(mark,model):
            CSwriter.writerow(i)
            table.insert("", END, values=(i[0],i[1],i[2],i[3],i[4]))
    start['state'] = tkinter.NORMAL

def excel_call():#если вызывать напрямую с передачей данных то она вызывается при инициализации кнопки
    excel(mark_for_parser,model_for_parser)


#----------------------------
#ВЫБОР МАРКИ/МОДЕЛИ и получение ссылки на авто: получаем индекс выбранной модели/марки если не выбирали
# то сохраняем прежнее значение для этого сделан Try/Except ссылка берется из таблицы treeview
#----------------------------
def choose(event):
    global index_marks,index_models,mark_for_parser,model_for_parser
    try:
        index_marks = entry_mark.curselection()[0]
        mark_for_parser = marks[index_marks]
    except:
        index_marks = index_marks

    choose_mark.config(text = f'MARK  {marks[index_marks]}')


    if index_marks == 0:
        model_list = vaz_model
        model_list_var = vaz_model_var
    elif index_marks == 1:
        model_list = honda_model
        model_list_var = honda_model_var
    else:
        model_list = bmw_model
        model_list_var = bmw_model_var

    entry_model.config(listvariable=model_list_var)
    try:
        index_models = entry_model.curselection()[0]
        model_for_parser = model_list[index_models]
    except:
        index_models = index_models


    choose_model.config(text = f'MODEL  {model_list[index_models]}' )

    try:
        link_to_car.delete(0, END)
        value = table.item(table.selection()[-1],option="values")
        link_to_car.insert(0, f'{value[-1]}')
    except:
        link_to_car.delete(0, END)
        link_to_car.insert(0, f'Cсылка на дром')



entry_mark = Listbox(listvariable = marks_var)#таблица марок
choose_mark = Label(window,text = f'MARK  {entry_mark.curselection()}',fg="#003b21",bg='#00AF64',relief=FLAT,bd='5')#выбранная марка
entry_model = Listbox(listvariable = vaz_model_var  )#таблица моделей
choose_model = Label(window,text = f'MODEL  {entry_model.curselection()}',fg="#003b21",bg='#00AF64',relief=FLAT,bd='5')#выбранная модель
table = ttk.Treeview(height=28, show="headings",selectmode='browse', columns=tab_header)#таблица с объявлениями
start = ttk.Button(window,text = "start",state = tkinter.NORMAL,cursor="top_left_corner",width=6,command=excel_call)#пуск парсера
link_to_car = Entry(background="#36D695", foreground="black", cursor="hand2",width=25)#ссылка на дром
lable_link = Label(window,text = 'Ccылка',fg="#003b21",bg='#00AF64',relief=FLAT,bd='5')#метка ссылки

for i in range(1, len(tab_header) + 1):#установка размеров таблицы
    if i == 3:
        table.column(f"#{i}", stretch=NO, width=425)

    elif i == 1:
        table.column(f"#{i}", stretch=NO, width=150)
    elif i == 4:
        table.column(f"#{i}", stretch=NO, width=175)

    else:
        table.column(f"#{i}", stretch=NO, width=110)


for head in tab_header:#установка названий колонок
            table.heading(head, text=head, anchor='center')


table.place(x =180 ,y = 5)
link_to_car.place(x=1045,y=40)
choose_model.place(x = 10, y = 325 )
entry_model.place (x = 10,y = 370)
choose_mark.place(x = 10 ,y = 5 )
entry_mark.place(x = 10,y = 50 )
start.place (x = 10, y = 290)
lable_link.place(x = 1045, y = 5)

window.bind('<ButtonPress>', choose )# действия по нажатию на кнопку мыши.

window.mainloop()



