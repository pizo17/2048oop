import math
import random
import os
import time


class Foreground_Colors:
    def __init__(self):
        self.black = "\u001b[30m"
        self.red = "\u001b[31m"
        self.green = "\u001b[32m"
        self.yellow = "\u001b[33m"
        self.blue = "\u001b[34m"
        self.magenta = "\u001b[35m"
        self.cyan = "\u001b[36m"
        self.white = "\u001b[37m"
        self.bright_black = "\u001b[30;1m"
        self.bright_red = "\u001b[31;1m"
        self.bright_green = "\u001b[32;1m"
        self.bright_yellow = "\u001b[33;1m"
        self.bright_blue = "\u001b[34;1m"
        self.bright_magenta = "\u001b[35;1m"
        self.bright_cyan = "\u001b[36;1m"
        self.bright_white = "\u001b[37;1m"
        self.reset = "\u001b[0m"

class Background_Colors:
    def __init__(self):
        self.black = "\u001b[40m"
        self.red = "\u001b[41m"
        self.green = "\u001b[42m"
        self.yellow = "\u001b[43m"
        self.blue = "\u001b[44m"
        self.magenta = "\u001b[45m"
        self.cyan = "\u001b[46m"
        self.white = "\u001b[47m"
        self.bright_black = "\u001b[40;1m"
        self.bright_red = "\u001b[41;1m"
        self.bright_green = "\u001b[42;1m"
        self.bright_yellow = "\u001b[43;1m"
        self.bright_blue = "\u001b[44;1m"
        self.bright_magenta = "\u001b[45;1m"
        self.bright_cyan = "\u001b[46;1m"
        self.bright_white = "\u001b[46;1m"
        self.reset = "\u001b[47;1m"



class Color_Manager:
    def __init__(self):
        self.fg_col = Foreground_Colors()
        self.bg_col = Background_Colors()
        self.exponent_codes = {2: 1, 
                                4: 2, 
                                8: 3, 
                                16: 4, 
                                32: 5, 
                                64: 6, 
                                128: 7, 
                                256: 8}
        self.col_codes = {1: self.bg_col.white + self.fg_col.black, 
                            2: self.bg_col.yellow + self.fg_col.black, 
                            3: self.bg_col.red + self.fg_col.white, 
                            4: self.bg_col.green + self.fg_col.black,
                            5: self.bg_col.cyan + self.fg_col.black, 
                            6: self.bg_col.blue + self.fg_col.white,
                            7: self.bg_col.magenta + self.fg_col.white, 
                            8: self.bg_col.black + self.fg_col.white} 



    def choose_color(self, number):
        color = self.bg_col.black
        if number in self.exponent_codes:
            color = self.col_codes.get(self.exponent_codes.get(number))
        else:
            power = math.log(number, 2)
            color = self.col_codes.get(power % 8)
        return color




class Coord_pair:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor



class Cell:
    def __init__(self, x_coor, y_coor, value, color =  "\u001b[47m"):
        self.coordinates = Coord_pair(x_coor, y_coor) 
        self.value = value
        self.color = color
    


    def update_value(self, value):
        self.value = value

    

    def update_color(self):
        pass

    
    def add_value(self, value):
        self.value += value


class Board:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.num_of_empty_cells = 0
        self.add_done_in_cycle =False
        self.build_board(size)

    

    def build_board(self, size):
        for i in range(size):
            row = []
            for j in range(size):
                cell = Cell(i, j, " ")
                row.append(cell)
            self.matrix.append(row)
        self.num_of_empty_cells = size * size
    

    def choose_next_number(self):
        wheighted_number_list = [2, 2, 2, 2, 4, 2, 2, 2, 2, 4]
        num_index = random.randint(0, 9)
        return wheighted_number_list[num_index]



    def choose_random_coordinates(self, size):
        return Coord_pair(random.randint(0, size), random.randint(0, size))



    def is_position_free(self, matrix, coords):
        return matrix[coords.x_coor][coords.y_coor].value == " "




    def add_coord_pair(self):
        if self.num_of_empty_cells > 0:
            coords = self.choose_random_coordinates(len(self.matrix)-1)
            while not self.is_position_free(self.matrix, coords):
                coords = self.choose_random_coordinates(len(self.matrix)-1)
            return coords

    def check_empty_cells(self):
        if self.num_of_empty_cells >= 2:
            return 2
        else:
            return self.num_of_empty_cells


    def update_with_new_nums(self):
        num_of_empty = self.check_empty_cells()
        for i in range(num_of_empty):
            coords = self.add_coord_pair()
            value = self.choose_next_number()
            self.matrix[coords.x_coor][coords.y_coor].value = value
            self.num_of_empty_cells -= 1



    def check_eq_side_to_side(self, i, j):
        return (j > 0 and self.matrix[i-1][j].value == self.matrix[i-1][j-1].value or 
                j < self.size-1 and self.matrix[i-1][j].value == self.matrix[i-1][j+1].value)


    def check_eq_up_down(self, i, j):
        return (i > 0 and self.matrix[i][j-1].value == self.matrix[i][j-1].value or
                i < self.size-1 and self.matrix[i][j-1].value == self.matrix[i-1][j-1].value)


    def cell_eq_check(self, i, j):
        if i > 0:
            if (self.matrix[i][j].value == self.matrix[i-1][j].value or 
                self.check_eq_side_to_side(i, j)):
                return True
        if j > 0:
            if (self.matrix[i][j].value == self.matrix[i][j-1].value or 
                self.check_eq_up_down(i, j)):
                return True
        if i < self.size-1:
            if (self.matrix[i][j].value == self.matrix[i+1][j].value or
                self.check_eq_side_to_side(i, j)):
                return True
        if j < self.size-1:
            if (self.matrix[i][j].value == self.matrix[i][j+1].value or
                self.check_eq_up_down(i, j)):
                return True
        return False


    def is_game_over(self):
        if self.num_of_empty_cells == 0:
            for i in range(1, self.size, 2):
                for j in range(1, self.size, 2):
                    if self.cell_eq_check(i, j):
                        return False
            return True
        return False



    def is_game_won(self):
        game_won = False
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j].value == 2048:
                    game_won = True
        return game_won



    def move_logic(self, i, j, i_offset=0, j_offset=0):
        if self.matrix[i+i_offset][j+j_offset].value == " " and self.matrix[i][j].value != " ":
            self.matrix[i+i_offset][j+j_offset].update_value(self.matrix[i][j].value)
            self.matrix[i][j].update_value(" ")



    def add_logic(self, excluded_indices, i, j, i_offset=0, j_offset=0):
        examined_index = j if i_offset != 0 else i
        if examined_index not in excluded_indices:
            if self.matrix[i][j].value == " ":
                return j if i_offset != 0 else i
            elif self.matrix[i][j].value == self.matrix[i+i_offset][j+j_offset].value:
                self.matrix[i+i_offset][j+j_offset].add_value(self.matrix[i][j].value)
                self.matrix[i][j].update_value(" ")
                self.num_of_empty_cells += 1
                self.add_done_in_cycle = True
                return j if i_offset != 0 else i



    def move_up(self):
        for i in range(1, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.move_logic(i, j, -1)



    def move_down(self):
        for i in reversed(range(len(self.matrix)-1)):
            for j in range(len(self.matrix[i])):
                self.move_logic(i, j, 1)



    def move_left(self):
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[i])):
                self.move_logic(i, j, 0, -1)
                


    def move_right(self):
        for i in range(len(self.matrix)):
            for j in reversed(range(len(self.matrix[i])-1)):
                self.move_logic(i, j, 0, 1)



    def add_up(self):
        excluded_indices = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                excluded_indices.add(self.add_logic(excluded_indices, i, j, -1))
            


    def add_down(self):
        excluded_indices = set()
        for i in reversed(range(len(self.matrix)-1)):
            for j in range(len(self.matrix[i])):
                excluded_indices.add(self.add_logic(excluded_indices, i, j, 1))
                


    def add_left(self):
        excluded_indices = set()
        for i in range(len(self.matrix)):   
            for j in range(1, len(self.matrix[i])):
                excluded_indices.add(self.add_logic(excluded_indices, i, j, 0, -1))



    def add_right(self):
        excluded_indices = set()
        for i in range(len(self.matrix)):
            for j in reversed(range(len(self.matrix[i])-1)):
                excluded_indices.add(self.add_logic(excluded_indices, i, j, 0, 1))



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





def main():
    engine = Engine()
    engine.runtime()

main()