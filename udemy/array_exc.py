from collections import defaultdict
from collections import Counter

def anagram(s1,s2):
  s1,s2 = s1.replace(" ",""),s2.replace(" ","")
  s1 = sorted(s1)
  s2 = sorted(s2)
  if s1 == s2:
    return True
  return False
print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('aa','bb'))
print(anagram('go go go','gggooo'))
print(anagram('abc','cba'))
print(anagram('hi man','hi     man'))
print(anagram('aabbcc','aabbc'))
print(anagram('123','1 2'))


def pair_sum(arr,k):
  st = set()
  while len(arr) > 0:
    num = arr.pop()
    for x in arr:
      if (num + x) == k:
        st.add((max(num,x),min(num,x)))
  return st
  
print(pair_sum([1,3,2,2],4))
print (pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))
print(pair_sum([1,3,2,2],4))
        
def finder(arr1,arr2):
  d = defaultdict(lambda: 0)
  for item in arr2:
    d[item] +=1
  for value in arr1:
    if d[value] == 0:
      return value
    else:
      d[value] -= 1
  return 0
  
def finder2(arr1,arr2):
  arr1.sort()
  arr2.sort()
  pairs = zip(arr1,arr2)
  for a,b in pairs:
    if a != b:
      return a
  return 0
  
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
arr3 = [5,5,7,7]
arr4 = [5,7,7]
print(finder(arr1,arr2))
print(finder(arr3,arr4))
print(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))

def large_cont_sum(arr):
  biggest = arr[0]
  acumm = arr[0]
  for item in arr[1:]:
    acumm = max(acumm + item,item)
    biggest = max(biggest,acumm)
  return biggest

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
print(large_cont_sum([1,2,-1,3,4,-1]))
print(large_cont_sum([-1,1]))

def rev_word(s):
  s = s.strip()
  return ' '.join(str(x) for x in s.split()[::-1])

print(rev_word('Hi John,   are you ready to go?'))
print(rev_word('    space before'))
print(rev_word('1'))

def compress(s):
  if len(s) == 1:
    return s
  c = Counter(s)
  result = ""
  for letter in c:
    if letter not in result:
      result += letter + str(c[letter])
  return result
    
print(compress('AAAAABBBBCCCC'))
print(compress(' '))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))

def uni_char(s):
  if len(s) == 0:
    return True
  if len(s) == 1:
    return True
  c = Counter(s)
  return c.most_common()[0][1] == 1
  
def uni_char2(s):
  return len(set(s)) == len(s)
  
print(uni_char(' '))  
print(uni_char('goo'))
print(uni_char('abcdefg'))
