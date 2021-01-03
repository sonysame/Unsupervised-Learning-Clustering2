# Unsupervised-Learning-Clustering2

EM알고리즘을 사용하여 가우시안 혼합모델을 데이터에 피팅

### Step 0: 변수의 준비 및 초기화
pi, mu, sigma, gamma에 초기값 부여

### Step 1: E step - gamma 갱신
입력 데이터에 대해 k에 따른 각 가우스 함수의 값을 계산하고 합이 1이 되도록 규격화 -> gamma 갱신
