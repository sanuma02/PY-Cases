from itertools import combinations

data = [(1,3),(7,10),(24332,24345),(2,6)]
l = list(combinations(data,2))
for i in xrange(len(l)):
   a,b = l[i]
   c,d = a
   e,f = b
   print set(range(c,d)) & set(range(e,f))
