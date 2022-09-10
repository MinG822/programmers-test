from collections import deque


def solution(rectangle, character_x, character_y, item_x, item_y):
    """
    좌표 character_x, character_y 에 위치한 캐릭터가, 좌표 item_, item_y 에 위치한 아이템을 갖기 위해 이동할 때,
    주어진 rectangle 들의 선분을 따라 가장 최소로 움직인 횟수를 구하는 함수
    단 좌표는 1 ~ 50

    NOTE 사각형들의 모서리가 겹치는 부분들을 해결하기 위해 2배율처리

    param rectange: 직사각형의 두 꼭지점 정보 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 로 이루어진 2차원 리스트
        1 <= 우측 상단 x - 좌측 하단 x <= 4
        rectangle 의 길이는 1 ~ 4
    param character_x: 캐릭터의 초기 x 좌표
    param character_y: 캐릭터의 초기 y 좌표
    param item_x : 아이템의 초기 x 좌표
    param item_y : 아이템의 초기 y 좌표
    return answer:  캐릭터의 최소 이동 횟수
    """
    N = 101
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for m_x, m_y, M_x, M_y in rectangle:
        for y in range(2 * m_y, 2 * M_y + 1):
            for x in range(2 * m_x, 2 * M_x + 1):
                maps[y][x] = 1

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if (
                maps[i][j]
                and maps[i + 1][j]
                and maps[i - 1][j]
                and maps[i][j + 1]
                and maps[i][j - 1]
            ):
                maps[i][j] = 2
                if (
                    (maps[i + 1][j + 1] == 0)
                    or (maps[i - 1][j + 1] == 0)
                    or (maps[i + 1][j - 1] == 0)
                    or (maps[i - 1][j - 1] == 0)
                ):
                    maps[i][j] = 1

    move_count = 0
    maps[character_y * 2][character_x * 2] = 0
    queue = deque([(character_x * 2, character_y * 2, move_count)])

    get_right = lambda x, y: (maps[y][x + 1], x + 1, y)
    get_bottom = lambda x, y: (maps[y + 1][x], x, y + 1)
    get_left = lambda x, y: (maps[y][x - 1], x - 1, y)
    get_top = lambda x, y: (maps[y - 1][x], x, y - 1)

    while queue:
        x, y, move_count = queue.popleft()
        if (x, y) == (item_x * 2, item_y * 2):
            return move_count / 2

        neighbors = [get_right(x, y), get_bottom(x, y), get_left(x, y), get_top(x, y)]
        for neighbor in neighbors:
            if neighbor[0] == 1:
                maps[neighbor[2]][neighbor[1]] = 0
                queue.append([neighbor[1], neighbor[2], move_count + 1])

    return move_count


if __name__ == "__main__":
    assert (solution([[1, 1, 50, 50]], 1, 1, 50, 50)) == 98
    assert (
        solution(
            [[2, 1, 3, 9], [1, 6, 10, 8], [7, 2, 9, 10], [4, 3, 11, 4]], 2, 8, 7, 3
        )
    ) == 28
    assert (solution([[1, 1, 3, 7], [2, 2, 7, 4], [4, 3, 6, 6]], 1, 2, 6, 6)) == 13
    assert (
        solution([[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4)
    ) == 8
    assert (solution([[1, 1, 5, 7]], 1, 1, 4, 7)) == 9
    assert (solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10)) == 15
    assert (solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)) == 10
    assert (
        solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
    ) == 17
