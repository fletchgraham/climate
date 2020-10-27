import matplotlib.pyplot as plt
import numpy as np

time_step = 10 # years
water_depth = 4000 # meters
L = 1350 # Watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67e-8 # W/m2 K4

# d_heat_content/dt = L * (1 - albedo) / 4 - epsilon * sigma * T ** 4

# T [K] = heat_content [J/m2] / heat_capacity [J/m2 K]

# heat_content(t+1) = heat_content(t) + d_heat_content/dt * time_step

heat_capacity = water_depth * 4.2e6 # J/m2 K

time_years = [0]
temp_kelvin = [400]

heat_content = temp_kelvin[-1] * heat_capacity
heat_in = L * (1 - albedo) / 4
#heat_out = epsilon * sigma * temp_kelvin[-1] ** 4
for step in range(1,100):
    #print(f'{time_years[-1]}, {temp_kelvin[-1]}')
    time_years.append(time_years[-1] + time_step)
    flux = heat_in - epsilon * sigma * temp_kelvin[-1] ** 4
    heat_content += flux * time_step * 3.14e7 # to seconds
    temp_kelvin.append(heat_content / heat_capacity)
    if time_years[-1] == 100:
        print(epsilon * sigma * temp_kelvin[-1] ** 4)

plt.plot(time_years, temp_kelvin, marker='o')
plt.title('Temperature as a function of Time')
plt.ylabel('Temperature (Kelvin)')
plt.xlabel('Time (years)')
#plt.xlim(0, 2000)
plt.show()