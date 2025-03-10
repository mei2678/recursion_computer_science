class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteTail(head):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    iterator = dummy

    while iterator.next.next:
        iterator = iterator.next
    
    iterator.next = None
    head = dummy.next
    return head
