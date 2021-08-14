%matplotlib inline

import numpy as np
import matplotlib.pylab as plt

def step_function(x):                       #계단 함수(활성화 함수) 구현 numpy의 array를 인자로 받음
    return np.array(x > 0, dtype=np.int)    #numpy.array중 0보다 큰 원소를 리턴해줌 dtype은 리턴해줄 타입을 의미

x = np.arange(-5.0, 5.0, 0.1)               #numpy의 arrange(a, b, c) = 구간 [a, b)의 수 중에 c의 단위만큼 numpy 배열로 return해줌
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)                         #그래프의 y축 시작과 끝 구간 설정
plt.show()
