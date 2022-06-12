import random



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
        self.magenta = "\u001b[44m"
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



class Board:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.build_board(size)

    

    def build_board(self, size):
        for i in range(size):
            row = []
            for j in range(size):
                cell = Cell(i, j, " ")
                row.append(cell)
            self.matrix.append(row)
    


    def update_with_new_num(self, coords, value):
        self.matrix[coords.x_coor][coords.y_coor].value = value




    def move_logic(self, i, j, i_offset=0, j_offset=0):
        if self.matrix[i+i_offset][j+j_offset].value == " " and self.matrix[i][j].value != " ":
            self.matrix[i+i_offset][j+j_offset].update_value(self.matrix[i][j].value)
            self.matrix[i][j].update_value(" ")



    def move_up(self):
        for i in range(1, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.move_logic(self.matrix, i, j, -1)



    def move_down(self):
        for i in reversed(range(len(self.matrix)-1)):
            for j in range(len(self.matrix[i])):
                self.move_logic(self.matrix, i, j, 1)



    def move_left(self):
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[i])):
                self.move_logic(self.matrix, i, j, 0, -1)
                


    def move_right(self):
        for i in range(len(self.matrix)):
            for j in reversed(range(len(self.matrix[i])-1)):
                self.move_logic(self.matrix, i, j, 0, 1)



    def print_board(self):
        for row in self.matrix:
            for elem in row:
                print(f"[{elem.value : ^4}]", end="")
            print()


class Number_management:
    def choose_next_number(self):
        wheighted_number_list = [2, 2, 2, 2, 4, 2, 2, 2, 2, 4]
        num_index = random.randint(0, 9)
        return wheighted_number_list[num_index]



    def choose_random_coordinates(self, size):
        return Coord_pair(random.randint(0, size), random.randint(0, size))



    def is_position_free(self, matrix, coords):
        return matrix[coords.x_coor][coords.y_coor].value == " "



    def is_board_full(self, matrix, return_num_of_empty_spaces=False):
        num_of_valid_spaces = 0
        for row in matrix:
            for elem in row:
                if elem.value == " " and num_of_valid_spaces <= 2:
                    num_of_valid_spaces += 1
        if return_num_of_empty_spaces:
            return num_of_valid_spaces == 0, num_of_valid_spaces
        else:
            return num_of_valid_spaces == 0



    def add_new_twos_and_fours(self, matrix):
        is_full, num_of_valid_spaces = self.is_board_full(matrix, True)
        if not is_full:
            for i in range(1, num_of_valid_spaces):
                coords = self.choose_random_coordinates(len(matrix)-1)
                while not self.is_position_free(matrix, coords):
                    coords = self.choose_random_coordinates(len(matrix)-1)
                return coords



class Engine:
    def __init__(self):
        self.size = int(input("Please specify the size of the game area:\n"))
        self.game_board = Board(self.size)
        self.num_management = Number_management()
        self.game_board.update_with_new_num(self.num_management.add_new_twos_and_fours(self.game_board.matrix),
                                            self.num_management.choose_next_number())



    def runtime(self):
        self.game_board.print_board()



def main():
    engine = Engine()
    engine.runtime()

main()