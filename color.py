class Colors:  #it is easier to put the class color in a different file in order to be aple to import it in any file and avoide duplicating the code
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow  = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    
    
    @classmethod #decorator #tells Python the method that follows is a class method, not an instance method  #using it allows you to call this method on the class itself without needing to create an instance of Colors
    def get_cell_colors (cls): #cls is like self  #the class method takes the class as its first parameter.
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]



