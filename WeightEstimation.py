import numpy as np
import pandas as pd


## Regression Data
W0 = [3417,2866,6614,9259,4244,10000,7020,3500,3300,3900,6173,6100,10000,6000,6000,6000,12675]
We = [2229,1880,3550,5445,2242,4990,3525,2306,2229,2050,3660,2995,4500,3900,3550,3600,7120]
log_W0 = np.log10(W0)
log_We = np.log10(We)
B, A = np.polyfit(log_We, log_W0,1)

def WeightEstimation():
    W_crew = 180
    W_payload = 2000
    W_guess = 5000
    error = 10^(-6)
    tol = 2*error
    W0 = W_guess
    while tol > error:
        empty_weight_frac = 10^(-A/B) * W0^(1/B-1)

        
        W0_new = (W_crew + W_payload)/(1-fuel_weight_ratio-empty_weight_frac)
        error = (W0_new - W0)/W0_new
        W0 = W0_new

