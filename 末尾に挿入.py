class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtTail(head,data):
    newNode = SinglyLinkedListNode(data)
    iterator = head
    while iterator.next:
        iterator = iterator.next

    iterator.next = newNode
    return head
