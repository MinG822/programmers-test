def merge_sort(targets):
    """
    합병 정렬 함수
    NOTE 비교 시, 각각을 비교하는 게 아니라, 이어붙였을 때를 비교함

    param targets: 스트링 변환된 음수가 아닌 정수들의 리스트, 길이 0 ~ 50000
    return sorted_targets: 주어진 수중 이어붙였을 때 가장 큰 수가 나오는 리스트
    """
    if len(targets) < 2:
        return targets

    left = merge_sort(targets[: len(targets) // 2])
    right = merge_sort(targets[len(targets) // 2 :])

    sorted_targets = []
    li, ri = 0, 0

    for _ in range(len(targets)):
        if ri == len(right):
            sorted_targets.extend(left[li:])
            break

        elif li == len(left):
            sorted_targets.extend(right[ri:])
            break

        if left[li] + right[ri] < right[ri] + left[li]:
            sorted_targets.append(right[ri])
            ri += 1

        else:
            sorted_targets.append(left[li])
            li += 1

    return sorted_targets


def solution(numbers):
    """
    0 또는 양의 정수들이 주어졌을 때, 정수들을 이어 붙여 만들 수 있는 가장 큰 수를 알아내는 함수

    NOTE 귀여운 버블 정렬로는 풀 수 없다

    param numbers: 음수가 아닌 정수들의 리스트, 길이 1 이상 100000 이하
    return answer: 스트링으로 변환된 이어붙어진 가장 큰 수
    """

    numbers = [str(n) for n in numbers]
    numbers = merge_sort(numbers) if len(numbers) > 1 else numbers

    if numbers[0] == "0":
        return "0"
    return "".join(numbers)


if __name__ == "__main__":
    assert solution([1]) == "1"
    assert solution([6, 10, 2]) == "6210"
    assert solution([3, 30, 34, 5, 9]) == "9534330"
    assert solution([0, 0]) == "0"
    assert solution([10000, 0]) == "100000"
    assert solution([10000, 1]) == "110000"
