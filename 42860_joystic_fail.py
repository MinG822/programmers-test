def solution(name):
    """
    조이스틱으로 주어진 알파벳 이름을 완성할 때, 필요한 최소 횟수를 찾는 함수
    처음 세팅은 A * len(name) 이며, 조이스틱을 위 아래로 움직여 알파벳 순서를 바꿀 수 있고,
    오른쪽 왼쪽으로 움직여 알파벳 위치를 바꿀 수 있음

    param name: 알파벳으로 이루어진 이름, 1이상 20 이하
    return minimun_count: 최소 횟수
    """
    alphabet_order = {chr(n): min(n - 65, 91 - n) for n in range(65, 91)}
    # print(alphabet_order)

    count = 0
    visited = [True if name[i] == "A" else False for i in range(len(name))]
    start_point = 0
    # print(visited)
    while True:
        count += alphabet_order[name[start_point]]
        visited[start_point] = True
        # print(count, name[start_point])
        if sum(visited) == len(name):
            break

        for i in range(1, len(name)):
            if not visited[start_point + i]:
                count += i
                start_point = start_point + i
                break
            if not visited[start_point - i]:
                count += i
                start_point -= i
                break
        # print(count, start_point)

    return count


if __name__ == "__main__":
    assert solution("JEROEN") == 56
    assert solution("JAN") == 23
    assert solution("AAJAN") == 1 + 13 + 2 + 9
    assert solution("AAB") == 2
    assert solution("AAABBBABA") == 10
    assert solution("AAAAABBAAAAAAABAAA") == 16
    assert solution("ABABAAAAABA") == 9
