def ODEpy(model, xinit, yinit, zinit, constants, timesteps, dt):
    """
    this function calculates the trajectory in phase space for a set of ordinary differential equations
    ---------------------------------------------------------------------------------------------------
    model [function]: function that returns dx/dt, dy/dt, dz/dt for a set of differential equations
    if no z dependency, specify zinit as None
    model arguments should require initial conditions in x, y, and optionaly z dimensions; and constants
    example function: 
    def model_name(X, Y, Z, constants):
        RHO, SIGMA, BETA = constants
        dx = SIGMA * (Y - X)
        dy = X * (RHO - Z) - Y
        dz = X * Y - BETA * Z
        return [dx, dy, dz]
    
    xinit, yinit, zinit [float]: initial x, y, z positions 
    
    constants [tuple]: tuple which stores all necessary constant values for evaluating ODEs
    example: constants = (28., 10., 8./3.)
    
    timesteps [integer]: number of iterations
    
    dt [float]: size of each timestep
    ----------------------------------
    OUTPUT [numpy array]: ouputs either 2 or 3 numpy position arrays for x, y, and z dimensions
    """
    
    import numpy as np # computational
    
    # ensure timestep is integer
    timesteps = int(timesteps)
    
    # if system of ODEs have 3 dimensions
    if zinit is not None:  
        # create empty array for storing position values
        xarr, yarr, zarr = np.zeros(timesteps), np.zeros(timesteps), np.zeros(timesteps)
        # assign inital values to zeroth entry
        (xarr[0], yarr[0], zarr[0]) = (xinit, yinit, zinit)
        # loop through each timestep
        for i in range(timesteps - 1):
            # calculate dx, dy, dz
            dX, dY, dZ = model(xarr[i], yarr[i], zarr[i], constants)
            # store dx, dy, dz into arrays
            xarr[i + 1] = xarr[i] + dX*dt
            yarr[i + 1] = yarr[i] + dY*dt
            zarr[i + 1] = zarr[i] + dZ*dt

        return xarr, yarr, zarr
    
    # if system of ODEs have 2 dimensions
    else:
        # create empty array for storing position values
        xarr, yarr = np.zeros(timesteps), np.zeros(timesteps)
        # assign inital values to zeroth entry
        (xarr[0], yarr[0]) = (xinit, yinit)
        # loop through each timestep
        for i in range(timesteps - 1):
            # calculate dx, dy
            dX, dY = model(xarr[i], yarr[i], constants)
            # store dx, dy, dz into arrays
            xarr[i + 1] = xarr[i] + dX*dt
            yarr[i + 1] = yarr[i] + dY*dt

        return xarr, yarr