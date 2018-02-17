class Tree:
    def __init__(self,root,left=None,right=None):
        self.root=root
        self.left=left
        self.right=right
    def __str__(self):
      return (str(self.root)+", left child :"+str(self.left)+ ", right child :" +str(self.right))

tree=Tree(5,Tree(3,1,4),Tree(8,7,9))
print(tree)