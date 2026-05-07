import numpy as np
from constantes import *
from hohmann import *

def mudanca_de_plano_simples(s: float, k: float, Δi: float) -> float:
    Δvsimples = 2 * velocidade_orbital(s, k) * np.sin(np.radians(Δi/2))
    return Δvsimples

def mudanca_de_plano_combinada(vi: float, vf: float, Δi: float):
    Δvcombinada = np.sqrt(abs(vi)**2 + abs(vf)**2 - (2*abs(vi)*abs(vf)*np.cos(np.radians(Δi))))
    return Δvcombinada

def comparar_eficiencia_para_manobras_orbitais (r1: float, r2: float, Δi: float):

    if r1 == r2:
        Δvsimples = mudanca_de_plano_simples(r1, r1, Δi)
        print("Como r1 = r2, é apenas uma mudança de plano simples.")
        print(f"Custo = {Δvsimples} km/s")

        return

    else:

        at, v1, vtransf1, v2, vtransf2, Δv1, Δv2, t = transf_de_hohmann(r1, r2)

        #Caso 1: Mudança de plano simples + Hohmann
        Δvsimples1 = mudanca_de_plano_simples(r1, r1, Δi)
        Δvtotal1 = Δvsimples1 + Δv1 + Δv2
        print("\nCaso 1: Mudança de plano simples + Transferência de Hohmann")
        print(f"{Δvtotal1} km/s")

        #Caso 2: Hohmann + Mudança de plano simples
        Δvsimples2 = mudanca_de_plano_simples(r2, r2, Δi)
        Δvtotal2 = Δv1 + Δv2 + Δvsimples2
        print("\nCaso 2: Transferência de Hohmann + Mudança de plano simples")
        print(f"{Δvtotal2} km/s")

        #Caso 3: Mudança de plano combinada no perigeu da órbita de transferência, depois segundo disparo de Homann
        Δvcombinada1 = mudanca_de_plano_combinada(v1, vtransf1, Δi)
        Δvtotal3 = Δvcombinada1 + Δv2
        print("\nCaso 3: Mudança de plano combinada no perigeu da órbita de transferência + Segundo disparo de Homann")
        print(f"{Δvtotal3} km/s")
    
        #Caso 4: Primeiro disparo de Hohmann, depois mudança de plano combinada no apogeu (Mudança de plano simples + primeiro disparo de Hohman)
        Δvcombinada2 = mudanca_de_plano_combinada(vtransf2, v2, Δi)
        Δvtotal4 = Δv1 + Δvcombinada2
        print("\nCaso 4: Primeiro disparo de Hohmann + Mudança de plano combinada no apogeu da órbita de transferência")
        print(f"{Δvtotal4} km/s")

        return