import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 함수의 극한 ####
# sympy.limit(expr, 변수, 접근값)

#### 급수계산 ####
# x= sympy.Sum(expr, (변수, 시작, 종료))      ##급수합
# x= sympy.Product(expr, (변수, 시작, 종료))  ##급수곱
# x.doit()            ## Sum은 인스턴스


x, y, z= sympy.symbols("x, y, z")
h= sympy.symbols("h")
n= sympy.symbols("n", integer=True)



#### 함수의 극한 ####
print(">>> 함수의 극한 <<<")
print(sympy.limit(sympy.sin(x)/x, x, 0))

#### 함수의 극한을 이용하는 대표적인 예제 ####
print("\n"+">>> 함수의 극한 예제 <<<")
f = sympy.Function("f")
diff_lim = (f(x+h) - f(x))/h
print(diff_lim)
print(sympy.limit(diff_lim.subs(f, sympy.cos), h, 0))
print(sympy.limit(diff_lim.subs(f, sympy.sin), h, 0))

expr = (x**2 - 3*x) / (2*x - 2)
p = sympy.limit(expr, x, oo)
print(p)
q = sympy.limit(expr/x, x, oo)
print(q)


#### 급수계산 ####
print("\n"+">>> 급수계산 <<<")
x = sympy.Sum(1/(n**2), (n,1,oo))
print(x)
print(x.doit())

y = sympy.Product(n, (n,1,7))
print(y)
print(y.doit())

