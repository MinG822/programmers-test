def solution(priorities, location):
    """
    중요한 문서가 먼저 인쇄되는 프린터에서, 
    주어진 location의 문서가 몇 번째로 인쇄되는 지 찾는 함수
    
    param priorities: 문서 중요도(1~9) 리스트, 길이 100 이하
    param location: 확인해야하는 문서의 위치, 0부터 시작
    return answer: location 문서의 프린트 순서
    """
    priority_map = {}
    priority_order = sorted(list(set(priorities)), key=lambda x: -x)
    for pi, priority in enumerate(priorities):
        priority_map[priority] = priority_map.get(priority, []) + [pi]
    
    def get_print_order(pos, pos_to_compare):
        print_order_front = []
        print_order_end = []
        for i in pos:
            if i > pos_to_compare:
                print_order_front.append(i)
            else:
                print_order_end.append(i)
        print_order = print_order_front + print_order_end
        return print_order
    
    answer = 1
    target_num = priorities[location]
    last_num_index = 0
    for pi, num in enumerate(priority_order):
        if num > target_num:
            answer += len(priority_map[num])
            continue
            
        if pi == 0:
            return answer + priority_map[num].index(location)
        
        last_num_index = get_print_order(priority_map[priority_order[pi-1]], last_num_index)[-1]
        print_order = get_print_order(priority_map[num], last_num_index)
        answer += print_order.index(location)
        break
        
        
    return answer

if __name__ == "__main__":
    assert solution([3, 1, 3, 1, 3], 1) == 4
    assert solution([5, 4, 3, 2, 1], 3) == 4
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
    assert solution([1, 2, 3, 4, 5], 3) == 2
    assert solution([1], 0) == 1
    assert solution([1, 1, 1, 1, 1], 3) == 4
    assert solution([2,1,3,2], 2) == 1
