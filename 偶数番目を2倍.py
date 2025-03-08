class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def addNextNode(nextNode, currentNode):
    tempNode = currentNode.next
    nextNode.next = tempNode
    currentNode.next = nextNode

def doubleEvenNumber(head):
    iterator = head
    index = 0
    while iterator is not None:
        next = iterator.next
        if index % 2 == 0:
            addNextNode(SinglyLinkedListNode(iterator.data * 2), iterator)
        index += 1
        iterator = next
    
    return head
