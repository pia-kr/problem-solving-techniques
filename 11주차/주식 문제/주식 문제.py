# n일간의 주식 가격이 주어짐(n개로) 주식을 사고 한 번 팔 수 있을 때 얻을 수 있는 최대 이익

n = int(input())
prices = list(map(int, input().split()))    
# 2일차 부터 파니 이후로 가격차 보기

diff = 0
for i in range(1, n):
    # 가격차는 i 번째 날 가격 - (1~ i-1) 번째 가격 중 최솟값
    # 슬라이싱은 a:b -> a~b-1 까지의 범위를 의미하므로 [:i]로 하면 0~i-1 번째 가격이 나옴
    if prices[i] - min(prices[:i]) > diff:
        diff = prices[i] - min(prices[:i])
print(diff)
