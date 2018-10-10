import numpy as np
import scipy.stats as ss
import math
import pandas as pd
from scipy import optimize
import datetime as dt

def d1f(S0,K,T,r,sigma):    # define a fuction to compute the factor: d1
    d1=(math.log(S0/K)+(r+0.5*(sigma**2)*T))/(sigma*math.sqrt(T))
    return d1

def BSM_call_value(S0,K,T,r,sigma):  # define a funtion to compute BSM call option price
    d1=d1f(S0,K,T,r,sigma)
    d2=d1-(sigma*math.sqrt(T))
    call_value=S0*ss.norm.cdf(d1)-math.exp(-r*T)*K*ss.norm.cdf(d2)
    return call_value

def Dif():                      # define a funtion to compute the difference of theoretical price of BSM call price and given market price
    C0=BSM_call_value(S0,K,T,r,sigma)
    Difference=C0-MP
    return Difference

def IVolBsm(S0, K, T, r, MP):   # define a funtion to compute implied volitility
    InitVol = .3
    error = lambda sigma: (BSM_call_value(S0, K, T, r, sigma) - MP)**2
    opt = optimize.fmin(error, InitVol)
    return opt[0]

#Given parameters are following:
S0=290.68                     # Current stock price
K=288                         # Strike price
Today=dt.date(2018,9,27)      # Today's date
Maturity=dt.date(2018,12,31)  # Maturity date
T=(Maturity-Today).days/365   # Time period = T
r=0.02                        # Risk-free rate
sigma=0.3                     # Volatility
MP=9.28                       # Market call price

BSM_call_value(S0,K,T,r,sigma) # output the BSM call price 

Dif() # output the difference of theoretical BSM call price and market price

IVolBsm(S0,K,T,r,MP) # output the implied volatility



