def solution(sizes):
    """
    다양한 사이즈의 명함이 주어졌을 때,
    모든 명함을 담을 수 있는 가장 최소 사이즈의 크기를 찾는 함수
    타임아웃과 런타임 에러 발생 => for/while 문으로 접근하기

    param sizes: [가로, 세로] 의 리스트, 가로와 세로는 1 ~ 1000 이며, 리스트의 길이는 1~10000
    return answer: 사이즈
    """

    def get_max_w_h(i, w, h):
        if i == len(sizes):
            return w, h

        else:
            w_1, h_1 = get_max_w_h(i+1, sizes[i][0], sizes[i][1])
            w_1, h_1 = max(w_1, w), max(h, h_1)

            if sizes[i][0] == sizes[i][1]:
                return w_1, h_1

            w_2, h_2 = get_max_w_h(i+1, sizes[i][1], sizes[i][0])
            w_2, h_2 = max(w_2, w), max(h, h_2)
            
            if w_1 * h_1 < w_2 * h_2:
                return w_1, h_1
            return w_2, h_2
        

    max_w, max_h = get_max_w_h(0, 0, 0)

    return max_w * max_h


if __name__ == "__main__":
    assert(solution([[1,1]])) == 1
    assert(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) == 4000
    assert(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) == 120
    assert(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) == 133