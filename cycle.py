class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

head=tail=Node(0)
import sys
n=sys.argv[1]
for i in range(int(n)):
    head=Node(i,head)

x=int(sys.argv[2])
mid=head
for i in range(x):
    mid = mid.next

tail.next=mid

def find_start(head):
    a=head.next
    b=a.next
    while a!=b:
        i+=1
        a=a.next
        b=b.next.next
    #i is now the collision point
    #reverse the list
    prev=a
    curr=prev.next
    next=curr.next

