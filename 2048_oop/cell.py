from coord_pair import *



class Cell:
    def __init__(self, x_coor, y_coor, value, color =  "\u001b[47m"):
        self.coordinates = Coord_pair(x_coor, y_coor) 
        self.value = value
        self.color = color
    


    def update_value(self, value):
        self.value = value


    
    def add_value(self, value):
        self.value += value