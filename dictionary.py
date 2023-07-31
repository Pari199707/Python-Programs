fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = {}

    # Count the elements in the list
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))