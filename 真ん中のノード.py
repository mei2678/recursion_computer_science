class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def middleNode(head):
    index = 0
    iterator = head
    while iterator:
        iterator = iterator.next
        index += 1

    iterator = head
    mid = index//2+1
    for i in range(1, mid):
        iterator = iterator.next
    return iterator
