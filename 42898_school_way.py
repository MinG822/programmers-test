def solution(m, n, puddles):
    """
    1, 1, 에 위치한 학생이, m, n 에 위치한 학교에 등교할 때,
    장애물인 puddles 를 피해 갈 수 있는 최단 거리

    param m, n : 학교 위치 (m 은 열, n 은 행 정보, 2이상 100 이하)
    param puddles : 웅덩이 위치 (열, 행)
    return answer: 최단 거리를 1,000,000,007 로 나눈 나머지
    """
    P = 9
    way_school = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

    for pi, pj in puddles:
        way_school[pj][pi] = P

    get_value_or_P = (
        lambda r, c: way_school[r][c] if ((r < n + 1) and (c < m + 1)) else P
    )
    print_way_school = lambda: print(
        "---------\n", [print(_) for _ in way_school], "\n----------"
    )
    for j in range(m - 1, -1, -1):
        curr_j = j
        print_way_school()
        for i in range(n, 0, -1):
            print(i, curr_j)
            if way_school[i][curr_j] == P:
                continue
            down = get_value_or_P(i + 1, curr_j)
            right = get_value_or_P(i, curr_j + 1)
            way_school[i][curr_j] = min(min(right, down) + 1, P)

            curr_j += 1
            if curr_j > m:
                break

    answer = min(way_school[1][2], way_school[2][1]) + 1
    return answer


if __name__ == "__main__":
    assert solution(4, 3, [[2, 2]]) == 4
