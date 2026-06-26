def primos(n):
    return [x for x in range(2, n+1) if all(x % d for d in range(2, x))]

print(primos(50))