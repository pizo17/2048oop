import math
from colors import *



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
        col_code_val = math.log(number, 2) % 8
        return self.col_codes.get(col_code_val if not col_code_val == 0 else 8) 
