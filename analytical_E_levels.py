from scipy import constants as const

def analytical_E(n):
    """
    Produced an energy eigenstate for a given value of n

    Parameters
    ----------
    n : int
        Principle quantum number.

    Returns
    -------
    E : float
        Energy eigenvalue at a given value of n (for an infinte square potential well).

    """
    gamma2=200  #unitless constant
    E=(n**2*const.pi**2)/gamma2 -1
    return E
