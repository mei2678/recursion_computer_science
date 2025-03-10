class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListSearch(head,data):
    index = 0
    result = -1
    iterator = head

    while iterator:
        if iterator.data == data and result == -1:
            result = index
        index += 1
        iterator = iterator.next
    
    return result

