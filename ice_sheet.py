import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_cells = 10 # number of buckets
domain_width = 1e6 # meters
time_step = 100 # years
num_years = 20000 # years
flow_param = 1e4 # m horizontal / yr
snow_fall = 0.5 # m / y

steps = int(num_years / time_step)
cell_width = domain_width / num_cells

# initialize the arrays
elevations = np.zeros(num_cells + 2)
flows = np.zeros(num_cells + 1)

# get the plot started
fig, ax = plt.subplots(figsize=(5, 3))
ax.set_ylim(-10, 4000)
line = ax.plot(elevations, lw=2)[0]

def update(i):

    # update flows
    for idx in range(len(flows)):
        slope = (elevations[idx] - elevations[idx + 1]) / cell_width
        correction = (elevations[idx] + elevations[idx + 1]) / 2 / cell_width
        flows[idx] = slope * flow_param * correction

    # use flows to update elevations
    for idx in range(1, num_cells+1):
        elevations[idx] += (snow_fall + flows[idx-1] - flows[idx]) * time_step

    # update the plot
    ax.set_title(f'Years: {i * time_step}')
    line.set_ydata(elevations) # update line

anim = FuncAnimation(fig, update, interval=10, frames=steps)
 
plt.draw()
plt.show()