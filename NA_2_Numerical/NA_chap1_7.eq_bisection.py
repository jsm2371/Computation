from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt


#### 수치적 해법 : 이분법 ####
## pp.243-244, 248-249 ##

### 메소드 ###
# optimize.bisect(func, a, b)
# optimize.brentq(func, a, b)
# optimize.brenth(func, a, b)

# 함수, 유효구간, 도메인 설정
f = lambda x: np.exp(x) - 2
tol = 0.1
a, b = -2, 2
x = np.linspace(-2.1, 2.1, 1000)

# f 도식화
fig, ax = plt.subplots(1, 1, figsize=(12,4))

ax.plot(x, f(x), lw=1.5)
ax.axhline(0, ls=':', color= 'k')
ax.set_xticks([-2, -1, 0, 1, 2])

# 이분법 과정을 나타내는 표 생성
fa, fb = f(a), f(b)

ax.plot(a, fa, 'ko')
ax.plot(b, fb, 'ko')
ax.text(a, fa+0.5, r"$a$", ha='center')
ax.text(b, fb+0.5, r"$b$", ha='center')

n=1
while b - a > tol:
    m = a+(b-a)/2
    fm = f(m)

    ax.plot(m, fm, 'ko')
    ax.text(m, fm-0.5, r"$m_%d$"%n, ha='center')
    n+=1

    if np.sign(fa) == np.sign(fm):
        a, fa = m, fm
    else:
        b, fb = m, fm

ax.plot(m, fm, 'r*', markersize=10)

fig.show()


# 실제로 해 구해보기
# 이분법을 이용한 해는 optimize.bisect(func, a, b)을 이용하여 구함
print(optimize.bisect(f, -2, 2))


## * 참고로 이분법을 프로그래밍에서 쓰기 좋게 개선한 방법이 존재한다.
# optimize.brentq/brenth
# brentq : 부호 변경 구간의 하한 값을 취함
# brenth : 부호 변경 구간의 상한 값을 취함
print('brentq =',optimize.brentq(f, -2, 2))
print('brentq =',optimize.brenth(f, -2, 2))
