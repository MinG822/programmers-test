def solution(k, dungeons):
    """
    던전마다 입장시 필요로 하는 피로도와
    던전 완료 시 소모되는 피로도가 주어질 때
    유저의 현재 피로도 k에서 최대로 돌 수 있는 던전의 개수를 찾는 함수
    
    개수가 크지 않아, 재귀로 풀이

    param k: 유저의 현재 피로도, 1 ~ 5000 이하
    param dungeons: 던전 피로도 정보, [[필요 피로도, 소모 피로도], ...],  길이 1 ~ 8
        필요 피로도 >= 소모 피로도, 각 1 ~ 1000
    """

    def run_dungeon(to_dos, curr_count, curr_k):
        max_curr_count = curr_count # for 문 바깥의 변수 하나
        for i, (need_k, use_k) in enumerate(to_dos):
            curr_curr_count = curr_count # 재귀 바깥의 변수 하나 
            curr_curr_k = curr_k

            if curr_curr_k < need_k:
                continue
        
            max_curr_count = max(run_dungeon(to_dos[i+1:] + to_dos[:i], curr_curr_count+1, curr_curr_k-use_k), max_curr_count)

        return max_curr_count

    return run_dungeon(dungeons, 0, k)    


if __name__ == "__main__":
    assert (solution(3, [[3,1], [2,1], [1,1]])) == 3
    assert (solution(4, [[4, 2], [3,1], [2,1], [1,1]])) == 3
    assert(solution(80, [[80, 20], [50, 40], [30, 10]])) == 3
    assert(solution(80, [[50, 40], [30, 10], [80, 20]])) == 3
    assert(solution(80, [[30, 10], [50, 40], [80, 20]])) == 3
    assert(solution(1, [[80, 20]])) == 0
    assert(solution(80, [[80, 20]])) == 1
    assert(solution(1, [[1, 1], [1, 1]])) == 1
    assert(solution(2, [[1, 1], [1, 1]])) == 2
    assert(solution(10, [[1, 1], [1, 1]])) == 2
    assert(solution(0, [])) == 0
    assert(solution(1000, [[100, 10]])) == 1
    