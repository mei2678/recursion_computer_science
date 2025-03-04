"""
連結リストとはコンピュータで頻繁に使用される最も基本的なデータ構造です。次の Item を参照することによって、要素どうしの繋がりを表現することができます。以下は各要素を表す Item クラスです。

int data: 要素の値
Item next: 1 つ先のノード。デフォルトでは null に設定してください。
各ノードを繋げた状態で、先頭を定義することによって、SinglyLinkedList クラスを表現できます。

Item head: 先頭の Item
SinglyLinkedList クラスから連結リストを作成し、while 文によって、各値を出力してください。
"""
class Item:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class SinglyLinkedList:
  def __init__(self, head=None):
    self.head = head

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next
      
item1 = Item(7)
item2 = Item(99)
item3 = Item(45)
item1.next = item2
item2.next = item3
sll = SinglyLinkedList(item1)
sll.print_list()
