import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 테일러 급수전개 ####
# sympy.series(ft, 변수, 상수, 마지막항)
#    ft.series(변수, 상수, 마지막항)
###    ft.series().remove0()  #맥클로린 상수 제거 **근데 에러남


x, y, z= sympy.symbols("x, y, z")
x0= sympy.symbols("{x_0}")



#### 급수전개 표현 ####
print(">>> 급수전개 <<<")
f = sympy.Function("f")(x)
print(sympy.series(f, x))  ##콘솔로는 다르게 나오는데 여기에 옮기고 싶진 않다.
print(f.series(x, x0, n=2))
#print(f.series(x, x0, n=2).remove0())  ##이거 에러나는데 뭐임?

#### 급수전개 표현을 이용하는 대표적인 예제 ####
print("\n"+">>> 급수전개 예제 <<<")
print(sympy.cos(x).series())
print(sympy.sin(x).series())
print(sympy.exp(x).series())
print((1/(1+x)).series())

#### 다변량 함수 급수전개 ####
print("\n"+">>> 다변량 함수 급수전개 <<<")
expr = sympy.cos(x) / (1+sympy.sin(x*y))
print(expr)
print(expr.series(x, n=4))
print(expr.series(y, n=4))
