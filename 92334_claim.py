def solution(id_list, report, k):
    """유저 아이디와, 유저 유저가 신고한 아이디 쌍, 정지 횟수가 주어질 때, 유저가 신고한 아이디 중 정지된 아이디 수의 리스트를 반환하는 함수"""

    result_dict = {}
    reporting_dict = {}

    for reporting in set(report):
        reporter, target = reporting.split(" ")
        result_dict[target] = result_dict.get(target, 0) + 1
        reporting_dict[reporter] = reporting_dict.get(reporter, []) + [target]

    notice_mail = []
    for reporter_id in id_list:
        if not reporting_dict.get(reporter_id):
            notice_mail.append(0)
            continue

        notice_mail.append(
            len(
                [
                    reported_target
                    for reported_target in reporting_dict[reporter_id]
                    if result_dict.get(reported_target, 0) >= k
                ]
            )
        )

    return notice_mail


if __name__ == "__main__":
    assert str(
        solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2,
        )
    ) == str([2, 1, 1, 0])
    assert str(
        solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
    ) == str([0, 0])
