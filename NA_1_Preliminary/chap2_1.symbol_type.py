import sympy
sympy.init_printing()


#### 기호 호출 ####
# x = sympy.Symbol(str, num_type=bool)
# x, y, z = sympy.symbols("x, y, z", num_type=bool)

#### 기호 숫자 타입 ####
# real, imaginary
# positive, negative
# integer
# odd, even
# prime
# finite, infinite
## 숫자 타임 검증 : is_(type)



#### 기호 호출 ####
print(">>> 기호 호출 <<<")
x = sympy.Symbol("x")
print(x)
x, y, z = sympy.symbols("x, y, z")
print(x, y, z)

print("\n"+">>> 기호 숫자 타입 검증 <<<")
y = sympy.Symbol("y", real=True)
print(y.is_real)
print(type(y))


