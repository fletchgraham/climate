"""Snowball Earth Model

By Fletcher Graham

This script creates a dashboard of plots showing the 
data and resulting model for the snowball earth phenomenon.

Python 3.7
"""
import numpy as np
import matplotlib.pyplot as plt

# Copy data from the readings:

planet_temp_data = np.array([
    265.0,
    255.0,
    245.0,
    235.0,
    225.0,
    215.0
])

ice_lat_data = np.array([
    75.0,
    60.0,
    45.0,
    30.0,
    15.0,
    0.0
])

albedo_data = np.array([
    0.15,
    0.25,
    0.35,
    0.45,
    0.55,
    0.65
])

# Use numpy's polyfit to do least squares regression on
# the provided data:

ice_slope, ice_intercept = np.polyfit(
    planet_temp_data,
    ice_lat_data,
    1 # first degree polynomial
)

albedo_slope, albedo_intercept = np.polyfit(
    planet_temp_data,
    albedo_data,
    1
)

# Initialize some values:
iterations = 100
L_low = 1200 # Watts/m2
L_high = 1390
L_step = 1
albedo = 0.65
sigma = 5.67e-8 # W/m2 K4 (a constant)

# for making plot requested by the prompt
all_iters_down = []
all_temps_down = []

# for showing the hysteresis
solar_constants_up = []
final_temps_up = []
solar_constants_down = []
final_temps_down = []

#### THE LOOPS ####

for L in range(L_low, L_high, L_step):
    for iteration in range(iterations):
        # calculate the temp based on the current L and albedo
        T = (L * (1 - albedo) / (4 * sigma)) ** .25

        # update albedo based on the temperature
        albedo = albedo_slope * T + albedo_intercept
        albedo = min(albedo, .65)
        albedo = max(albedo, .15)

        # update ice latitude based on temperature
        ice_lat = ice_slope * T + ice_intercept
        ice_lat = min(ice_lat, 90)
        ice_lat = max(ice_lat, 0)

    solar_constants_up.append(L)
    final_temps_up.append(T)

for L in range(L_high, L_low, -L_step):
    for iteration in range(iterations):
        # calculate the temp based on the current L and albedo
        T = (L * (1 - albedo) / (4 * sigma)) ** .25

        # update albedo based on the temperature
        albedo = albedo_slope * T + albedo_intercept
        albedo = min(albedo, .65)
        albedo = max(albedo, .15)

        # update ice latitude based on temperature
        ice_lat = ice_slope * T + ice_intercept
        ice_lat = min(ice_lat, 90)
        ice_lat = max(ice_lat, 0)

        all_iters_down.append(iteration)
        all_temps_down.append(T)

    all_iters_down.append(np.nan) # this makes each line separate
    all_temps_down.append(np.nan)

    solar_constants_down.append(L)
    final_temps_down.append(T)

# The rest of the code is mostly about drawing the plots:

def make_plots():
    """Create a dashboard of plots for visualizing the provided
    data and the resulting model.
    """
    plt.style.use('seaborn')
    gridsize = (2, 4)
    fig = plt.figure(figsize=(12,6))

    ax1 = plt.subplot2grid(gridsize, (0,0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (0,2), colspan=2)
    ax3 = plt.subplot2grid(gridsize, (1,2))
    ax4 = plt.subplot2grid(gridsize, (1,3))

    # PLOT ONE: Temp vs Iterations
    ax1.plot(all_iters_down, all_temps_down)

    ax1.set_title(
        'Temperature vs Iterations '
        'for Descending Values of L'
        )
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Temp (K)')

    # PLOT TWO: Converged Temp vs Solar Constants
    ax2.plot(solar_constants_up, final_temps_up, label='Up')
    ax2.plot(solar_constants_down, final_temps_down, label='Down')

    ax2.set_title('Hysteresis')
    ax2.set_xlabel('Solar Constant')
    ax2.set_ylabel('Final Temp')
    ax2.legend()

    # PLOT THREE: Ice Latitude Regression
    ice_best_fit = ice_slope * planet_temp_data + ice_intercept
    ax3.plot(planet_temp_data, ice_lat_data, 'o', label='data')
    ax3.plot(planet_temp_data, ice_best_fit, label='best fit')

    ax3.set_title('Ice Latitude')
    ax3.set_xlabel('Temp (K)')
    ax3.set_ylabel('Lat')
    ax3.legend()

    # PLOT FOUR: Albedo Regression
    albedo_best_fit = albedo_slope * planet_temp_data + albedo_intercept
    ax4.plot(planet_temp_data, albedo_data, 'o', label='data')
    ax4.plot(planet_temp_data, albedo_best_fit, label='best fit')

    ax4.set_title('Planetary Albedo')
    ax4.set_xlabel('Temp (K)')
    ax4.set_ylabel('Albedo')
    ax4.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':

    make_plots()



