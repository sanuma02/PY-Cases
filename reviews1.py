from collections import defaultdict

data = ["I could not get my dog","Location was good","location was not bad but not Great","great food great personal","great location"]
datan = ['1','1','2','2','2']
words = ["Great","location","food"]

d = defaultdict(str)
x = zip(datan,data)


for k,v in x:
    d[k] = d[k] + " " + v
    
print(d)
main = []

def Match(list_sentences, words):
    result = 0
    for word in words:
      result += list_sentences.lower().count(word.lower())
    return result
  
for k,v in d.items():
  main.append((k,Match(v,words)))


print(main)
print(sorted(main, key=lambda x: x[1], reverse=True)) 
