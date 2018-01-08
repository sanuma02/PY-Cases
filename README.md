## PY-Notes

### Python v2 vs v3
###### Division
"Classic" division vs "True" division. 
Two option for Python v2:
```
# Specifying one of the numbers as a float or casting it 
float(3)/2
```
```
from __future__ import division
3/2
```
In case "Classic division is needed on Python v3:
```
3//2
```
###### Functions

Map, Reduce, and Filter functions in Python 3 return iterators instead of lists (as in Python 2). To get a list for any of these functions in Python 3, you can just cast it as a list using list() around the function.

More details [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

### String
Strings are **immutable**. This means that once a string is created, the elements within it can not be changed or replaced.
While slicing the instruction to Python is to  grab everything from 0 up to 3. It doesn't include the 3rd index on a "up to, but not including" fashion
- Everything --> s[:]
- Grab everything past the first element --> s[1:]
- Grab everything UP TO the 3rd index --> s[:3]
- Last letter (one index behind 0 so it loops back around) --> s[-1]
- Grab everything but the last letter --> s[:-1]
- Grab everything, but go in step sizes of 2 --> s[::2]
- Backwards --> s[::-1] (for palindromes on pyv3 make sure to use s.casefold())

String can be concatenated and multiply:
```
letter = 'z'
letter*10
-------
Output:'zzzzzzzzzz'
```
**Basic Built-in String methods**
- s.lower(),s.upper()
- s.islower(), s.isupper()
- s.count('p') -- How many time does 'p' appears on s
- s.find('p') -- Find the index where 'p' is
- s.capitalize()
- s.endswith('p')
- s.isalnum(), s.isalpha()
- s.split() -- By default uses " ". Parameter can be used: 'hello'.split('e') --> ['h', 'llo']

**Print Formatting**
```
'Insert another string with curly brackets: {}'.format('The inserted string')
'First: {x}, Second: {x}'.format(x='new')
'First: %s, Second: %s' %('hi',2)
'Floating number with 3 decimals %1.3f' %(13.45)
```
### List
Unlike strings, they are mutable, meaning the elements inside a list can be changed!
Lists can actually hold different object types
+ and * Can be use to concatenate lists without changing the original list (same as strings)

**Basic List methods**

- l.append(object) 
- l.pop() ---  "pop off" an item from the list, by default pop takes off the last index l.pop(0) --> first element
- l.reverse() --- Permanent
- l.sort()
- l.count(element) -- takes in an element and returns the number of times it occures in your list
- l.extend([list]) -- extends list by appending elements from the iterable
- l.index -- index will return the index of whatever element is placed as an argument
- l.insert(index, element)
- l.remove(element) -- removes the first occurrence of a value

**List Comprehensions**
They build lists on a different notation, one line for inside brackets
It starts by the result you want to see on the list, for example x elevated to 2, the append is implicit
```
lst= [x**2 for  x in xrange(1,4)] 
```
### Dictionary

**Basic Dictionary methods**
```
d = {'key1':1,'key2':2,'key3':3}
print(d.keys())
print(d.values())
print(d.items())
```
Python 2 will have available methods d.iterkeys(), d.itervalues() and d.iteritems():

**Dictionary Comprehensions**
```
d= {x:x**2 for x in range(10)}
```

### Tuple
In Python tuples are very similar to lists, however, unlike lists they are **immutable** meaning they can not be changed. You would use tuples to present things that shouldn't be changed.

```
t = (1,2,3)
t = ('one',2)
```
len(t), indexing and slicing are available for tuples just like in lists, however methods like append or extend are not

**Basic Tuple Methods**
```
# Use .index to enter a value and return the index
t.index('one')
```
```
# Use .count to count the number of times a value appears
t.count('one')
```








