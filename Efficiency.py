import numpy as np
import sympy as sy
#P_f = 
#P_gt = 
#P_gb = 
#P_s1 = 
#P_e1 = 
#P_bat = 
#P_p1 = 

P_f, P_gt, P_gb, P_s1, P_e1, P_bat, P_p1 = sy.symbols("P_f P_gt P_gb P_s1 P_e1 P_bat P_p1", real=True)

n_gt = 0.43
n_gb = 0.98
n_p1 = 0.80
n_em1 = 0.95
n_pm = 0.95

phi = P_bat/(P_bat+P_f) # Supplied Power Ratio

P_p_over_W = 1/5

W = 1

A = np.array([ [-n_gt, 1, 0, 0, 0, 0, 0], 
               [0, -n_gb, -n_gb, 1, 0, 0 ,0],
               [0, 0, 0, -n_p1, 0, 0, 1],
               [0, 0, 1, 0, -n_em1, 0, 0],
               [0, 0, 0, 0, 1, -n_pm, 0],    
               [-phi, 0, 0, 0, 0, 1-phi, 0],
               [0, 0, 0, 0, 0, 0, 1]        ])

B = np.array([  [P_f/W],
                [P_gt/W],
                [P_gb/W],
                [P_s1/W],
                [P_e1/W],
                [P_bat/W],
                [P_p1/W],       ])

C = np.array([  [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [P_p_over_W]    ])

test = np.linalg.solve(A, C)
print(test)