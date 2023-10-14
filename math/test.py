def check_prime(n):
    for i in range(2, n+1):
        if n % i == 0:
            break
    print(i)
    if n == i:
        print(n, i)

check_prime(7)