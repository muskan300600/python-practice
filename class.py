class Human():

    def __init__(self,n,j,a):
        self.name=n
        self.job=j
        self.age=a

    def work(self):
        if self.job== "Cricket Player":
            print(self.name,"of age",self.age, "plays Cricket")
        elif self.job=="Singer":
            print(self.name,"of age ",self.age, "sings beautiful songs")
    def greet(self):
        print(self.name, "has made India proud")

Dhoni = Human("Dhoni", "Cricket Player", "45")
Dhoni.work()
Dhoni.greet()

Shreya = Human("Shreya", "Singer", "40")
Shreya.work()
Shreya.greet()


