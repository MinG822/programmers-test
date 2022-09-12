def solution(number, k):
    answer = []
    ni = 0
    number = [int(n) for n in number]
    # print(number)
    while ni < len(number):
        # print("-----------")
        # print(ni, number[ni], k, answer)
        if k == 0:  # 더 이상 숫자를 빼지 않아도 될 때
            answer.extend(number[ni:])
            # print("case 1 no more drop")
            break

        if len(number) - k == ni:  # 남은 숫자들을 전부 빼야할 때
            # print("case 2 drop all")
            break
        if number[ni] == 9:
            answer.append(number[ni])
            ni += 1
            continue
        # print("case 3, check and drop or not")
        max_check_i = ni + k
        # max_n, max_ni = number[ni], ni
        # for nni in range(ni + 1, max_check_i + 1):
        #     if number[nni] > max_n:
        #         max_n = number[nni]
        #         max_ni = nni

        max_n, max_ni = number[max_check_i], max_check_i
        for nni in range(max_check_i, ni - 1, -1):
            if number[nni] < max_n:
                continue
            max_n = number[nni]
            max_ni = nni

        # print("max n", max_n, "max_ni", max_ni)
        answer.append(max_n)
        k -= max_ni - ni
        ni = max_ni + 1
        # print("next one", ni, k, answer)

    return "".join([str(n) for n in answer])


if __name__ == "__main__":
    assert (solution("1234", 3)) == "4"
    assert (solution("1924", 2)) == "94"
    assert (solution("1231234", 3)) == "3234"
    assert (solution("4177252841", 4)) == "775841"
    assert (solution("1111", 2)) == "11"
