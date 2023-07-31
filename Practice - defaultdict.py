import _collections
pizzas=['margherita','cheese_and_corn','farm_house','tandoori',
         'margherita','cheese_and_corn','farm_house']

pizzaCounter=_collections.defaultdict(int)

for pizza in pizzas:
    pizzaCounter[pizza] += 1

for k,v in pizzaCounter.items():
    print(k,v)