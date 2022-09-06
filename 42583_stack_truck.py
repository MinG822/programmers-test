def solution(bridge_length, weight, truck_weight):
    """
    길이가 bridge_length 이고 weight 만큼의 하중을 견딜 수 있는 다리를
    길이가 1 이고 무게가 각기 다른 트럭들이 건널 수 있는 최소 시간
    단, 다리를 지날 땐, 주어진 순서(truck_weight 내 위치)대로 건너야하며
    트럭의 길이 = 다리 길이 1 이다.

    param bridge_length : 다리의 길이(= 다리에 올라갈 수 있는 트럭 수), 1~10000
    param weight : 다리가 견딜 수 있는 하중, 1~10000
    param truck_weight : 트럭들의 무게(1~)를 담고 있는 길이 1~10000 의 리스트
    return truck_weight answer : 모든 트럭이 다리를 건널 수 있는 최소 시간
    """
    answer = 1 # NOTE 차가 다리를 다 지나는 데 걸리는 시간은 다리 길이 + 1 이니 answer = 1 로 설정
    pointer = 0
    running_truck_weights = 0 # NOTE 매번 다시 계산하는 것보다 변수로 각각 빼두는 편이 코드가 길어져도 속도에 빠름
    running_truck_counts = 0
    running_trucks = []
    fininshed_truck_counts = 0

    while fininshed_truck_counts < len(truck_weight):

        if pointer < len(truck_weight):
            target_truck = truck_weight[pointer]
            if (running_truck_weights+target_truck) <= weight and (running_truck_counts + 1) <= bridge_length:
                running_truck_counts += 1
                running_truck_weights += target_truck
                running_trucks.append((target_truck, bridge_length))
                pointer += 1

        answer += 1
        running_trucks = [(t, l-1) for t,l in running_trucks]

        if running_trucks[0][1] == 0:
            fininshed_truck = running_trucks.pop(0)
            running_truck_counts -= 1
            running_truck_weights -= fininshed_truck[0]
            fininshed_truck_counts += 1

    return answer


if __name__ == "__main__":
    assert solution(2, 10, [7]) == 3
    assert solution(2, 10, [7, 4]) == 5
    assert solution(2, 10, [7, 4, 5]) == 6
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(1, 1, [1]) == 2
    assert solution(10000, 10000, [1]) == 10001
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110