class Greeter:
    def __init__(self,name):
        self.name = name
    def greet(self,loud=False):
        if loud:
            print('Hello, %s!'% self.name.upper()) #or print('Hello, {}!'.format(self.name.upper()))
        else:
            print('Hello, ',self.name)
ob = Greeter('Fred')
ob.greet()
ob.greet(loud=True)