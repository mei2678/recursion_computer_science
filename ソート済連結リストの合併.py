class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def addNextNode(head1, head2, node):
    if not head1 and not head2:
        return
    elif not head1:
        node.next = head2
        return
    elif not head2:
        node.next = head1
        return

    if head1.data < head2.data:
        node.next = SinglyLinkedListNode(head1.data)
        return addNextNode(head1.next, head2, node.next)
    else:
        node.next = SinglyLinkedListNode(head2.data)
        return addNextNode(head1, head2.next, node.next)


def mergeTwoSortedLinkedLists(head1,head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    if head1.data < head2.data:
        newNode = SinglyLinkedListNode(head1.data)
        iterator1 = head1.next
        iterator2 = head2
    else:
        newNode = SinglyLinkedListNode(head2.data)
        iterator2 = head2.next
        iterator1 = head1

    addNextNode(iterator1, iterator2, newNode)
    return newNode
