class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMergeNode(headA,headB):
    nodesA, nodesB = [], []

    while headA:
        nodesA.append(headA)
        headA = headA.next
    
    while headB:
        nodesB.append(headB)
        headB = headB.next

    indexA, indexB = len(nodesA)-1, len(nodesB)-1
    merge_node = None

    while indexA >= 0 and indexB >= 0 and nodesA[indexA].data == nodesB[indexB].data:
        merge_node = nodesA[indexA]
        indexA -= 1
        indexB -= 1

    return merge_node.data if merge_node else -1
