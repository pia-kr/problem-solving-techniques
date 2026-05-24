# 예제 : 갯수 기반 -> 거리 기반으로

# 입력 받기
N, C = map(int, input().split())

# 집 주소 저장용
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()


# 최소 거리 dist 이상으로 공유기 설치 가능한가?
def can_cover(dist):
    count = 1  # 첫 집 설치
    last = houses[0]

    for i in range(1, N):
        # 마지막 공유기 위치와 dist 이상 차이나면 설치
        if houses[i] - last >= dist:
            count += 1
            last = houses[i]

    return count >= C


# 거리 범위
low = 1
high = houses[-1] - houses[0]

answer = 0

while low <= high:
    mid = (low + high) // 2

    if can_cover(mid):
        answer = mid
        low = mid + 1      # 더 큰 거리 가능한지
    else:
        high = mid - 1     # 거리 줄이기

print(answer)