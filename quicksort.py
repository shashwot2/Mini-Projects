def quicksort(arr):
  if len(arr) == 1 or len(arr) == 0:
      return arr
  else:
    mid = len(arr)//2
  pivot = arr[mid]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quicksort(left) + middle + quicksort(right)
  
  

arr = [5,6,7,6,8,9,10,20,30]  
print(quicksort(arr))