arr = [13, 3, -2, 9, 8, 7, 4, 11, 0]
l = 0 # left margin
r = len(arr)-1 # right margin

def partition(arr, l, r):
    """ divide arr in to partition """

    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] < pivot:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[r],arr[i+1] = arr[i+1],arr[r]
    

    return i+1

def qs(arr, l, r):
    """sort the arr"""

    if l>=r:
        return arr
    p = partition(arr, l, r)

    qs(arr, l, p-1)
    qs(arr, p+1, r)

qs(arr,l,r)
   
print(arr)