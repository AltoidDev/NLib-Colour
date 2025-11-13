class colour:
    # base class for all colours
    pass

class HSV:
    def __init__(self,Hue:int,Saturation:int,Value:int):
        self.h:int = Hue
        self.s:int = Saturation
        self.v:int = Value
        self.t:tuple = (Hue,Saturation,Value)

class RGB:
    def __init__(self,Red:int,Green:int,Blue:int):
        self.r:int = Red
        self.g:int = Green
        self.b:int = Blue
        self.t:tuple = (Red,Green,Blue)

def checkall(list:list,type):
    # Returns true if all elements in list are of class type, else returns false
    
    for x in list:
        if not isinstance(x,type):
            return False
    return True


def average(colours:list):
    validcolours:list = []
    for current in colours:
        curcol = (0,0,0)
        if current is tuple:
            curcol = current
        elif isinstance(current,colour):
            curcol = current.t
        else:
            raise TypeError() # 1 or more item in list isn't a colour and can't be averaged.
        validcolours.append(curcol)
