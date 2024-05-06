class TextInput():
    def __init__(self):
        self.initial=""
    def add(self, character):
        self.initial=self.initial + character
    def get_value(self):
        return self.initial




class NumericInput(TextInput):
    def add(self,character):
        try:
            int(character)>-100000
        except Exception as e:
            pass
        else:
            self.initial= self.initial + character



if __name__ == '__main__':
   input = NumericInput()
   input.add("1")
   input.add("a")
   input.add("0")
   print(input.get_value())