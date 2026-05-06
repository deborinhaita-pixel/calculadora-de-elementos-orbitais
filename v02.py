import numpy as np

print("Digite as componentes do vetor posição em km:")
vetR = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])
print("Digite as componentes do vetor velocidade em km/s:")
vetV = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])

p = 3.986 * (10**5) #parâmetro gravitacional em km^3/s^2
RTerra = 6378.14 #km
versori = np.array([1, 0, 0])
versork = np.array([0, 0, 1])
h = np.cross(vetR, vetV) #momento angular específico
Em = ((np.linalg.norm(vetV)**2/2) - (p/np.linalg.norm(vetR))) #energia mecânica específica
a = -p / (2 * Em) #semi-eixo maior
vetE = ((np.cross(vetV, h)/p) - (vetR/np.linalg.norm(vetR))) #vetor E
e = np.linalg.norm(vetE) #excentricidade

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

def calculadora_elementos_orbitais (Em: float, a: float, vetE: np.ndarray, e: float, vetR: np.ndarray, vetV: np.ndarray):

    print(f"A energia mecânica específica (Em) = {Em} km²/s²")
    print(f"O semi-eixo maior (a) = {a} km")
    print(f"O vetor E = {vetE}")
    if e == 0:
        print(f"Como e = {e}, a órbita é circular.")
    elif 0 < e < 1:
        print(f"Como e = {e}, a órbita é elíptica.")
    elif e == 1:
        print(f"Como e = {e}, a órbita é parabólica.")
    elif e > 1:
        print(f"Como e = {e}, a órbita é hiperbólica.")
    print(f"O vetor momento angular específico (h) = {h} km²/s")
    print(f"A inclinação (i) = {inclinacao(versork, h)}°")

    #Caso 1: Órbita circular e equatorial
    #Não possui perigeu e não possui nodo
    #Argumento do perigeu (ω), ascensão reta do nodo ascendente (Ω) e anomalia verdadeira (ν) indefinidos
    if e == 0 and (inclinacao(versork, h) == 0 or inclinacao(versork, h) == 180):
        l = () #longitude verdadeira
        print(f"Longitude verdadeira (l) = {l}°")

    #Caso 2: Órbita circular e inclinada
    #Não possui perigeu
    #Argumento do perigeu (ω) e anomalia verdadeira (ν) indefinidos
    elif e == 0 and (inclinacao(versork, h) != 0 and inclinacao(versork, h) != 180):
        u = () #argumento de latitude
        print(f"Argumento de latitude (u) = {u}°\n")
        print(f"O vetor nodo (n) = {nodo(versork, h)}")
        print(f"A ascensão reta do nodo ascendente (Ω) = {ascencao_reta_do_nodo_ascendente(versori, nodo(versork, h))}°")
    
    #Caso 3: Órbita elíptica e equatorial
    #Não possui nodo
    #Argumento do perigeu (ω) e ascensão reta do nodo ascendente (Ω) indefinidos
    elif 0 < e < 1 and (inclinacao(versork, h) == 0 or inclinacao(versork, h) == 180):
        Π = () #longitude do perigeu
        print(f"longitude do perigeu (Π) = {Π}°\n")
        print(f"A anomalia verdadeira (ν) = {anomalia_verdadeira(vetE, vetR, e, vetV)}°")
    
    #Caso 4: Órbita elíptica e inclinada
    elif 0 < e < 1 and (inclinacao(versork, h) != 0 and inclinacao(versork, h) != 180):
        print(f"O argumento do perigeu (ω) = {argumento_do_perigeu(nodo(versork, h), vetE, e)}°")
        print(f"A ascensão reta do nodo ascendente (Ω) = {ascencao_reta_do_nodo_ascendente(versori, nodo(versork, h))}°")
        print(f"A anomalia verdadeira (ν) = {anomalia_verdadeira(vetE, vetR, e, vetV)}°")
    
    else:
        print("Órbita não classificada.") #parabólica ou hiperbólica

calculadora_elementos_orbitais(Em, a, vetE, e, vetR, vetV)