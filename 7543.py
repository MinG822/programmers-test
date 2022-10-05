from collections import deque


def solution(maps):
    lands = []
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]

    need_to_check = lambda x, y: (visited[x][y] != 1) and (maps[x][y] != ".")

    for i in range(n):
        for j in range(m):

            if not need_to_check(i, j):
                continue

            queue = deque([(i, j)])
            curr_dict = {}

            while queue:
                ii, jj = queue.pop()

                if visited[ii][jj]:
                    continue

                visited[ii][jj] = 1

                if curr_dict.get(maps[ii][jj]) is None:
                    curr_dict[maps[ii][jj]] = 1
                else:
                    curr_dict[maps[ii][jj]] += 1

                if (ii + 1 < n) and need_to_check(ii + 1, jj):
                    queue.append((ii + 1, jj))
                if (jj + 1 < m) and need_to_check(ii, jj + 1):
                    queue.append((ii, jj + 1))
                if (ii - 1 > -1) and need_to_check(ii - 1, jj):
                    queue.append((ii - 1, jj))
                if (jj - 1 > -1) and need_to_check(ii, jj - 1):
                    queue.append((ii, jj - 1))

            lands.append(curr_dict)

    after_war = {}

    for land in lands:
        countries = sorted(
            [(c, c_count) for c, c_count in land.items()], key=lambda x: (x[1], x[0])
        )
        winner = countries[-1]
        if after_war.get(winner[0]) is None:
            after_war[winner[0]] = winner[1]
        else:
            after_war[winner[0]] += winner[1]

        for c, c_cnt in countries[:-1]:
            if c_cnt < winner[1]:
                after_war[winner[0]] += c_cnt
            else:
                if after_war.get(c) is None:
                    after_war[c] = c_cnt
                else:
                    after_war[c] += c_cnt

    sorted_c = sorted(
        [(c, c_cnt) for c, c_cnt in after_war.items()], key=lambda x: x[1]
    )
    if not len(sorted_c):
        return 0

    return sorted_c[-1][1]


if __name__ == "__main__":
    assert (
        solution(
            [
                "AABCA.QA",
                "AABC..QX",
                "BBBC.Y..",
                ".A...T.A",
                "....EE..",
                ".M.XXEXQ",
                "KL.TBBBQ",
            ]
        )
        == 15
    )
    assert solution(["XY..", "YX..", "..YX", ".AXY"]) == 5
