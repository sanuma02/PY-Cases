from math import pi

def pinthdigit(n):
  if n > 20:
    n = 20
  return round(pi,n)
  

def Fibonacci(n):
  if n > 20:
    n = 20
  a = 1
  b = 1
  while n > 0:
    yield a
    old_a = a
    a = b
    b = old_a + b
    n -= 1


def isPrime(n):
  if n > 1:
    if n == 2:
      return True
    else:
      for x in range(2,n):
        if n % x == 0:
          return False
      return True
  else:
    return False
      
def primeList(n):
  return [x for x in range(1,n) if isPrime(x)]
  
def get_prime_factors(n):
  factors = []
  for i in range(1,n+1):
    if n % i == 0 and isPrime(i):
      factors.append(i)
  return factors
 
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
    
def factorial1(n):
  r = 1
  for i in range(1,n+1):
    r = r * i
  return r
  
  
def timesOver(amount,currancy):
  times = 0
  while amount >= currancy:
    times += 1
    amount -= currancy
  return times,amount

options = [50000,20000,10000,5000,2000,1000,500,100,50,25,10,5,1]
amount = 5000
total = 2563
change = amount - total
changelst = []
for option in options:
  if option <= change :
    t,a = timesOver(change,option)
    changelst.append((t,option))
    change -= (t * option)
    
print(changelst)




