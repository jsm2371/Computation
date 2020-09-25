import numpy as np



#### 데이터 생성 ####
# 생성되는 데이터는 기본적으로 타입 float64 (부분적으로 int32)

#### 단순 생성 #####
# np.array([[1,2,3],[3,4,5]])
# np.empty(size)       >>공배열 생성
##   self.fill(data)   >>공배열 전체 data값 채우기.
#                        특별한 경우 아니면 일괄생성 이용하는게 더 나음.

#### 일괄 생성 #####
# np.full(size, data)  >>위의 empty -> fill과 동일결과
# np.zeros(size)
# np.ones(size)
# np.random.rand(size) >> 0~1 사이의 난수열 생성

#### 행렬 생성 #####
# np.identity(dim)
# np.eye(dim,right_shift)
# np.diag(data,right_shift)

#### 증분수열 생성 #####
# np.arange(start, stop+differ, differ)
# np.linspace(start, stop, size)
# np.logspace(start_power, stop_power, size, base=10.0)

#### 격자 생성 #####
# np.meshgrid(x, y)
# np.fromfunction(function, size)

#### 호출 생성 ####
# np.loadtxt(file)
# np.genfromtxt >> loadtxt와 동일
# np.fromfile(file)   >> 하이퍼텍스팅

#### 저장 #####
# np.savetxt(file, data)



####### np.diag 보충 설명 #######
# np.diag(data,right_shift)
x= np.diag([2,3],-2)   #>>대각성분을 우측으로 -2칸 시프트
print(x)
#>> x= [[0 0 0 0]
#       [0 0 0 0]
#       [2 0 0 0]
#       [0 3 0 0]]


####### np.arange 보충 설명 #######
# np.arange(start, stop+differ, differ)
x=np.arange(0, 9+1, 1)
print(x)
#>> x = [0 1 2 3 4 5 6 7 8 9]
# ※주의. stop부분에 입력해야하는 값이 stop이 아니라 stop+differ이다.
#         즉, 실제 위의 선언은 np.arange(0, 10, 1) 가 된 것.


####### np.logspace 보충 설명 #######
# np.logspace(start_power, stop_power, size, base=10.0)
# power가 linspace처럼 할당되며, base^power를 수열로 리턴한다.
x=np.logspace(0,2,10)
print(x)
#>> [  1.           1.66810054   2.7825594    4.64158883   7.74263683
#     12.91549665  21.5443469   35.93813664  59.94842503 100.        ]
# 10^0부터 10^2까지의 로그 수열을 생성한 결과이다.


####### np.meshgrid 보충 설명 #######
# np.meshgrid(x, y)
# 좌표격자를 반환하며, X선, Y후 형식으로 좌표할당이 된다.
x=np.array([1,2,3])
y=np.array([0,2,4])
X,Y=np.meshgrid(x,y)
print(X)
print(Y)
#>>X=[[1 2 3]
#     [1 2 3]
#     [1 2 3]]
#>>Y=[[0 0 0]
#     [2 2 2]
#     [4 4 4]]


####### np.fromfunction 보충 설명 #######
# np.fromfunction(function, size)
# 좌표를 함수값으로 반환한 배열을 생성한다.
f = lambda x, y : x+10*y
A = np.fromfunction(f, (3,3))
print(A)
#>>A=[[ 0. 10. 20.]
#     [ 1. 11. 21.]
#     [ 2. 12. 22.]]


####### np.loadtxt 보충 설명 #######
# np.loadtxt(file, dtype, delimiter=None, skiprows=0, usecols=None)
# 텍스트 파일로부터 값을 배열로 읽어온다.
# 데이터는 반드시 행렬형이어야 함.
# delimiter : 구분기호를 토큰 삼아 구별할 수 있다. (콤마 생략 가능)
# skiprows : 특정 행을 생략할 수 있다. (코맨트 생략 가능)
# usecols : 특정 열만 출력할 수 있다. (데이터 필드 구별지정가능)
txt=np.loadtxt('chap1_2_1.test.txt')
print(txt)


####### np.savetxt 보충 설명 #######
# np.savetxt(file, data, fmt='%.18e', delimiter=' ', newline='\\n', header='',
#            encoding=None)
# 지정된 배열을 txt로 저장한다.
# 포맷/구분자/헤더/인코딩이 옵션
# header : 저장되는 값의 첫행에 코멘트를 남길 수 있다.
# encoding : 언어 인코딩 형식을 지정할 수 있다. 
txt=txt+1
np.savetxt('chap1_2_2.test.txt', txt, fmt='%3d', delimiter='\t', header='test')
# 포맷의 경우 %숫자+형식 : 숫자:자릿수  형식d:int  형식e:float(기본)
#         예) %3d  인 경우 자릿수 3칸이 할당된 int로 저장
# 구분자의 경우 \n:enter \t:tab  보통 여기에 콤마같은걸 많이 쓴다.


#### 부록. np.fromfile 보충 설명 ######
image=np.fromfile('chap1_2_3.test_Lena.png', dtype=np.uint8)
print(image)
#>> [137  80  78 ...  66  96 130]
# 참고로 137, 80, 78 (십진수)에 대응하는 ASCII 코드는 PNG 이다.
# 이 말은 즉, 위 출력문은 데이터를 그대로 하이퍼텍스팅 한다는 의미이다.
#### ※ 나중에 파일구조 공부할 때 이걸 직접 이용하면 된다.


