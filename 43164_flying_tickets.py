from collections import deque


def solution(tickets):
    """
    주어진 항공편을 모두 사용할 때 방문하는 공항 경로를 찾는 함수
    단, 여러 경로를 찾을 수 있다면 알파벳 순서가 앞서는 경로를 반환하며, 출발지는 항상 ICN

    NOTE 중복 티켓 존재

    param tickets: [출발지, 도착지] 로 이루어진 길이 3 ~ 10000 리스트
    return answer: 방문하는 공항 경로, [출발지, 공항1, 공항2, 도착지]
    """

    ticket_dict = {}

    for departure, arrival in tickets:
        ticket_dict[departure] = ticket_dict.get(departure, []) + [arrival]

    for departure in ticket_dict.keys():
        ticket_dict[departure].sort()

    queue = deque([(["ICN"], {})])

    while queue:
        tours, used_tickets = queue.pop()

        if len(tours) == (len(tickets) + 1):
            return tours

        for i, candi_arriaval in enumerate(ticket_dict.get(tours[-1], [])[::-1]):
            if used_tickets.get((tours[-1], candi_arriaval, i)):
                continue

            queue.append(
                (
                    tours + [candi_arriaval],
                    {**used_tickets, (tours[-1], candi_arriaval, i): True},
                )
            )

    raise Exception("Bad Condition")


if __name__ == "__main__":
    assert (
        str(
            solution(
                [
                    ["ICN", "AAA"],
                    ["ICN", "AAA"],
                    ["ICN", "AAA"],
                    ["AAA", "ICN"],
                    ["AAA", "ICN"],
                ]
            )
        )
    ) == str(["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
    assert (str(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))) == str(
        ["ICN", "JFK", "HND", "IAD"]
    )
    assert (
        str(
            solution(
                [
                    ["ICN", "SFO"],
                    ["ICN", "ATL"],
                    ["SFO", "ATL"],
                    ["ATL", "ICN"],
                    ["ATL", "SFO"],
                ]
            )
        )
    ) == str(["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
    assert (
        str(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
    ) == str(["ICN", "A", "D", "B", "A", "C"])
    assert (
        str(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["B", "A"], ["C", "A"]]))
    ) == str(["ICN", "A", "B", "A", "C", "A"])
