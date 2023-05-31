class Node:
    def __init__(self,x):
        self.key = x
        self.left = None
        self.right = None
        self.p = None
class BST:
    def __init__(self):
        self.root = None
    def BST_minimum(self,x):
        while x.left != None:
            x = x.left
        return x
    def BST_insert(self,z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
    def BST_search(self,k):
        x = self.root
        while x != None and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        if x != None:
            print(x.key)
        else:
            print(x)
    def BST_delete(self,z):
        if z.left == None and z.right == None:
            if z == self.root:
                self.root = None
            else:
                if z == z.p.left:
                    z.p.left = None
                else:
                    z.p.right = None
        elif z.left != None and z.right != None:
            y = self.BST_minimum(z.right)
            z.key = y.key
            self.BST_delete(y)
        else:
            if z.left != None:
                if z == self.root:
                    self.root = None
                else:
                    if z == z.p.left:
                        z.p.left = z.left
                    else:
                        z.p.right = z.left
            else:
                if z == self.root:
                    self.root = None
                else:
                    if z == z.p.left:
                        z.p.left = z.right
                    else:
                        z.p.right = z.right
    def BST_Print_inOrderD(self, x, d):
        if x == None:
            return
        self.BST_Print_inOrderD(x.right,d+1)
        print(d*"_",x.key)
        self.BST_Print_inOrderD(x.left,d+1)
my_BST = BST()
a = Node("abba")
b = Node("ba")
c = Node("ab")
d = Node("cabba")
e = Node("ebba")
f = Node("abc")
g = Node("egf")
h = Node("xyz")
my_BST.BST_insert(a)
my_BST.BST_insert(b)
my_BST.BST_insert(c)
my_BST.BST_insert(d)
my_BST.BST_insert(e)
my_BST.BST_insert(f)
my_BST.BST_insert(g)
my_BST.BST_insert(h)
my_BST.BST_Print_inOrderD(a,0)