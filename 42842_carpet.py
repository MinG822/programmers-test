def solution(brown, yellow):
    """
    카펫 바깥 격자의 수(brown)와 안쪽 격자의 수(yellow)가 주어질 때,
    카펫의 가로, 세로 크기를 찾는 함수
    단, 가로의 길이가 세로의 길이보다 크거나 같음

    param brown : 카펫 바깥 격자의 수, 8 ~ 5000
    param yellow : 카펫 안쪽 격자의 수, 1 ~ 2000000
    return answer : (가로, 세로)
    """
    for i in range(yellow, int(yellow**0.5)-1, -1): # NOTE
        if yellow % i != 0:
            continue

        w, h = i, int(yellow/i)
        b_w, b_h = w+2, h+2
        if 2 * (b_w + b_h) - 4  == brown:
            return [b_w, b_h]

    raise Exception("BAD REQUEST")


if __name__ == "__main__":
    assert str(solution(10,2)) == str([4,3])
    assert str(solution(8,1)) == str([3,3])
    assert str(solution(24,24)) == str([8,6])