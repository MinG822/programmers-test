from collections import deque


def solution(n, m, x, y, r, c, k):

    queue = deque([])
    queue.append((x, y, "", 0))

    while queue:
        c_x, c_y, acc, n = queue.pop()
        print(c_x, c_y, acc, n)
        if n == k:
            if (c_x, c_y) == (r, c):
                return acc
        else:
            c_x > 1 and queue.append((c_x - 1, c_y, acc + "u", n + 1))
            c_y < m and queue.append((c_x, c_y + 1, acc + "r", n + 1))
            c_y > 1 and queue.append((c_x, c_y - 1, acc + "l", n + 1))
            c_x < n and queue.append((c_x + 1, c_y, acc + "d", n + 1))

            # c_x > 1 and queue.append((c_x - 1, c_y, acc + "u"))
            # c_y < m and queue.append((c_x, c_y + 1, acc + "r"))
            # c_y > 1 and queue.append((c_x, c_y - 1, acc + "l"))
            # c_x < n and queue.append((c_x + 1, c_y, acc + "d"))

    return "impossible"


def solution(n, m, x, y, r, c, k):

    queue = deque([])
    queue.append((x, y, ""))

    while queue:
        c_x, c_y, acc = queue.pop()
        print(c_x, c_y, acc)
        if len(acc) == k:
            if (c_x, c_y) == (r, c):
                return acc
        else:
            c_x > 1 and queue.append((c_x - 1, c_y, acc + "u"))
            c_y < m and queue.append((c_x, c_y + 1, acc + "r"))
            c_y > 1 and queue.append((c_x, c_y - 1, acc + "l"))
            c_x < n and queue.append((c_x + 1, c_y, acc + "d"))

    return "impossible"


if __name__ == "__main__":
    assert solution(3, 4, 2, 3, 3, 1, 5) == "dllrl"
    assert solution(2, 2, 1, 1, 2, 2, 2) == "dr"
    assert solution(3, 3, 1, 2, 3, 3, 4) == "impossible"
