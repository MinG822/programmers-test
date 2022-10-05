# n_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

# from collections import deque


# def solution(k):
#     answers = set()
#     queue = deque([("", k)])

#     while queue:
#         curr_n, curr_cnt = queue.popleft()

#         for n, n_cnt in n_dict.items():
#             if n_cnt == curr_cnt:
#                 answers.add(curr_n + str(n))
#             elif n_cnt < curr_cnt:
#                 queue.append((curr_n + str(n), curr_cnt - n_cnt))
#     # print(answers)
#     print(len(answers))
#     return len(answers)

n_dict = {6: [0, 6, 9], 2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 7: [8]}
from collections import deque
from itertools import combinations


def solution(k):
    answers = set()
    queue = deque([({}, k)])

    while queue:
        curr_answers, curr_cnt = queue.popleft()

        for n_cnt in n_dict.keys():
            if n_cnt == curr_cnt:
                for n in n_dict[n_cnt]:
                    if len(curr_answers):
                        for curr_answer in curr_answers:
                            answers.add(int(str(n) + str(curr_answer)))
                    else:
                        answers.add(n)
                print(answers)
            elif n_cnt < curr_cnt:
                new_set = {}
                for n in n_dict[n_cnt]:
                    for curr_answer in curr_answers:
                        new_set.add(int(str(n) + str(curr_answer)))
                queue.append((new_set, curr_cnt - n_cnt))
    # print(answers)
    print(len(answers))
    return len(answers)


if __name__ == "__main__":
    assert solution(5) == 5
    assert solution(6) == 7
    assert solution(11) == 99
    assert solution(1) == 0
