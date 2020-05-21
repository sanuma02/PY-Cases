a = [3,5,10,11,9,4,6,7]

class Node:
  def __init__(self, value):
    self.value = value
    self.left_node = None
    self.right_node = None
    
  def insert(self, node, value):
    if node == None:
      new_node = Node(value)
      return new_node
    if value < node.value:
      node.left_node = self.insert(node.left_node, value)
    elif value > node.value:
      node.right_node = self.insert(node.right_node, value)
    return node



    
    
half = len(a)//2
root_value = a[half]
root = Node(root_value)


for i,e in enumerate(a):
  if i == half:
    continue
  root.insert(root, e)

print(root.value)
print(root.left_node.value)
print(root.right_node.value)
