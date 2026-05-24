arr = [2, 3, 5, 7, 9]
target = 10

arr.sort()

left = 0
right = len(arr) - 1

found = False

while left < right:
    s = arr[left] + arr[right]

    if s == target:
        found = True
        print(arr[left], arr[right])
        break

    elif s < target:
        left += 1

    else:
        right -= 1

print(found)