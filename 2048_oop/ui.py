from color_management import *
import os
import time



class UI:
    def __init__(self):
        self.valid_inputs = ["W", "A", "S", "D", "Q"]
        self.col_manager = Color_Manager()



    def get_control_input(self):
        usr_input = input().upper()
        while usr_input not in self.valid_inputs:
            usr_input = input().upper()
        return usr_input



    def get_size_input(self):
        os.system('cls')
        size = input("Please specify the size of the game area:\n")
        while not size.isnumeric():
            os.system('cls')
            size = input("The entered value is invalid.\nPlease specify the size of the game area:\n")
        return int(size)



    def print_board(self, matrix):
        os.system('cls')
        for row in matrix:
            for elem in row:
                color = self.col_manager.bg_col.white + self.col_manager.fg_col.black
                if not elem.value == " ":
                    color = self.col_manager.choose_color(elem.value)
                print(f"{color}[{elem.value : ^4}]", end="")
            print()
        print(f"{self.col_manager.bg_col.black}{self.col_manager.fg_col.white}Use W, A, S, D keys to play, press Q to quit\n")
        time.sleep(0.5)



    def print_message(self, message_id):
        if message_id == 1:
            print("You lost!")
        if message_id == 2:
            print("You win, but you can keep playing!")