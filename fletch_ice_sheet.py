# 1-Dimensional Ice Sheet Model
# By Fletcher Graham
# Python 3.7

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# parameters:
num_cells = 10 # number of cells
domain_width = 1e6 # meters
time_step = 100 # years
num_years = 20000 # years (per the prompt specs)
flow_param = 1e4 # m horizontal / yr
snow_fall = 0.5 # m / y
steps = int(num_years / time_step)
cell_width = domain_width / num_cells

# initialize the arrays
elevations = np.zeros(num_cells + 2)
flows = np.zeros(num_cells + 1)

# get the plot started
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(5, 3))
ax.set_ylim(-10, 4000)
ax.set_title(f'Years: ---')
ax.set_ylabel('Elevation (m)')
ax.set_xlabel('Cell Index')
line = ax.plot(elevations, lw=2)[0]

def update(i):
    '''Insead a loop, I define this function,
    which matplotlib will use to update the arrays and then the plot
    '''
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

    # print per the prompt spec
    print(f'Years: {i * time_step} | Elevation at center: {elevations[5]}')

# this function gets used when the animation loops
def reset_arrays():
    '''Reset the elevations and flows.
    '''
    elevations[:] = 0
    flows[:] = 0

# tell matplotlib to animate
anim = FuncAnimation(
    fig,
    update, # defined above
    init_func=reset_arrays, # defined above
    interval=50, # this basically controls the speed of the playback
    frames=steps
)
 
plt.draw()
plt.tight_layout()
plt.show()