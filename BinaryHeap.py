#Cada nodo contiene un valor superior al de sus hijos (para un montículo por máximos) o más pequeño que el de sus hijos (para un montículo por mínimos).
#El nodo raíz se almacena en la posición 0 del arreglo.
#Los hijos de un nodo almacenado en la posición k se almacenan en las posiciones 2k+1 y 2k+2 respectivamente.
#0|05|09|11|14|18|19|21|33|17|27|None Valores ---> 5(raiz) LEFFT 05 RIGHT 09
#----------------------------------
#0|01|02|03|04|05|06|07|08|09|10|11 Index

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        
        while i // 2 > 0:
            
            if self.heapList[i] < self.heapList[i // 2]:
                
            
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        
        while (i * 2) <= self.currentSize:
            
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:
            
            return i * 2
        else:
            
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1