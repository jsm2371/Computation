import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 수식 전개 ####
# sympy.expand(expr, expr_type=True)
# sympy.self.simplify(expr_type=True)

#### 전개하려는 수식 타입 ####
# trig : 삼각함수 전개
# log : 로그함수 전개
# complex: 복소수 전개
# power_base : 지수밑 전개
# power_exp :지수 전개


x, y= sympy.symbols("x, y")
a, b= sympy.symbols("a, b", positive = True)

#### 수식 전개 ####
print(">>> 수식 전개 <<<")
expr = (x+1) * (x+2)
print(expr)
print(sympy.expand(expr))
print(expr.expand())
print(expr)

print("\n"+">>> 삼각함수 전개 <<<")
print(sympy.sin(x+y).expand(trig=True))

print("\n"+">>> 로그함수 전개 <<<")
print(sympy.log(a*b).expand(log=True))

print("\n"+">>> 복소수 전개 <<<")
print(sympy.exp(I*a+b).expand(complex=True))

print("\n"+">>> 지수밑 전개 <<<")
print(sympy.expand((a*b)**x, power_base=True))

print("\n"+">>> 지수 전개 <<<")
print(sympy.exp((a-b)*x).expand(power_exp=True))


