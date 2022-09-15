from collections import deque


def solution(number, k):
    """
    https://school.programmers.co.kr/questions/32364 참고
    다음 위치 부터 마지막까지 비교할 필요없이,
    바로 직전에 넣은 값과 비교하면 된다
    마지막까지 비교해서, 다음 최대로 바로 이동하는 로직은,
    최악의 경우, 그러니까 단조증가하는 경우 효율이 별로다
    """
    answer = deque([])
    ni = 0
    number = [int(n) for n in number]

    if k == len(number) - 1:
        return str(max(number))

    while ni < len(number):
        if k == 0:  # 더 이상 숫자를 빼지 않아도 될 때
            answer.extend(number[ni:])
            break

        if not len(answer) or k == 0:
            answer.append(number[ni])
            ni += 1
            continue

        while len(answer) and answer[-1] < number[ni] and k > 0:
            answer.pop()
            k -= 1

        answer.append(number[ni])

        ni += 1

    answer_str = ""
    answer_under = len(answer) - k
    for ai, answer_num in enumerate(answer):
        if ai < answer_under:
            answer_str += str(answer_num)

    return answer_str


if __name__ == "__main__":
    assert (solution("1234", 2)) == "34"
    assert (solution("1234", 2)) == "34"
    assert (solution("1924", 2)) == "94"
    assert (solution("1231234", 3)) == "3234"
    assert (solution("4177252841", 4)) == "775841"
    assert (solution("1111", 2)) == "11"
