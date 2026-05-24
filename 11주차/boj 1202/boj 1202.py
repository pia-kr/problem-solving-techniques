'''핵심 아이디어 : 용량이 작은 가방부터 채울 것인지 Vs 가치가 높은 가방부터 채울 것인지
용량이 작은 가방이 넣을 수 있는 경우가 작으니 얘부터 하기
'''
import heapq

# N K 입력
N, K = map(int, input().split())

# N 번 K 번 반복하며 입력 받기
jewel = []
bag = []
for _ in range(N):
    Mi , Vi = map(int, input().split())
    jewel.append((Mi, Vi))

for _ in range(K):
    Ci = int(input())
    bag.append(Ci) 

# 가방과 보석을 오름차순으로 정렬 -> 용량 작은거 부터 넣기 위해
jewel.sort()
bag.sort()

# 가방 기준으로 자기 무게보다 작은 보석 중 값이 제일 큰거 넣기

# 최대 가격을 뽑기 위한 heap
heap = []

# 보석 인덱스
index = 0

# 결과값
result = 0

# 가방 하나씩 확인
for current_bag in bag:

    # 현재 가방에 들어갈 수 있는 보석들 heap에 추가
    while index < N and jewel[index][0] <= current_bag:

        # heapq는 min heap 이므로 가격에 - 붙이기
        heapq.heappush(heap, -jewel[index][1])

        index += 1

    if heap:
        # 가장 가치가 큰 보석 추가
        result += -heapq.heappop(heap)

# 결과 출력
print(result)