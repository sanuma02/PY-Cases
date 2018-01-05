## PY-Notes

###### Python v2 vs v3

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
More details [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

###### String
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




