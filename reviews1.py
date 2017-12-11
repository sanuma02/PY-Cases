from collections import defaultdict

data = ["I could not get my dog","Location was good","location was not bad but not Great","great food great personal","great location"]
datan = ['1','1','2','2','2']
words = ["Great","location","food"]

d = defaultdict(list)
x = zip(data,datan)
print x

for k,v in x:
    d[v].append(k)
    
print d
main = defaultdict(lambda: 0)

def Match(list_sentences, word):
    q = 0
    for s in list_sentences:
        s = s.lower()
        q += s.count(word.lower())
    return q

for k,v in d.iteritems():
    for w in words:
        main[k] +=  Match(v,w)

print main
print sorted(main.items(), key=lambda x: x[1], reverse=True)