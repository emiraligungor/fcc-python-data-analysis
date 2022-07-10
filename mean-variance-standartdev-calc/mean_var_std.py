import numpy as np

def calculate(list):

    calculations = 0
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        a = np.array(list).reshape(3,3)
        flt_mean = np.mean(a).tolist()
        ax1_mean = np.mean(a, axis = 0).tolist()
        ax2_mean = np.mean(a, axis = 1).tolist()
        
        flt_var = np.var(a).tolist()
        ax1_var = np.var(a, axis = 0).tolist()
        ax2_var = np.var(a, axis = 1).tolist()
        
        flt_std = np.std(a).tolist()
        ax1_std = np.std(a, axis = 0).tolist()
        ax2_std = np.std(a, axis = 1).tolist()
        
        flt_max = np.max(a).tolist()
        ax1_max = np.max(a, axis = 0).tolist()
        ax2_max = np.max(a, axis = 1).tolist()
        
        flt_min = np.min(a).tolist()
        ax1_min = np.min(a, axis = 0).tolist()
        ax2_min = np.min(a, axis = 1).tolist()
        
        flt_sum = np.sum(a).tolist()
        ax1_sum = np.sum(a, axis = 0).tolist()
        ax2_sum = np.sum(a, axis = 1).tolist()

        calculations = {
            'mean': [ax1_mean, ax2_mean, flt_mean],
            'variance': [ax1_var, ax2_var, flt_var],
            'standard deviation': [ax1_std, ax2_std, flt_std],
            'max': [ax1_max, ax2_max, flt_max],
            'min': [ax1_min, ax2_min, flt_min],
            'sum': [ax1_sum, ax2_sum, flt_sum]
        }
            
    return calculations


