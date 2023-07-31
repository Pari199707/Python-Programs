import collections
dict1={'parinitha':12,'manjula':13,'chinni':15}
print(dict1)
ordered_dict=collections.OrderedDict(dict1)
print(ordered_dict)
top_item=ordered_dict.popitem()
print("Top item:",top_item)
for i,names in enumerate(ordered_dict,start=1):
    print(i,names)
for k,v in ordered_dict.items():
    print(k,v)

ordered_dict1=collections.OrderedDict({'a':1,'b':2,'c':3})
ordered_dict2=collections.OrderedDict({'a':1,'c':3,'b':2})
if (ordered_dict1==ordered_dict2):
    print("Ordered Dict is same as Normal Dict")
else:
    print("Ordered Dict is not same as Normal Dict")