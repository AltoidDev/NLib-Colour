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
    total = (0,0,0)
    for current in colours:
        curcol = (0,0,0)
        if current is tuple or isinstance(current,colour):
            curcol = current
        else:
            raise TypeError() # 1 or more item in list isn't a colour and can't be averaged.
        validcolours.append(curcol)
    if checkall(validcolours,RGB):
        for x in validcolours:
            total[0] += x.r
            total[1] += x.g
            total[2] += x.b
    elif checkall(validcolours,HSV):
        for x in validcolours:
            total[0] += x.h
            total[1] += x.s
            total[2] += x.v
    else:
        print("\nNot all values in list are of the same type, so they'll just be averaged as raw numbers.\n")
        for x in validcolours:
            total[0] += x[0]
            total[1] += x[1]
            total[2] += x[2]
    total[0] = total[0] / len(validcolours)
    total[1] = total[1] / len(validcolours)
    total[2] = total[2] / len(validcolours)

    return(total)
