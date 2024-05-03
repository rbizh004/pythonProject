class human:
    def __init__(self, height, weight):
        self.height=height
        self.weight=weight
    def BMI(self):
       a= self.height/self.weight
       print( 'my weight is {}'.format(a))



me=human(160,50)
me.BMI()