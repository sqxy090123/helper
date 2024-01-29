
class color:
    def __init__(self, string:str):
        self.string = string
    def recover(self):
        return "\033[0m"+self.string
    def overstriking(self):
        return "\033[1m"+self.string
    def faint(self):
        return "\033[2m"+self.string
    def italic(self):
        return "\033[3m"+self.string
    def underline(self):
        return "\033[4m"+self.string
    def bright(self):
        return "\033[5m"+self.string
    def invert(self):
        return "\033[7m"+self.string
    def hidden(self):
        return "\033[8m"+self.string
    def delete(self):
        return "\033[9m"+self.string
    def black(self):
        return "\033[30m"+self.string
    def red(self):
        return "\033[31m"+self.string
    def green(self):
        return "\033[32m"+self.string
    def yellow(self):
        return "\033[33m"+self.string
    def blue(self):
        return "\033[34m"+self.string
    def purple(self):
        return "\033[35m"+self.string
    def cyan(self):
        return "\033[36m"+self.string
    def white(self):
        return "\033[37m"+self.string
    def background_red(self):
        return "\033[41m"+self.string
    def background_green(self):
        return "\033[42m"+self.string
    def background_yellow(self):
        return "\033[43m"+self.string
    def background_blue(self):
        return "\033[44m"+self.string
    def background_purple(self):
        return "\033[45m"+self.string
    def background_cyan(self):
        return "\033[46m"+self.string
    def background_white(self):
        return "\033[47m"+self.string
    
    


