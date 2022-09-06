def solution(priorities, location):
    """
    중요한 문서가 먼저 인쇄되는 프린터에서, 
    주어진 location의 문서가 몇 번째로 인쇄되는 지 찾는 함수
    
    param priorities: 문서 중요도(1~9) 리스트, 길이 100 이하
    param location: 확인해야하는 문서의 위치, 0부터 시작
    return answer: location 문서의 프린트 순서
    """
    answer = 0
    while True:
        curr_doc = priorities.pop(0)
        if len(priorities) == 0:
            return answer + 1

        if max(priorities) > curr_doc:
            priorities.append(curr_doc)
        else:
            answer += 1
            if location == 0:
                return answer
        
        location = len(priorities) - 1 if location < 1 else location - 1



    
if __name__ == "__main__":
    assert solution([3, 1, 3, 1, 3], 1) == 4
    assert solution([5, 4, 3, 2, 1], 3) == 4
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
    assert solution([1, 2, 3, 4, 5], 3) == 2
    assert solution([1], 0) == 1
    assert solution([1, 1, 1, 1, 1], 3) == 4
    assert solution([2,1,3,2], 2) == 1
