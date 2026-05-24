# N S 입력받기
N, S = map(int, input().split())

# 수열 입력받기
num = list(map(int, input().split()))

# 부분 수열을 보고 합이 S 가 되는 경우에 카운트 증가 하는 함수
def count_subsequences(start, current_sum):

    if start == N:
        if current_sum == S:
            return 1
        return 0
    # 경우 1 : 현재 보고있는 수(start 번째) 포함하는 경우 -> 포함했으니 합에 추가
    include_current = count_subsequences( start + 1, current_sum + num[start])
    
    # 경우 2 : 현재 보고있는 수(start 번째) 포함하지 않는 경우
    exclude_current = count_subsequences( start + 1, current_sum )

    # 두 경우 합치기
    return include_current + exclude_current
# 부분 수열의 합이 S가 되는 경우의 수 계산
ans = count_subsequences(0, 0)

# 공집합 제거
if S == 0:
    ans -= 1

print(ans)