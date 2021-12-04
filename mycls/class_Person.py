class Person:
    def __init__(self,name):
        print('Hello')
        print('my name is=',name)

        self.name=name
    def live(self,n):
        print(self.name,' is ',n,'th    alive')
    def die(self):
        print(self.name,'th you will die')
    def address(self,address):
        print('내이름은 ',self.name,'이고 내 주소는 ',address)