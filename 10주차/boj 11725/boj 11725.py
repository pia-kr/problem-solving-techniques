import sys
sys.setrecursionlimit(10**5)

N = int(input())

graph = [[] for _ in range(N + 1)]
# 확인용 배열
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    # 부모 - 자식 관계가 아니라 단순 연결 관계이기에 양방향 탐색을 위해 배열 2개
    graph[a].append(b)
    graph[b].append(a)


def dfs(now):
    for i in graph[now]:
        if parent[i] == 0:   # 아직 방문 안 함
            # 표시를 해두어야 다음번 탐색에서 위의 if 조건으로 막음
            # 간 곳은 표시 = 표시된건 이미 방문한 곳(부모노드임)
            # ex) graph[6] = [1, 3] , parent가 이 노드로 온 곳인지 이 노드에서 갈 곳인지 알려줌
            # 갈 곳이면 간 후 parent 를 바꿈
            parent[i] = now
            dfs(i)

dfs(1)

# 2번 노드 부터 출력
for i in range(2, N + 1):
    print(parent[i])