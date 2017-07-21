shapes = [[10,10,10,10],[86,90,86,90],[4,45,64,23],[34,34,34,45],[-100,19,-23,-9]]
s = 0
r = 0
n = 0

for i in xrange(len(shapes)):
   data = shapes[i]
   if all(j > 0 for j in data):
      if data[0] == data[2] and data[1] == data[3] and len(data) == 4:
         if data[1] == data[0]:
            s += 1
         else:
            r += 1
      else:
         n += 1
   else:
      n += 1

print str(s) +str(r) +str(n)
