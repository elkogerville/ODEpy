def ODEplot(X, Y, Z, size = .35, alpha = .1, color = 'white', darkmode = True, dpi = 100, 
            elev = 20, azim = 45, xlim = None, ylim = None, zlim = None, **kwargs):
    """
    this function is optimized for plotting ODEpy outputs in 2 or 3 dimensions 
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
    
    elev/azim [float]: sets altitude and azimuthal pan of plotting camera for 3D plots
    
    xlim/ylim/zlim [boolean]: if set to True, will ask user to input values for axes limits
    
    **kwargs [string]: x_label, y_label, z_label; sets axes labels; if plotting in 2D only use x and y labels
    ex: xlabel = "position"
    """
    
    # import plotting tools
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    dpi = int(dpi) # ensure dpi is integer
    # set label names
    x_label = r'$\chi$'
    y_label = r'$\Upsilon$'
    z_label = 'Z'
    # change label names if passed in **kwargs
    if ('x_label') in kwargs:
        x_label = kwargs['x_label']
    if ('y_label') in kwargs:
        y_label = kwargs['y_label']
    if ('z_label') in kwargs:
        z_label = kwargs['z_label']
    
    if Z is not None:        
        fig = plt.figure(figsize=(10, 10), dpi = 100)
        ax = plt.axes(projection='3d')
        ax.view_init(elev = elev, azim = azim)
        
        # formatting
        plt.rcParams['font.family'] = 'serif' # set font

        ax.set_xlabel(x_label, size = 17)
        ax.set_ylabel(y_label, size = 17)
        ax.set_zlabel(z_label, size = 17)
        # set axes limits
        if xlim is not None:
            xmin = int(input('xlim min: '))
            xmax = int(input('xlim max: '))
            ax.set_xlim(xmin, xmax)
        if ylim is not None:
            ymin = int(input('ylim min: '))
            ymax = int(input('ylim max: '))
            ax.set_ylim(ymin, ymax)
        if zlim is not None:
            zmin = int(input('zlim min: '))
            zmax = int(input('zlim max: '))
            ax.set_zlim(zmin, zmax)
        # background color
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
        plt.show()
        
    if Z is None:
        # background color
        if darkmode is True:
            plt.style.use('dark_background')
            fig, ax = plt.subplots(figsize = (13, 13))
        else:
            fig, ax = plt.subplots(figsize = (13, 13))
            fig.patch.set_facecolor('white')
            color = 'black'

        # formatting
        plt.rcParams['font.family'] = 'serif' # set font
        plt.xlabel(x_label, size = 25)
        plt.ylabel(y_label, size = 25)
        # set axes limits
        if xlim is not None:
            xmin = int(input('xlim min: '))
            xmax = int(input('xlim max: '))
            ax.set_xlim(xmin, xmax)
        if ylim is not None:
            ymin = int(input('ylim min: '))
            ymax = int(input('ylim max: '))
            ax.set_ylim(ymin, ymax)

        # plot
        plot2d = ax.scatter(X[:], Y[:], s = size, alpha = alpha, color = color)
        plt.show()