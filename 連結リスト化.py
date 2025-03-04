"""
整数で構成される配列 arr が与えられるので、片方向リスト化する getLinkedList という関数を作成してください。

関数の入出力例
入力のデータ型： integer[] arr
出力のデータ型： SinglyLinkedListNode<integer>

getLinkedList([3,2,1,5,6,4]) --> 3➡2➡1➡5➡6➡4➡END
getLinkedList([7,8,2,3,1,7,8,11,4,3,2]) --> 7➡8➡2➡3➡1➡7➡8➡11➡4➡3➡2➡END
getLinkedList([34,35,64,34,10,2,14,5,353,23,35,63,23]) --> 34➡35➡64➡34➡10➡2➡14➡5➡353➡23➡35➡63➡23➡END
getLinkedList([1]) --> 1➡END
"""

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLinkedList(arr):
    """
    整数配列を単方向連結リストに変換する関数

    Args:
        arr (list[int]): 整数の配列

    Returns:
        SinglyLinkedListNode: 連結リストの先頭ノード

    Raises:
        ValueError: 配列が空の場合
    """
    if not arr:
        raise ValueError("配列が空です")

    # 先頭ノードの作成
    head = SinglyLinkedListNode(arr[0])
    
    # 配列の長さが1の場合はそのまま返す
    if len(arr) == 1:
        return head

    # 残りのノードを連結
    prev = head
    for node in arr[1:]:
        current = SinglyLinkedListNode(node)
        prev.next = current
        prev = current
    
    return head

