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