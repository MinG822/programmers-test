from collections import deque


def solution(cap, n, deliveries, pickups):
    """
    트럭에 실을 수 있는 최대 상자 개수, 배달할 집 개수, 배달할 상자 개수, 수거할 상자 개수들이 주어질 때,
    트럭의 최소 이동 거리를 구하는 함수
    NOTE 트럭은 항상 물류창고에서 시작하며, i 위치와의 거리는 i + 1 이다

    param cap : 1 ~ 50 이하
    param n : 1 ~ 100000 이하
    param deliveries, pickups: 0 ~ 50 이하
    return result: 최소 이동 거리
    """
    result = 0
    curr_d, curr_p = cap, cap

    is_stop_over = True
    is_p_stop_over = True

    d_results, p_results = deque([]), deque([])

    i = n - 1
    again_i = False
    while i > -1:
        if curr_d - deliveries[i] < 0:
            is_stop_over = True
            if deliveries[i] - curr_d >= n:
                deliveries[i] -= curr_d
                curr_d = n
                again_i = True
            else:
                curr_d = cap - (deliveries[i] - curr_d)
        else:
            if curr_d == n:
                is_stop_over = True
            curr_d -= deliveries[i]

        if curr_p - pickups[i] < 0:
            is_p_stop_over = True
            if pickups[i] - curr_p >= n:
                pickups[i] -= curr_p
                curr_p = n
                again_i = True
            else:
                curr_p = cap - (pickups[i] - curr_p)
        else:
            if curr_p == n:
                is_p_stop_over = True
            curr_p -= pickups[i]

        if is_stop_over and deliveries[i]:
            d_results.append(i)
            is_stop_over = False

        if is_p_stop_over and pickups[i]:
            p_results.append(i)
            is_p_stop_over = False

        if again_i:
            again_i = False
        else:
            i -= 1

    result = 0
    # print(d_results, p_results)
    while True:
        if p_results:
            pi = p_results.popleft()
            if d_results:
                di = d_results.popleft()
                result += (max(pi, di) + 1) * 2
            else:
                result += (pi + 1) * 2
        elif d_results:
            di = d_results.popleft()
            result += (di + 1) * 2

        else:
            break
    return result


if __name__ == "__main__":
    assert solution(1, 1, [1], [0]) == 2
    assert solution(1, 1, [0], [1]) == 2
    assert solution(1, 1, [0], [2]) == 4
    assert solution(1, 1, [0], [3]) == 6
    assert solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]) == 16
    assert solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]) == 30
