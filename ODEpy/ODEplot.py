def ODEplot(X, Y, Z, size = .35, alpha = .1, color = 'white', darkmode = True, dpi = 100, 
            alt = 20, az = 45):
    """
    this function is optimized for plotting ODEpy outputs in 2 or 3 dimensions with 
    ---------------------------------------------------------------------------------------
    X, Y, Z [numpy array]: x, y, z positions to be plotted for 3D plot
    shape: (N,), (N,), (N,)
    
    FOR 2 DIMENSIONAL PLOTS: set Z = None
    
    size [float]: sets scatter plot size
    alpha [float]: sets opacity for plot
    color [matplotlib color]: must be a color in matplotlib library
        ex: color = 'mediumslateblue'
    
    darkmode [boolean]: if set to True, will use darkmode for plotting; if false will use white background
    
    dpi [integer]: sets resolution of plot
    
    alt/az []: sets altitude and azimuthal pan of plotting camera for 3D plots
    """
    
    # import plotting tools
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    dpi = int(dpi) # ensure dpi is integer
    
    if Z is not None:        
        fig = plt.figure(figsize=(10, 10), dpi = 100)
        ax = plt.axes(projection='3d')
        ax.view_init(elev = alt, azim = az)
        
        # formatting
        plt.rcParams['font.family'] = 'serif' # set font

        #plt.title('Clifford Attractor', size = 17)
        ax.set_xlabel(r'$\chi$', size = 17)
        ax.set_ylabel(r'$\Upsilon$', size = 17)
        ax.set_zlabel('Z', size = 17)
        
        if darkmode is True:
            # set background color to black
            ax.xaxis.set_pane_color((.0, .0, .0, 1.0))
            ax.yaxis.set_pane_color((.0, .0, .0, 1.0))
            ax.zaxis.set_pane_color((.0, .0, .0, 1.0))
        
        else:
            # set background color to white
            ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
            ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
            ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
            color = 'black' # set plot color to black
        # plot
        plot3d = ax.scatter(X[:], Y[:], Z[:], s = size, alpha = alpha, color = color)
        
    if Z is None:
        if darkmode is True:
            plt.style.use('dark_background')
            fig, ax = plt.subplots(figsize = (13, 13))
        else:
            fig, ax = plt.subplots(figsize = (13, 13))
            #plt.style.use('classic')
            fig.patch.set_facecolor('white')
            color = 'black'

        # formatting
        plt.rcParams['font.family'] = 'serif' # set font
        plt.xlabel(r'$\chi$', size = 25)
        plt.ylabel('Y', size = 25)

        # plot
        plot2d = ax.scatter(X[:], Y[:], s = size, alpha = alpha, color = color)
