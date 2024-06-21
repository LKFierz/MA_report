import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

log_name = 'Monte_Carlo/Rough_Map_Complete_Randomization/not_coincident_WPs'



# Plot points
fig, ax = plt.subplots()
img = mpimg.imread('scripts/high_100m_arroyo_grid.png')  # Load background image
ax.imshow(img, extent=[-100, 100, -100, 100])  # Adjust extent as needed 
# Mission waypoint
ax.scatter(0,0, color='black')
ax.scatter(-11.563968813290693, 24.739966478190148, color='orange')
ax.scatter(-4.30025, 0.834371, color='yellow')
ax.scatter(-7.00025,0.884371, color='green')
plt.plot([-4.30025, -7.00025], [0.834371, 0.884371], linestyle='-', color='black')

# Customize plot
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
# plt.title('Demo Landing')
plt.grid(True)
plt.savefig(f"plots/landing_attempts.pdf")
plt.show()
