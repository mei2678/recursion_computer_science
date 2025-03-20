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
  
def dailyStockPrice(stocks):
  n = len(stocks)
  result = [0] * n

  stack = Stack()
  for i in range(n-1, -1, -1):
    # スタックのトップにある株価が現在の株価以下であれば、待ち日数の候補にならないため取り除く
    while stack.peek() is not None and stack.peek()[0] <= stocks[i]:
      stack.pop()
    # スタックが空の場合は未来のデータがないため待ち日数は0
    if stack.peek() is None:
      result[i] = 0
    else:
      result[i] = stack.peek()[1] - i
  
    stack.push((stocks[i], i))

  return result
