import numpy as np
from scipy import stats

arr = np.array([1,2,3,2,2,4,5,6,3,4,5,1,6,7])

# MEAN CALCULATION
mean_value = np.mean(arr)
print(mean_value)

# MEDIAN CALCULATION
median_value = np.median(arr)
print(median_value)

# MODE CALCULATION
mode_value = stats.mode(arr)
print(mode_value)

# VARRIENCE CALCULATION
varrience_value = np.var(arr)
print(varrience_value)

# STANDAR DEVIATION CALCULATION
standard_deviation_value = np.std(arr)
print(standard_deviation_value)
