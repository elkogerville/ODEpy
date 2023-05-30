def ODEattractor(model, xinit, yinit, zinit, constants, timesteps):
    """
    this function is useful for graphing certain systems such as the clifford attractor, or the pendulum 
    ----------------------------------------------------------------------------------------------------
    model [function]: choose one of the ODEpy functions or create your own
    model arguments should require initial conditions in x, y, and optionaly z dimensions; and constants
    example function: 
    -----------------------------------
    def model_name(X, Y, Z, constants):
        RHO, SIGMA, BETA = constants
        dx = SIGMA * (Y - X)
        dy = X * (RHO - Z) - Y
        dz = X * Y - BETA * Z
        return [dx, dy, dz]
    ------------------------------------------------------------------- 
    xinit/yiniy/zinit [float]: initial conditions in x, y, z directions
    ------------------------------------------------
    zinit = True: ALLOWS FOR 3D GRAPH OF 2D FUNCTION
    zinit = None: ALLOWS FOR 2D GRAPH
    ------------------------------------------------
    constants [tuple] = tuple which stores all necessary constant values for evaluating ODEs
    example: constants = (28., 10., 8./3.)
    
    timesteps [integer]: integration timescale
    """
    
    import numpy as np # computational
    # ensure timesteps is integer
    timesteps = int(timesteps)
    # 3D PLOTS
    if zinit is not None:
        # PLOT 2D GRAPH IN 3D SPACE
        if zinit is True:
            # initialize arrays for storing positions
            xarr, yarr, zarr = np.zeros((timesteps,1)), np.zeros((timesteps,1)), np.zeros((timesteps,1))
            # loop through each timestep
            for i in range(timesteps):
                # calculate position for given timestep
                xinit, yinit = model(xinit, yinit, constants)
                xarr[i] = xinit # append x position
                yarr[i] = yinit # append y position 
            return xarr, yarr, zarr
        # PLOT 3D GRAPH
        else:
            # initialize arrays for storing positions
            xarr, yarr, zarr = np.zeros((timesteps,1)), np.zeros((timesteps,1)), np.zeros((timesteps,1))
            # loop through each timestep
            for i in range(timesteps):
                # calculate position for given timestep
                xinit, yinit, zinit = model(xinit, yinit, zinit, constants)
                xarr[i] = xinit # append x position
                yarr[i] = yinit # append y position 
                zarr[i] = zinit # append z position
            return xarr, yarr, zarr
    # 2D PLOTS
    if zinit is None:
        # initialize arrays for storing positions
        xarr, yarr = np.zeros((timesteps,1)), np.zeros((timesteps,1))
        # loop through each timestep
        for i in range(timesteps):
            # calculate position for given timestep
            xinit, yinit = model(xinit, yinit, constants)
            xarr[i] = xinit # append x position
            yarr[i] = yinit # append y position 
        return xarr, yarr