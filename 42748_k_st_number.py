def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def solution(array, commands):
    """
    숫자리스트를 commands 에 따라
    i ~ j 번째 숫자까지 자르고 정렬했을 때 k 번째 있는 수를 구하는 함수

    NOTE 주어진 리스트 크기가 작기 때문에 귀여운 버블소트 사용

    param array: 1 ~ 100 사이의 숫자 리스트, 길이 1~ 100 이하
    param commands: [[i,j,k], ...] , 명령들의 리스트
    return answer: 각 명령을 수행했을 때의 숫자
    """
    answer = []

    for i, j, k in commands:
        i, k = i - 1, k - 1
        check_array = [*array[i:j]]
        sorted_array = bubble_sort(check_array)
        answer.append(sorted_array[k])

    return answer
