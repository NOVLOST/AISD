import tkinter
from dataclasses import field
from tkinter import *
from tkinter import ttk

HEIGHT = 800
WIDTH = 600

class Window():

    def __init__(self,height,width):

        self.height = height
        self.width = width
        self.root = Tk()
        self.root.geometry(f"{self.height}x{self.width}+200+200")
        self.root.resizable(False, False)





    def loop(self):
        self.root.mainloop()






    def printPressedButton(self,event):
        mouse_x = event.x - (event.x % 10)
        mouse_y = event.y - (event.y % 10)

        print(mouse_y,mouse_x)

        tic.draw_Human_sight(mouse_x,mouse_y)







class Board():

    def __init__(self):

        self.board = [0,1,2,3,4,5,6,7,8]
        self.board_coord_colect = []
        canvas = Canvas(bg="black", width=5, height=100)
        self.borders = canvas.create_line(0, 0, 100, 0,smooth=True,fill="orange",width=10)
        canvas.place(x=50, y=50)


    def init_coord_board(self,height):

        for i in range (200, 600 ,150):
            for y in range (100, 500 ,150):
               self.board_coord_colect.append([i,y])


        return self.board_coord_colect
    def init_board_borders(self,height,widht):

        canvas = Canvas(bg="black", width=5, height=500)
        self.borders = canvas.create_line(0, 0, 100, 0, smooth=True, fill="black", width=10)
        canvas.place(x=(height // 2)+75, y=(widht // 2)-250)

        canvas = Canvas(bg="black", width=5, height=500)
        self.borders = canvas.create_line(0, 0, 100, 0, smooth=True, fill="black", width=10)
        canvas.place(x=(height // 2) - 75, y=(widht // 2) - 250)

        canvas = Canvas(bg="black", width=500, height=5)
        self.borders = canvas.create_line(0, 0, 100, 0, smooth=True, fill="black", width=10)
        canvas.place(x=150, y=225)

        canvas = Canvas(bg="black", width=500, height=5)
        self.borders = canvas.create_line(0, 0, 100, 0, smooth=True, fill="black", width=10)
        canvas.place(x=150, y=375)


class TicTac():


    def draw_Human_sight(self,mouse_x,mouse_y):

        canvas = Canvas(bg="black", width=100, height=100)

        self.icon_x = (canvas.create_line(10, 10, 90, 90,smooth=True,fill="orange",width=10),
                       canvas.create_line(10, 90, 90, 10,smooth=True,fill="orange",width=10))
        # self.icon_o = canvas.create_oval(10, 10, 200, 50, fill="#80CBC4", outline="#004D40")
        index = 0
        for i in battle_field.board_coord_colect:
            if i[0] <= mouse_x <= i[0]+100 and i[1] <= mouse_y <= i[1]+100 :

                canvas.place(x=i[0],y=i[1])

                battle_field.board[index] = 'x'
            index += 1
        print(battle_field.board)
        win.root.update()


class Comp_Enemy():
    def __init__(self):
        self.varius_of_step = (4, 0, 2, 6, 8, 1, 3, 5, 7)







win = Window(HEIGHT,WIDTH)
battle_field = Board()
tic = TicTac()


canvas = tkinter.Canvas(win.root, height=win.height, width=win.width+200)
img = tkinter.PhotoImage(file='cosmos.png')
image = canvas.create_image(-1, -1, anchor='nw', image=img)
canvas.place(x=0, y=0)

battle_field.init_coord_board(HEIGHT)
battle_field.init_board_borders(HEIGHT,WIDTH)

win.root.bind('<ButtonPress>', win.printPressedButton )


print(battle_field.board_coord_colect)


win.loop()