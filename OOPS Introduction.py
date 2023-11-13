class Pen:
    def __init__(self,ink_color):
        self.color = ink_color
    
    def write(self):
        print(self.color,"Write Functionality exists")
        

pen1 = Pen ("Red")
pen1.write()
