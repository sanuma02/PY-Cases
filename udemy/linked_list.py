class Node:

  def __init__(self, value):
    self.value = value
    self.nextnode  = None
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

def nth_to_last_node(n, head):
  pointer = head
  current = head
  counter = 0
  while current.nextnode != None:
    print(current.value,counter)
    if counter == n:
      pointer = pointer.nextnode
      counter = 0
      current = pointer
    else:
      current = current.nextnode
    counter += 1
  return pointer
  
tmp = nth_to_last_node(2, a) 
print(tmp.value)

def reverse(head):
      
      
def cycle_check(node):