import random

def fibonacci_RE(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_RE(n - 1) + fibonacci_RE(n - 2)

def fibonacci_DI(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        Res = fibonacci_DI(n - 1, memo) + fibonacci_DI(n - 1, memo)
        memo[n] = Res

        return Res

if __name__ == '__main__':
    #n = int(input('Escoge un numero: '))

    n = random.randint(1,10)

    Res = fibonacci_DI(n)
    
    print(n)

    print(Res)