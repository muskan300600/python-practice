class Father():
    def gardening(self):
        print("I know gardening")

class Mother():
    def cooking(self):
        print("I know cooking")

class child(Father, Mother):

        print ("I know sports")

c = child()
c.gardening()
c.cooking()

