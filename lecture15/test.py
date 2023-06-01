def f(n):
    x=[1]
    if n==1:
        return x
    elif n==2:
        return x + x
    elif n>2:
        for y in range(0, len(f(n-1))-1):
            x.append(f(n-1)[y]+f(n-1)[y+1])
        x.append(1)
        return x

def g(m):
    for i in range(1,m+1):
        print(f(i))
g(6)
