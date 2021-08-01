"""Funktionen für die Verwendung von Föppel Klammern mit standard Python"""


def foeppl(var_x, grenze_a, potenz_n):
    """Funktion für die Föppl Klammer"""

    if (var_x - grenze_a) == 0:
        raise ValueError("Föppl Klammer für var_x-a == 0 nicht definiert")

    if (var_x - grenze_a) < 0:
        return 0

    return (var_x - grenze_a) ** potenz_n


def foeppl_inkl_null(var_x, grenze_a, potenz_n):
    """Funktion für die Föppl Klammer mit ((var_x-a)==0) = 0"""
    if (var_x - grenze_a) <= 0:
        return 0

    return (var_x - grenze_a) ** potenz_n
