import itertools


def solution(users, emoticons):
    results = []
    for p in itertools.product([40, 30, 20, 10], repeat=4):
        plus_user = 0
        sales = 0
        for user in users:
            ratio, budget = user[0], user[1]
            price_sum = 0
            for pp, emo in zip(p, emoticons):
                if pp >= ratio:
                    price_sum += int(emo * (1 - pp / 100))

                if price_sum >= budget:
                    plus_user += 1
                    break
            else:
                sales += price_sum
        results.append((plus_user, price_sum))
    results = sorted(results, key=lambda x: (-x[0], -x[1]))
    print(results)
    return results[0]


if __name__ == "__main__":
    assert str(solution([[40, 10000], [25, 10000]], [7000, 9000])) == str([1, 5400])
