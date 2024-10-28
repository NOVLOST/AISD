
import tkinter
import time
from tkinter import *
from tkinter import ttk



open_flag = False #отвечает за отрытое положение микроволновки
work_flag = False #отвечает за рабочее положение микроволновки
rozet_flag =True  #вкл/выкл вылки из разетки
time_minute = 0   #кол-во минут на таймере
time_second = 0   #кол-во секунд на таймере
minut_string = "" #строки вывода на таймер
second_string = ""


class Window(): # окно на котом все рисуется
    def __init__(self):
        self.height = 850
        self.width  =  720
        self.win = Tk()
        self.win.geometry(f"{self.height}x{self.width}+200+200")
        self.win.resizable(False, False)
        self.win.config(bg='#007241')
        self.canvas = tkinter.Canvas(self.win, height=self.height, width=self.width, bg="white")  # отрисовка фона


    def loop(self):
        self.win.mainloop()

    def printPressedButton(self, event):  # действия при нажатии на мыш или клавиатуру
        global canvas, img, open_flag,work_flag, rozet_flag,img_rozet

        #
        # Close/Open
        #
        if 450 <= event.x <=600 and 250 <= event.y <= 300 and open_flag== False:

            img = PhotoImage(file='microwave_opened.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            open_flag = True
        elif 450 <= event.x <= 600 and 250 <= event.y <= 300 and open_flag== True:

            img = PhotoImage(file='microwave_close.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            open_flag = False


        #
        # ON/OFF Eсли розетка не воткнута то работать печь не будет
        #
        elif 450 <= event.x <= 600 and 10 <= event.y <= 250 and (work_flag == False and rozet_flag == False) :

             # отрисовка фона
            img = PhotoImage(file='microwave_work.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            work_flag = True

        elif 450 <= event.x <= 600 and 10 <= event.y <= 250 and work_flag == True:

              # отрисовка фона
            img = PhotoImage(file='microwave_close.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            work_flag = False

        #
        # Розетка вкл/выкл
        #

        elif 750 <= event.x <= 900 and 10 <= event.y <= 250 and rozet_flag == True:


            img_rozet = PhotoImage(file='rozet.png')
            canvas.create_image(600, 10, anchor='nw', image=img_rozet)

            rozet_flag = False

        elif 750 <= event.x <= 900 and 30 <= event.y <= 150 and rozet_flag == False:

            img_rozet = PhotoImage(file='rozet_off.png')
            canvas.create_image(600, 10, anchor='nw', image=img_rozet)

            img = PhotoImage(file='microwave_close.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            rozet_flag = True
            work_flag = False
    #---------------------------
    #ЛОГИКА ТАЙМЕРА ПО МИНУТАМ
    #---------------------------
    def logic_timer_minute(self,time):
        global time_minute,minut_string

        if 0 < time < 10:
            minut_string = f"0{time_minute}"
        elif 0 < time < 100:
            minut_string = f"{time_minute}"
        elif time < 0: # чтобы не выдавало -1 на таймере

            minut_string = f"00"

        else:# когда кол-во минут большее 100
            time_minute = 0
            minut_string = f"0{time_minute}"

        #отображение минут
        minute = Label(win.win, text=minut_string, fg="orange", bg='black', relief=FLAT, bd='5', font=("Arial", 20))
        minute.place(x=480, y=40)
        self.win.update()

    def timer_minute(self): # функция прибавления времени
        global time_minute,minut_string

        time_minute += 1

        self.logic_timer_minute(time_minute)

    # ---------------------------
    # ЛОГИКА ТАЙМЕРА ПО СЕКУНДАМ
    # ---------------------------
    def logic_timer_second(self,time):#
        global time_second, second_string


        if 10 <= time < 60:
            second_string = f"{time_second}"

        elif time < 0: # чтобы не выдавало -1 на таймере
            time_second = 0
            second_string = f"0{time_second}"

        elif time < 10:
            second_string = f"0{time_second}"

        else : #чтобы секунды больше 60 переводить в минуту
            win.timer_minute()
            time_second = 0
            second_string = f"0{time_second}"



        second = Label(win.win, text=f': {second_string}', fg="orange", bg='black', relief=FLAT, bd='5',font=("Arial", 20))
        second.place(x=520, y=40)
        self.win.update()



    def timer_second(self):
        global time_second, second_string

        time_second += 10

        self.logic_timer_second(time_second)

    #если секунды < 0 отнимаем 1 минуту и смотрим, если < 0 минут осталось то выходим иначе отсчитываем секунды дальше
    def countdown(self):
        global time_second,time_minute

        while (time_minute > 0 or time_second > 0):
            time_second -= 1
            self.win.after(1000,self.logic_timer_second(time_second))
            if time_second <= 0:
                time_minute -= 1
                self.win.after(1000, self.logic_timer_minute(time_minute))
                if time_minute >= 0:
                    time_second = 59
                    self.win.after(1000, self.logic_timer_second(time_second))

                else:
                    time_second = 0
                    self.win.after(1000, self.logic_timer_second(time_second))
                    

    #кнопка сброс
    def reset(self):
        global time_second, time_minute

        time_second = 0
        time_minute = 0

        second = Label(win.win, text=': 00', fg="orange", bg='black', relief=FLAT, bd='5',font=("Arial", 20))
        second.place(x=520, y=40)

        minute = Label(win.win, text='00', fg="orange", bg='black', relief=FLAT, bd='5', font=("Arial", 20))
        minute.place(x=480, y=40)




win = Window()

# необязательно каждый раз рисовать canvas можно просто вызывать create_image и лепать на старом canvas

canvas = Canvas(win.win, height=win.width, width=win.height)  # отрисовка фона
img = PhotoImage(file='microwave_close.png')
canvas.create_image(-1, -1, anchor='nw', image=img)

img_rozet = PhotoImage(file='rozet_off.png') # отрисовка розетки
canvas.create_image(600, 10, anchor='nw', image=img_rozet)

#отрисовка дисплея таймера
minute = Label(win.win, text='00',fg = "orange",bg = 'black',relief=FLAT,bd='5',font=("Arial", 20))
second = Label(win.win, text=': 00',fg = "orange",bg = 'black',relief=FLAT,bd='5',font=("Arial", 20))

#кнопки добавления минут,секунд сброс и пуск
add_minute = ttk.Button(win.win,text = "+1 мин",cursor="top_left_corner",width=6,command=win.timer_minute)
add_second = ttk.Button(win.win,text = "+10 сек",cursor="top_left_corner",width=6 ,command=win.timer_second)
reset_time = ttk.Button(win.win,text = "сброс",cursor = "top_left_corner",width = 6,command=win.reset)
start = ttk.Button(win.win,text = "пуск",cursor="top_left_corner",width=6 ,command=win.countdown)

minute.place(x = 480 , y = 40)
second.place(x = 520 , y = 40 )
reset_time.place(x = 530 , y = 150  )
start.place (x = 460, y = 150)
add_minute.place(x = 460,y=200 )
add_second.place(x = 530,y=200 )
canvas.place(x=0,y=0)



win.win.bind('<ButtonPress>', win.printPressedButton )# действия по нажатию на кнопку мыши.

win.loop()