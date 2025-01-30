import numpy as np
import pandas as pd
import math 
## Regression Data
W0 = [3417,2866,6614,9259,4244,10000,7020,3500,3300,3900,6173,6100,10000,6000,6000,6000,12675]
We = [2229,1880,3550,5445,2242,4990,3525,2306,2229,2050,3660,2995,4500,3900,3550,3600,7120]
log_W0 = np.log10(W0)
log_We = np.log10(We)
B, A = np.polyfit(log_We, log_W0,1)

def WeightEstimation():
    W_crew = 180 #lbs
    W_payload = 2000 #lbs
    Range = 3220000 #ft
    Endurance = 28800 #seconds
    V_inf = 337.562 #ft/s
    SFC = 0.25*32 #(lbm/hr)/lbf
    prop_eff = 0.8
    LD_ratio = 12
    W_guess = 5000
    cruise = math.exp(-(Range*SFC)/(prop_eff*LD_ratio))
    loiter = math.exp((-Endurance*V_inf*SFC)/(prop_eff*LD_ratio))
    fuel_weight_ratio = 1 - 0.996*0.995*0.996*0.998*0.999*0.998*cruise*loiter
    tol = 10**(-6)
    error = 2*tol
    W0 = W_guess
    while tol < error:
        empty_weight_frac = 10**(-A/B) * W0**(1/B-1)
        W0_new = (W_crew + W_payload)/(1-fuel_weight_ratio-empty_weight_frac)
        error = abs((W0_new - W0)/W0_new)
        W0 = W0_new
        print(W0)


WeightEstimation()
