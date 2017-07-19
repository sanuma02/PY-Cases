from collections import defaultdict
from collections import Counter

data = ["I could not get my dog","Location was good","location was not bad but not Great","great food great personal","great location"]
datan = ['1','1','2','2','2']
words = ["Great","location","food"]

d = defaultdict(str)
main = []
words = map(lambda x:x.lower(),words)

def countMatches(c,a):
   r = 0
   for i in xrange(len(a)):
      if c[words[i]] != 0:
         r += c[words[i]]
   return r


for i in xrange(0,5):
   hid = datan[i]
   comment = data[i]
   if len(d[hid]) != 0:
      d[hid] = d[hid] + " "+ comment.lower()
   else:
      d[hid] = comment.lower()

for k,v  in d.viewitems():
   s = v.split()
   c = Counter(s)
   res = countMatches(c,words)
   main.append((int(k),res))

main.sort(key=lambda x: x[1],reverse=True)
print main