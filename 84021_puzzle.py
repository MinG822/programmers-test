from collections import deque


def get_new_visited(N):
    """
    행과 열의 길이가 N 이며, 초기값 0 으로 채워진 2차원 리스트를 반환하는 함수
    param N: 행과 열의 크기
    return visited: 0으로 초기화된 2차원 리스트
    """
    return [[0 for _ in range(N)] for __ in range(N)]


def get_neighbors(target, visited, i, j, check_value, N):
    neighbors = []
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    is_in_target = lambda x: (x > -1 and x < N)

    for di, dj in directions:
        mi, mj = i + di, j + dj
        if not is_in_target(mi):
            continue
        if not is_in_target(mj):
            continue
        if visited[mi][mj]:
            continue
        if target[mi][mj] != check_value:
            continue
        visited[mi][mj] = 1
        neighbors.append([mi, mj])
    return neighbors


def get_curr_min_max_size(i, j, visited, target, target_value, N):
    """
    2차원 리스트 target 에서 i, j 에 위치했을 때,
    target_value 에 해당하는 구역의 최솟값과 최댓값을 구하는 함수

    param i, j: 주어진 현재 위치
    param visited: 이제까지 찾은 위치를 1 로 표시한 target 과 같은 크기의 2차원 리스트
    param target: 찾으려는 대상, 2차원 리스트
    param target_value: 찾으려는 값
    param N: target 의 길이
    return min_i, min_j, max_i, max_j : 찾은 범위의 최솟 값과 최댓값
    """
    queue = deque([(i, j)])
    min_i, min_j, max_i, max_j = i, j, i, j
    visited[i][j] = 1

    while queue:
        curr_i, curr_j = queue.pop()
        min_i, min_j, max_i, max_j = (
            min(min_i, curr_i),
            min(min_j, curr_j),
            max(max_i, curr_i),
            max(max_j, curr_j),
        )
        neighbors = get_neighbors(target, visited, curr_i, curr_j, target_value, N)
        for neighbor in neighbors:
            queue.append((neighbor[0], neighbor[1]))
    return min_i, min_j, max_i, max_j


def rotate_90(target):
    """
    2차원 리스트 target 을 오른 쪽으로 90도 돌리는 함수
    param target: 2차원 리스트
    return answer: 오른쪽으로 90도 돌려진 2차원 리스트
    """
    return [
        [target[i][j] for i in range(len(target) - 1, -1, -1)]
        for j in range(len(target[0]))
    ]


def solution(gameboard, table):
    """
    퍼즐 조각들을 넣을 수 있게 구멍이 뚫린 gameboard 와,
    퍼즐 조각들이 놓여진 table 이 주어질 때,
    최대 몇 개의 퍼즐 조각들을 gameboard 에 넣을 수 있을지 찾는 함수
    단, 퍼즐 조각은 뒤집을 수 없고, 게임 보드의 구멍 크기와 퍼즐 조각이 딱 맞아야한다.
    퍼즐 조각은 1*1 사이즈의 정사각형이 1 ~ 6개가 연결된 형태이며, gameboard 위의 퍼즐 조각들은 서로 인접해 있지 않다.

    param gameboard: 3 * 3 ~ 50 * 50 사이즈의 정사각형 2차원 리스트, 하나 이상의 빈칸이 있음
    param table: gameboard 와 사이즈가 동일, 하나 이상의 퍼즐 조각이 있음
    return answer: 최대로 맞출 수 있는 퍼즐 조각 개수
    """
    N = len(gameboard)
    answer = 0

    visited = get_new_visited(N)
    empties = []

    for i in range(N):
        for j in range(N):
            if gameboard[i][j]:
                continue
            if visited[i][j]:
                continue

            min_i, min_j, max_i, max_j = get_curr_min_max_size(
                i, j, visited, gameboard, 0, N
            )

            empties.append(
                [
                    [gameboard[pi][pj] for pj in range(min_j, max_j + 1)]
                    for pi in range(min_i, max_i + 1)
                ]
            )

    visited = get_new_visited(N)
    for i in range(N):
        for j in range(N):
            if not table[i][j]:
                continue
            if visited[i][j]:
                continue

            min_i, min_j, max_i, max_j = get_curr_min_max_size(
                i, j, visited, table, 1, N
            )

            puzzles = [
                [
                    [table[pi][pj] for pj in range(min_j, max_j + 1)]
                    for pi in range(min_i, max_i + 1)
                ]
            ]

            # 0, 180
            for _ in range(3):
                puzzles.append(rotate_90(puzzles[-1]))

            find_puzzle = False

            while puzzles and not find_puzzle:
                puzzle = puzzles.pop()
                ph, pw = len(puzzle), len(puzzle[0])

                for ei, empty in enumerate(empties):
                    eh, ew = len(empty), len(empty[0])
                    if (eh, ew) != (ph, pw):
                        continue

                    result = [
                        [c + d != 1 for c, d in zip(a, b)]
                        for a, b, in zip(empty, puzzle)
                    ]
                    find_puzzle = sum(sum(result, [])) == 0

                    if find_puzzle:
                        answer += sum(sum(puzzle, []))
                        empties.pop(ei)
                        break

    return answer


if __name__ == "__main__":
    assert (
        solution([[1, 0, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 1, 1], [1, 0, 1]])
    ) == 6
    assert (
        solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    ) == 9
    assert (
        solution([[0, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        == 1
    )
    assert (
        solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]])
        == 0
    )
    assert (
        solution(
            [
                [1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0],
            ],
            [
                [1, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
            ],
        )
    ) == 14
