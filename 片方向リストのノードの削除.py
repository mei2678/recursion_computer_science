class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNthNode(head,n):
    if n == 0: return head

    index = 0
    iterator = head
    while iterator is not None:
        index += 1
        iterator = iterator.next
    if n > index: return head

    deleteIndex = index - n
    # 削除する要素がリストの先頭にある場合
    if deleteIndex == 0:
        return head.next

    iterator = head
    index = 0
    while iterator is not None:        
        index += 1
        # 次のノードが削除対象の場合
        if index == deleteIndex:
            # 二つ先のノードがある場合
            if iterator.next is not None:
                iterator.next = iterator.next.next
                iterator = iterator.next
            # 二つ先のノードがない場合
            else:
                iterator = None
        # 次のノードが削除対象でない場合
        else:
            iterator = iterator.next

    return head
