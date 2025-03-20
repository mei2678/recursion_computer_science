class Item:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self, head=None):
    self.head = head
    
  def push(self, data):
    self.head = Item(data, self.head)
    
  def pop(self):
    if self.head is None:
      return None
    else:
      data = self.head.data
      self.head = self.head.next
      return data
  
  def peek(self):
    if self.head is None:
      return None
    return self.head.data
  
def consecutiveWalk(arr):
  # スタックから取り出した時に単調増加となる部分配列を返す
  if len(arr) < 1: return arr
  
  result_arr = []
  stack = Stack(Item(arr[0]))
  for i in arr:
    stack.push(i)

  result_arr.append(stack.pop())

  peek = stack.peek()
  while peek is not None and peek < result_arr[-1]:
    result_arr.append(stack.pop())
    peek = stack.peek()

  return result_arr

print(consecutiveWalk([3,4,20,45,56,6,4,3,2,3,9])) # [9,3,2]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54])) # [-54]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4])) # [4,-54]
print(consecutiveWalk([])) # []
print(consecutiveWalk([1])) # [1]
print(consecutiveWalk([1,2,3,2,4])) # [4,2]
