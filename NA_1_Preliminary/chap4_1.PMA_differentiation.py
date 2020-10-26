import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 도함수 ####
# sympy.diff(ft, symbol, times)
# sympy.diff(ft, symbols)
#    ft.diff(symbol, times)
#    ft.diff(symbols)                  #이 함수들은 계산결과만 출력한다

## 또는 아래의 순서를 따라 출력하는 것도 가능
# d = sympy.Derivative(expr, symbols)  #도함수 표현
# d.doit()                             #도함수 계산 결과

x, y, z= sympy.symbols("x, y, z")
a, b, c= sympy.symbols("a, b, c")


#### 미정의 함수의 도함수 ####
print(">>> 미정의 함수의 도함수 <<<")
f = sympy.Function('f')(x)
print(f)
print(sympy.diff(f, x))  ##콘솔에서 선언하면 아래와 같이 출력됨
"""
d       
──(f(x))
dx    
"""
print(sympy.diff(f, x, x)) #2계 도함수
print(sympy.diff(f, x, 2)) #위와 동일
"""
  2      
 d       
───(f(x))
  2      
dx   
"""
print(sympy.diff(f, x, 3)) 

g = sympy.Function('g')(x, y)
print(g)
print(g.diff(x, y))
"""
   2          
  ∂           
─────(g(x, y))
∂y ∂x
"""
print(g.diff(x, 3, y, 2))
"""
    5           
   ∂            
───────(g(x, y))
  2   3         
∂y  ∂x
"""


#### 수식의 도함수 ####
print("\n"+">>> 수식의 도함수 <<<")
print(">>> 단순 항등식 도함수 <<<")
expr = x**4 + x**3 + x**2 + x + 1
print(expr)
print(expr.diff(x))
print(expr.diff(x, 2))

print("\n"+">>> 다변수 함수의 도함수 <<<")
expr = (x+1)**3 *y**2 *(z-1)
print(expr)
print(expr.diff(x,y,z))

print("\n"+">>> 삼각함수의 도함수 <<<")
expr = sympy.sin(x*y)*sympy.cos(x/2)
print(expr)
print(expr.diff(x))   #연쇄법칙도 성립함


print("\n"+">>> 도함수 또다른 방법 <<<")
#계산전의 도함수 표현을 출력할수 있다.
d = sympy.Derivative(expr, x)
print(d)              
print(d.doit())


