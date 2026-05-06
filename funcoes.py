import numpy as np
from constantes import *

def raio_do_perigeu(a: float, e: float) -> float:
    rp = a * (1 - e)
    return rp

def raio_do_apogeu(a: float, e: float) -> float:
    ra = a * (1 + e)
    return ra