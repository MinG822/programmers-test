def solution(answers):
    """
    일정한 찍기 패턴을 가진 학생들이 주어질 때,
    가장 많이 맞춘 학생들을 찾아내는 함수

    param answers: 시험 정답(1, 2, 3, 4, 5) 리스트, 길이는 ~ 10000
    return top_students: 가장 높은 점수를 받은 학생들의 번호
    """
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    student_score = [0, 0, 0]
    
    for ai, answer in enumerate(answers):
        for si, student in enumerate(students):
            if student[ai%len(student)] == answer:
                student_score[si] += 1

    top_score = max(student_score) or 1
    top_students = [si + 1 for si in range(len(student_score)) if student_score[si] == top_score]
    
    return top_students


if __name__ == "__main__":
    assert str(solution([1, 2, 3, 4, 5])) == str([1])
    assert str(solution([1, 3, 2, 4, 2])) == str([1, 2, 3])
    assert str(solution([5])) == str([])
    assert str(solution([])) == str([])