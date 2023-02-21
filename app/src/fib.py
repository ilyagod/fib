def calc_fib(n):
    if n in {0, 1}:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)