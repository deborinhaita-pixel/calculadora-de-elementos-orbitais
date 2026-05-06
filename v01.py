import numpy as np

print("Digite as componentes do vetor posição em km:\n")
vetR = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])
print("\n")
print("Digite as componentes do vetor velocidade em km/s:\n")
vetV = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])

p = 3.986 * (10**5) #parâmetro gravitacional em km^3/s^2
RTerra = 6378.14 #km

versori = np.array([1, 0, 0])
versork = np.array([0, 0, 1])

#np.array avisa para o python que a lista de entrada é uma matriz

def calculadora_elementos_orbitais(vetR: np.ndarray, vetV: np.ndarray) -> tuple:
    #np.arry é o comando para transformar em matriz e np.ndarray é para indicar que a variável é uma matriz
    #tuple é um pacotinho de valores
    print("\n")
    if np.linalg.norm(vetR) > RTerra:
        print(f"Módulo da posição (R) = {np.linalg.norm(vetR)} km")
        print("Como R > Raio da Terra, podemos concluir que o V/E está em órbita.\n")

        Em = ((np.linalg.norm(vetV)**2)/2) - (p/np.linalg.norm(vetR)) #energia mecânica específica
        if Em > 0:
            print(f"Energia mecânica específica (Em) = {Em}")
            print("Como Em > 0, a órbita é hiperbólica.\n")
        elif Em == 0:
            print(f"Energia mecânica específica (Em) = {Em}")
            print("Como Em = 0, a órbita é parabólica.\n")
        else:
            print(f"Energia mecânica específica (Em) = {Em}")
            print("Como Em < 0, a órbita é circular ou elíptica.\n")

        a = -p/(2*Em) #semi-eixo maior
        print(f"Semi-eixo maior (a) = {a} km\n")

        h = np.cross(vetR, vetV) #momento angular específico
        print(f"Vetor momento ângular específico (h) = {h} km²/s\n")

        vetE = ((np.cross(vetV, h)/p) - (vetR/np.linalg.norm(vetR))) #vetor E
        print(f"Vetor E = {vetE}")
        e = np.linalg.norm(vetE) #excentricidade
        print(f"Excentricidade (e) = {np.linalg.norm(vetE)}\n")
        if e == 0:
            print("Como e = 0, a órbita é circular.\n")
        elif 0 < e < 1:
            print("Como 0 < e < 1, a órbita é elíptica.\n")
        elif e == 1:
            print("Como e = 1, a órbita é parabólica.\n")
        elif e > 1:
            print("Como e > 1, a órbita é hiperbólica.\n")

        i = np.degrees(np.arccos((versork.dot(h))/np.linalg.norm(h))) #inclinação
        print(f"Inclinação (i) = {i}°\n")
        #o python devolve i em radianos
        #np.degrees converte para graus

        #órbita circular e equatorial
        #problemas: ω, Ω e ν são indefinidos pois não possui perigeu e nem linha dos nodos
        #o que é possível calcular? l (longitude verdadeira)
        #longitude verdadeira (l) é o ângulo medido desde a direção principal até a posição do V/E.  
        if e == 0 and (i == 0 or i == 180):
            print(f"Como e = {e} e i = {i}°, a órbita é simultaneamente circular equatorial.")
            print("Como consequência, não possui argumento do perigeu (ω), ascensão reta do nodo ascendente (Ω) e nem anomalia verdadeira (ν).")
            print("Nesse caso, Utilizaremos o elemento orbital alternativo l, chamado de longitude verdadeira.")
            l = () #longitude verdadeira
            print(f"Longitude verdadeira (l) = {l}°")
        
        #órbita circular e inclinada
        #problemas: ω e ν são indefinidos pois não possui perigeu
        #o que é possível calcular? n, Ω e u(argumento de latitude)
        #argumento de latitude (u) é o ângulo medido desde o nodo ascendente até a posição do veículo espacial (V/E).
        elif e == 0 and (i !=0 and i != 180):
            print("Como e = 0, a órbita é circular e, portanto, a anomalia verdadeira (v) e o argumento do perigeu (ω) são indefinidos.")
            print("Nesse caso, utilizamos o elemento orbital alternativo u, chamado de argumento de latitude.")
            u = () #argumento de latitude
            print(f"Argumento de latitude (u) = {u}°\n")

            n = np.cross(versork, h) #vetor nodo
            print(f"Vetor nodo (n) = {n}")
            print(f"Módulo do vetor nodo (n) = {np.linalg.norm(n)}\n")

            Ω = np.degrees(np.arccos((versori.dot(n))/np.linalg.norm(n))) #ascenção reta do nodo ascendente
            if n[1] < 0:
                Ω = 360 - Ω
            print(f"Longitude do nodo ascendente (Ω) = {Ω}°\n")

        #órbita não circular e equatorial
        #problemas: ω e Ω são indefinidos pois não possui linha dos nodos
        #o que é possível calcular? ν e Π (longitude do perigeu)
        #longitude do perigeu (Π) é o ângulo medido desde a direção principal até o perigeu.
        elif e != 0 and (i == 0 or i == 180):
            print("Como a órbita é elíptica e não possui inclinação, o argumento do perigeu (ω) e a ascenção reta do nodo ascendente (Ω) é indefinida.")
            print("Nesse caso, utilizamos o elemento orbital alternativo Π, chamado de longitude do perigeu.")
            Π = () #longitude do perigeu
            print(f"longitude do perigeu (Π) = {Π}°\n")

            ν = np.degrees(np.arccos((vetE.dot(vetR))/(np.linalg.norm(vetE)*np.linalg.norm(vetR)))) #anomalia verdadeira
            if vetR.dot(vetV) > 0:
                print(f"Anomalia verdadeira (ν) = {ν}°")
            elif vetR.dot(vetV) < 0:
                ν = 360 - ν
                print(f"Anomalia verdadeira (ν) = {ν}°")
            elif vetR.dot(vetV) == 0 and vetE.dot(vetR) > 0:
                ν = 0
                print(f"Anomalia verdadeira (ν) = {ν}°")
                print("O V/E está no perigeu.\n")
            elif vetR.dot(vetV) == 0 and vetE.dot(vetR) < 0:
                ν = 180
                print(f"Anomalia verdadeira (ν) = {ν}°")
                print("O V/E está no apogeu.\n")
    
        #órbita não circular e inclinada
        elif e != 0 and (i != 0 and i != 180):
            n = np.cross(versork, h) #vetor nodo
            print(f"Vetor nodo (n) = {n}")
            print(f"Módulo do vetor nodo (n) = {np.linalg.norm(n)}\n")

            Ω = np.degrees(np.arccos((versori.dot(n))/np.linalg.norm(n))) #ascençõ reta do nodo ascendente
            if n[1] < 0:
                Ω = 360 - Ω
            print(f"Longitude do nodo ascendente (Ω) = {Ω}°\n")

            ω = np.degrees(np.arccos((n.dot(vetE))/(np.linalg.norm(n)*np.linalg.norm(vetE)))) #argumento do perigeu
            if vetE[2] < 0:
                ω = 360 - ω
            print(f"Argumento do perigeu (ω) = {ω}°\n")

            ν = np.degrees(np.arccos((vetE.dot(vetR))/(np.linalg.norm(vetE)*np.linalg.norm(vetR)))) #anomalia verdadeira

            if vetR.dot(vetV) > 0:
                print(f"Anomalia verdadeira (ν) = {ν}°")
            elif vetR.dot(vetV) < 0:
                ν = 360 - ν
                print(f"Anomalia verdadeira (ν) = {ν}°")
            elif vetR.dot(vetV) == 0 and vetE.dot(vetR) > 0:
                ν = 0
                print(f"Anomalia verdadeira (ν) = {ν}°")
                print("O V/E está no perigeu.\n")
            elif vetR.dot(vetV) == 0 and vetE.dot(vetR) < 0:
                ν = 180
                print(f"Anomalia verdadeira (ν) = {ν}°")
                print("O V/E está no apogeu.\n")

    else:
        print(f"O módulo do vetor posição é {np.linalg.norm(vetR)} km, ou seja, menor ou igual ao raio da Terra (6378.14 km).")
        print("Então, não é possível que o V/E esteja em órbita.\n")
    
    return

calculadora_elementos_orbitais(vetR, vetV)