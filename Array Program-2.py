from array import *
vals=array('i',[2,4,5,34,45])
print(vals)
print(vals.typecode)
print(vals.buffer_info())
vals.reverse()
print(vals)