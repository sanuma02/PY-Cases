#O(n2)
def swap(x,y,arr):
  arr[x],arr[y] =  arr[y],arr[x]
  

def bubble(arr):
  if len(arr) <= 0:
    return arr
  for x in range(len(arr)-1,0,-1):
    for y in range(x):
      if arr[x] < arr[y]:
        swap(x,y,arr)
  return arr
    
arr = [1,5,8,2,3]
print(bubble(arr))
    
def selectionSort(arr):
  for tobefill in range(len(arr) -1,0,-1): #start for the last position to place the highest element
    index_max = 0
    for index in range(1,tobefill+1): #find the highest on the elements not sorted yet
      if arr[index] > arr[index_max]:
        index_max = index
    arr[tobefill],arr[index_max] = arr[index_max],arr[tobefill]
  return arr
  
arr = [5,8,3,10,1]
print(selectionSort(arr))

      
def insertionSort(arr):
  for i in range(1,len(arr)):
    to_insert_value = arr[i]
    to_insert_index = i
    if to_insert_value < arr[to_insert_index - 1]: #if the prev one is higher 
      while to_insert_value < arr[to_insert_index - 1] and to_insert_index > 0: #then find the insert index it needs to be in
        arr[to_insert_index] = arr[to_insert_index -1]
        to_insert_index -= 1 #inserted
      arr[to_insert_index] = to_insert_value
  return arr
  
arr=[5,6,1,3,4]
print(insertionSort(arr))

def insertionSortGap(start,arr,gap):
  for i in range(start+gap,len(arr),gap):
    to_insert_value = arr[i]
    to_insert_index = i
    if to_insert_value < arr[to_insert_index - gap]:
      while to_insert_value < arr[to_insert_index - gap] and to_insert_index >= gap:
        arr[to_insert_index] = arr[to_insert_index -gap]
        to_insert_index = to_insert_index - gap
      arr[to_insert_index] = to_insert_value
    
#O(n log n2)
def shellSort(arr):
  items_apart = len(arr) //2
  while items_apart > 0:
    for i in range(len(arr)):
      insertionSortGap(i,arr,items_apart)
    items_apart = items_apart // 2
  return arr
    
arr=[5,6,1,3,4]
print(shellSort(arr))

#O(n log n)

def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2 
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    mergeSort(leftarr)
    mergeSort(rightarr)
    i = 0 
    j = 0 
    k = 0 
    
    while i < len(leftarr) and j <len(rightarr):
      if leftarr[i] < rightarr[j]:
        arr[k] = leftarr[i]
        i+= 1
      else:
        arr[k] = rightarr[j]
        j+=1
      k+=1
    while i < len(leftarr):
      arr[k] = leftarr[i]
      i += 1 
      k += 1 
    while j < len(rightarr):
      arr[k] = rightarr[j]
      j += 1 
      k += 1
    #print("mergin:", arr)
    return arr
    
arr=[5,6,1,5,32,74,224,3,4]
print(mergeSort(arr))
    
def setMarkers(arr,first_index,last_index):
  pivotvalue = arr[first_index]
  leftmark = first_index+1
  rightmark = last_index
  while True:
    while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
      leftmark = leftmark + 1
    while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark -1
    if rightmark < leftmark:
      break
    else:
      temp = arr[leftmark]
      arr[leftmark] = arr[rightmark]
      arr[rightmark] = temp

  temp = arr[first_index]
  arr[first_index] = arr[rightmark]
  arr[rightmark] = temp
  return rightmark
  
  
def split_point(arr,start,end):
  if start < end:
    split = setMarkers(arr,start,end)
    split_point(arr,start,split-1)
    split_point(arr,split+1,end)
    

def quickSort(arr):
  split_point(arr,0,len(arr)-1)
  return arr
    
arr=[5,6,1,5,32,74,224,3,4]
print(quickSort(arr))