def solution(sizes):
    """
    다양한 사이즈의 명함이 주어졌을 때,
    모든 명함을 담을 수 있는 가장 최소 사이즈의 크기를 찾는 함수
    모든 경우의 수를 다 구해야하는 줄 알았는 데, 현재 가방을 회전해서 크기 비교한 후 작은 것 만 넣으면 된다.
    => 다른 사람의 풀이를 본 후 ) 전체 사이즈 중에 가장 큰 길이 * w, h 쌍 중 작은 값들 중 가장 큰 길이

    param sizes: [가로, 세로] 의 리스트, 가로와 세로는 1 ~ 1000 이며, 리스트의 길이는 1~10000
    return answer: 사이즈
    """
    w, h = sizes[0]
    from collections import deque

    queue = deque([[w, h, 0], [h, w, 0]] if w != h else [[w, h, 0]])

    while len(queue):
        former_w, former_h, i = queue.popleft()

        if i+1 == len(sizes):
            queue.append([former_w, former_h, i])
            break

        w, h = sizes[i+1][0], sizes[i+1][1]

        if w == former_w and h == former_h: # NOTE 중복 제거
            queue.append([w, h, i+1])
            continue

        curr_w, curr_h = max(former_w, w), max(former_h, h)
        
        if w != h: # NOTE 중복 제거
            curr_w_2, curr_h_2 = max(former_w, h), max(former_h, w)
            if (curr_w == curr_w_2) and (curr_h == curr_h_2): # NOTE 중복 제거
                queue.append([curr_w, curr_h, i+1]) # NOTE 이 부분이 없으면 실패
                continue 
            
            if curr_w * curr_h < curr_w_2 * curr_h_2: # NOTE 둘 중 최소만 넣도록 하면 타임아웃에러 해결
                queue.append([curr_w, curr_h, i+1])
            else:
                queue.append([curr_w_2, curr_h_2, i+1])
            continue
        
        queue.append([curr_w, curr_h, i+1])

    answer = queue[0][0] * queue[0][1]
    for w, h, _ in queue:
        if w*h < answer:
            answer = w*h

    return answer


if __name__ == "__main__":
    assert(solution([[1,1]])) == 1
    assert(solution([[60, 50], [30, 70]])) == 3500
    assert(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) == 4000
    assert(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) == 120
    assert(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) == 133