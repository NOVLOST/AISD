
import tkinter
from tkinter import *



open_flag = False
work_flag = False
rozet_flag =True

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
        if 30 <= event.x <=450 and 10 <= event.y <= 450 and open_flag== False:

            img = PhotoImage(file='microwave_opened.png')
            canvas.create_image(-1, -1, anchor='nw', image=img)

            open_flag = True
        elif 10 <= event.x <= 450 and 10 <= event.y <= 350 and open_flag== True:

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


win = Window()

# необязательно каждый раз рисовать canvas можно просто вызывать create_image и лепать на старом canvas

canvas = Canvas(win.win, height=win.width, width=win.height)  # отрисовка фона
img = PhotoImage(file='microwave_close.png')
canvas.create_image(-1, -1, anchor='nw', image=img)

img_rozet = PhotoImage(file='rozet_off.png') # отрисовка розетки
canvas.create_image(600, 10, anchor='nw', image=img_rozet)
canvas.place(x=0,y=0)

win.win.bind('<ButtonPress>', win.printPressedButton )# действия по нажатию на кнопку мыши.

win.loop()