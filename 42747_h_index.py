from collections import deque


def solution(citations):
    """
    인용 정보로 나타난 n편의 citations 가 주어질 때,
    어떤 수 h 번 이상 인용된 논문이 h 번 이상이고, 나머지 논문이 h 번 이하 인용되었을 때,
    h의 최댓값을 구하는 함수
    param citations: 논문 인용 수, 길이 1 ~ 1000 이하, 인용 수는 0회 이상 10000 이하
    return answer: h index
    """
    citation_count = [0 for _ in range(10001)]  # NOTE 10000 이하

    for c in citations:
        citation_count[c] += 1

    sorted_citation = deque([])
    for ci, c_count in enumerate(citation_count):
        sorted_citation.extend([ci for _ in range(c_count)])

    h_index = 0  # NOTE [1000] case
    checked_citation = []

    while sorted_citation:
        if h_index > sorted_citation[0]:
            checked_citation.append(sorted_citation.popleft())
            continue

        is_cited_h_or_more = len(sorted_citation) >= h_index
        is_cited_under_h = len(checked_citation) <= h_index

        if is_cited_h_or_more and is_cited_under_h:
            h_index += 1
            continue

        break

    return h_index - 1


if __name__ == "__main__":
    assert solution([3, 0, 6, 1, 5]) == 3
    assert solution([0, 0]) == 0
    assert solution([1, 1]) == 1
    assert solution([0]) == 0
    assert solution([1000]) == 1
    assert solution([1, 2, 3]) == 2
    assert solution([1, 2, 4]) == 2
    assert solution([6, 5, 5, 5, 3, 2, 1, 0]) == 4
