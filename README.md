# Unsupervised-Learning-Clustering2

## EM 알고리즘
EM알고리즘을 사용하여 가우시안 혼합모델을 데이터에 피팅
### *EM-algorithm.py*
### Step 0: 변수의 준비 및 초기화
pi, mu, sigma, gamma에 초기값 부여<br/>

![image](https://user-images.githubusercontent.com/24853452/103482679-8b22c400-4e25-11eb-9e06-236aba52c3a4.png)

### Step 1: E step - gamma 갱신
입력 데이터에 대해 k에 따른 각 가우스 함수의 값을 계산하고 합이 1이 되도록 규격화 -> gamma 갱신<br/>

![image](https://user-images.githubusercontent.com/24853452/103482683-937aff00-4e25-11eb-9752-6f58ab3d5982.png)

### Step 2: M step - pi, mu, sigma 갱신
pi: 각 클러스터에 속하는 데이터 수 <br/>
mu: 각 클러스터에 대해 부담률의 가중치를 더한 데이터 평균<br/>

![image](https://user-images.githubusercontent.com/24853452/103482695-9a097680-4e25-11eb-8104-0249d1bcf832.png)

### *EM-algorithm-20times.py*
최종적으로 3개의 별에 나타난 중심 벡터는 각 클러스터의 중심 부근에 정착<br/>
각 데이터의 클러스터에 소속이 부담률이라는 확률로 표현, 클러스터의 경계 부근에서는 중간적인 색으로 데이터 표시
![image](https://user-images.githubusercontent.com/24853452/103482873-ca9de000-4e26-11eb-828e-f4bf789e4588.png)

## 가능도
K-means 기법의 경우 클러스터링의 장점을 평가하기 위해 왜곡척도(Distortion Measure)를 사용했지만, 가우시한 혼합 모델의 경우는 **가능도**를 사용

### *EM-algorithm-likelihood.py*
![image](https://user-images.githubusercontent.com/24853452/103483250-426d0a00-4e29-11eb-84f2-3282197a50d6.png)
