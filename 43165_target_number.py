def solution(numbers, target):
    """
    일련의 숫자들이 주어질 때, 
    이들을 더하거나 빼서 어떤 숫자가 되도록하는 가짓 수를 구하는 함수

    재귀로 풀게되면 스택이 2의 20 만큼 쌓이기 때문에 큐로 풀이 

    param numbers: 숫자(1 ~ 50) 리스트, 길이 2 ~ 20
    param target: 1 ~ 1000 의 숫자

    return answer: 가짓 수
    """
    from collections import deque
    
    queue = deque([(0, numbers[0]), (0, -numbers[0])])
    answer = 0

    while queue:
        i, acc = queue.pop()

        if (i == (len(numbers) - 1)) and (acc == target):
            answer += 1
            continue

        if i < (len(numbers) - 1):
            queue.append((i+1, acc + numbers[i+1]))
            queue.append((i+1, acc - numbers[i+1]))

    return answer

if __name__ == "__main__":
    assert(solution([1, 1, 1, 1, 1], 3)) == 5
    assert(solution([4, 1, 2, 1], 4)) == 2
    assert(solution([1, 1], 1)) == 0