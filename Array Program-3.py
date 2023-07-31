from array import *
vals=array('i',[2,4,5,34,45])
newArray=array(vals.typecode,(a for a in vals))
newArray.reverse()
print(newArray)
