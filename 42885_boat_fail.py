from collections import deque


def solution(people, limit):
    """
    사람들의 몸무게와 보트의 제한이 있을 때,
    가장 적게 보트를 사용해 모든 사람들을 태울 수 있는 방법을 찾는 함수

    param people: 사람들의 몸무게, 길이 1 ~ 50000 이하. 몸무게는 각 40 ~ 240 이하
    param limit: 보트의 무게 제한. 40 ~ 240 이하. max(people) 이하
    return boat_count: 최소로 필요한 보트의 개수
    """
    people = deque(sorted(people))
    half_limit = limit / 2
    boats = deque()
    count = 0

    # print(people)
    while people:
        # print(boats, count)
        target = people.pop()
        if target > half_limit:
            if limit - 40 < target:
                count += 1
                continue
            boats.append(target)
        else:
            people.append(target)
            break

    while people:
        # print(people, count, boats)
        target = people.popleft()

        if not len(boats):
            boats.append(target)
            continue

        find_place = False
        while boats:
            count += 1
            boat = boats.pop()
            if target + boat <= limit:
                find_place = True
                break

        if not find_place:
            boats.append(target)

    return len(boats) + count


if __name__ == "__main__":
    # assert (solution([70, 50, 80, 50], 100)) == 3
    # assert (solution([70, 80, 50], 100)) == 3
    # assert (solution([30, 30, 30], 100)) == 2
    # assert (solution([30, 30, 30], 40)) == 3
    # assert (solution([30], 30)) == 1
    assert (solution([40, 100, 100, 160], 200)) == 2
    assert (solution([40, 190], 200)) == 2
