from typing import Tuple

class colour:
    # base class for all colours
    pass

class HSV:
    def __init__(self,Hue: int|float,Saturation: int|float,Value: int|float):
        self.h: int|float = Hue
        self.s: int|float = Saturation
        self.v: int|float = Value
        
        self.t:Tuple[float,float,float] = (Hue,Saturation,Value)

class RGB:
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
    validcolours:list = []
    
    for current in colours:
        curcol = (0,0,0)
        
        if current is tuple or isinstance(current,colour):
            curcol = current

        else:
            raise TypeError() # 1 or more item in list isn't a colour and can't be averaged.

        validcolours.append(curcol)
        
    if checkall(validcolours,RGB):
        total:Tuple[int,int,int] = (0,0,0)
        
        for x in validcolours:
            total[0] += x.r
            total[1] += x.g
            total[2] += x.b
            
    elif checkall(validcolours,HSV):
        total:Tuple[float,float,float] = (0.0,0.0,0.0)
        
        for x in validcolours:
            total[0] += x.h
            total[1] += x.s
            total[2] += x.v
            
    else:
        print("\nNot all values in list are of the same type, so they'll just be averaged as raw numbers.\n")
        
        if checkall(validcolours[1],float):
            total:Tuple[float,float,float] = (0.0,0.0,0.0)
            
        else:
            total:Tuple[int,int,int] = (0,0,0)
            
        for x in validcolours:
            total[0] += x[0]
            total[1] += x[1]
            total[2] += x[2]
            
    total[0] = total[0] / len(validcolours)
    total[1] = total[1] / len(validcolours)
    total[2] = total[2] / len(validcolours)

    return(total)
