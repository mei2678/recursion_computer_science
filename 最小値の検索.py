class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMinNum(head):
    min = head.data
    iterator = head
    min_index = 0

    index = 0
    while iterator:
        if iterator.data <= min:
            min_index = index
            min = iterator.data
        index += 1
        iterator = iterator.next

    return min_index

