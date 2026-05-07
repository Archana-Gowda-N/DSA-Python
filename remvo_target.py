arr = [1,2,3,2,4]
target = 2

k = 0

for i in range(len(arr)):

    if arr[i] != target:
        arr[k] = arr[i]
        k += 1

print(arr[:k])


#find target in the array and remove it by replacing it with the last element of the array and reducing the size of the array by one. This approach does not maintain the order of the elements in the array.

arr = [1,2,3,2,4]
target = 2
k = len(arr)

for i in range(len(arr)):
    if arr[i] == target:
        arr[i] = arr[k-1]
        k -= 1

print(arr[:k])