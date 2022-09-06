def solution(prices):
    """
    초 단위로 기록된 주식 가격이 담긴 리스트 prices 에 대해서,
    각 초의 가격이 떨어지지 않은 기간을 반환하는 함수
    param prices : 초 단위로 기록된 주식 가격(1~10000) 리스트, 길이 2 ~ 100000
    return answer : 각 초의 가격이 떨어지지 않은 시간의 리스트
    """
    answer = []
    price_dict = {n:0 for n in range(10000)}
    price_dict[prices[-1]] = -1
    last_num = prices[-1]
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > last_num:
            price_dict[prices[i]] = 1
            answer.append(1)

        elif prices[i] == last_num:
            price_dict[prices[i]] += 1
            answer.append(price_dict[prices[i]])
        
        else:
            curr_answer = 1
            num_idx_to_check = i + 1

            while True:
                if prices[num_idx_to_check] < prices[i]: # NOTE
                    break

                delta = price_dict[prices[num_idx_to_check]]
                num_idx_to_check += delta
                curr_answer += delta

                if (num_idx_to_check) >= (len(prices) - 1):
                    break 
            price_dict[prices[i]] = curr_answer
            answer.append(curr_answer)

        last_num = prices[i]
    answer.reverse()
    return answer


if __name__ == "__main__":
    assert str(solution([5, 8, 6, 2, 4, 1])) == str([3, 1, 1, 2, 1, 0])
    assert str(solution([3, 2, 1])) == str([1, 1, 0])
    assert str(solution([1, 2, 4, 2, 4])) == str([4, 3, 1, 1, 0])
    assert str(solution([1, 2, 2, 3, 3])) == str([4, 3, 2, 1, 0])
    assert str(solution([1, 2, 2, 3, 3, 2, 2])) == str([6,5,4,2,1,1,0])
    assert str(solution([3, 1, 3, 4, 4, 2, 2, 1])) == str([1,6,3,2,1,2,1,0])
    assert str(solution([10, 1])) == str([1, 0])
    assert str(solution([1, 10])) == str([1, 0])
    assert str(solution([1,1,1])) == str([2,1,0])
    assert str(solution([10, 100])) == str([1, 0])
    assert str(solution([1, 2, 3, 2, 3])) == str([4, 3, 1, 1, 0])