def wavenum(f,d,g=9.8):
    import numpy as np
    # INPUTS:
    # f: frequency which is a vector
    # water depth
    # OUTPUT
    # wavenumber
    # METHOD
    # wavenumber is estimated using newtons method. 
    # Shallow water wavenumber is used as the first guess is 
    T=1/f
    omega = 2 * np.pi *f
    k = omega / np.sqrt(g)
    f = g * k * np.tanh(k * d) - omega**2
    while np.abs(f.max()) > 1e-10:
        dfdk = g*k*d*(1/(np.cosh(k*d)))** 2+g*np.tanh(k*d)
        k = k - f/dfdk
        f = g*k*np.tanh(k*d) - omega**2
    return k
