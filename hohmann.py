import numpy as np
from constantes import *

def energia_mecanica_especificaA (n) -> float: #fórmula alternativa
    em = -p / (2 * n)
    return em

def velocidade_orbital (s: float, k: float) -> float:
    vo = np.sqrt((energia_mecanica_especificaA(s) + (p/k)) * 2)
    return vo

def transf_de_hohmann (r1: float, r2: float) -> float:
    v1 = velocidade_orbital(r1, r1)
    vtransf1 = velocidade_orbital(at, r1)
    v2 = velocidade_orbital(r2, r2)
    vtransf2 = velocidade_orbital(at, r2)
    t = np.pi * np.sqrt((at**3)/p) #tempo da transferência de Hohmann
    Δv1 = abs(vtransf1 - v1) #abs é módulo
    Δv2 = abs(v2 - vtransf2)
    return Δv1, Δv2, t