pizzas=['margherita','cheese_and_corn','farm_house','tandoori',
         'margherita','cheese_and_corn','farm_house']

pizzaCounter={}

for pizza in pizzas:
    if pizza in pizzaCounter.keys():
        pizzaCounter[pizza]+=1
    else:
        pizzaCounter[pizza] = 1

for k,v in pizzaCounter.items():
    print(k,v)
