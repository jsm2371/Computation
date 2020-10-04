import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 인수 구분 ####
# 정확히 말하자면 이것은 expand의 역수행 함수이다
# sympy.factor(expr)     ## 수식전개 (인수분해)
# sympy.logcombine(expr) ## 로그함수 병합
# expr.collect(symbol)   ## 기호 전개

#### 유리식 전개 ####
# sympy.apart(expr, symbol) ## 해당 기호 기준 분모별 전개
# sympy.together(expr)      ## 유리식 결합
# sympy.cancel(expr)        ## 약분


x, y, z= sympy.symbols("x, y, z")
a, b= sympy.symbols("a, b", positive = True)

#### 인수 구분 ####
print(">>> 수식 전개 <<<")
expr = x**2 -1
print(expr)
print(sympy.factor(expr))
expr = x * sympy.cos(y) + sympy.sin(z) * x
print(expr)
print(sympy.factor(expr))
print(sympy.trigsimp(expr))

print("\n"+">>> 로그함수 병합 <<<")
expr = sympy.log(a) - sympy.log(b)
print(expr)
print(sympy.factor(expr))
print(sympy.logcombine(expr))

print("\n"+">>> 기호 전개 <<<")
expr = x + y + x*y*z
print(expr)
print(expr.collect(x))
print("\n"+">>> 기호 전개 응용<<<")
expr = sympy.cos(x + y) + sympy.sin(x - y)
print(expr)
print(expr.expand(trig=True))
print(expr.expand(trig=True).collect([sympy.cos(x), sympy.sin(x)]))
print(expr.expand(trig=True).collect([sympy.cos(x),
                                      sympy.sin(x)]).collect(
                                          sympy.cos(y) - sympy.sin(y)))
# 위와 같이 기호 전개를 체인콜 시키는게 가능하다!



#### 유리식 전개 ####
print("\n"+">>> 유리식 전개 <<<")
print(">>> 분모별 전개 <<<")
expr = 1/(x**2 + 3*x + 2)
print(expr)
print(sympy.apart(expr, x))

print("\n"+">>> 유리식 결합 <<<")
expr = 1/(y*x + y) + 1/(1+x)
print(expr)
print(sympy.together(expr))

print("\n"+">>> 약분 <<<")
expr = y / (y*x + y)
print(expr)
print(sympy.cancel(expr))






