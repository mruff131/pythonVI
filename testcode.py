def Iteration(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Iteration(n - 1) + Iteration(n - 2)

def fib(n):
    for i in range(n + 1):
        print("Iteration({i}): {r}".format(i=i,r=Iteration(i+1)))

fib(5)