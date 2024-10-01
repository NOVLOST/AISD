import tkinter
from itertools import count
from tkinter import *
from tkinter import ttk



HEIGHT = 800 # размер окна
WIDTH = 600

comp_sigh = 'o' # знаки игрока и компьютера
human_sigh = 'x'

count_steps = 0 # счетчик количества ходов

# координаты по которым раставляются знаки
board_coord_colect = ((200,100),(350,100),(500,100),(200,250),(350,250),(500,250),(200,400),(350,400),(500,400))

# если game_over == True то выходит сообщение о "GAME OVER!!!"
game_over_flag = False

#флаг для костыля чтобы он использовался только один раз
fix_me_flag = True
class Window(): # класс отвечает за построение окна , за сообщениея "GAME OVER" , действия при нажатии игрока на мышку

    def __init__(self,height,width):

        self.height = height #ширина и высота
        self.width = width
        self.root = Tk()
        self.root.geometry(f"{self.height}x{self.width}+200+200")
        self.root.resizable(False, False)



    def loop(self):
        self.root.mainloop()

    def printPressedButton(self,event):#действия при нажатии на мыш или клавиатуру

            mouse_x = event.x
            mouse_y = event.y  #координаты кусора



            if game_over_flag == False:# если игры не окончилась

                if (tic.draw_Human_sight(mouse_x,mouse_y) != False):# если тыкнули в правильном месте
                    my_pc.Comp_step(comp_sigh,human_sigh)# комп делает свой ход


                    if count_steps >= 9:# для того чтобы фиксировать ничью


                        win.game_over()

    def game_over(self):# выводит сообщение о окончании игры
        global game_over_flag,count_steps

        canvas = Canvas(bg="black", width=600, height=100)#надпись "GAME OVER"
        label = ttk.Label(text="GAME OVER!!!", font=("Arial", 30),background="black",foreground="yellow")

        game_over_flag = True # чтобы игрок не мог больше ходить
        count_steps = 0 # обнуляем счетчик ходов

        canvas.place( x = 100, y = 300)
        label.place(x=250, y=320)


        new_game_button = Button(win.root,text="Новая игра",command = click_new_game, background="black", fg="yellow", relief=FLAT, cursor="mouse")
        new_game_button.place(x=250 , y=420)


        exit_game_button = Button(win.root ,text="Выход", command= click_quit ,background="black", fg="yellow", relief=FLAT, cursor="mouse")
        exit_game_button.place(x=450, y = 420 )

class Board():# класс отвечает за игровую доску ,за проверку на победу и ничью ,отрисовку полей поля для GUI

    def __init__(self):

        self.board = [0,1,2,3,4,5,6,7,8]#ячейки игрового поля вместо чисел ставятся знаки игрока и компьютера
        canvas = Canvas(bg="black", width=5, height=100)
        self.borders = canvas.create_line(0, 0, 100, 0,smooth=True,fill="orange",width=10)
        canvas.place(x=50, y=50)
        self.winner_combination = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # горизонтальные комбинации
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # вертикальные комбинации
            (0, 4, 8), (2, 4, 6,))           # диагональные комбинции

    def check_winner(self,board): #метод проверяет на победу или поражение , ничью каждый ход

        winner = False

        for i in self.winner_combination:
            if (board[ i[0] ] == board[ i[1] ] and board[ i[1] ] == board[ i[2] ]):
                winner = board[ i[0] ]
        if winner == 'o':

            win.game_over()


        return winner

    def init_board_borders(self,height,widht):#отрисовка игрового поля на GUI
        coords = ((150,225),(150,375),(475,50),(325,50))#координаты линий
        widht = 500#ширина
        height = 5#высота
        count = 0#счетчик  для того чтобы начать рисовать горизонтальные линии

        for i in range(0,len(coords)):
            if count == 2 :# поворот линий на 90 градусов
                widht = 5
                height = 500

            canvas = Canvas(bg="black", width=widht, height=height)
            self.borders = canvas.create_line(0, 0, 100, 0, smooth=True, fill="black", width=10)
            canvas.place(x=coords[i][0], y=coords[i][1])
            count += 1

class TicTac():# отрисовка знака игрока


    def draw_Human_sight(self,mouse_x,mouse_y):
        global count_steps

        canvas = Canvas(bg="black", width=100, height=100)

        self.icon_x = (canvas.create_line(10, 10, 90, 90,smooth=True,fill="orange",width=10),#крестик состоит из двух пересеченных линий
                       canvas.create_line(10, 90, 90, 10,smooth=True,fill="orange",width=10))

        index = 0 #необходим чтобы записать в нужную ячейку знак
        step_was_do = False# чтобы программа не рисовала знак если игрок тычет куда не надо

        for i in board_coord_colect:
            if i[0] <= mouse_x <= i[0]+100 and i[1] <= mouse_y <= i[1]+100 : # если попал в диапазон координат то рисуем

                canvas.place(x=i[0],y=i[1])

                battle_field.board[index] = 'x'
                step_was_do = True#шаг сделан компьютер может ходить

            index += 1


        if step_was_do == False:#омпьютер ничего неделает

            return False

        count_steps += 1

        battle_field.check_winner(battle_field.board)#проверка на победу

        win.root.update()#бновляем окно


class Comp_Enemy():# это бот
    # работает так : сначало в пустые клетки пробует подставить свой знак ,если победный ход ,то делает его в текущуюю ячейку
    # иначе он делает тоже самое с знаком игрока
    # затем пробует поставить в клетки из varius_of_step это лучшие ходы в порядке убывания
    def __init__(self):
        self.varius_of_step = (4, 0, 2, 6, 8, 1, 3, 5, 7)#учшие ходы в порядке убывания

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

        if battle_field.board[5]== human_sigh and battle_field.board [7]  == human_sigh and (fix_me_flag == True) \
                and battle_field.board[8] != human_sigh and battle_field.board[8] != comp_sigh:
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

    def draw_Comp_sight(self,index):#отрисовка знака компьютера ,передаем идекс ячейки и берем ей соотвествующие координаты



        canvas = Canvas(bg="black", width=100, height=100)

        self.icon_o = canvas.create_oval(10, 10, 90, 90, fill="#80CBC4", outline="#004D40")

        canvas.place(x=board_coord_colect[index][0], y=board_coord_colect[index][1])

def click_quit():#выход по кнопке

    quit()


def click_new_game(): #новая игра по кнопке
    global game_over_flag,fix_me_flag,count_steps

    game_over_flag = False #приводим в исходное положение флаги
    fix_me_flag = True
    count_steps = 0


    main()# заново отрисовываем окно игры

def main(): #главный цикл игры

    global count_steps

    battle_field.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]#обновляем игровую доску

    canvas = tkinter.Canvas(win.root, height=win.height, width=win.width+200)#отрисовка фона
    img = tkinter.PhotoImage(file='cosmos.png')
    image = canvas.create_image(-1, -1, anchor='nw', image=img)
    canvas.place(x=0, y=0)

    battle_field.init_board_borders(HEIGHT,WIDTH)# игровое поле на GUI



    win.root.bind('<ButtonPress>', win.printPressedButton )# действия по нажатию на кнопку.

    win.loop()


win = Window(HEIGHT,WIDTH)#инициализация объектов
battle_field = Board()#доска
tic = TicTac()#знаки
my_pc = Comp_Enemy()#бот



main()#входим в главный цикл  
