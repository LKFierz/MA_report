import numpy as np
import matplotlib.pyplot as plt

# Fixed parameters
baseline = 0.092  # meters
focal_length = 275.42  # pixels
disparity_error = 0.5  # pixels

def calculate_altitude(depth_error, baseline, focal_length, disparity_error):
    altitude = np.sqrt(depth_error * focal_length * baseline) / (disparity_error)
    return altitude

# Generate depth error values
depth_errors = np.linspace(0, 1, 1000)  # Depth errors from 0 to 1 meters

# Calculate altitudes for each depth error
altitudes = [calculate_altitude(error, baseline, focal_length, disparity_error) for error in depth_errors]

# Find the index of the depth error value closest to 0.1 meters
target_depth_error = 0.1
target_altitude = calculate_altitude(target_depth_error,baseline, focal_length, disparity_error)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(depth_errors, altitudes, label='Altitude vs. Depth Error')
plt.xlabel('Depth Error [m]', fontsize=14)
plt.ylabel('Altitude [m]', fontsize=14)
plt.title('Flight altitudes possible for different depth errors with b=9.2cm, f=256px, \u0394d=0.5', fontsize=14)
plt.legend()
plt.grid(True)

# Add annotation at the depth error value of 0.1 meters
plt.annotate(f'Depth Error of {target_depth_error}m at {np.round(target_altitude,3)}m Altitude',
             xy=(target_depth_error, target_altitude),
             xytext=(target_depth_error + 0.6, target_altitude + 1.8),
             arrowprops=dict(facecolor='black', shrink=0.05, linewidth=0.1),
             fontsize=12,
             ha='center')

# Add vertical line at the annotated point
plt.axvline(x=target_depth_error, color='black', linestyle='--', linewidth=1)

# Add horizontal line at the annotated point
plt.axhline(y=target_altitude, color='black', linestyle='--', linewidth=1)

# Show the plot
plt.savefig("C:/Users/fierz/Documents/LF/studium/Master/master_thesis/RSL/Report/plots/stereo_limit.pdf")
plt.show()
