def lorenz_system(X, Y, Z, CONTS):
    """calculates dx/dt, dy/dt, dz/dt for the lorenz system of equations given inital conditions, rho, sigma
    and beta values"""
    RHO, SIGMA, BETA = CONTS
    # equations for lorenz system
    dx = SIGMA * (Y - X)
    dy = X * (RHO - Z) - Y
    dz = X * Y - BETA * Z
    return [dx, dy, dz]
    
def clifford_attractor(X, Y, CONST):
    """calculates dx, dy for clifford attractor given initial conditions, a, b, c, and d values
    """
    import numpy as np
    A, B, C, D = CONST
    dx = np.sin(A*Y) + C*np.cos(A*X)
    dy = np.sin(B*X) + D*np.cos(B*Y)
    return [dx, dy]

def rossler_attractor(X, Y, Z, CONST):
    """calculates dx, dy, dz for rossler attractor given initial conditions, a, b, and c values"""
    A, B, C = CONST
    # rossler system equations
    dx = -Y - Z
    dy = X + A*Y
    dz = B + Z*(X - C)
    return [dx, dy, dz]

def pendulum(X, Y, CONST):
    """calculates dx, dy for pendulum with friction given intial conditons, friction and grav.constant/length"""
    A, B = CONST # 
    # equations of motion for pendulum
    dx = Y
    dy = -A*Y - B*np.sin(X)
    return [dx, dy]