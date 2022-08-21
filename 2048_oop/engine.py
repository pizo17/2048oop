from ui import *
from board import *


class Engine:
    def __init__(self):
        self.gameui = UI()
        self.size = self.gameui.get_size_input()
        self.game_board = Board(self.size)
        self.game_board.update_with_new_nums()



    def move_control(self, usr_input):
        if usr_input == "W":
                self.game_board.move_up()
        if usr_input == "A":
                self.game_board.move_left()
        if usr_input == "S":
                self.game_board.move_down()
        if usr_input == "D":
                self.game_board.move_right()



    def add_control(self, usr_input):
        if usr_input == "W":
            self.game_board.add_up()
        if usr_input == "A":
            self.game_board.add_left()
        if usr_input == "S":
            self.game_board.add_down()
        if usr_input == "D":
            self.game_board.add_right()



    def runtime(self):
        quit = False
        self.gameui.print_board(self.game_board.matrix)
        while not quit:
            self.game_board.add_done_in_cycle = False
            usr_input = self.gameui.get_control_input()
            if usr_input != "Q":
                self.add_control(usr_input)
                for i in range(self.game_board.size):
                    self.move_control(usr_input)
                    self.gameui.print_board(self.game_board.matrix)
                self.game_board.update_with_new_nums()
                self.gameui.print_board(self.game_board.matrix)
                if not self.game_board.add_done_in_cycle:
                    self.add_control(usr_input)
                    self.move_control(usr_input)
                if self.game_board.is_game_over():
                    self.gameui.print_message(1)
                    quit = True
                if self.game_board.is_game_won():
                    self.gameui.print_message(2)

            else:
                quit = True