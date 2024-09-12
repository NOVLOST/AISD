
from tabnanny import check
from tkinter import *
from tkinter import ttk
from random import *
from tkinter import messagebox
import csv

#NOTE:осталось добавить надписи на секторы и сделать ctrl+C  ctrl+V для рабочих и все :D
#----------------------


order_list = [] #в него добавляются строки из файла
circle_list = []#хранит объекты класса Circle_diagram():
check_list = [] #хранит имена которые УЖЕ подсчитаны
headrs = ["№","Phone","Name","Worker"] #заголовки для таблицы
circle_colors = ["red","orange","yellow","green","skyblue","darkblue","purple"]#цвета для диаграммы
unic_worker_color_list = []#хранит имена закачиков без повторений для указания к какому из них относиться цвет на круге
unic_customer_color_list = []# тоже самое что выше только для рабочих

#-----------------------


class Circle_diagram(): #принимает количество повторов имени закачика , рабочего  сами их имена и цвет для круга
    def __init__(self,name_num,worker_num,cust_tag,work_tag,color):
        self.coord = 10,10,300,300
        # self._start_angel = 0
        # self.end_angel = 0
        self.outline = "orange"
        self.width = 4
        # self.color = 'red'
        self.count_name = name_num
        self.count_worker = worker_num
        self.customer_tag = cust_tag
        self.worker_tag = work_tag
        self.paint_color = color



class Order(): #принимает номер заказа , телефона , имя заказчика ,имя рабочего это и есть класс договора
    def __init__(self,number,phone_number,customer_name,worker_name):
        self.customer = customer_name
        self.worker = worker_name
        self.order_number = number
        self.phone = phone_number



class Window(): # окно на котом все рисуется
    def __init__(self):
        self.height = 850
        self.width  =  720
        self.win = Tk()
        self.win.geometry(f"{self.height}x{self.width}+200+200")
        self.win.resizable(False, False)
        self.win.config(bg='#007241')
        welcome = Label(self.win, text='Здравствейте!Вся информация о ваших клиента в одном приложении',fg = "#003b21",bg = '#00AF64',relief=FLAT,bd='5')
        welcome.place(x=self.height//2-200,y=self.width*0.1-70)



    def registration(self):#чтение из файла (предупреждение об его отсуствии) и создание таблицы

        count_name = 0 #для посчета имен
        count_worker = 0




        #таблица с именами
        #-------------------------------
        table = ttk.Treeview(height=5, show="headings", columns=headrs)#таблица с заказами
        table.place(x=20,y=50)
        #-------------------------------



        #заголовки таблицы
        #------------------------------
        for head in headrs:
            table.heading(head,text=head,anchor='center')
        #------------------------------


        #первое чтение при запуске программы
        #-------------------------------
        try: #пробуем читать файл
            with open('Orders.csv', 'r') as file:
                for contact in csv.reader(file):
                    table.insert("", END, values=contact)
                    order_list.append(Order(contact[0], contact[1], contact[2],contact[3]))



                count = 0

                for i_el in order_list: #берем имя и просто перебираем ,считатаем  а конце добовляем в спискок УЖЕ использованных имен
                    for y_el in order_list:#иначе лишенего насчитаем ,а также набиваем список именами БЕЗ повторов



                        if i_el.customer not in  check_list  and i_el.customer == y_el.customer:
                            count_name += 1


                        if i_el.worker not in check_list  and i_el.worker == y_el.worker:
                            count_worker += 1







                        if i_el.worker not in unic_worker_color_list:
                            unic_worker_color_list.append(i_el.worker)


                        elif i_el.customer not in unic_customer_color_list:
                            unic_customer_color_list.append(i_el.customer)



                    circle_list.append(Circle_diagram(count_name,count_worker,i_el.customer,i_el.worker,circle_colors[count]))
                    check_list.append(i_el.customer)
                    check_list.append(i_el.worker)
                    count_worker = 0
                    count_name = 0
                    count += 1
                    if count == 7:
                        count = 0



        except IOError:
            Error_mesage = messagebox.showerror("FILE ERROR", "ФАЙЛ НЕ ОБНАРУЖЕН")





        check_list.clear()#чтоб памать не ел







    def diagram(self):#рисуем круг


        sum_names=0
        sum_workers=0


        for el in circle_list: # общее количество имен считаем и делим на 360 получем одну часть которую надо умножить на кол-во одного из имени
            sum_names += el.count_name
            sum_workers += el.count_worker



        one_part_names = 360 / sum_names
        one_part_workers = 360 / sum_workers



        arhc_canvas_names = Canvas(win.win,bg="#007241",width=300,height=300)
        arhc_canvas_workers = Canvas(win.win, bg="#007241", width=300, height=300) #круги



        last_coord_names = 0
        last_coord_workers = 0 # нужно для того чтобы не рисовать последующие секторы с 0
        y_tag_cicrle = 410 #стратовая координата для имен с цветами
        unic_count_names = 0 #для цвета к каждому имени
        unic_count_workers = 0



        for el in circle_list: # рисуем  диаграммы

            arhc_names = arhc_canvas_names.create_arc(el.coord,start = last_coord_names,extent = (el.count_name * one_part_names ),
                                                fill =el.paint_color,outline = el.outline , width = el.width  )
            arhc_canvas_names.place(x=120,y=415)



            arhc_workers = arhc_canvas_workers.create_arc(el.coord, start=last_coord_workers, extent=(el.count_worker * one_part_workers),
                                                fill=el.paint_color, outline=el.outline, width=el.width)
            arhc_canvas_workers.place(x=540, y=415)




            if unic_count_names != len(unic_customer_color_list):

                circle_name_tag = Label(win.win, text=f'{unic_customer_color_list[unic_count_names]}', fg="#003b21",bg='#00AF64', relief=FLAT, bd='5')
                circle_name_tag.place(x=30, y=y_tag_cicrle)


                paint_tag_names = Canvas(win.win, bg=el.paint_color, width=10, height=10)
                paint_tag_names.place(x=10, y=y_tag_cicrle + 10)

                unic_count_names += 1


            if unic_count_workers != len(unic_worker_color_list):

                circle_worker_tag = Label(win.win, text=f'{unic_worker_color_list[unic_count_workers]}', fg="#003b21",bg='#00AF64', relief=FLAT, bd='5')
                circle_worker_tag.place(x=450, y=y_tag_cicrle)


                paint_tag_workers = Canvas(win.win, bg=el.paint_color, width=10, height=10)
                paint_tag_workers.place(x=430, y=y_tag_cicrle + 10)

                unic_count_workers += 1


            last_coord_names = el.count_name * one_part_names + last_coord_names #тоесть сколько градусов на одно кол-во имен + прошлые коорды
            last_coord_workers = el.count_worker * one_part_workers + last_coord_workers

            y_tag_cicrle += 40







    #функция для поиска заказов по имени
    #-----------------------------------
    def search(self):

       #функция добавления найденого имени в таблицу

        def get_search():

            #очистка таблицы
            search_table.delete(*search_table.get_children())


            search_name = entry_search.get()
            for el in order_list:
                if el.worker  == search_name or el.customer == search_name:
                    search_table.insert("",END,values=(el.order_number,el.phone,el.customer,el.worker))

        #-------------------------------

       #текст , кнопка и таблица для найденых имен(органы управления)
       #--------------------------------
        search_tag = Label(self.win, text = "Введите имя заказчика или рабочего ",fg="#003b21",bg='#00AF64',relief=FLAT,bd='5' )
        search_tag.place(x = 90,y = 340)



        entry_search = Entry(background="#36D695", foreground="black", cursor="hand2")
        entry_search.place(x = 20,y = 380)



        search_button = Button(text="Ввод", command=get_search,background="#00AF64",fg = "#003b21",relief=FLAT,cursor="mouse")
        search_button.place(x = 20,y = 340)



        search_table = ttk.Treeview(height=5, show="headings", columns=headrs)
        search_table.place(x = 20, y = 200)
        #----------------------------------


        # заголовки таблицы
        # ------------------------------
        for head in headrs:
            search_table.heading(head,text = head, anchor = 'center')
        # ------------------------------




    def loop(self):
        self.win.mainloop()




win = Window()

style = ttk.Style(win.win)


style.theme_use("clam")#нужно чтобы изменить фон на treeview
style.configure("Treeview",   fieldbackground="#00AF64")

win.registration()
win.diagram()
win.search()
win.loop()



