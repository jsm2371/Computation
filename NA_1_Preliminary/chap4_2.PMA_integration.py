import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 적분 ####
# sympy.integrate(ft, (symbol, start, end))

## 또는 아래의 순서를 따라 출력하는 것도 가능
# d = sympy.Integral(expr, symbols)  #적분 표현
# d.doit()                             #적분 계산 결과

x, y, z= sympy.symbols("x, y, z")
a, b, c= sympy.symbols("a, b, c")


#### 적분 ####
print(">>> 적분 <<<")
f = sympy.Function('f')(x)
print(f)
print(sympy.integrate(f, x))  ##콘솔에서 선언하면 아래와 같이 출력됨
"""
⌠        
⎮ f(x) dx
⌡       
"""
print(sympy.integrate(f, (x, a, b))) 
"""
b        
⌠        
⎮ f(x) dx
⌡        
a    
"""


#### 수식의 적분 ####
print("\n"+">>> 수식의 적분 <<<")
print(">>> 단순 항등식 적분 <<<")
expr = x**4 + x**3 + x**2 + x + 1
print(expr)
print(sympy.integrate(expr, x))
print(sympy.integrate(expr, (x, 0, 1)))
print(sympy.integrate(expr, x, x))

print("\n"+">>> 다변수 함수의 적분 <<<")
expr = (x+1)**3 *y**2 *(z-1)
print(sympy.integrate(expr, x,y,z))
print(sympy.integrate(expr, (x, 0, 1), (y, 0, 1), (z, 0, 1)))
print(sympy.integrate(expr, (y, 0, 1), (z, 0, 1), (x, 0, 1)))

print("\n"+">>> 삼각함수의 적분 <<<")
expr = sympy.sin(x*sympy.exp(y))
print(expr)
print(sympy.integrate(expr, x))
print(sympy.integrate(expr, (x,0,pi)))
expr = sympy.sin(x*y)*sympy.cos(x/2)
print(expr)
print(sympy.integrate(expr, x))
print(sympy.integrate(expr, (x,0,pi)))  #조각함수로도 결과가 나올수 있다.


print("\n"+">>> 적분 또다른 방법 <<<")
#계산전의 적분 표현을 출력할수 있다.
expr = sympy.sin(x*sympy.exp(y))
d = sympy.Integral(expr, x)
print(d)              
print(d.doit())


