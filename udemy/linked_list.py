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

    
def cycle_check(node):
  pointer1 = node
  pointer2 = node
  while pointer2.nextnode != None and pointer2.nextnode.nextnode != None:
    pointer1 = pointer1.nextnode
    pointer2= pointer2.nextnode.nextnode
    if pointer2 == pointer1:
      return True
  return False 
  
'''
# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(a))  
print(cycle_check(x))  
'''

def reverse(head):
  prev = head
  current = head.nextnode
  prev.nextnode = None
  while current.nextnode != None:
    tmp = current.nextnode
    current.nextnode = prev
    prev = current
    current = tmp
  current.nextnode = prev
  
# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a)  
  
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value) 