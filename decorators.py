
#Decorators

#Funcitons that modify the funcitnally of other funtions

#globals() 
#locals()
#dictionary of variables

#EXMAPLE without@
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

#Example with @

@heyIhaveADecorador
def needDecorator():
  print( 'I need Decorator!!!!')
  
  
needDecorator()

#***Yield VS return ***
#*** Avoid having entire list on memory ****

def generateCube(n):
  for x in range(n):
    yield x ** 3
    
for i in generateCube(10):
  print(i)
  
  
def RetunedCube(n):
  l = []
  for x in range(n):
    l.append(x ** 3)
  return l
  