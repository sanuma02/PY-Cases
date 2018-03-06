import ctypes
class M():
  
  def public(self):
    print('You can check me with tab')
    
  def _private(self):
    print('No you cant see me with tab')
    
m = M()
m._private()

class DynamicArray():
  
  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)
    
  def __len__(self):
    return self.n
    
  def __getitem__(self,k):
    if not 0 <= k < self.n:
      return IndexError('k is out of bounds')
    return self.A[k]
    
  def append(self,element):
    if self.capacity == self.n:
      self._resize(2*self.capacity)
    self.A[self.n] = element
    self.n += 1
      
  def _resize(self,capacity):
    B = self.make_array(capacity)
    for item in range(self.n):
      B[item] = self.A[item]
    
    self.A = B
    self.capacity = capacity
    
  def make_array(self,capacity):
    return (capacity * ctypes.py_object)()
    
arr = DynamicArray()
arr.append(2)
print(len(arr))
    
      
    