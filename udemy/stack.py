def balance_check(s):
  if len(s) == 0:
    return False
  if len(s) % 2 != 0:
    return False
  open_options = "[{("
  matches = ["()","[]","{}"]
  seen_opened = []
  for caract in s:
    if caract in open_options:
      seen_opened.append(caract)
    else:
      if seen_opened == []:
        return False
      a = seen_opened.pop()
      match = a+caract
      if match not in matches:
        return False
  return len(seen_opened) == 0
      
print(balance_check('[](){([[[]]])}('))
print(balance_check('[{{{(())}}}]((()))'))
print(balance_check('[[[]])]'))
    

    
class Queue2Stacks(object):
    
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
  
  def enqueue(self,element):
    self.stack1.append(element)
    
  def dequeue(self):
    if len(self.stack2) == 0: 
      while len(self.stack1) > 0:
        ele = self.stack1.pop()
        self.stack2.append(ele)
    return self.stack2.pop()
 
 
q = Queue2Stacks()   
for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())