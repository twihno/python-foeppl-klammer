"""Funktionen für die Verwendung von Föppel Klammern mit numpy"""


import numpy as np


def foeppl_np(var_x, grenze_a, potenz_n):
    """Numpy Funktion für die Föppl Klammer"""

    if ((var_x - grenze_a) == 0).any():
        raise ValueError("Föppl Klammer für var_x-a == 0 nicht definiert")

    return np.where((var_x - grenze_a) < 0, 0, (var_x - grenze_a) ** potenz_n)


def foeppl_np_inkl_null(var_x, grenze_a, potenz_n):
    """Numpy Funktion für die Föppl Klammer mit ((var_x-a)==0) = 0"""

    return np.where((var_x - grenze_a) <= 0, 0, (var_x - grenze_a) ** potenz_n)
