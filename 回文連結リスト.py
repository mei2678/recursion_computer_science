class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def SinglyLinkedList(list):
    head = SinglyLinkedListNode(list[0])
    iterator = head
    for i in range(1, len(list)):
        iterator.next = SinglyLinkedListNode(list[i])
        iterator = iterator.next

    return head

def palindromeLinkedList(head):
    if head is None or head.next is None:
        return True

    stack = []
    current = head
    while current:
        stack.append(current.data)
        current = current.next
    
    current = head
    while current:
        if current.data != stack.pop():
            return False
        current = current.next
    
    return True
