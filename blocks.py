from block import Block 
from position import Position

#LBlock
class LBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 1) #super is a function used to call the attributes of the parent class #passses an argument id = 1
        self.cells = {
            0: [Position(0, 2),Position(1, 0),Position(1, 1),Position(1, 2)],
            1: [Position(0, 1),Position(1, 1),Position(2, 1),Position(2, 2)],
            2: [Position(1, 0),Position(1, 1),Position(1, 2),Position(2, 0)],
            3: [Position(0, 0),Position(0, 1),Position(1, 1),Position(2, 1)]
        }

class JBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 2) 
        self.cells = {            
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }


class IBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 3) 
        self.cells = {0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }

class OBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 4) 
        self.cells = {
            0: [Position(0, 0),Position(0, 1),Position(1, 0),Position(1, 1)],
            1: [Position(0, 0),Position(0, 1),Position(1, 0),Position(1, 1)],
            2: [Position(0, 0),Position(0, 1),Position(1, 0),Position(1, 1)],
            3: [Position(0, 0),Position(0, 1),Position(1, 0),Position(1, 1)]
        }




class SBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 5) 
        self.cells = {            
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }



class TBlock(Block):  #(Block) establishes the inheritance relationship
    def __init__(self): 
        super().__init__(id = 6) 
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }