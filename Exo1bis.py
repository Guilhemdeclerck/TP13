from Exo1 import *

class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def getroot(self):
        return self.__root

    def setroot(self, root):
        if root < 0:
            print("error")
        else: root = self.__root

    def isRoot(self, root):
        if root == self.__root :
            print(root,"est le noeud racine")
        else :
            print(root,"n'est pas le noeud racine")

    def Size(self,node):
        if node is None :
            return +0
        else:
            return self.Size(node.getright()) + self.Size(node.getleft()) +1

    def printValues(self, node):
        if node is None :
            return ""
        else:
            return self.printValues(node.getright()) + self.printValues(node.getleft()) +" "+ str(node.getval())

    def sumValues(self, node):
        if node is None:
            return +0
        else:
            return node.getval() +self.sumValues(node.getright()) + self.sumValues(node.getleft())

    def numberLeaves(self, node):
        if node is None :
            return +0
        if node.getleft() is None and node.getright() is None:
            return +1
        else:
            return self.numberLeaves(node.getright()) + self.numberLeaves(node.getleft())

    def numberInternalNodes(self, node):
        if node.getleft() is None and node.getright() is None:
            return +0
        else:
            return self.numberLeaves(node.getright()) + self.numberLeaves(node.getleft())+1

    def height(self, node):
        if node.getleft() is None and node.getright() is None:
            return +0
        if node.getleft() is not None:
            return +1
        else:
            return self.numberLeaves(node.getright()) + self.numberLeaves(node.getleft())

    def belongs(self, node, val):
        if node.getval() == val:
            return True
        if node.getval() != val:
            return False
        else:
            return self.belongs(node.getright(), node.getright().getval()) + self.belongs(node.getleft(), node.getleft().getval())

    def ancestors(self, node, val):
        if node.getval() == val:
            return

    def descendants(self, node, val):
        if node.getval() == val:
            return

    #def prefix(self, node):

    #def infix(self, node):

    #def postfixe(self,node):

    #def parcoursLargeur(self,node):


N21 = Node(21, None, None)
N18 = Node(18, None, None)
N3 = Node(3, None, None)

N19 = Node(19, N21, N18)
N4 = Node(4, None, N3)
N6 = Node(6, None, None)

N17 = Node(17, N19, None)
N5 = Node(5, N6, N4)

N12 = Node(12, N17, N5)
Tree = BinaryTree(N12)

print(Tree.Size(Tree.getroot()))
print(Tree.sumValues(Tree.getroot()))
print(Tree.printValues(Tree.getroot()))
print(Tree.numberLeaves(Tree.getroot()))
print(Tree.numberInternalNodes(Tree.getroot()))
print(Tree.height(Tree.getroot()))
print(Tree.belongs(Tree.getroot(), Tree.getroot().getright()))

#t= BinaryTree(Node(12))
#t.getleft().setval(5)
#t.getleft().setval(3)
#t.getright().setval

#NoeudRacine = Node(12,17,5)
#Tree = BinaryTree(NoeudRacine)



