def solution(n, computers):
    """
    임의로 연결된 n 개의 computers들이 있고,
    연결된 모든 컴퓨터들을 하나의 네트워크로 여길 때,
    몇 개의 네트워크가 존재하는 지 찾는 함수

    param n : 컴퓨터 개수
    param computers : n * n 크기의 2차원 리스트
    return answer : 네트워크의 개수
    """
    from collections import deque

    network_count = 0
    for i in range(n):
        if not computers[i][i]:
            continue

        network_count += 1
        queue = deque([i])

        while queue:
            computer_no = queue.popleft()
            computers[computer_no][computer_no] = 0

            for j in range(n):
                if computers[computer_no][j]:
                    computers[computer_no][j] = 0
                    computers[j][computer_no] = 0
                    queue.append(j)

    return network_count


if __name__ == "__main__":
    assert (solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) == 2
    assert (solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) == 1
    assert (solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])) == 3
    assert (solution(1, [[1]])) == 1
    assert (solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])) == 1
    assert (solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) == 1
    assert (solution(4, [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1]])) == 1
