class MinHeap:
    def __init__(self):
        self.data = [0]

    @staticmethod
    def get_parent_node(child_node):
        return child_node//2
    
    @staticmethod
    def get_child_node(parent_node):
        return parent_node * 2
    
    def get_min_value(self):
        return self.data[1]

    def insert(self, num):
        self.data.append(num)
        target_idx = len(self.data) - 1
        while target_idx != 1:
            parent_idx = self.get_parent_node(target_idx)
            if self.data[target_idx] < self.data[parent_idx]:
                self.data[target_idx], self.data[parent_idx] = self.data[parent_idx], self.data[target_idx]
                target_idx = parent_idx
            else:
                break
    
    def delete_min(self):
        end_node = self.data.pop()
        if len(self.data) == 1:
            return

        self.data[1] = end_node
        target_idx = 1

        while True:
            child_node = self.get_child_node(target_idx)
            
            if len(self.data) <= child_node:
                break

            child_value = self.data[child_node]
            
            if len(self.data) > child_node + 1:
                if self.data[child_node + 1] <= child_value:
                    child_value = self.data[child_node + 1]
                    child_node += 1
            
            if self.data[target_idx] > child_value:
                self.data[target_idx], self.data[child_node] = child_value, self.data[target_idx]
                target_idx = child_node
            else:
                break

def solution(scovile, K):
    """
    음식들의 매운 지수가 주어질 때,
    가장 낮은 음식의 매운 지수가 K 이상이 되도록 섞어야 하는 최소 횟수
    음식을 섞을 때는, 가장 낮은 지수의 음식 + 두 번째로 낮은 지수의 음식 * 2 가 되도록 하며,
    K 이상이 될 수 없다면 최소 횟수는 -1 로 한다.
    효율성 테스트 실패 => deque 의 popleft 를 사용하면 더 줄일 수 있다고들 한다

    param scovile : 음식의 매운 지수(0 ~ 백만)의 리스트, 길이 2 ~ 백만
    param K : 최소 매운 지수, 0 ~ 10억
    return count: 음식을 섞어야하는 최소 횟수
    """
    if K == 0:
        return 0
    
    if min(scovile) >=  K:
        return 0

    min_heap = MinHeap()

    for food in scovile:
        min_heap.insert(food)
    
    count = 0

    while min_heap.get_min_value() < K:
        if len(min_heap.data) <= 2:
            count = -1
            break

        min_value = min_heap.get_min_value()
        min_heap.delete_min()
        second_min_value = min_heap.get_min_value()
        min_heap.delete_min()
        value_to_insert = min_value + second_min_value * 2
        min_heap.insert(value_to_insert)
        count += 1
    return count

    

if __name__ == "__main__":
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([1, 12], 1) == 0
    assert solution([1, 0], 0) == 0
    assert solution([1, 0], 1) == 1
    assert solution([1, 1], 4) == -1
    assert solution([0, 0], 1) == -1
    assert solution([0, 0], 0) == 0
    assert solution([1, 1, 2], 3) == 2
    assert solution([1,1,1,1,1,1,100,100,100,100,0,0,0,0,0], 11) == 10
    

