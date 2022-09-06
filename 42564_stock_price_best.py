def solution(prices):
    """
    다른 사람의 풀이 중 가장 깔끔하고 문제에 의도에 맞는 풀이
    나와 풀이하는 사고 방식이 달랐다 
    """
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer


if __name__ == "__main__":
    assert str(solution([1, 2, 4, 2, 4])) == str([4, 3, 1, 1, 0])
    assert str(solution([5, 8, 6, 2, 4, 1])) == str([3, 1, 1, 2, 1, 0])
    assert str(solution([3, 2, 1])) == str([1, 1, 0])
    assert str(solution([1, 2, 2, 3, 3])) == str([4, 3, 2, 1, 0])
    assert str(solution([1, 2, 2, 3, 3, 2, 2])) == str([6,5,4,2,1,1,0])
    assert str(solution([3, 1, 3, 4, 4, 2, 2, 1])) == str([1,6,3,2,1,2,1,0])
    assert str(solution([10, 1])) == str([1, 0])
    assert str(solution([1, 10])) == str([1, 0])
    assert str(solution([1,1,1])) == str([2,1,0])
    assert str(solution([10, 100])) == str([1, 0])
    assert str(solution([1, 2, 3, 2, 3])) == str([4, 3, 1, 1, 0])