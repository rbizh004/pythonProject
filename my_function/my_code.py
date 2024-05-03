class human:
    def __init__(self, height, weight):
        self.height=height
        self.weight=weight
    def BMI(self):
       a= self.height/self.weight
       print( 'my BMI is {}'.format(a))

    def size(self,another_guy):
        if self.weight < another_guy:
            print(f"I am smaller than him by {self.weight-another_guy}")
        else:
            print("I'm the man")


me=human(160,50)
me.BMI()
me.size(201)
print('a')