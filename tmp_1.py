def get_zero_daystamp(target_date):
    """
    YYYY.MM.DD 형태의 주어진 target_date 에 대해,
    0년 0월 0일 기준의 날 일 수를 구함
    NOTE 날짜는 1 ~ 28일로만 이루어졌음
    """
    y, m, d = [int(_) for _ in target_date.split(".")]

    result = 0
    result += d
    result += m * 28
    result += y * 28 * 12

    return result


def solution(today, terms, privacies):
    """
    오늘 날짜와 약관의 유효기간이 담긴 1차원 배열, 수집된 개인 정보의 정보를 담은 1차원 문자배열이 주어질 때,
    파기해야할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 반환하는 함수

    NOTE 날짜는 1 ~ 28일로만 이루어졌으며, 1일인 경우 01로 표시
    NOTE 개인 정보 번호는 i + 1 번으로 반환

    param today: YYYY.MM.DD 형태의 오늘 날짜
    param terms: 길이 1 ~ 20, "약관종류 유효기간" 형태의ㄴ 문자열, 약관 종류는 A~Z 중 하나. 중복 x
    param privacies: 길이 1 ~ 100, "수집된날짜 약관종류" 형태의 문자열
    return result: 파기 해야할 개인정보의 번호(i+1)의 오름차순 배열 ex) [1, 3]
    """
    term_days = {}
    for term in terms:
        t, d = term.split(" ")
        term_days[t] = int(d) * 28

    results = []
    today_daystamp = get_zero_daystamp(today)

    for i, privacie in enumerate(privacies):
        start_date, term = privacie.split(" ")

        if get_zero_daystamp(start_date) + term_days.get(term) > today_daystamp:
            continue
        results.append(i + 1)
    return results


if __name__ == "__main__":
    assert str(
        solution(
            "2022.05.19",
            ["A 6", "B 12", "C 3"],
            ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        )
    ) == str([1, 3])
    assert str(
        solution(
            "2020.01.01",
            ["Z 3", "D 5"],
            [
                "2019.01.01 D",
                "2019.11.15 Z",
                "2019.08.02 D",
                "2019.07.01 D",
                "2018.12.28 Z",
            ],
        )
    ) == str([1, 4, 5])
