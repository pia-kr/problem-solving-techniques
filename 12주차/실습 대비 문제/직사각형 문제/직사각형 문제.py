def maxNestedRectangles(rects):

    # 넓이 기준 오름차순 정렬
    rects.sort(key=lambda r: (r[2] - r[0]) * (r[3] - r[1]))

    n = len(rects)

    # dp[i] :
    # i번째 직사각형까지 봤을 때
    # rects[i]를 마지막으로 하는 최대 포함 개수
    dp = [1] * n

    # 모든 직사각형 비교
    for i in range(n):

        for j in range(i):

            # i가 j를 포함하는지 확인
            if (rects[i][0] <= rects[j][0] and
                rects[i][1] <= rects[j][1] and
                rects[i][2] >= rects[j][2] and
                rects[i][3] >= rects[j][3]):

                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0


# 입력
N = int(input())

rects = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    rects.append([x1, y1, x2, y2])


# 결과 출력
print(maxNestedRectangles(rects))