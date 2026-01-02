import numpy as np 

def stat() :
    data = np.loadtxt("populations.txt")
    
    hare = data[:, 1]
    
    min_year_hare = data[np.argmin(hare), 0]
    
    lynx_avg = np.mean(data[:, 2])
    
    total_population = np.sum(data[:, 1:], axis= 1)
    new_data = np.column_stack((data, total_population))
    
    new_data[new_data[:, 3] < 40000, 3 ] = 0
    
    return data, hare, min_year_hare, lynx_avg, new_data
