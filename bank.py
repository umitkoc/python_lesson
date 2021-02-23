##oop bank example
from os import system
from time import sleep

class Bank:
    def __init__(self,money):
        page="""
                    XXXXX      X      XX    X  X    X
                    X    X    X X     X X   X  X  XX
                    XXXXX    XXXXX    X  X  X  XXX
                    X    X  X     X   X   X X  X  XX
                    XXXXXX X       X  X    XX  X    X
                    
                    WELCOME BANK
                  
        
        """
        self.page1="""
                    1:MONEY ADD
                    2:MONEY TAKE
                    3:ABOUT
                    4:EXİT
        """
        print(page)
        self.money=money
        sleep(3)
        system("cls")
        self.start()
    def start(self):
        sleep(2)
        system("cls")
        print(self.page1)
        print("do you want to do another action ?")
        try:
            answer=int(input('please click key'))
        except:
            print("not found")
            self.start()
        if answer==1:
            self.add()
        elif answer==2:
            self.take()
        elif answer==3:
            self.about()
        elif answer==4:
            self.finish()
        else:
            print("not found")
    def add(self):
        try:
            x=abs(int(input('please money add')))
        except:
            print("not found")
            self.add()
        
        self.money+=x
        print(f"money {self.money} $")
        self.start()
    def take(self):
        try:
            x=abs(int(input('please money take')))
        except:
            print("not found")
            self.take()
        if x<=self.money:
            self.money-=x
        self.start()
    def about(self):
        print(f"money: {self.money} $")
        self.start()
    def finish(self):
        print("GOOD BYE BANK")
        exit()

if __name__=="__main__":
    Bank(200)