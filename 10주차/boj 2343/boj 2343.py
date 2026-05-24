N, M = map(int, input().split())

# N개 입력받기
arr = list(map(int, input().split()))

# 최소 크기 : 1개만 들어감 -> 가장 큰애는 들어가야함
left = max(arr)
# 최대 크기 : 모두가 1개에 들어감
right = sum(arr)

# 이분 탐색하기
def count_blueray(mid):
    total = 0
    # 블루레이 갯수
    count = 1

    for i in arr:
        
        if total + i <= mid:
            total += i

        else:
            count += 1
            total = i
    
    return count

# Minimum 값 찾아보기
while left <= right:
    mid = (left + right) // 2

    ans = count_blueray(mid)

    if ans <= M:
        right = mid - 1
    else:
        left = mid + 1
# 가능한 최소 값은 저 범위 left ~ right 중 left 값임
print(left)

