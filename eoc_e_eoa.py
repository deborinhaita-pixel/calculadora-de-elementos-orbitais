import numpy as np
from constantes import *

def inclinacao(versork: np.ndarray, h: np.ndarray) -> float:
    i = np.degrees(np.arccos((versork.dot(h))/np.linalg.norm(h)))
    return i

def nodo (versork: np.ndarray, h: np.ndarray) -> np.ndarray:
    n = np.cross(versork, h)
    return n

def ascencao_reta_do_nodo_ascendente(versori: np.ndarray, nodo: np.ndarray) -> float:
    Ω = np.degrees(np.arccos((versori.dot(nodo))/np.linalg.norm(nodo)))
    if nodo[1] < 0:
        Ω = 360 - Ω
    return Ω

def argumento_do_perigeu (nodo: np.ndarray, vetE: np.ndarray, e: float) -> float:
    ω = np.degrees(np.arccos((nodo.dot(vetE))/(np.linalg.norm(nodo)*e)))
    if vetE[2] < 0:
        ω = 360 - ω
    return ω

def anomalia_verdadeira(vetE: np.ndarray, vetR: np.ndarray, e: float, vetV: np.ndarray) -> float:
    v = np.degrees(np.arccos((vetE.dot(vetR))/(e*np.linalg.norm(vetR))))
    if vetR.dot(vetV) < 0:
        v = 360 - v
    elif vetR.dot(vetV) == 0 and vetE.dot(vetR) > 0:
        v = 0
    elif vetR.dot(vetV) == 0 and vetE.dot(vetR) < 0:
        v = 180
    return v

def raio_do_perigeu(a: float, e: float) -> float:
    rp = a * (1 - e)
    return rp

def raio_do_apogeu(a: float, e: float) -> float:
    ra = a * (1 + e)
    return ra

def calculadora_elementos_orbitais (vetr: np.ndarray, vetv: np.ndarray):

    if np.linalg.norm(vetr) > rterra:
        h = np.cross(vetr, vetv) #momento angular específico
        Em = ((np.linalg.norm(vetv)**2/2) - (p/np.linalg.norm(vetr))) #energia mecânica específica
        a = -p / (2 * Em) #semi-eixo maior
        vetE = ((np.cross(vetv, h)/p) - (vetr/np.linalg.norm(vetr))) #vetor E
        e = np.linalg.norm(vetE) #excentricidade
        print(f"\nEnergia mecânica específica (Em) = {Em} km²/s²")
        print(f"Vetor E = {vetE}")
        print(f"Raio do perigeu (rp) = {raio_do_perigeu(a, e)} km")
        print(f"Raio do apogeu (ra) = {raio_do_apogeu(a, e)} km")
        print(f"Vetor momento angular específico (h) = {h} km²/s")
        print(f"Módulo do vetor momento angular específico (h) = {np.linalg.norm(h)} km²/s")
        print("\nElementos orbitais:")
        print(f"\n - Semi-eixo maior (a) = {a} km")
        print(f" - Excentricidade (e) = {e}")
        if np.isclose(e, 0, atol = 10**-4):
            #np.isclose considera próximo quando a diferença está perto da 10^-8
            #para aumentarmos o que o python considera próximo de 0, utilizamos np.isclose(e, 0, atol = 10**-4)
            print(f"   Como e ≈ 0, a órbita é circular.")
        elif 0 < e < 1:
            print("   Como 0 < e < 1, a órbita é elíptica.")
        elif np.isclose(e, 1, atol = 10**-4):
            print(f"   Como e ≈ 1, a órbita é parabólica.")
        elif e > 1:
            print(f"   Como e > 1, a órbita é hiperbólica.")
        print(f" - Inclinação (i) = {inclinacao(versork, h)}°")
        if np.isclose(inclinacao(versork,h), 0, atol = 10**-4):
            print("   Como i ≈ 0, a órbita é equatorial.")
        elif inclinacao(versork, h) < 90:
            print(f"   Como i < 90°, a órbita é prógrada.")
        elif np.isclose(inclinacao(versork, h), 90, atol = 10**-4):
            print("   Como i ≈ 90°, a órbita é polar.")
        else:
            print(f" Como i > 90°, a órbita é retrógrada.")

        #Caso 1: Órbita circular e equatorial
        #Não possui perigeu e não possui nodo
        #Argumento do perigeu (ω), ascensão reta do nodo ascendente (Ω) e anomalia verdadeira (ν) indefinidos
        if np.isclose(e, 0, atol = 10**-4) and (np.isclose(inclinacao(versork, h), 0) or np.isclose(inclinacao(versork, h), 180)):
            l = () #longitude verdadeira
            print(f" - Longitude verdadeira (l) = {l}°")

        #Caso 2: Órbita circular e inclinada
        #Não possui perigeu
        #Argumento do perigeu (ω) e anomalia verdadeira (ν) indefinidos
        elif np.isclose(e, 0, atol = 10**-4) and (not np.isclose(inclinacao(versork, h), 0) and not np.isclose(inclinacao(versork, h), 180)):
            u = () 
            print(f" - Argumento de latitude (u) = {u}°")
            print(f" - Vetor nodo (n) = {nodo(versork, h)}")
            print(f" - Ascensão reta do nodo ascendente (Ω) = {ascencao_reta_do_nodo_ascendente(versori, nodo(versork, h))}°")
        
        #Caso 3: Órbita elíptica e equatorial
        #Não possui nodo
        #Argumento do perigeu (ω) e ascensão reta do nodo ascendente (Ω) indefinidos
        elif 0 < e < 1 and (np.isclose(inclinacao(versork, h), 0) or np.isclose(inclinacao(versork, h), 180)):
            Π = () #longitude do perigeu
            print(f" - Longitude do perigeu (Π) = {Π}°")
            print(f" - Anomalia verdadeira (ν) = {anomalia_verdadeira(vetE, vetR, e, vetV)}°")
        
        #Caso 4: Órbita elíptica e inclinada
        elif 0 < e < 1 and (not np.isclose(inclinacao(versork, h), 0) and not np.isclose(inclinacao(versork, h), 180)):
            print(f" - Argumento do perigeu (ω) = {argumento_do_perigeu(nodo(versork, h), vetE, e)}°")
            print(f" - Ascensão reta do nodo ascendente (Ω) = {ascencao_reta_do_nodo_ascendente(versori, nodo(versork, h))}°")
            print(f" - Anomalia verdadeira (ν) = {anomalia_verdadeira(vetE, vetR, e, vetV)}°")
        
        else:
            print("Órbita não classificada.") #parabólica ou hiperbólica
    
    else:
        print("\nNão é possível que o V/E esteja em órbita.")