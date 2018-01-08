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
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in Celsius ]
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
### Set
Sets are an unordered collection of unique elements. We can construct them by using the set() function
```
x = set()
x.add(1) # add an element that already exists wont do anything
print(x) # will output {1}, sets can be think of as dictionary with only keys, but is not really a dictionary
```
**Basic Set Methods**

- s.add(element)
- s.clear() -- Removes all elements from the set
- s.copy() -- Returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy
- s.difference(sc) -- Returns the difference of two or more sets
- set1.difference_update(set2) -- Returns set1 after removing elements found in set2
- s.discard(2) -- Removes an element from a set if it is a member.If the element is not a member, does nothing
- s1.intersection(s2) -- Returns the intersection of two or more sets as a new set.(elements that are common to all of the sets)
- s1.intersection_update(s2) -- Returns set1 with the intersection of itself and another
- s1.isdisjoint(s2) -- This method will return True if two sets have a null intersection
- s1.issubset(s2) -- This method reports whether another set contains this set
- s2.issuperset(s1) -- This method will report whether this set contains another set
- s1.union(s2) -- Returns the union of two sets (i.e. all elements that are in either set)
- s1.update(s2) -- Update a set with the union of itself and other

### Files
Python has a built-in open function that allows us to open and play with basic file types.
```
# Open text.txt file
my_file = open('test.txt')
my_file.read() #this leaves the cursor at the end fo the file, my_file.seek(0) can be used to return to the top of the file
```
```
# Write to the file
my_file = open('test.txt','w+')
my_file.write('This is a new line')
```
Iteration through a File
```
for line in open('test.txt'):
    print(line)
```
### lambda expressions

ad-hoc functions without needing to properly define a function using def. "anonymous" functions
```
square = lambda num: num**2
square(2) # will output 4
```
```
adder = lambda x,y : x+y
adder(2,3) # will output 5
```

### Built-in Functions

**Map**

map() is a function that takes in two arguments: a function and a sequence iterable. In the form: map(function, sequence)
```
F_temps = map(fahrenheit, lst)
F_temps = map(lambda x: (5.0/9)*(x - 32), lst)
```
map() can be applied to more than one iterable. The iterables have to have the same length.
For instance, if we are working with two lists-map() will apply its lambda function to the elements of the argument lists, i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached.
```
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
map(lambda x,y:x+y,a,b)
map(lambda x,y,z:x+y+z, a,b,c)
```
**Reduce**

The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value. Like [ function(function(s1, s2),s3), ... , sn ]
```
lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst) # will output 113 --> (((47 + 11) + 42)+13)
```
**Filter**

The function filter(function, list) offers a convenient way to filter out all the elements of an iterable, for which the function returns True.
```
filter(lambda x: x%2==0,lst)
```
**Zip**

zip() makes an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
```
x = [1,2,3]
y = [4,5,6,7,8]

# Zip the lists together
zip(x,y) # output [(1, 4), (2, 5), (3, 6)]
```
Zip is defined by the shortest iterable length
```
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

zip(d1,d2) #output [('a', 'c'), ('b', 'd')] because simply iterating through the dictionaries will result in just the key
zip(d2,d1.values()) #  [('c', 1), ('d', 2)] mix keys and values
```
**Enumerate**

Enumerate allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element), 
enumerate() becomes particularly useful when you have a case where you need to have some sort of tracker.
```
lst = ['a','b','c']

for index,item in enumerate(lst):
    print index
    print item
```
**all() and any()**

all() and any() are built-in functions in Python that allow us to conveniently check for boolean matching in an iterable. all() will return True if all elements in an iterable are True
```
lst = [True,True,False,True]
all(lst) #output False
any(lst) #output True
```

A quick note for Python 3 users for the Map, Reduce, and Filter functions. These functions return iterators in Python 3 instead of lists (as in Python 2). To get a list for any of these functions in Python 3, you can just cast it as a list using list() around the function.

Also in Python 3, reduce is imported from functools.

**Decorators**

Decorators can be thought of as functions which modify the functionality of another function.
EXMAPLE without @

```
def needDecorator():
  print( 'I need Decorator!!!!')

def heyIhaveADecorador(func):
  
  def IAMtheDecorator():
    print('Decorating:')
    func()
    print('ALL DONE!')
  return IAMtheDecorator
  
needDecorator()
needDecorator = heyIhaveADecorador(needDecorator)
needDecorator()
```
#EXMAPLE with @

```
@heyIhaveADecorador
def needDecorator():
  print( 'I need Decorator!!!!')
  
  
needDecorator()
```

### Iterators and Generators

Generators allow us to generate as we go along, instead of holding everything in memory.
In Python 2 xrange() is a generator

Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. The main difference in syntax will be the use of a yield statement.

In most aspects, a generator function will appear very similar to a normal function. The main difference is when a generator function is compiled they become an object that support an iteration protocol. That means when they are called in your code the don't actually return a value and then exit, the generator functions will automatically suspend and resume their execution and state around the last point of value generation.

```
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
```
Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.

**next() and iter()**
The **next** function allows us to access the next element in a sequence. Lets check it out:

```
g = gencubes()
next(g) #output 0
next(g) #output 1
```

After yielding all the values next() caused a StopIteration error. What this error informs us of is that all the values have been yielded.

There are objects that are iterables but are not iterators like a string, you can iterate a string and get every word, however the object is not an iterator meaning you can not call the next method on them

The **iter()** function allows to convert objects that are iterable into iterators themselves!

```
s = 'hello'
s_iter = iter(s)
next(s_iter)
next(s_iter)
```

### Collections Module

**Counter**

Counter is a dict subclass which helps count hash-able objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

```
from collections import Counter
#Numbers
l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
# Output --- Counter({1: 6, 2: 6, 3: 4, 32: 1, 12: 1, 21: 1, 223: 1})
#Letters
Counter('aabsbsbsbhshhbbsbs')
# Output --- Counter({'b': 7, 's': 6, 'h': 3, 'a': 2})
#Words
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
Counter(words)
# Output --- Counter({'word': 3, 'each': 3, 'times': 2, 'show': 1, 'this': 1, 'many': 1, 'in': 1, 'up': 1, 'How': 1, 'does': 1, 'sentence': 1})
```

**Counter Common tasks**

- c.most_common(2) # [('word', 3), ('each', 3)]
- c.clear()                       # reset all counts
- list(c)                         # list unique elements
- set(c)                          # convert to a set
- dict(c)                         # convert to a regular dictionary
- c.items()                       # convert to a list of (elem, cnt) pairs
- Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
- c.most_common()[:-n-1:-1]       # n least common elements
- c += Counter()                  # remove zero and negative counts

**defaultdict**

defaultdict is a dictionary like object which provides all methods provided by dictionary but takes first argument (default_factory) as default data type for the dictionary

```
from collections import defaultdict
d  = defaultdict(object)
d  = defaultdict(list)
d  = defaultdict(str)
d = defaultdict(lambda: 0) # initialize with default value 0

```
A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

**OrderedDict**

An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

```
print 'Dictionaries are equal? '

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = collections.OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2) #Output False (a regular dict will say True)
```

**namedtuple**
Work like a quick way of creating a new object/class type with some attribute fields.

```
from collections import namedtuple

Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")

print(sam)
print(sam.age)
print(frank.name)
```
First pass the object type name (Dog) and then pass a string with the variety of fields as a string with spaces between the field names.

### datetime
**time**

```
import datetime

t = datetime.time(4, 20, 1)
# Lets show the different compoenets

print(t) # Output 04:20:01
print('hour  :', t.hour) # Output hour  : 4
print('minute:', t.minute) # Output minute: 20
print('second:', t.second) # Output second: 1
print('microsecond:', t.microsecond) # Output microsecond: 0
print('tzinfo:', t.tzinfo) # Output tzinfo: None

```
 **date**
 
 ```
 today = datetime.date.today()
print(today) # Output 2015-09-18
print('ctime:', today.ctime()) # Output ctime: Fri Sep 18 00:00:00 2015
print('ordinal:', today.toordinal()) # Output ordinal: 735859
print('Year:', today.year) # Output Year: 2015
print('Mon :', today.month) # Output Mon : 9
print('Day :', today.day) # Output Day : 18
```
 **timedelta**
 
 ```
 today = datetime.date.today()
 one_day = datetime.timedelta(days=1)
 yesterday = today - one_day
 tomorrow = today + one_day
 
 print('tomorrow - yesterday:', tomorrow - yesterday) #output 2 days, 0:00:00
 ```

### Object Oriented Programming

Define a class

```
class Dog(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
sam = Dog('Lab','Sam')
```

Methods

```
class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius
        

c = Circle()
c.setRadius(2)
print('Radius is: ',c.getRadius())
print('Area is: ',c.area())
```
**Inheritance**
```
class Animal(object):
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "Woof!"
```
**Special Methods**

```
class Book(object):
    def __init__(self, title, author, pages):
        print "A book is created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print "A book is destroyed"
```
