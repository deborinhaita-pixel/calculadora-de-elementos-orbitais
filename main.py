import numpy as np
from constantes import *
from funcoes import *
from hohmann import *
from eoc_e_eoa import *

print("Digite o número de acordo com o dado que você quer obter:\n1. Elementos orbitais\n2. Transferência de Hohmann\n")
x = int(input("Digite o número: "))

if x == 1:
    while True:
        print("Digite as componentes do vetor posição em km:")
        vetR = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])
        print("Digite as componentes do vetor velocidade em km/s:")
        vetV = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])

        h = np.cross(vetR, vetV) #momento angular específico
        Em = ((np.linalg.norm(vetV)**2/2) - (p/np.linalg.norm(vetR))) #energia mecânica específica
        a = -p / (2 * Em) #semi-eixo maior
        vetE = ((np.cross(vetV, h)/p) - (vetR/np.linalg.norm(vetR))) #vetor E
        e = np.linalg.norm(vetE) #excentricidade
        calculadora_elementos_orbitais(Em, a, vetE, e, h, vetR, vetV)
        print("\n")
        continuar = input("Deseja calcular os elementos orbitais de outra órbita? (S/N): ")
        if continuar == "N":
            print("Encerrando o programa...")
            break

elif x == 2:
    while True:
        r1 = float(int(input("Digite o raio da órbita inicial (km): ")))
        r2 = float(int(input("Digite o raio da órbita final (km): ")))
        at = (r1 + r2) / 2

        Δv1, Δv2, t = transf_de_hohmann(r1, r2)
        #O return não imprime nada na tela.
        #Ele só devolve o valor para quem chamou a função. Se você não captura e imprime, o valor é simplesmente descartado.
        #O primeiro valor vai para Δv1, o segundo para Δv2, o terceiro para t. Salva na mesma ordem que a função entrega.
        #Isso se chama desempacotamento de tupla em Python.

        Δvtotal = Δv1 + Δv2

        print(f"Δv1 = {Δv1} km/s")
        print(f"Δv2 = {Δv2} km/s")
        print(f"Δvtotal = {Δvtotal} km/s")
        print(f"Tempo de transferência = {t/(60*60)} h")
        print("\n")
        continuar = input("Deseja calcular outra transferência de Hohmann? (S/N): ")
        if continuar == "N":
            print("Encerrando o programa...")
            break
