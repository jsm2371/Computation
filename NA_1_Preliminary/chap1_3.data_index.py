import numpy as np



#### 데이터 인덱싱 ####
# 데이터의 일부를 직접 호출할 수 있다.
# 심지어 일부를 참조시켜 활용, 변환 하는 것 또한 가능하다.
# 인덱스 값은 반드시 정수만으로 취할수 있다.

#### 단순 인덱싱 #####
# array[index]  >>index = num , num , ... 으로 표현
#                 index 구성은 행 우선 열 차후 순서로 표현된다.
# array[-m]     >> +의 경우 0부터 시작, -의 경우 -1부터 시작하는 위치 참조.

#### 단순 슬라이싱 #####
# array[m:n]    >>슬라이싱 : 인덱스 m부터 n-1까지
#                 m의 경우 생략시 0이 고정, n의 경우 -1이 고정
# array[:]      >>슬라이싱 : 지정축 모든 원소

#### 점프 슬라이싱 #####
# array[m:n:p]  >>슬라이싱 : 인덱스 m부터 n-1까지 매 p번째 원소 선택
# array[::-1]   >> 위의 응용 - 배열을 역순으로 호출

#### 팬시 인덱싱 #####
# array[list]   >> 리스트에 속한 인덱스의 배열값들을 반환한다.
# array[array]  >> 위와 동일

#### 부울 인덱싱 #####
# array[logic]  >> 넘파이에서는 논리도 array로 반환한다.
#                  단, 1차원 배열을 출력한다.

#### 뷰(참조) #####
# A=np.array
# B=A[slice]
# 위와 같이 B가 정의된 경우, B를 변화시키면, A도 함께 변환된다.
# 왜냐하면 B는 A의 참조값이기 때문이다.
### b.base  >> A

#### 논뷰(복사) #####
# A=np.array
# B=np.copy(A)
# 위와 같이 B가 정의된 경우, B와 A는 독립적인 데이터이다.
### b.base  >> self



#### 실제 예제 #####
f= lambda x, y : x+10*y
A = np.fromfunction(f, (6,6), dtype=np.int)
print(">>> Normal Data <<<")
print(A)

#### 단순 슬라이싱 #####
print(">>> A[:,1] <<<")
print(A[:,1])
print(">>> A[1,:] <<<")
print(A[1,:])
print(">>> A[:3,:3] <<<")
print(A[:3,:3])
print(">>> A[3:,:3] <<<")
print(A[3:,:3])

#### 점프 슬라이싱 #####
print(">>> A[::2,::2] <<<")
print(A[::2,::2])
print(">>> A[1::2,1::3] <<<")
print(A[1::2,1::3])

#### 팬시 인덱싱 #####
print(">>> A[[0,2,4],] <<<")  # 콤마 생략해도 되긴 됨.
print(A[[0,2,4]],)

#### 부울 인덱싱 #####
print(">>> Logic Array <<<")  # 실제 원소들과 비교한다.
print(A > 3)      # 타입 : bool 로 출력된다.
print(A > 39)     
print(A[A > 39])  # 1차원 논뷰 배열 출력. 마찬가지 행선 열후 출력.





