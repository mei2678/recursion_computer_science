class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getIndexValue(head,index):
    iterator = head
    for i in range(1, index):
        iterator = iterator.next
        if iterator.next is None: return None

    return iterator.data
