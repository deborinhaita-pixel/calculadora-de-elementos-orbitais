import numpy as np
from constantes import *
from hohmann import *
from eoc_e_eoa import *

while True:
    print("\nDigite o número de acordo com o dado que você quer obter:\n1. Elementos orbitais\n2. Transferência de Hohmann\n3. Encerrar o programa\n")
    x = int(input("Digite o número: "))

    if x == 1:
        while True:
            print("\nDigite as componentes do vetor posição em km:")
            vetr = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])
            print("\nDigite as componentes do vetor velocidade em km/s:")
            vetv = np.array([float(input("i: ")), float(input("J: ")), float(input("K: "))])

            calculadora_elementos_orbitais(vetr, vetv)
            break

    elif x == 2:
        while True:
            r1 = float(int(input("\nDigite o raio da órbita inicial (km): ")))
            r2 = float(int(input("\nDigite o raio da órbita final (km): ")))

            Δv1, Δv2, t = transf_de_hohmann(r1, r2)
            #O return não imprime nada na tela.
            #Ele só devolve o valor para quem chamou a função. Se você não captura e imprime, o valor é simplesmente descartado.
            #O primeiro valor vai para Δv1, o segundo para Δv2, o terceiro para t. Salva na mesma ordem que a função entrega.
            #Isso se chama desempacotamento de tupla em Python.

            Δvtotal = Δv1 + Δv2

            print(f"\nΔv1 = {Δv1} km/s")
            print(f"Δv2 = {Δv2} km/s")
            print(f"Δvtotal = {Δvtotal} km/s")
            print(f"Tempo de transferência = {t/(60*60)} h")
            break
    
    elif x == 3:
        print("\nPrograma encerrado.")
        break
