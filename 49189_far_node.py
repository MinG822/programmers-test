def solution(n, edge):
    """
    1~n 까지 적힌 n개의 노드가 있는 그래프에서,
    1번 노드에서 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드들의 개수를 구하는 함수

    param n : 노드의 개수,2이상 2만 이하
    param edge : [[node_1, node_2], [node_4, node_2], ...] 란 형식의 간선 2차원 리스트, 1개 이상 5만 이하
    return answer : 1번 노드로부터 가장 멀리 떨어진 노드들의 개수
    """

    visited = {n: False for n in range(1, n + 1)}
    node_edge = {n: dict() for n in range(1, n + 1)}

    for node_1, node_2 in edge:
        node_edge[node_1][node_2] = True
        node_edge[node_2][node_1] = True

    visited[1] = True
    queue = [[1]]

    while queue:
        answer = len(queue[0])
        node_to_check = queue.pop()
        queue.append([])

        for node in node_to_check:
            for neighbor in node_edge[node].keys():
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                queue[-1].append(neighbor)

        if not len(queue[-1]):
            queue.pop()

    return answer


if __name__ == "__main__":
    assert (solution(2, [[1, 2]])) == 1
    assert (solution(3, [[1, 2], [1, 3]])) == 2
    assert (solution(3, [[1, 2], [2, 3]])) == 1
    assert (solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) == 3
