T = int(input())
ans = []

for i in range(T):

    n = int(input())
    prices = list(map(int, input().split()))

    # 뒤에서부터 볼 때의 최대 주가
    max_price = 0

    # 최대 이익
    diff = 0

    # 뒤에서부터 탐색
    for i in range(n - 1, -1, -1):

        # 현재 가격이 더 크면 최고가 갱신
        if prices[i] > max_price:
            max_price = prices[i]

        # 현재 가격에 사서 미래 최고가에 판다고 생각
        else:
            diff += max_price - prices[i]

    ans.append(diff)

for i in ans:
    print(i)
