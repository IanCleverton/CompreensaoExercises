def tem_divisor(n):
    return [d for d in range(2, n) if n % d == 0] == []

def primos(n):
    return [x for x in range(2, n+1) if tem_divisor(x)]

print(primos(int(input())))