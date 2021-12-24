fname="input"
nums = [int(x) for x in open(fname).read()[0:-1].split(',')]

def f(x):
    return sum(map(lambda n: abs(n-x), nums))

def triangular_num(x):
    return x*(x+1)//2

def f2(x):
    return sum(map(lambda n: triangular_num(abs(n-x)), nums))

def fp(f, x):
    return (f(x+.1)-f(x))/0.1

def bisect(f,a,b,tol):
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    return (a+b)/2

print(f(round(bisect(lambda x: fp(f, x),min(nums),max(nums),0.01))))
print(f2(round(bisect(lambda x: fp(f2, x),min(nums),max(nums),0.01))))
