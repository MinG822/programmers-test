def solution(queue_1, queue_2):
    """
    길이가 같은 두 개의 큐에서,
    pop & insert 를 통해 각 큐의 원소 합이
    동일하게 만드는 최소 횟수를 찾는 함수
    동일하게 만들 수 없다면 -1 반환.

    NOTE pop 은 큐의 앞에서, insert 는 큐의 뒤로, pop & insert 를 한 번으로
    NOTE 효율성을 통과하지 못한 이유는 전탐을 했기 때문. 작을 경우나, 높을 경우를 체크해서 늘려나가는 방식도 있었다

    param queue_1, queue2 : 1 ~ 10^9를 원소로 가지는 길이 1 이상 300000의 리스트
    return answer: 동일하게 만드는 최소 합
    """
    total_sum = sum(queue_1) + sum(queue_2)
    if total_sum % 2:
        return -1

    to_be = total_sum / 2
    n = len(queue_1)

    answers = []
    total = queue_1 + queue_2

    for p_1 in range(2 * n - 1):
        curr_sum = total[p_1]

        for p_2 in range(p_1 + 1, n):
            if curr_sum == to_be:
                answers.append(p_1 + p_2 + n)
            curr_sum += total[p_2]
        start = p_1 + 1 if p_1 > n else n
        for p_2 in range(start, 2 * n):
            if curr_sum == to_be:
                answers.append(p_1 + p_2 - n)
            curr_sum += total[p_2]

    if not len(answers):
        return -1
    return min(answers)


if __name__ == "__main__":
    assert solution([3, 2, 7, 2], [4, 6, 5, 1]) == 2
    assert solution([1, 2, 1, 2], [1, 10, 1, 2]) == 7
    assert solution([1, 1], [1, 5]) == -1
    assert solution([1], [3]) == -1
    assert solution([1], [1]) == 0
    assert solution([1000000000, 1000000000], [1, 1]) == 2
