def solution(n, results):
    """
    주어진 경기 결과에서, 순위를 확정할 수 있는 선수의 수를 찾는 함수

    1. 모든 선수는 1대 1로 경기를 진행했음
    2. 일부 경기 결과가 없어짐
    3. 확실하게 자신의 순위를 매길 수 있는 선수를 골라내기

    param n: 경기에 참여한 선수, 1 ~ 100명
    param results: [[이긴선수, 진선수], ...] 의 형태로 순위 정보가 저장된 경기 결과 2차원 리스트, 1 ~ 4500 개 이하
    """
    result_map = {player: {"win": set(), "lose": set()} for player in range(1, n + 1)}

    for winner, loser in results:
        result_map[winner]["win"].add(loser)
        result_map[loser]["lose"].add(winner)

    for target_player in range(1, n + 1):
        for state in ["win", "lose"]:

            queue = [*result_map[target_player][state]]

            while queue:
                player_to_compare = queue.pop()
                losers_to_update = (
                    result_map[player_to_compare][state]
                    - result_map[target_player][state]
                )
                if len(losers_to_update):
                    result_map[target_player][state].update(losers_to_update)
                    queue.extend([*losers_to_update])

    ranked_player_count = len(
        [
            *filter(
                lambda x: (len(result_map[x]["win"]) + len(result_map[x]["lose"]))
                == (n - 1),
                result_map.keys(),
            )
        ]
    )
    return ranked_player_count


if __name__ == "__main__":
    assert (solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) == 2
