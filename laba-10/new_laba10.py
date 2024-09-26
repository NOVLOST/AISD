import tkinter
from itertools import count
from tkinter import *
from tkinter import ttk



HEIGHT = 800
WIDTH = 600

comp_sigh = 'o'
human_sigh = 'x'

count_steps = 0


game_over_flag = False
fix_me_flag = True
class Window():

    def __init__(self,height,width):

        self.height = height
        self.width = width
        self.root = Tk()
        self.root.geometry(f"{self.height}x{self.width}+200+200")
        self.root.resizable(False, False)
        self.can_play_flag = True





    def loop(self):
        self.root.mainloop()






    def printPressedButton(self,event):

            mouse_x = event.x - (event.x % 10)
            mouse_y = event.y - (event.y % 10)



            if game_over_flag == False:

                if (tic.draw_Human_sight(mouse_x,mouse_y) != False):
                    my_pc.Comp_step(comp_sigh,human_sigh)

                    print(count_steps)
                    if count_steps >= 9:


                        win.game_over()

    def game_over(self):
        global game_over_flag,count_steps

        canvas = Canvas(bg="black", width=600, height=100)
        label = ttk.Label(text="GAME OVER!!!", font=("Arial", 30),background="black",foreground="yellow")

        game_over_flag = True
        count_steps = 0

        canvas.place( x = 100, y = 300)
        label.place(x=250, y=320)




        new_game_button = Button(win.root,text="Новая игра",command = click_new_game, background="black", fg="yellow", relief=FLAT, cursor="mouse")
        new_game_button.place(x=250 , y=420)


        exit_game_button = Button(win.root ,text="Выход", command= click_quit ,background="black", fg="yellow", relief=FLAT, cursor="mouse")
        exit_game_button.place(x=450, y = 420 )

















class Board():

    def __init__(self):

        self.board = [0,1,2,3,4,5,6,7,8]
        self.board_coord_colect = []
        canvas = Canvas(bg="black", width=5, height=100)
        self.borders = canvas.create_line(0, 0, 100, 0,smooth=True,fill="orange",width=10)
        canvas.place(x=50, y=50)
        self.winner_combination = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # горизонтальные комбинации
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикальные комбинации
            (0, 4, 8), (2, 4, 6,))           # диагональные комбинции


    def init_coord_board(self,height):

        for i in range (100,500,150):
            for y in range (200,600,150):
               self.board_coord_colect.append([y,i])

        return self.board_coord_colect



    def check_winner(self,board):

        winner = False

        for i in self.winner_combination:
            if (board[ i[0] ] == board[ i[1] ] and board[ i[1] ] == board[ i[2] ]):
                winner = board[ i[0] ]
        if winner == 'o':

            win.game_over()


        return winner



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
        global count_steps

        canvas = Canvas(bg="black", width=100, height=100)

        self.icon_x = (canvas.create_line(10, 10, 90, 90,smooth=True,fill="orange",width=10),
                       canvas.create_line(10, 90, 90, 10,smooth=True,fill="orange",width=10))

        index = 0
        step_was_do = False

        for i in battle_field.board_coord_colect:
            if i[0] <= mouse_x <= i[0]+100 and i[1] <= mouse_y <= i[1]+100 :

                canvas.place(x=i[0],y=i[1])

                battle_field.board[index] = 'x'
                step_was_do = True

            index += 1


        if step_was_do == False:

            return False

        count_steps += 1

        battle_field.check_winner(battle_field.board)

        win.root.update()


class Comp_Enemy():
    def __init__(self):
        self.varius_of_step = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    def Comp_step(self,comp_sign,human_sign):
        global count_steps
        global fix_me_flag
        save_free_cell = 0


        for sign in (comp_sign,human_sign):
            for index in range(0,len(battle_field.board)):
                save_free_cell = battle_field.board[index]
                if type(battle_field.board[index]) == int :
                    battle_field.board[index] = sign


                if (battle_field.check_winner(battle_field.board)!= False):
                    self.draw_Comp_sight(index)
                    battle_field.board[index] = comp_sign

                    count_steps += 1
                    return 0

                else:
                    battle_field.board[index] = save_free_cell

        if battle_field.board[5]== human_sigh and battle_field.board [7]  == human_sigh and (fix_me_flag == True) and battle_field.board[8] != human_sigh:
            fix_me_flag = False
            self.draw_Comp_sight(8)
            battle_field.board[8] = comp_sigh
            battle_field.check_winner(battle_field.board)
            count_steps += 1
            return 0

        for el in self.varius_of_step:
            if el in battle_field.board:
                battle_field.board[el] = comp_sign
                self.draw_Comp_sight(el)
                count_steps += 1

                return 0








    def draw_Comp_sight(self,index):



        canvas = Canvas(bg="black", width=100, height=100)

        self.icon_o = canvas.create_oval(10, 10, 90, 90, fill="#80CBC4", outline="#004D40")

        canvas.place(x=battle_field.board_coord_colect[index][0], y=battle_field.board_coord_colect[index][1])




def click_quit():

    quit()


def click_new_game():
    global game_over_flag,fix_me_flag,count_steps

    game_over_flag = False
    fix_me_flag = True
    count_steps = 0


    main()



def main():

    global count_steps

    battle_field.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    canvas = tkinter.Canvas(win.root, height=win.height, width=win.width+200)
    img = tkinter.PhotoImage(file='cosmos.png')
    image = canvas.create_image(-1, -1, anchor='nw', image=img)
    canvas.place(x=0, y=0)


    battle_field.init_board_borders(HEIGHT,WIDTH)



    win.root.bind('<ButtonPress>', win.printPressedButton )





    win.loop()


win = Window(HEIGHT,WIDTH)
battle_field = Board()
tic = TicTac()
my_pc = Comp_Enemy()

battle_field.init_coord_board(HEIGHT)

main()
