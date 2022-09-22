def solution(survey, choices):
    """
    두 쌍의 성격으로 이루어진 길이 2의 문자열들의 리스트 survey 와 이에 대한 사용자의 응답 choices 가 주어질 때,
    성격 유형 결과를 알아내는 함수

    param survey: 길이 2의 문자열들의 리스트
    param choices: 해당하는 survey 원소에 대해 1 ~ 7 로 답한 결과들의 리스트, 1 ~ 1000 dlgk
    return answer: 사용자의 성격유형
    """
    result_dict = {"R": 0, "T": 0, "F": 0, "C": 0, "M": 0, "J": 0, "A": 0, "N": 0}
    vs_list = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    for types, choice in zip(survey, choices):
        if choice < 4:
            result_dict[types[0]] += 4 - choice
        elif choice > 4:
            result_dict[types[1]] += choice - 4

    result = ""
    for a, b in vs_list:
        if result_dict[a] < result_dict[b]:
            result += b
        else:
            result += a

    return result


if __name__ == "__main__":
    solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) == "TCMA"
    solution(["TR", "RT", "TR"], [7, 1, 3]) == "RCJA"
    solution(["TR"], [7]) == "RCJA"
