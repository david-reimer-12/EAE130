import numpy as np
import pandas as pd
import math 
## Regression Data Ag Aircraft
def AgRegressionData():
    global A, B
    W0 = [3417,2866,6614,9259,4244,10000,7020,3500,3300,3900,6173,6100,10000,6000,6000,6000,12675]
    We = [2229,1880,3550,5445,2242,4990,3525,2306,2229,2050,3660,2995,4500,3900,3550,3600,7120]
    log_W0 = np.log10(W0)
    log_We = np.log10(We)
    B, A = np.polyfit(log_We, log_W0,1)

## Regression Data Twin Engine Aircraft
def TwinRegressionData():
    global A, B
    W0 = [3900, 5100, 6775, 9630, 5150, 5990,6850,6750,7450,8200,6500,7000,5500,3800,3800,8700,3050,2183,9480,10325,7350,2900]
    We = [2466,3236,4423,5765,3305,3948,4077,4368,4668,4915,4003,4221,3737,2354,2430,4910,2100,1322,5732,6629,4100,1610]
    log_W0 = np.log10(W0)
    log_We = np.log10(We)
    B, A = np.polyfit(log_We, log_W0,1)

def WeightEstimation():
    W_crew = 180 #lbs
    W_payload = 2000 #lbs
    Range = 3.706*10**(6) #ft
    Endurance = 28800 #seconds
    V_inf = 290.303 #ft/s
    SFC = 7.06*10**(-9) #1/ft
    prop_eff = 0.8
    LD_ratio = 11.8
    W_guess = 5000
    cruise = math.exp(-(Range*SFC)/(prop_eff*LD_ratio))
    loiter = math.exp((-Endurance*V_inf*SFC)/(prop_eff*LD_ratio))
    fuel_weight_ratio = 1 - 0.996*0.995*0.996*0.998*0.999*0.998*cruise*loiter
    tol = 10**(-6)
    error = 2*tol
    W0 = W_guess

    while tol < error:
        empty_weight_frac = 10**(-A/B) * W0 **(1/B-1)
        W0_new = (W_crew + W_payload)/(1-1.06*fuel_weight_ratio-empty_weight_frac) + 400
        error = abs((W0_new - W0)/W0_new)
        W0 = W0_new

        if tol > error:
            We = empty_weight_frac*W0
            print("TOGW")
            print(W0)
            print("Empty Weight:")
            print(We)

    

TwinRegressionData()
WeightEstimation()
print(" ")
AgRegressionData()
WeightEstimation()
