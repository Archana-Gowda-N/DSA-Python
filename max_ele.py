arr = [4, 7, 2, 9, 1, 5]

max_ele = arr[0]

for i in arr:
    if i > max_ele:
        max_ele = i

print("Maximum =", max_ele)


# Output: Maximum = 9

arr = [4, 7, 2, 9, 1, 5]

left = 0
right = len(arr) - 1

max_ele = arr[0]

while left <= right:

    if arr[left] > max_ele:
        max_ele = arr[left]

    if arr[right] > max_ele:
        max_ele = arr[right]

    left += 1
    right -= 1

print("Maximum =", max_ele)

# Output: Maximum = 9