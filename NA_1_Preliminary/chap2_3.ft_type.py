import sympy
sympy.init_printing()



#### 미정의 함수 지정 ####
# f = sympy.Function(input)
# f = sympy.Function(input)(var)

#### 익명 함수 지정 ####
# g = sympy.Lambda(domain, image)

#### 명시된 함수 ####
# sympy.sin(input)
# sympy.cos(input)
# sympy.exp(input)
# sympy.log(input)   #변수 데이터의 타입은 positive로 선언해야 함



print(">>> 기호 숫자 타입 검증 <<<")
x, y, z = sympy.symbols("x, y, z", real=True)
print(type(x))


#### 미정의 함수 지정 ####
print("\n"+">>> 미정의 함수 지정 <<<")
f = sympy.Function("f")
print(type(f))

f = sympy.Function("f")(x, y, z)
print(f)
print(f.free_symbols)


#### 익명 함수 지정 ####
print("\n"+">>> 익명 함수 지정 <<<")
f = sympy.Lambda(x, x**2)
print(type(f))
print(f(5))
print(f((x+1)))
