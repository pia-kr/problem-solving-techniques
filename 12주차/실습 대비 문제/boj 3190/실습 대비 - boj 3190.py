from collections import deque

# N 입력 받기
N = int(input())

# K 입력받기
K = int(input())

# 사과 위치 저장
apples = []
for i in range(K):
    x, y = map(int, input().split())
    apples.append((x, y))

# 방향 변환 횟수
L = int(input())

# 방향 정보 저장
directions = {}
for i in range(L):
    n, d = input().split()
    directions[int(n)] = d

# 방향: 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시작 방향 = 오른쪽
dir_idx = 0

# 뱀 위치 저장
# deque 쓰는 이유는 꼬리 제거할 때 O(1)로 가능하기 때문
snake = deque()
snake.append((1, 1))

# 현재 머리 위치
head_x, head_y = 1, 1

# 시간
time = 0

while True:
    time += 1

    # 다음 위치
    nx = head_x + dx[dir_idx]
    ny = head_y + dy[dir_idx]

    # 벽 충돌
    if nx < 1 or nx > N or ny < 1 or ny > N:
        print(time)
        break

    # 몸 충돌
    if (nx, ny) in snake:
        print(time)
        break

    # 머리 이동
    snake.append((nx, ny))

    # 사과 있으면 길이 증가
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        # 사과 없으면 꼬리 제거
        snake.popleft()

    # 머리 갱신
    head_x, head_y = nx, ny

    # 방향 전환
    if time in directions:
        if directions[time] == 'D':
            dir_idx = (dir_idx + 1) % 4
        else:  # L
            dir_idx = (dir_idx - 1) % 4