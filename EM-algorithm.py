import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):
	N,D=x.shape
	c1=1/(2*np.pi)**(D/2)
	c2=1/(np.linalg.det(sigma)**(1/2))
	inv_sigma=np.linalg.inv(sigma)
	c3=x-mu
	c4=np.dot(c3, inv_sigma)
	c5=np.zeros(N)
	for d in range(D):
		c5=c5+c4[:,d]*c3[:,d]
	p=c1*c2*np.exp(-c5/2)
	return p

def mixgauss(x,pi,mu,sigma):
	N,D=x.shape
	K=len(pi)
	p=np.zeros(N)
	for k in range(K):
		p=p+pi[k]*gauss(x,mu[k,:], sigma[k,:,:])
	return p

def show_contour_mixgauss(pi, mu, sigma):
	xn=40
	x0=np.linspace(X_range0[0], X_range0[1], xn)
	x1=np.linspace(X_range1[0], X_range1[1], xn)
	xx0,xx1=np.meshgrid(x0,x1)
	x=np.c_[np.reshape(xx0,(xn*xn,1)), np.reshape(xx1, (xn*xn,1))]
	f=mixgauss(x,pi, mu, sigma)
	f=f.reshape(xn,xn)
	cont=plt.contour(xx0,xx1,f,10,colors='gray')
	cont.clabel(fmt='%3.2f', fontsize=8)


def show_mixgauss_prm(x, gamma, pi, mu, sigma):
	N,D=x.shape
	show_contour_mixgauss(pi,mu,sigma)
	for n in range(N):
		col=gamma[n,0]*X_col[0]+gamma[n,1]*X_col[1]+gamma[n,2]*X_col[2]
		plt.plot(x[n,0], x[n,1], 'o', color=tuple(col), markeredgecolor='black', markersize=6, alpha=0.5)
	for k in range(K):
		plt.plot(mu[k,0], mu[k,1], marker='*', markerfacecolor=tuple(X_col[k]), markersize=15, markeredgecolor='k', markeredgewidth=1)
	plt.grid(True)

def e_step_mixgauss(x,pi, mu, sigma):
	N,D=x.shape
	K=len(pi)
	y=np.zeros((N,K))
	for k in range(K):
		y[:,k]=gauss(x,mu[k,:], sigma[k,:,:])
	gamma=np.zeros((N,K))
	for n in range(N):
		wk=np.zeros(K)
		for k in range(K):
			wk[k]=pi[k]*y[n,k]
		gamma[n,:]=wk/np.sum(wk)
	return gamma

def m_step_mixgauss(x,gamma):
	N,D=x.shape
	N,K=gamma.shape
	pi=np.sum(gamma,axis=0)/N
	mu=np.zeros((K,D))
	for k in range(K):
		for d in range(D):
			mu[k,d]=np.dot(gamma[:,k],x[:,d])/np.sum(gamma[:,k])
	
	sigma=np.zeros((K,D,D))
	for k in range(K):
		for n in range(N):
			wk=x-mu[k]
			wk=wk[n,:,np.newaxis]
			sigma[k]=sigma[k]+gamma[n,k]*np.dot(wk,wk.T)
		sigma[k]=sigma[k]/np.sum(gamma[:,k])
	return pi, mu, sigma

N=100
K=3
outfile=np.load('data_ch9.npz')

X=outfile['X']
X_range0=outfile['X_range0']
X_range1=outfile['X_range1']
X_col=np.array([[0.4,0.6,0.95],[1,1,1],[0,0,0]])

pi=np.array([0.33,0.33,0.34])
mu=np.array([[-2,1],[-2,0],[-2,-1]])
sigma=np.array([[[1,0],[0,1]],[[1,0],[0,1]],[[1,0],[0,1]]])
gamma=np.c_[np.ones((N,1)), np.zeros((N,2))]

plt.figure(1,figsize=(4,4))
show_mixgauss_prm(X,gamma,pi,mu,sigma)

plt.figure(2,figsize=(4,4))
gamma=e_step_mixgauss(X,pi,mu,sigma)
show_mixgauss_prm(X,gamma,pi,mu,sigma)

plt.figure(3,figsize=(4,4))
pi,mu,sigma=m_step_mixgauss(X,gamma)
show_mixgauss_prm(X,gamma,pi,mu,sigma)
plt.show()

