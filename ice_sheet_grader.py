import numpy as np

num_cells = 10 # number of buckets
domain_width = 1e6 # meters
time_step = 100 # years
num_years = float(input(''))
flow_param = 1e4 # m horizontal / yr
snow_fall = 0.5 # m / y

steps = int(num_years / time_step)
cell_width = domain_width / num_cells

# initialize the arrays
elevations = np.zeros(num_cells + 2)
flows = np.zeros(num_cells + 1)

def update(i):
    # update flows
    for idx in range(len(flows)):
        slope = (elevations[idx] - elevations[idx + 1]) / cell_width
        correction = (elevations[idx] + elevations[idx + 1]) / 2 / cell_width
        flows[idx] = slope * flow_param * correction

    # use flows to update elevations
    for idx in range(1, num_cells+1):
        elevations[idx] += (snow_fall + flows[idx-1] - flows[idx]) * time_step

for i in range(steps):
    update(i)
    
print(elevations[5])