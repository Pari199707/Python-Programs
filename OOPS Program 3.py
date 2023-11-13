class Pen:
    def __init__(self,ink_color):
        self.color = ink_color
    
    def write(self):
        print(self.color,"Write Functionality exists")
     
    def ink_full(self):
        full = input ("Enter True or False:\n")
        if  full:
            print(self.color,"Ink filled")
        else:
            print(self.color,"need to be filled")

pen1 = Pen ("Red")
pen1.write()
pen1.ink_full()
