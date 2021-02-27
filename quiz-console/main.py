import random
from os import mkdir,path,system


class Quiz:
    def __init__(self, name):
        self.name = name
        self._score=""
        if not self.score():
            self._score = "empty!"
        print(f"""
                    QUİZMAGİC
                          WELCOME {self.name}
                          START--->KEY ENTER
                          10 ask 10 answer
                          EXIT----->Q

                          score----->        {self._score}          <-----------

        """)
        self.point = 0
        self.step = 0
        self.start()
    def score(self):
        if path.isdir("data"):
            with open("data/data.txt", "r", encoding="utf-8") as file:
                _data = file.readline()
                self._score = f"{_data}"
            file.close()
            return True
        
        mkdir("data")
        with open("data/data.txt", "w", encoding="utf-8") as file:
            file.close()
        return False
        

    def start(self):
        self.next = input("continue ?")
        if self.step == 10 or self.next.lower() == "q":
            with open("data/data.txt", "r+", encoding="utf-8") as _file:
                _file.write(f"name: {self.name} score: {self.point}")
            _file.close()
            print(f"you point: {self.point}")
            exit()
        else:
            system("cls")
            print(f"-------------------{self.step}-------------------------")
            self.step += 1
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)
            self.z = random.randint(0, 4)
            if self.z == 1:
                self.one()
            elif self.z == 2:
                self.two()
            else:
                self.three()

    def one(self):
        print(f"{self.x} x {self.y} = ?")
        try:
            self.answer = int(input())
        except:
            print("please number input")
            self.one()
        if (self.answer == self.x*self.y):
            self.point += 1
        else:
            print(f"{self.x*self.y}")
            print("False")
        self.start()

    def two(self):
        print(f"{self.x} + ? = {self.y}")
        try:
            self.answer = int(input())
        except:
            print("number input please")
            self.two()
        if (self.answer == self.y-self.x):
            self.point += 1
        else:
            print(f"{self.y-self.x}")
            print("False")
        self.start()

    def three(self):
        print(f"? + {self.y} = {self.x}")
        try:
            self.answer = int(input())
        except:
            print("please input number")
            self.three()
        if (self.answer == self.x-self.y):
            self.point += 1
        else:
            print("False")
        self.start()


if __name__ == "__main__":
    answer = input("please name:")
    if answer!="":
        Quiz(answer)
    else:
        print("System  start again ")
