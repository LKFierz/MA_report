import numpy as np

print(2.5**2 * 0.5/(0.1*275.42))
depth_error = 0.1
focal_length = 275.42
baseline = 0.092
disparity_error = 0.5
print(np.sqrt(depth_error * focal_length * baseline) / (disparity_error))