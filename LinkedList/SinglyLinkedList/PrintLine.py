class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

head = Listnode(10)
head.next = Listnode(20)
head.next.next = Listnode(30)

printLinkedList(head)