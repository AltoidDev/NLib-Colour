import sys
from src.libncolour import colour

test = colour.RGB(128,128,128)
test2 = colour.RGB(130,130,130)

print(colour.average([test,test2]))
