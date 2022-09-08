def solution(maps):
    """
    n * m 크기의 맵이 주어질 때
    (0, 0) 위치의 유저가 (n - 1, m - 1) 위치의 상대팀 진영에 도착하는 
    가장 최소의 거리를 구하는 함수

    param maps: 1 과 0 으로 이루어진 2차원 리스트, 크기 2 ~ 10000
    return answer: 최소 거리
    """
    find = False
    
    m, n = len(maps), len(maps[0])
    answer = m * n

    maps[m-1][n-1] = 1

    from collections import deque

    queue = deque([(0, 0, 1)])

    while queue:
        x, y, acc = queue.popleft()
        
        if (x, y) == (m-1, n-1):
            find = True
            answer = min(answer, acc)
            break
            
        if x > 0 and maps[x-1][y]: 
            maps[x-1][y] = 0
            queue.append((x-1, y, acc+1))

        if x < (m - 1) and maps[x+1][y]:
            maps[x+1][y] = 0
            queue.append((x+1, y, acc+1))

        if y > 0 and maps[x][y-1]:
            maps[x][y-1] = 0
            queue.append((x, y-1, acc+1))
        
        if y < (n - 1) and maps[x][y+1]:
            maps[x][y+1] = 0
            queue.append((x, y+1, acc+1))

    if not find:
        answer = -1

    return answer

if __name__ == "__main__":
    assert(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) == 11
    assert(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) == -1