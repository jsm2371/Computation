#### sympy 패키지 ####
import sympy

#### 고유 기호들 ####
# 자주 사용하는 기호들은 로컬 네임스페이스에 임포트 시키는게 좋음
# 그렇게하지 않는 경우 일일히 sympy.@@ 같은 식으로 계속 호출해야함.
from sympy import I, pi, oo
# I 는 허수
# E 는 자연상수
# pi 는 파이   ## numpy.pi와 충돌이 일어나지 않도록 주의
# EulerGamma 는 오일러 상수
# oo 는 무한대

# 출력을 정해줌.
## jupyter nootbook과 같은 환경에서는 LaTeX 스타일로 출력해준다.
## LaTeX 스타일을 호출 하지 못하는 파워셀 환경에선 적절한 형태로 출력함.
sympy.init_printing()


n = sympy.Symbol("n")
print(sympy.cos(n * pi))
## 콘솔에서 직접 sympy.cos(n * pi)를 입력해보아라

