# 인풋 처리 부분 생략

N = int(input())       # 집의 개수
K = int(input())       # 경비실 개수
houses = list(map(int, input().split()))  # 집의 위치 배열

houses.sort()

# 거리 D로 K개 이하의 경비실을 사용해 모든 집을 커버할 수 있는지 확인
def can_cover(max_dist):
    count = 1

    # 첫 번째 경비실의 최대 커버 범위:
    # 첫 집의 좌표 + (최대 거리 * 2)
    limit = houses[0] + max_dist * 2

    for i in range(1, N):
        if houses[i] > limit:
            count += 1
            limit = houses[i] + max_dist * 2

    return count <= K


# 이분 탐색 범위 설정
low = 0

# 가능한 최대 거리는 양 끝 집 사이의 거리
high = houses[-1] - houses[0]

answer = high

while low <= high:
    mid = (low + high) // 2

    if can_cover(mid):
        answer = mid      # 조건 만족 시 정답 갱신
        high = mid - 1    # 더 작은 최대값 가능한지 탐색
    else:
        low = mid + 1     # 조건 불만족 시 거리 증가

print(answer)