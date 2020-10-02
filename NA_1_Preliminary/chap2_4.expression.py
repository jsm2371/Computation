import sympy
sympy.init_printing()



#### 수식 지정 ####
# x = sympy.Symbol("x")
# expr = f(x)

## 저장된 수식은 수식 트리로 저장된다.
## 수식은 args 속성을 이용해 명시적으로 접근 할 수 있다.


print(">>> 기호 숫자 타입 검증 <<<")
x, y, z = sympy.symbols("x, y, z", real=True)
print(type(x))


#### 수식 지정 ####
print("\n"+">>> 식 지정 <<<")
expr = 1+ 2 * x**2 + 3 * x**3
print(type(expr))
print(expr)
print(expr.args)
print(expr.args[1])
print(expr.args[1].args[1])
print(expr.args[1].args[1].args[0])


