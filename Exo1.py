class Node :
    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getval(self):
        return self.__val

    def getright(self):
        return self.__right

    def getleft(self):
        return self.__left

    def setval(self, a):
        if a < 0 :
            print("error")
        else : self.__val = a

    def setright(self, b):
        if b < 0 :
            print("error")
        else : self.__right = b

    def setleft(self, c):
        if c < 0 :
            print("error")
        else : self.__left = c

    def aff(self):
        print("Noeud actuel :",self.__val,",Noeud droite :",self.__right,",Noeud gauche :",self.__left)


obj = Node(1,2,3)
print("Val=", obj.getval())
obj.setleft(-2)
obj.aff()

