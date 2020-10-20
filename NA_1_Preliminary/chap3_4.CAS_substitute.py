import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 치환 ####
# expr.subs(domain, image) ## 변수치환
# expr.subs({domain: image}.dict) ## 다변수치환


x, y, z= sympy.symbols("x, y, z")

#### 치환 ####
print(">>> 치환 <<<")
print(">>> 변수 치환 <<<")
expr = x+y
print(expr)
print(expr.subs(x, y))

print("\n"+">>> 수식 치환 <<<")
expr = sympy.sin(x)
print(expr)
print(expr.subs(sympy.sin, sympy.cos))

print("\n"+">>> 다중치환 <<<")
expr = sympy.sin(x*z)
print(expr)
print(expr.subs({z:sympy.exp(y), x:y, sympy.sin:sympy.cos}))

print("\n"+">>> 값 대입 <<<")
expr = x * y + z**2 *x
print(expr)
values = {x:1.25, y:0.4, z:3.2}
print(values)
print(expr.subs(values))








