def solution(fees, records):
    """주차 요금 정보와, 차량들의 입출차시간이 주어질 때, 결제할 주차 요금을 반환하는 함수"""
    basic_time, basic_fee, unit_time, unit_fee = fees

    def time_to_min(x):
        t = x.split(":")
        return int(t[0]) * 60 + int(t[1])

    LAST_TIME = time_to_min("23:59")

    car_records = {}
    for record in records:
        recorded_time, car_id, _ = record.split(" ")
        car_records[car_id] = car_records.get(car_id, []) + [time_to_min(recorded_time)]

    car_fee = {}
    for car_id, car_record in car_records.items():

        if len(car_record) % 2:
            car_record.append(LAST_TIME)

        car_total_time = sum(
            [car_record[i] - car_record[i - 1] for i in range(1, len(car_record), 2)]
        )
        car_total_fee = (
            basic_fee
            if car_total_time <= basic_time
            else basic_fee + unit_fee * -(-(car_total_time - basic_time) // unit_time)
        )
        car_fee[car_id] = car_total_fee

    return [car_fee[k] for k in sorted(car_fee.keys())]


if __name__ == "__main__":
    assert str(
        solution(
            [180, 5000, 10, 600],
            [
                "05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT",
            ],
        )
    ) == str([14600, 34400, 5000])

    assert str(
        solution(
            [120, 0, 60, 591],
            [
                "16:00 3961 IN",
                "16:00 0202 IN",
                "18:00 3961 OUT",
                "18:00 0202 OUT",
                "23:58 3961 IN",
            ],
        )
    ) == str([0, 591])

    assert str(solution([1, 461, 1, 10], ["00:00 1234 IN"])) == str([14841])
