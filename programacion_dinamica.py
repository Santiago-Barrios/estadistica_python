import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = fibonacci_dinamico(n - 1, memo ) + fibonacci_dinamico( n - 2, memo )
        memo[n] = result
        return result

def run():
    sys.setrecursionlimit(10002)
    fibonacci_number = int(input('Give me the fibonacci number sequence that you want: '))
    # result = fibonacci_recursivo(fibonacci_number)
    result_dinamico = fibonacci_dinamico(fibonacci_number)
    # print(f'{result} result normal fibonacci')
    print(f'{result_dinamico} result dinamic_fibonacci')

if __name__ == '__main__':
    run()