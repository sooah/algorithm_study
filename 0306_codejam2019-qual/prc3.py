import string

def GCD(x, y):
    while(x != 0):
        x, y = x, y%x
    return y

t = int(input())
for i in range(1, t + 1):
    N, L = map(int, input().split(" "))
    ciphers = list(map(int, input().split(" ")))

    primes = []
    for i in range(0, L-1):
        prime = GCD(ciphers[i], ciphers[i+1])
        primes.append(prime)
        primes.append(ciphers[i]//prime)
        primes.append(ciphers[i+1]//prime)
    print(primes)
    primes = sorted(primes)
    print(primes)

    alphabet = dict(zip(string.ascii_uppercase, [0]*26))




