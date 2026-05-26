def solve():

    K = int(input())

    # 메모이제이션
    # key : (현재 숫자, 현재 깊이)
    # value : 가능한 숫자들 집합
    memo = {}

    def dfs(current_val, depth):

        # 정확히 K번 역추적 완료
        if depth == K:
            return {current_val}

        # 이미 계산한 경우
        if (current_val, depth) in memo:
            return memo[(current_val, depth)]

        # 가능한 숫자들 저장
        possible_candidates = set()

        # 경우 1 : 이전 수가 짝수였던 경우
        # current_val * 2 -> /2 -> current_val
        possible_candidates.update(
            dfs(current_val * 2, depth + 1)
        )

        # 경우 2 : 이전 수가 홀수였던 경우
        if (current_val - 1) % 3 == 0:

            prev_odd = (current_val - 1) // 3

            # 홀수 + 자연수 조건
            if prev_odd > 1 and prev_odd % 2 != 0:

                possible_candidates.update(
                    dfs(prev_odd, depth + 1)
                )

        # 메모 저장
        memo[(current_val, depth)] = possible_candidates

        return possible_candidates

    final_numbers = dfs(1, 0)

    print(min(final_numbers))
    print(max(final_numbers))


solve()