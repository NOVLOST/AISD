
import tkinter
from tkinter import *
from tkinter import ttk



open_flag = False #отвечает за отрытое положение микроволновки
work_flag = False #отвечает за рабочее положение микроволновки
rozet_flag =True  #вкл/выкл вылки из разетки
time = 0   #время работы храниться в секундах
power_state = "disable"



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
        global canvas, img, open_flag,work_flag, rozet_flag,img_rozet,power_state,reset_time,add_second,add_minute,start

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
        # Розетка вкл/выкл
        #

        elif 750 <= event.x <= 900 and 10 <= event.y <= 250 and rozet_flag == True:


            img_rozet = PhotoImage(file='rozet.png')
            canvas.create_image(600, 10, anchor='nw', image=img_rozet)

            # вкл/выкл кнопок взависимотси от состояния розетки
            rozet_flag = False
            reset_time['state']= tkinter.NORMAL
            start['state'] = tkinter.NORMAL
            add_second['state'] = tkinter.NORMAL
            add_minute['state'] = tkinter.NORMAL


        elif 750 <= event.x <= 900 and 30 <= event.y <= 150 and rozet_flag == False:

            img_rozet = PhotoImage(file='rozet_off.png')
            canvas.create_image(600, 10, anchor='nw', image=img_rozet)

            img = PhotoImage(file='microwave_close.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)


            #вкл/выкл кнопок взависимотси от состояния розетки
            rozet_flag = True
            work_flag = False
            reset_time['state']= tkinter.DISABLED
            start['state'] = tkinter.DISABLED
            add_second['state'] = tkinter.DISABLED
            add_minute['state'] = tkinter.DISABLED
    #---------------------------
    #ЛОГИКА ТАЙМЕРА ПО МИНУТАМ И СЕКУНДАМ
    #---------------------------
    def logic_timer(self,minute,seconds):


        #логика минут
        if 0 < minute < 10:
            minut_string = f"0{minute}"

        elif 0 < minute < 100:
            minut_string = f"{minute}"

        else:# когда кол-во минут большее 100
            minute = 0
            minut_string = f"0{minute}"





        #логика секунд
        if 10 <= seconds < 60:
            second_string = f"{seconds}"

        elif seconds < 10:
            second_string = f"0{seconds}"

        else : #чтобы секунды больше 60 переводить в минуту
            seconds = 0
            second_string = f"0{seconds}"


        #отображение секунд
        second_label = Label(win.win, text=f': {second_string}', fg="orange", bg='black', relief=FLAT, bd='5',font=("Arial", 20))
        second_label.place(x=520, y=40)

        #отображение минут
        minute_label = Label(win.win, text=minut_string, fg="orange", bg='black', relief=FLAT, bd='5', font=("Arial", 20))
        minute_label.place(x=480, y=40)
        self.win.update()

    def timer_minute(self): # функция прибавления времени
        global time

        time += 60
        #первый аргумент минуты второй секунды
        self.logic_timer(time // 60,time - ((time // 60) * 60))





    def timer_second(self):
        global time

        time += 10

        self.logic_timer(time // 60,time - ((time // 60) * 60))

    #---------------------------------------------------------------
    #СЧЕТЧИК:отнимаем секунду и отправляем минуты и секунды на обработку
    #------------------------------------------------------------------
    def countdown(self):
        global time,img,canvas,open_flag

        if (work_flag == False and rozet_flag == False):
            open_flag = False
            img = PhotoImage(file='microwave_work.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)


            while ( time > 0 ) and (rozet_flag == False) and (open_flag == False):

                time -= 1
                min = time // 60
                sec = time - (min * 60)
                self.win.after(1000, self.logic_timer(min,sec))

            if open_flag == False:
                img = PhotoImage(file='microwave_close.png')
                canvas.create_image(-1, -1, anchor='nw', image=img)





    #кнопка сброс
    def reset(self):
        global time,work_flag,img,canvas

        time = 0

        second_label = Label(win.win, text=': 00', fg="orange", bg='black', relief=FLAT, bd='5',font=("Arial", 20))
        second_label.place(x=520, y=40)

        minute_label = Label(win.win, text='00', fg="orange", bg='black', relief=FLAT, bd='5', font=("Arial", 20))
        minute_label.place(x=480, y=40)

        img = PhotoImage(file='microwave_close.png')
        canvas.create_image(-1, -1, anchor='nw', image=img)

        work_flag = False




win = Window()

# необязательно каждый раз рисовать сanvas можно просто вызывать create_image и лепать на старом canvas

canvas = Canvas(win.win, height=win.width, width=win.height)  # отрисовка фона
img = PhotoImage(file='microwave_close.png')
canvas.create_image(-1, -1, anchor='nw', image=img)

img_rozet = PhotoImage(file='rozet_off.png') # отрисовка розетки
canvas.create_image(600, 10, anchor='nw', image=img_rozet)

#отрисовка дисплея таймера
minute_label = Label(win.win, text='00',fg = "orange",bg = 'black',relief=FLAT,bd='5',font=("Arial", 20))
second_label = Label(win.win, text=': 00',fg = "orange",bg = 'black',relief=FLAT,bd='5',font=("Arial", 20))

#кнопки добавления минут,секунд сброс и пуск
add_minute = ttk.Button(win.win,text = "+1 мин",state = tkinter.DISABLED,cursor="top_left_corner",width=6,command=win.timer_minute)
add_second = ttk.Button(win.win,text = "+10 сек",state = tkinter.DISABLED,cursor="top_left_corner",width=6 ,command=win.timer_second)
reset_time = ttk.Button(win.win,text = "сброс",state = tkinter.DISABLED,cursor = "top_left_corner",width = 6,command=win.reset)
start = ttk.Button(win.win,text = "пуск",state = tkinter.DISABLED,cursor="top_left_corner",width=6 ,command=win.countdown)

minute_label.place(x = 480 , y = 40)
second_label.place(x = 520 , y = 40 )
reset_time.place(x = 530 , y = 150  )
start.place (x = 460, y = 150)
add_minute.place(x = 460,y=200 )
add_second.place(x = 530,y=200 )
canvas.place(x=0,y=0)



win.win.bind('<ButtonPress>', win.printPressedButton )# действия по нажатию на кнопку мыши.

win.loop()