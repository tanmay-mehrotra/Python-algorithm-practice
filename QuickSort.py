'''
Created on Jul 11, 2014

@author: tanmaymehrotra
'''
data = [0,13,9,4,19,17,9,5,10,15]

def quickSort(st,end):
    if st<end:
        partIndex = partition(st,end)
        quickSort(st,partIndex-1)
        quickSort(partIndex+1,end)
      
def partition(st,end):
    partIndex = st
    pivot = data[st]
    for i in range(st+1,end+1):
        if data[i] < pivot:
            swap(i,partIndex+1)
            partIndex+=1
    swap(st,partIndex)
    return partIndex
    
def swap(a,b):
    swap = data[a];data[a]=data[b];data[b]=swap;
    
if __name__ == '__main__':
    quickSort(0,len(data)-1)
    print data