import numpy as np

sigma = 5.67e-8 # W/m2 K4
albedo = .65

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

# use numpy's polyfit to do least squares regression on
# first degree polynomial

ice_slope, ice_intercept = np.polyfit(planet_temp_data, ice_lat_data, 1)
albedo_slope, albedo_intercept = np.polyfit(planet_temp_data, albedo_data, 1)

def run_model(L, albedo, iterations):
    """Return Temperature and albedo

    these doctests fail because they're too precise but I could see the script
    will work...

    >>> run_model(1280, .15, 100)
    255.45242794389384 0.24547572056106137

    >>> run_model(1200, .65, 100)
    207.4443257628261 0.65
    """
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

    print(str(T) + ' ' + str(albedo))

L, albedo, iterations = input('').split()
L, albedo, iterations = [float(L), float(albedo), int(iterations)]

run_model(L, albedo, iterations)


