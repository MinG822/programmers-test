from collections import deque


def solution(begin, target, words):
    """
    단어 begin 과 target 이 주어질 때, words 에 있는 단어만을 활용해
    한 단어씩만이 다른 단어로 바꿔 begin 이 target 으로 바꿀 때,
    단어를 바꾸는 가장 최소의 횟수를 찾는 함수
    이때 단어의 길이는 3 ~ 10 이며, 주어진 모든 단어의 길이는 동일함

    param begin: 시작 단어
    param target: 끝 단어
    param wards: 중복되지 않은 길이 3 ~ 50의 단어 리스트
    return answer: 최소 횟수
    """
    answer = 0

    if target not in words:
        return answer

    queue = deque([(begin, answer)])
    visited = [
        0 for _ in range(len(words))
    ]  # NOTE 다른 사람의 풀이를 보니 visited 를 dict 로 가지고 있기도 한 데, 훨씬 나은 듯 하다

    is_adjacent = (
        lambda word_a, word_b: sum([w != c for w, c in zip(word_a, word_b)]) == 1
    )

    while queue:
        curr_word, depth = queue.popleft()

        for i in range(len(words)):
            if visited[i]:
                continue

            if is_adjacent(words[i], curr_word):
                if words[i] == target:
                    return depth + 1

                visited[i] = 1
                queue.append((words[i], depth + 1))

    return answer


if __name__ == "__main__":
    assert (solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) == 4
    assert (solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) == 0
