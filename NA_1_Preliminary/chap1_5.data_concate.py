import numpy as np



#### 데이터 결합 ####
# 생성된 데이터들을 하나로 결합하는 방법.
# 또는 생성된 데이터에 추가 데이터를 결합시키는 방법.
# 물론 데이터의 일부를 제거하는 방법도 언급할 것이다.

#### 직접 결합 ####
# np.vstack((data))   >> 횡단 결합 배열 반환
# np.hstack((data))   >> 종단 결합 배열 반환
# np.concatenate((data), axis=0) >> 단순 결합
# np.concatenate((data), axis=1) >> 종단 결합

#### 생성 결합 ####
# self.append(data)
# self.insert(index, data)
# self.delete(index)



#### 직접 결합 ####
data = np.arange(5)
print(data)
print("")

### 횡단 결합 배열 ###
print(">>> 횡단 결합 <<<")
vdata = np.vstack((data, data, data))
print(vdata)
print("")

### 종단 결합 배열 ###
print(">>> 종단 결합(NG) <<<")
data = np.arange(5)
hdata = np.hstack((data, data, data))
hdata = np.concatenate((data, data, data), axis=0)
print(hdata)
print("")
# ※주의. 열벡터들을 횡측으로 결합하기 위한 수단이다.
print(">>> 종단 결합(올바른 법) <<<")
data_col = data[:, np.newaxis]
hdata = np.hstack((data_col, data_col, data_col))
hdata = np.concatenate((data_col, data_col, data_col), axis=1)
print(hdata)

