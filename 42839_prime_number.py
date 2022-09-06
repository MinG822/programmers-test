def get_prime_sieve(n):
    """
    주어진 숫자 n 까지 소수를 판별한 리스트
    에라토스테네스의 체 방법으로 구현
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity
    
    param n : 주어진 숫자
    return sieve : 이번에 주어진 숫자까지 계산한 체
    """  
    sieve = [False, False]
    if n < 2:
        return sieve
    
    sieve += [True for _ in range(2, n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i*i, n+1, i):
                sieve[j] = False
                
    return sieve
    
def solution(numbers):
    """
    주어진 한자리 숫자들을 조합해 
    각기 다른 소수를 최대 몇 개 만들 수 있는 지 찾는 함수

    만들 수 있는 최대 숫자 조합은 7!(5040개), 범위는 1 ~ 9999999
    이므로 조합을 찾고 난 이후, 소수인지 판단하도록 함

    param numbers: 한자리 숫자(0~9)들의 리스트, 길이 1 ~ 7
    return answer: 만들 수 있는 소수의 개수
    """
    answer = 0
    
    all_nums = []

    import itertools
    for size in range(1, len(numbers)+1):
        all_nums += [int("".join(num)) for num in itertools.permutations(numbers, size)]
    
    all_nums = list(set(all_nums))
    max_num = max(all_nums)

    sieve = get_prime_sieve(max_num)

    for num in all_nums:
        if sieve[num]:
            answer += 1
        
    return answer

if __name__ == "__main__":
    assert solution("17") == 3
    assert solution("011") == 2
    assert solution("1") == 0
    assert solution("1276543") == 1336
    assert solution("0") == 0