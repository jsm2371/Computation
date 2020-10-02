from chap1_0_supporter import data_info 
import numpy as np



# 데이터 타입
# 넘파이에서 자체 제공하기 때문에 np.int8 같은 형태로 사용한다.
################# 데이터 타입 ##################
## int     # int8      int16      int32      int64
## uint    # uint8     uint16     uint32     uint64
## float   # float16   float32    float64    float128
## complex # complex64 complex128 complex256  
## bool    # Bool

########### 1. 타입+숫자형 #############
int8_x = np.empty(1, dtype=np.int8)
data_info(int8_x,"Type = int8")

int16_x = np.empty(1, dtype=np.int16)
data_info(int16_x,"Type = int16")

int32_x = np.empty(1, dtype=np.int32)
data_info(int32_x,"Type = int32")

int64_x = np.empty(1, dtype=np.int64)
data_info(int64_x,"Type = int64")

com64_x = np.empty(1, dtype=np.complex64)
data_info(com64_x,"Type = complex64")

## 부가설명 : 타입+숫자가 붙는데, 이 때의 숫자가 데이터에 할당되는 크기 bits.

 
########### 2. 기본 제공형 #############
# int=int32
int_x = np.empty(1, dtype=np.int)  
data_info(int_x,"Type = int") 

# int=uint32
uint_x = np.empty(1, dtype=np.uint)  
data_info(uint_x,"Type = uint")

# float=float64
float_x = np.empty(1, dtype=np.float)  
data_info(float_x,"Type = float")

# complex=complex128
complex_x = np.empty(1, dtype=np.complex)  
data_info(complex_x,"Type = complex")

# bool 형식은 1 byte 할당
bool_x = np.empty(1, dtype=np.bool)  
data_info(bool_x,"Type = bool")


########### 3. 타입 변환 #############
# ※주의. x에 타입이 주어진 경우, x의 타입을 곧바로 변환할 수는 없다.
# 3-1. y=np.array(x, dtype=다른 타입)
# 3-2. y=x.astype(다른 타입)
# 위와 같이 새로운 배열을 선언 해주어야만 한다.
## ※예외. 연산의 결과가 다른 타입이 될수 있다. (예. 나눗셈)
print("")
print(">>>타입 변환<<<")

x=np.empty(3)
print("x_type =",x.dtype)

y=np.array(x,dtype=np.int)
print("new_x1_type =",y.dtype)

y=x.astype(np.int)
print("new_x2_type =",y.dtype)







