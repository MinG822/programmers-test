def solution(name):
    """
    조이스틱으로 주어진 알파벳 이름을 완성할 때, 필요한 최소 횟수를 찾는 함수
    처음 세팅은 A * len(name) 이며, 조이스틱을 위 아래로 움직여 알파벳 순서를 바꿀 수 있고,
    오른쪽 왼쪽으로 움직여 알파벳 위치를 바꿀 수 있음

    NOTE 모든 케이스를 커버하지 못함. 재귀로 모든 경우를 탐색한 후 비교하는 게 낫다. 탐욕법이 아닌듯.

    param name: 알파벳으로 이루어진 이름, 1이상 20 이하
    return minimun_count: 최소 횟수
    """
    alphabet_order = {chr(n): min(n - 65, 91 - n) for n in range(65, 91)}
    # print(alphabet_order)

    count = 0
    visited = [True if name[i] == "A" else False for i in range(len(name))]
    start_point = 0
    half = len(name) // 2 + 1 if len(name) % 2 else len(name) // 2
    # print(visited)
    while True:
        count += alphabet_order[name[start_point]]
        print(start_point, "도착함", count, name[start_point])
        visited[start_point] = True
        # print(count, name[start_point])
        if sum(visited) == len(name):
            print("끝", count)
            break

        right_end, left_end = 0, 0
        right_start, left_start = half, half

        for i in range(1, half + 1):
            if not visited[(start_point + i) % len(name)]:
                right_end = max(right_end, i)
                right_start = min(i, right_start)
            if not visited[(start_point - i) % len(name)]:
                left_end = max(left_end, i)
                left_start = min(left_start, i)
        print(right_end, left_end, start_point)
        if right_end == 0:
            count += left_start
            start_point = (start_point - left_start) % len(name)
            print("왼쪽으로감", count, start_point)
            continue

        elif left_end == 0:
            count += right_start
            start_point = (start_point + right_start) % len(name)
            print("오른쪽으로감", count, start_point)
            continue
        print(right_start, left_start)
        right_start = (
            right_end
            if visited[(start_point + right_start) % len(name)]
            else right_start
        )
        left_start = (
            left_end if visited[(start_point - left_start) % len(name)] else left_start
        )

        right_cost = 2 * (right_end) + (left_end)
        left_cost = 2 * (left_end) + (right_end)
        print(right_start, right_end, left_start, left_end, right_cost, left_cost)
        if right_cost > left_cost:
            count += left_start
            start_point = (start_point - left_start) % len(name)
            print("비교 후 왼쪽으로감", count, start_point)
        else:
            count += right_start
            start_point = (start_point + right_start) % len(name)
            print("비교 후 오른쪽으로감", count, start_point)

    return count


if __name__ == "__main__":
    # assert solution("JEROEN") == 56
    # assert solution("JAN") == 23
    assert solution("AAJAN") == 1 + 13 + 2 + 9
    # assert solution("AAB") == 2
    # assert solution("BBA") == 3
    # assert solution("AAABBBABA") == 10
    # assert solution("AAAAABBAAAAAAABAAA") == 16
    # assert solution("ABABAAAAABA") == 10
