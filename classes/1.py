class Modify():
    def __init__(self):
        self.name = ''
        
    def getString(self):
        self.name = input()
        
    def printString(self):
        print(self.name.upper())
name = Modify()
name.getString()
name.printString()
  
        