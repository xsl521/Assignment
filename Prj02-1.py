import numpy as np
import scipy.stats as ss
import time
import math

# Given Parameters are following:
S0=100.0
K=110.0
T=1
r=0.0475
sigma=0.20
n=4
t=np.linspace(0,T,n+1)

SIGMA=(sigma/n)*math.sqrt((n+1)*(2*n+1)/6)
R=0.5*SIGMA**2+0.5*(n+1)*(r-0.5*sigma**2)/n

def d1f(S0,K,T,R,SIGMA):
    d1=(math.log(S0/K)+(R+0.5*(SIGMA**2)*T))/(SIGMA*math.sqrt(T))
    return d1

def BSM_call_value(S0,K,T,R,SIGMA):
    d1=d1f(S0,K,T,R,SIGMA)
    d2=d1-(SIGMA*math.sqrt(T))
    call_value=S0*ss.norm.cdf(d1)-math.exp(-R*T)*K*ss.norm.cdf(d2)
    return call_value

def Asian_call_value():
    ASC0=math.exp((R-r)*T)*BSM_call_value(S0,K,T,R,SIGMA)
    print('The Asian call option value is: %.10f'%ASC0)

Asian_call_value()