import random

def generar_solucion_inicial():
    return [random.randint(0, 7) for i in range(8)]

def imprimir_tablero(solucion):
    for i in range(8):
        for j in range(8):
            if solucion[i] == j:
                print("R", end=" ")
            else:
                print("-", end=" ")
        print()
    print()
    
def evaluar_solucion(solucion):
    ataques = 0
    for i in range(len(solucion)):
        for j in range(i+1, len(solucion)):
            if solucion[i] == solucion[j] or abs(i-j) == abs(solucion[i]-solucion[j]):
                ataques += 1
    return ataques

def cruce(padre1, padre2, probCruce):
    if random.random() < probCruce:
        if random.random() > 0:
            nuevoPadre1 = padre1[:4] + padre2[4:]
        else:
            nuevoPadre1 = padre2[:4] + padre1[4:]   
    return nuevoPadre1

def mutacion(solucion, probabilidad):
    if random.random() < probabilidad:
        indice = random.randint(0, 7)
        nuevaColumna = random.randint(0, 7)
        solucion[indice] = nuevaColumna
    return solucion

def aptitud(solucion):
    conflictos = 0
    for i in range(len(solucion)):
        for j in range(i+1, len(solucion)):
            if (solucion[j] - solucion[i]) == j - i:
                conflictos += 1
    return 1 / (conflictos + 1)


def seleccion_de_padre(poblacion, probPadre):
    probsbilidades = [0.6/4] * 4 + [probPadre]
    numeroAleatorio = random.uniform(0,1)
    sumAcumulada = 0
    for i, prob in enumerate(probsbilidades):
        sumAcumulada += prob
        if sumAcumulada >= numeroAleatorio:
            nuevoPadre = poblacion[i]
    return nuevoPadre
    
  
def algoritmo_evolutivo(tamPoblacion, probMutacion, probPadre, tmGeneraciones, probCruce):
    poblacion = [generar_solucion_inicial() for i in range(tamPoblacion)]
    for i in range(tmGeneraciones):
        poblacion.sort(key=lambda sol: evaluar_solucion(sol))
        
        print("Generación", i, "-", poblacion[0], "- Ataques:", evaluar_solucion(poblacion[0]), ", Aptitud: ", aptitud(poblacion[0])) 
        if evaluar_solucion(poblacion[0]) == 0:
            imprimir_tablero(poblacion[0])
            break
        descendietes = []
        while len(descendietes) < tamPoblacion:
            padre1 = seleccion_de_padre(poblacion, probPadre)
            padre2 = seleccion_de_padre(poblacion, probPadre)
            hijo1 = cruce(padre1, padre2, probCruce)
            mutacion(hijo1, probMutacion)
            descendietes.append(hijo1)

        poblacion = descendietes
    return poblacion[0]

#individuos, probabilidad mutacion, probabilidad de ser padre, tamañao de generacion#, probabilidad de cruza
mejor_solucion = algoritmo_evolutivo(30, 1, .4, 10000, 1)
print(mejor_solucion) 