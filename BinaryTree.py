def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#OOO

class BinaryTree(object):
  
  def __init__(self,rootObj):
    self.key = rootObj
    self.leftChild = None
    self.rightChild  = None
    
  def insertLeft(self,newNode):
    if self.leftChild == None:
      self.leftChild = BinaryTree(newNode)
    else:
      new_child = BinaryTree(newNode)
      new_child.leftChild = self.leftChild # To push down the current child at the left
      self.leftChild = new_child

    
    
  def insertRight(self,newNode):
    if self.rightChild == None:
      self.rightChild = BinaryTree(newNode)
    else:
      new_child = BinaryTree(newNode)
      new_child.leftChild = self.rightChild # To push down the current child at the right
      self.rightChild = new_child
      
  def getRightChild(self):
    return self.rightChild
    
  def getLeftChild(self):
    return self.leftChild
    
  def setRootVal(self,value):
    self.key = value
    
  def getRootVal(self):
    return self.key


    
r = BinaryTree('r')
r.insertLeft('e')
r.getLeftChild().insertLeft('x')
r.getLeftChild().getLeftChild().insertLeft('y')
r.getLeftChild().getLeftChild().insertRight('s')
r.insertRight('a')
r.getRightChild().insertLeft('t')
r.getRightChild().getLeftChild().insertLeft('aa')
r.getRightChild().getLeftChild().insertRight('o')
r.getRightChild().getLeftChild().getRightChild().insertLeft('n')

#traversals
#PREORDER

def preOrder(tree):
  if(tree != None):
    print(tree.key)
    preOrder(tree.leftChild)
    preOrder(tree.rightChild)
    
print(preOrder(r))

def postOrder(tree):
  if tree != None:
    postOrder(tree.leftChild)
    postOrder(tree.rightChild)
    print(tree.key)
    
print(postOrder(r)) # starts from the leafs left to right ends on root

def inOrder(tree):
  if tree != None:
    inOrder(tree.leftChild)
    print(tree.key)
    inOrder(tree.rightChild)
    
print(inOrder(r)) #from the leafs left top right root in the middle
    