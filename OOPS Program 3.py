class Pen:
    def __init__(self,ink_color):
        self.color = ink_color
    
    def write(self):
        print(self.color,"Write Functionality exists")
     
    def ink_full(self):
        full = input ("Enter True or False:\n")
        if  full == True:
            print(self.color,"Ink filled")
        elif full == False:
            print(self.color,"need to be filled")
        else:
            print("Please enter correct value")

pen1 = Pen ("Red")
pen1.write()
pen1.ink_full()

pen2 = Pen ("Black")
pen2.write()
pen2.ink_full()
