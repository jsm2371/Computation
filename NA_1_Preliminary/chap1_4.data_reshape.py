import numpy as np



#### 데이터 재배열 ####
# 생성한 데이터의 형태를 변형하는 방법.
# 데이터 처리를 위해 데이터 재배열을 해야하는 경우가 빈번하다.
# 따라서 매우 중요한 메소드.

#### 단순 재배열 ####
# np.reshape(data, size)
# self.reshape(size)
# np.resize(data, size)  >> reshape와 다르게 원소수가 달라도 재배열한다.

#### 1차원 재배열 ####
# self.flatten()   >> dim=1인 재배열 언뷰를 반환.
# self.ravel()     >> dim=1인 재배열 뷰를 반환. (언뷰를 반환하는 경우도 있음)

#### 축 확장 ####
# np.expand_dims(data, axis=0)
# [np.newaxis]       >> 속성

#### 축 제거 ####
# np.squeeze(data)   >> 길이 1인 축을 제거.

#### 행렬 전치 ####
# np.transpose(data)
# self.T


#### 1차원 재배열 설명 #####
data = np.array([[1,2],[3,4]])

### 1차원 언뷰 반환 ###
data_a=data.flatten()
data_a[1]=1
print(">>> 1차원 언뷰 <<<")
print(data)
#>> array([[1, 2],
#          [3, 4]])
print("")

### 1차원 뷰 반환 ###
data_b=data.ravel()
data_b[1]=1
print(">>> 1차원 뷰 <<<")
print(data)
#>> array([[1, 1],
#          [3, 4]])
print("")



#### 축 확장 설명 ####
data = np.arange(0,5)

### X축으로 확장 ###
row = np.expand_dims(data,axis=0)
row = data[np.newaxis, :]
print(">>> X축 확장 <<<")
print(row)
print(row.shape)
print("")

### Y축으로 확장 ###
col = np.expand_dims(data,axis=1)
col = data[:, np.newaxis]
print(">>> Y축 확장 <<<")
print(col)
print(col.shape)
print("")

### 3D축 확장 ###
TD = data[np.newaxis, :, np.newaxis]
print(">>> X,Z축 확장 <<<")
print(TD)
print(TD.shape)
print("")





