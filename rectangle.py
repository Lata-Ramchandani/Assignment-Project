class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}


rect = Rectangle(4,8)

for each in rect:
    print(each)