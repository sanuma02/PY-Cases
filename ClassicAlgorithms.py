#Classic Algorithms

def conjecture(n):
  if n == 1:
    return 0
  else:
    times = 0
    while n > 1:
      if n % 2 == 0:
        n = n // 2
      else: 
        n = n * 3 + 1 
      times += 1
    return times
    
lst = [5,1,4,2,8]
print(lst[0])


def bubble(to_sort):
  i = 0
  times = 0
  while i < len(to_sort) -1:
    if to_sort[i] > to_sort[i+1]:
      to_sort[i],to_sort[i+1] =to_sort[i+1],to_sort[i]
      times += 1
    i += 1
  return times, to_sort
  
def bubble_up(to_sort):
  times = 1
  while times != 0:
    times, to_sort = bubble(to_sort)
  return to_sort
  
print(bubble_up(lst))
    
def merge(lst0, lst1):
    ret = []
    while lst0 and lst1:
        if lst0[0] <= lst1[0]:
            ret.append(lst0.pop(0))
        else:
            ret.append(lst1.pop(0))
    ret.extend(lst0)
    ret.extend(lst1)
    return ret
print(merge([17,26,54,93],[20,31,44,55,77]))

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    # random to avoid dead loop for special sequence
    r = lst[random.randint(0, len(lst) - 1)]
    left, mid, right = [], [], []
    for i in lst:
        if i < r:
            left.append(i)
        elif i == r:
            mid.append(i)
        else:
            right.append(i)
    left = mergesort(left)
    left.extend(mid)
    right = mergesort(right)
    ret = merge(left, right)
    return ret
    
    
def mergesort1(lst):
  if len(lst) <=1:
    return lst
  half = len(lst)//2
  left = lst[:half]
  right= lst[half:]
  return left,right
  

  
print(mergesort1([5,1,5,5,9,4,2,8]))
    
    

    