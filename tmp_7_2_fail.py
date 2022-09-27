import itertools


def solution(n, m, x, y, r, c, k):
    for p in itertools.product(["d", "l", "r", "u"], repeat=k):
        cx, cy = x, y
        for pp in p:
            if pp == "d":
                if cx < n:
                    cx += 1
                else:
                    break
            elif pp == "u":
                if cx > 1:
                    cx -= 1
                else:
                    break
            elif pp == "l":
                if cy > 1:
                    cy -= 1
                else:
                    break
            else:
                if cy < m:
                    cy += 1
                else:
                    break
        else:
            if (cx, cy) == (r, c):
                return "".join(p)

    return "impossible"


if __name__ == "__main__":
    assert solution(3, 4, 2, 3, 3, 1, 5) == "dllrl"
    assert solution(2, 2, 1, 1, 2, 2, 2) == "dr"
    assert solution(3, 3, 1, 2, 3, 3, 4) == "impossible"
