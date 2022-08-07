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
        self.bright_white = "\u001b[47;1m"
        self.reset = "\u001b[47;1m"



fg_col = Foreground_Colors()
bg_col = Background_Colors()
print(f"{bg_col.red}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.red}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.green}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.green}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.yellow}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.yellow}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.blue}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.blue}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.magenta}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.magenta}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.cyan}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.cyan}2048{bg_col.black}")
print(f"{fg_col.black}{bg_col.white}2048{bg_col.black}")
print(f"{fg_col.white}{bg_col.white}2048{bg_col.black}")
print(f"{bg_col.bright_black}2048{bg_col.black}")


'''
print(f"{bg_col.bright_red}2048{bg_col.black}")
print(f"{bg_col.bright_green}2048{bg_col.black}")
print(f"{bg_col.bright_yellow}2048{bg_col.black}")
print(f"{bg_col.bright_blue}2048{bg_col.black}")
print(f"{bg_col.bright_magenta}2048{bg_col.black}")
print(f"{bg_col.bright_cyan}2048{bg_col.black}")
print(f"{bg_col.bright_white}2048{bg_col.black}")
'''
