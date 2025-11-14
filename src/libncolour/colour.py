from typing import Tuple

class Colour:
    # base class for all colours
    pass

class HSV(Colour):
    def __init__(self,Hue: int|float,Saturation: int|float,Value: int|float):
        self.h: int|float = Hue
        self.s: int|float = Saturation
        self.v: int|float = Value
        
        self.t:Tuple[float,float,float] = (Hue,Saturation,Value)

class RGB(Colour):
    def __init__(self,Red:int,Green:int,Blue:int):
        self.r:int = Red
        self.g:int = Green
        self.b:int = Blue
        
        self.t:Tuple[int,int,int] = (Red,Green,Blue)

def checkall(list:list|tuple,type):
    # Returns true if all elements in list are of class type, else returns false
    
    for x in list:
        if not isinstance(x,type):
            return False
        
    return True


def average(colours:list):
    # returns an average of all colours in colours:list as the appropriate Colour class if they're all the same type
    # otherwise returns a tuple average of the raw values 
    validcolours:list = []
    type:str = ""
    
    for current in colours:
        curcol = (0,0,0)
        
        if current is tuple or isinstance(current,Colour):
            curcol = current

        else:
            raise TypeError() # 1 or more item in list isn't a colour and can't be averaged.

        validcolours.append(curcol)
        
    if checkall(validcolours,RGB):
        total:Tuple[int,int,int]|RGB = (0,0,0)
        type = "RGB"
        
        for x in validcolours:
            total = tuple((total[0]+x.r,total[1]+x.g,total[2]+x.b))
            
    elif checkall(validcolours,HSV):
        total:Tuple[float,float,float]|HSV = (0.0,0.0,0.0)
        type = "HSV"
        
        for x in validcolours:
            total = tuple((total[0]+x.h,total[1]+x.s,total[2]+x.v))
            
    else:
        print("\nNot all values in list are of the same type, so they'll just be averaged as raw numbers.\n")
        
        if checkall(validcolours[1],float):
            total:Tuple[float,float,float] = (0.0,0.0,0.0)
            
        else:
            total:Tuple[int,int,int] = (0,0,0)
            
        for x in validcolours:
            total = tuple((total[0]+x[0],total[1]+x[1],total[2]+x[2]))

    l = len(validcolours)
    if type == "RGB":
        total = tuple(( int(total[0]/l), int(total[1]/l), int(total[2]/l) ))
    else:
        total = tuple(( total[0]/l, total[1]/l, total[2]/l ))

    if type == "HSV":
        total = HSV(total[0],total[1],total[2])
    elif type == "RGB":
        total = RGB(total[0],total[1],total[2])

        
    return(total)
