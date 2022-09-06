

def solution(scovile, K):
    """
    음식들의 매운 지수가 주어질 때,
    가장 낮은 음식의 매운 지수가 K 이상이 되도록 섞어야 하는 최소 횟수
    음식을 섞을 때는, 가장 낮은 지수의 음식 + 두 번째로 낮은 지수의 음식 * 2 가 되도록 하며,
    K 이상이 될 수 없다면 최소 횟수는 -1 로 한다.

    param scovile : 음식의 매운 지수(0 ~ 백만)의 리스트, 길이 2 ~ 백만
    param K : 최소 매운 지수, 0 ~ 10억
    return count: 음식을 섞어야하는 최소 횟수
    """
    if K == 0:
        return 0
    
    if min(scovile) >=  K:
        return 0

    import heapq

    heapq.heapify(scovile)
    
    count = 0

    while scovile[0] < K:
        if len(scovile) <= 1:
            count = -1
            break

        min_value = heapq.heappop(scovile)
        second_min_value = heapq.heappop(scovile)
        value_to_insert = min_value + second_min_value * 2
        heapq.heappush(scovile, value_to_insert)
        count += 1
    
    return count

    

if __name__ == "__main__":
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([1, 12], 1) == 0
    assert solution([1, 0], 0) == 0
    assert solution([1, 0], 1) == 1
    assert solution([1, 1], 4) == -1
    assert solution([0, 0], 1) == -1
    assert solution([0, 0], 0) == 0
    assert solution([1, 1, 2], 3) == 2
    assert solution([1,1,1,1,1,1,100,100,100,100,0,0,0,0,0], 11) == 10
    

