def solve(K):

    # 현재 단계에서 가능한 수들 저장
    current_set = {1}

    # K번 역추적
    for _ in range(K):

        # 다음 단계 저장
        next_set = set()

        # 현재 가능한 숫자들 탐색
        for x in current_set:

            # 1. 이전 수가 짝수였던 경우
            # x*2 -> /2 -> x
            next_set.add(x * 2)

            # 2. 이전 수가 홀수였던 경우
            # prev -> 3*prev+1 -> x
            if (x - 1) % 3 == 0:

                prev_odd = (x - 1) // 3

                # 이전 수는 홀수여야 함
                if prev_odd > 1 and prev_odd % 2 != 0:
                    next_set.add(prev_odd)

        # 다음 단계로 이동
        current_set = next_set

    # 결과 출력
    print(min(current_set), max(current_set))


# 입력
K = int(input())

solve(K)