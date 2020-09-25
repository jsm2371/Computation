import numpy as np



# 데이터 구조 ndarray 클래스
# 클래스가 갖는 대표적인 속성
# 각 데이터 타입 / 내부 데이터 개수/ 데이터 형태의 크기 / 데이터 용량
def data_info(x=np.empty(1),text="  "):
    print("")
    print(">>>"+text+"<<<")
    print("data =",x)
    print("data type =",x.dtype,end=" | ")
    print("size =",x.size,end=" | ")
    print("shape =",x.shape,end=" | ")
    print("byte =",x.nbytes, "bytes",end=" | ")
    print("")




