# ODEpy
python package for graphing systems of ODEs

## running the code
```python
# import packages
from ODEpy import ODEpy
from ODEpy import ODEplot
from ODEpy import lorenz_system
from ODEpy import clifford_attractor
from ODEpy import rossler_attractor
from ODEpy import pendulum
# define constants
l = (28., 10., 8./3.)
# integrate
X, Y, Z = ODEpy(lorenz_system, 1.,1.,1., l, 200000, .001)
# plot
ODEplot(X,Y,Z, size = .02, alpha = .5, alt = 0, az = 0)
```

