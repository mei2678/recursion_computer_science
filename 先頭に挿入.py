class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtHead(head,data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = head
    return newNode
