# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

def selectionSort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    new_arr.append(arr.pop(smallest))
    return new_arr
  
print(selectionSort([10, 2, 3, 6, 3]))