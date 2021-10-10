def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1,1

    i = 3
    while  i <= n:
        i = i + 1
        fib_x, fib_next =