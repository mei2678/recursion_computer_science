class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertHead(head, data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = head
    return newNode

def insertTail(head, data):
    newNode = SinglyLinkedListNode(data)
    iterator = head
    while iterator.next:
        iterator = iterator.next

    iterator.next = newNode
    return head

def insertHeadTail(head,data):
    newListHead = insertHead(head, data)
    newListHead = insertTail(newListHead, data)

    return newListHead
