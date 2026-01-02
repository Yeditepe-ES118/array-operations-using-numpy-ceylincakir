import numpy as np

def stat():
    data = np.loadtxt("populations.txt", skiprows=1)

    hare = data[:, 1]

    min_year_hare = np.argmin(hare)

    lynx_avg = np.mean(data[:, 2])

    total = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, total))

    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data

