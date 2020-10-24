import numpy as np
import matplotlib.pyplot as plt 

# copy data from the readings

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

# The lines of best fit will look like this:
# ice_lat = m1 * T + b1
# albedo = m2 * T + b2

# use numpy's polyfit to do least squares regression on
# first degree polynomial

m1, b1 = np.polyfit(planet_temp_data, ice_lat_data, 1)
m2, b2 = np.polyfit(planet_temp_data, albedo_data, 1)

# now we have the slope and y-intercept to use in our
# linear functions:

def get_ice_lat(temperature):
    """Return the latitude to which ice can form for the given 
    planetary temperature.
    """
    return m1 * temperature + b1 

def get_albedo(temperature):
    """Return the planetary albedo due to ice for the given 
    planetary temperature.
    """
    return m2 * temperature + b2

def make_plots():
    """Create a dashboard of plots for visualizing the provided
    data and the resulting model
    """

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8,8))

    ax1.plot(planet_temp_data, ice_lat_data, 'o', label='data')
    ax1.plot(planet_temp_data, get_ice_lat(planet_temp_data), label='best fit')

    ax1.set_title('Ice Latitude')
    ax1.set_xlabel('Temp (K)')
    ax1.set_ylabel('Lat')
    ax1.set_axisbelow(True)
    ax1.grid(linestyle='--')
    ax1.legend()

    ax2.plot(planet_temp_data, albedo_data, 'o', label='data')
    ax2.plot(planet_temp_data, get_albedo(planet_temp_data), label='best fit')

    ax2.set_title('Planetary Albedo')
    ax2.set_xlabel('Temp (K)')
    ax2.set_ylabel('Albedo')
    ax2.set_axisbelow(True)
    ax2.grid(linestyle='--')
    ax2.legend()

    plt.show()

def auto_grader():
    """An alternate function to run if the script is being 
    submitted to the coursera auto grader.
    """
    pass


if __name__ == '__main__':
    # Uncomment the appropriate function below depending 
    # on the use of the script.
    
    make_plots()
    # auto_grader()