"""A simplified fluid sim to wrap my brain around the shallow water assignment"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# arrays to keep track of water height

nrows = 20
ncols = 20
damp = .8

buffer2 = np.zeros((nrows,ncols))
buffer1 = np.zeros((nrows,ncols))

# get the plot started
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title(f'Fluid')

def setup():
    """Runs at the beginning"""
    buffer2[5,5] = .9


def draw(frame):
    """Update the plot"""
    for i in range(1, nrows-1):
        for j in range(1, ncols-1):
            buffer2[i,j] = (
                (
                    buffer1[i-1,j] +
                    buffer1[i+1,j] + 
                    buffer1[i,j+1] + 
                    buffer1[i,j-1]
                ) / 2 - buffer2[i][j]
            )
            buffer2[i,j] *= damp
    
    ax.imshow(buffer2, vmin=-1, vmax=1)

    #swap
    
    #temp = buffer2[:,:]
    #buffer2[:,:] = buffer1[:,:]
    #buffer1[:,:] = temp[:,:]
    
    buffer1[:,:], buffer2[:,:] = buffer2[:,:], buffer1[:,:]

anim = FuncAnimation(
    fig,
    draw, # defined above
    init_func=setup, # defined above
    interval=1, # this basically controls the speed of the playback
    frames=200
)
 
#plt.draw()
#plt.tight_layout()
plt.show()