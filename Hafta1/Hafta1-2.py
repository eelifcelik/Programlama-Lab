#bubble sort
def bubbleSort(list_1):
  n= len(list_1)

  for i in range (n,0,-1):
  
    for j in range(n):

      if list_1[j]> list_1[j+1]:
        t = list_1[j+1]
        list_1[j+1]=list_1[j]
        list_1[j] =t
        
return list_1

#selection sort

def selectionSort(list_1):
  n = len(list_1)

  for i in range(n): 
       
    min = i 
    for j in range(i+1, n): 
        if A[min] > A[j]: 
            min = j 
               
    A[i], A[min] = A[min], A[i] 
  
return list_1
