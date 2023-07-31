import collections
pizzas1=['margherita','cheese_and_corn','farm_house','tandoori',
         'margherita','cheese_and_corn','farm_house','tikka','cheese_and_corn']
pizzas2= ['sausage','kheema','chicken_feast','chicken_dominator','tikka']
counter1 = collections.Counter(pizzas1)
counter2 = collections.Counter(pizzas2)
print(counter1)
print(counter1['tandoori'])
print(counter1.get('farm_house'))
print("Total values in the dictionary counter1:",sum(counter1.values()),"Total Pizzas Available")
print("Total keys in the dictionary counter1:",list(counter1.keys()))
print("Most common elements",counter1.most_common(3))
counter1.update(pizzas2)
print("Total values in the dictionary counter1:",sum(counter1.values()),"Total Pizzas Available")
print("Total keys in the dictionary counter1:",list(counter1.keys()))
print("Most common elements",counter1.most_common(3))
counter1.subtract(pizzas2)
print("Total values in the dictionary counter1:",sum(counter1.values()),"Total Pizzas Available")
print("Total keys in the dictionary counter1:",list(counter1.keys()))
print("Common elements",counter1 & counter2)