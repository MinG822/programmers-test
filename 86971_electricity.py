def solution(n, wires):
    """
    하나로 연결된 n개의 전선들에 대해,
    어떤 연결을 끊어 끊긴 각 부분의 연결 수 차이가 가장 작을 때,
    그때의 차이를 찾는 함수

    TODO 다음엔 Union-Find 로 구현해보기
    param n: 주어진 전선의 개수, 2 ~ 100
    param wires: 주어진 전선의 연결 정보, [[전선1, 전선2]]
        이때, 각 전선의 번호는 1 ~ n 로 표현
    return answer: 연결을 끊을 때 가장 최소의 연결 차   
    """
    from collections import deque

    min_diff = n - 2
    for i in range(len(wires)):
        visited = [0 for _ in range(n+1)]
        wire_dict = {node:[] for node in range(1, n+1)}

        for j in range(len(wires)):
            if i == j : continue
            v1, v2 = wires[j]
            wire_dict[v1].append(v2)
            wire_dict[v2].append(v1)

        queue = deque(wires[(i+1)%len(wires)])

        while queue:
            node = queue.pop()
            if visited[node]: continue

            visited[node] = 1
            for another_node in wire_dict[node]:
                if visited[another_node]: continue
                queue.append(another_node)
        
        min_diff = min(abs(n - 2 * sum(visited)), min_diff)

    return min_diff

if __name__ == "__main__":
    assert(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) == 3
    assert(solution(4, [[1,2],[2,3],[3,4]])) == 0
    assert(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) == 1
    assert(solution(2, [[1, 2], [2, 1]])) == 0