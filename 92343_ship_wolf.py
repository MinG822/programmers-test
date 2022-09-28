def solution(info, edges):
    graph = {}
    for parent, child in edges:
        if graph.get(parent) is not None:
            graph[parent]["right"] = child
        else:
            graph[parent] = {"left": child}

    curr_node = 0
    parents = []
    visited = [0] * len(info)
    animals = []
    # TODO 순회 + 재귀 (완탐)
    while True:

        if graph.get(curr_node) is None:
            visited[curr_node] = True
            if len(parents):
                curr_node = parents.pop()
                continue
            else:
                break

        if (
            graph[curr_node].get("left") is not None
            and not visited[graph[curr_node]["left"]]
        ):
            parents.append(curr_node)
            curr_node = graph[curr_node]["left"]
            visited[curr_node] = True

        elif (
            graph[curr_node].get("right") is not None
            and not visited[graph[curr_node]["right"]]
        ):
            parents.append(curr_node)
            curr_node = graph[curr_node]["right"]
            visited[curr_node] = True

        elif len(parents):
            curr_node = parents.pop()
        else:
            break

    return


if __name__ == "__main__":
    assert (
        solution(
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [
                [0, 1],
                [1, 2],
                [1, 4],
                [0, 8],
                [8, 7],
                [9, 10],
                [9, 11],
                [4, 3],
                [6, 5],
                [4, 6],
                [8, 9],
            ],
        )
        == 5
    )
    assert (
        solution(
            [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [
                [0, 1],
                [0, 2],
                [1, 3],
                [1, 4],
                [2, 5],
                [2, 6],
                [3, 7],
                [4, 8],
                [6, 9],
                [9, 10],
            ],
        )
        == 5
    )
