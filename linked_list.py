class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
n1=Node(20)
n2=Node(20)
n3=Node(20)

n1.next=n2
print(str(n1.next))
print(n2)
n2.next=n3
