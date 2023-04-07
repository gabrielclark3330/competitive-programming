
def prime_sieve(n):
    primes_to_return = []
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            primes_to_return.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

    return primes_to_return

cases = int(input())

primes_to_n = prime_sieve(32000)
for _ in range(cases):
    test_case = int(input())

    primes_set = set(primes_to_n)
    answer_set = [] 
    
    for i in range(0, len(primes_to_n)):
        if primes_to_n[i] > test_case/2:
            break
        if test_case - primes_to_n[i] in primes_set:
            answer_set.append((primes_to_n[i], test_case-primes_to_n[i]))

    print(f"{test_case} has {len(answer_set)} representation(s)")

    for a,b in answer_set:
        print(f"{a}+{b}")
    print()
