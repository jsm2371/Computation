import sympy
sympy.init_printing()



#### 데이터 숫자 타입 지정 ####
# x = sympy.data_type(input)

#### 데이터 숫자 타입 ####
# Integer
# Float
# Rational
## type(x) 를 해보면 위의 기호의 타입과 다르게 실제 수치적 타입이 정해짐
## 정수인 경우 오버플로우를 제어하는 정수 계산이 가능하다던지
## 실수인 경우 마무리오차를 제어하는 실수 계산이 가능하다던지
## 유리수인 경우 분수 표현이 된다던지와 같은 처리가 가능하게 됨.




print("\n"+">>> 기호 숫자 타입 검증 <<<")
y = sympy.Symbol("y", real=True)
print(type(y))


#### 데이터 숫자 타입 지정 ####
print("\n"+">>> 데이터 숫자 타입 검증 <<<")
x = sympy.Integer(18)
print(x)
print(type(x))


#### Integer 타입의 계산 특성들 ####
## 정수인 경우 오버플로우를 제어하는 정수 계산이 가능
print("\n"+">>> Integer <<<")
print(sympy.factorial(100))  ## 자동적으로 계산 한도 제어해줌


#### Float 타입의 계산 특성들 ####
## 실수인 경우 마무리오차를 제어하는 실수 계산이 가능
print("\n"+">>> Float <<<")
print("%.25f"%0.3)           ## 마무리오차 발생
print(sympy.Float(0.3, 25))  ## 마무리오차 발생
print(sympy.Float("0.3", 25))


#### Rational 타입의 계산 특성들 ####
## 유리수인 경우 분수 표현이 된다던지와 같은 처리가 가능
print("\n"+">>> Rational <<<")
print(sympy.Rational(11, 13))
r1=sympy.Rational(2, 3)
r2=sympy.Rational(4, 5)
print("r1*r2 =", r1 * r2)
print("r1/r2 =", r1 / r2)




