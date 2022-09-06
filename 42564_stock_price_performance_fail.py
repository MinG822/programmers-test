def solution(prices):
    """
    초 단위로 기록된 주식 가격이 담긴 리스트 prices 에 대해서,
    각 초의 가격이 떨어지지 않은 기간을 반환하는 함수
    param prices : 초 단위로 기록된 주식 가격(1~10000) 리스트, 길이 2 ~ 100000
    return answer : 각 초의 가격이 떨어지지 않은 시간의 리스트
    """
    answer = []
    min_last_idx = {}
    curr_min = 10001

    for i in range(len(prices) - 1, -1, -1):
        if min_last_idx.get(prices[i]) is None:
            min_last_idx[prices[i]] = [i]
            
        else:
            if i - min_last_idx[prices[i]][-1] > 1:
                min_last_idx[prices[i]] = [i]
            else:
                min_last_idx[prices[i]].append(i)
        # 현재 내 가격 보다 더 작은 가격까지의 거리
        if curr_min < prices[i]:
            smaller_price_distances = [min_last_idx[min_price][-1] for min_price in min_last_idx.keys() if min_price < prices[i]]
            curr_min_idx = min(smaller_price_distances) - i
        else:
            curr_min_idx = len(prices) - 1 - i
            curr_min = prices[i]    
            
        answer.insert(0, curr_min_idx)
    return answer


if __name__ == "__main__":
    # assert str(solution([3, 2, 1])) == str([1, 1, 0])
    # assert str(solution([1, 2, 4, 2, 4])) == str([4, 3, 1, 1, 0])
    # assert str(solution([1, 2, 2, 3, 3])) == str([4, 3, 2, 1, 0])
    assert str(solution([1, 2, 2, 3, 3, 2, 2])) == str([6,5,4,2,1,1,0])