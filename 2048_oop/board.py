from cell import *
import random



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