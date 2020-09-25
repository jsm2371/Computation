from chap1_0.supporter import data_info 
import numpy as np



# 넘파이의 다차원 배열 데이터 구조 np.ndarray의 설명
#help(np.ndarray)

# 데이터 구조 ndarray 클래스
# 클래스가 갖는 대표적인 속성
# 각 데이터 타입 / 내부 데이터 개수/ 데이터 형태의 크기 / 데이터 용량
### 데이터 정보 호출함수 data_info(data,text)
x = np.empty(2)
data_info(x, "단순 배열")

y = np.empty((2,3))
data_info(y, "다차원 배열")

## 부가설명 : 데이터 타입 * 각 데이터 크기 만큼의 저장공간이 할당됨.
## float64 = 8 bytes, size = 6 => 데이터 크기 = 48 bytes






