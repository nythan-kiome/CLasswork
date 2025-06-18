class TreeNode:

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value




    def insert(self, key):
        if key < self.value:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)

        elif key > self.value:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)




    def find(self, key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key)
        else:
            return True



    #preorder prints after visiting for the first time
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        print(self.value)

        if self.right:
            self.right.preorder_traversal()


    #Inorder prints during the 2nd visit
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()




    def postorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.postorder_traversal()
        print(self.value)

        if self.right:
            self.right.postorder_traversal()

if __name__ == '__main__':

    tree = TreeNode("50")


    tree.insert("3")
    tree.insert("4")
    tree.insert("5")
    tree.insert("11")
    tree.insert("12")
    tree.insert("13")

    print("\n preorder_traversal :")
    tree.preorder_traversal()

    print("\n inorder_traversal :")
    tree.inorder_traversal()

    print("\n postorder_traversal :")
    tree.postorder_traversal()