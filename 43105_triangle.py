def solution(triangle):
    """
    정수로 이루어진 삼각형이 주어질 때,
    삼각형의 꼭대기부터 바닥까지 이어지는 경로 중
    거쳐간 숫자의 가장 큰 합을 찾는 함수

    param triangle: 삼각형의 맨 위 왼쪽 부터의 숫자가 나열된 2차원 숫자 리스트, 길이 1 이상 500 이하
    return answer: 경로의 가장 큰 합
    """
    for i in range(1, len(triangle)):

        triangle[i][0] += triangle[i - 1][0]

        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

        triangle[i][-1] += triangle[i - 1][-1]

    return max(triangle[-1])


if __name__ == "__main__":
    assert solution([[1]]) == 1
    assert solution([[10], [10, 10]]) == 20
    assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
