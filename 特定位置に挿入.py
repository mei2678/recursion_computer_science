class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeInSorted(head,data):
    dummy = SinglyLinkedListNode(0)
    dummy.next = head

    prev = dummy
    curr = head

    while curr is not None and curr.data < data:
        prev = curr
        curr = curr.next
    
    new_node = SinglyLinkedListNode(data)
    prev.next = new_node
    new_node.next = curr

    return dummy.next
