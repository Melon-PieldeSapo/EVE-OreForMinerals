import random
from Individuo import Individuo
import Problema
import statistics
import math

num = 200  # La cantidad de individuos que habra en la poblacion
pressure = 100  # Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
pressure2 = 2  # Cuantos individuos se seleccionan para no mutar si son iguales al mejor
mutation_chance = 0.5  # La probabilidad de que un individuo mute
current_step = 0
max_step = 50000
problem = Problema.Problema(92181772, 12332376, 4596379, 668078, 197089, 22261, 61863, 0)


def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    list = []
    for i in range(num):
        random.seed(i)
        sol = Individuo()
        list.append(sol)
    return list


def calcularFitness(individual):
    """
        Calcula el fitness de un individuo concreto.
    """
    problem.CalculateFitness(individual)
    return individual.fitness


def selection_and_reproduction_and_mutation(population):
    """
        Puntua todos los elementos de la poblacion (population) y se queda con los mejores
        guardandolos dentro de 'selected'.
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).

        Por ultimo muta a los individuos.

    """
    puntuados = [calcularFitness(i) for i in population]
    print("step %s - mean: %s" % (current_step, statistics.mean(puntuados[num - pressure:num])))
    # Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    puntuados = sorted(population, key=lambda x: x.fitness,
                       reverse=True)
    # Ordena los pares ordenados y se queda solo con el array de valores
    population = puntuados

    print("%s | %s | %s | %s | %s | %s | %s " % (
    population[num - 1].fitness,population[num - 2].fitness,population[num - 3].fitness,
    population[num - 4].fitness,population[num - 5].fitness,population[num - 6].fitness,
    population[num - 7].fitness))

    # print("puntuados sorted :\n%s" % ([i.fitness for i in population]))  # Se muestra la poblacion inicial
    selected = population[(len(puntuados) - pressure):]
    # Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
    # print("selected :\n%s" % ([i.fitness for i in selected]))  # Se muestra la poblacion inicial

    # Se mezcla el material genetico para crear nuevos individuos
    for i in range(num - pressure):

        #if random.random() <= 0.1:
        #    padre = population[num - 1]  # Se eligen al mejor
        #    population[i] = padre.procreate(padre)
        #    population[i] = population[i].mutate(1)
        #    calcularFitness(population[i])
        #else:
        padre = random.sample(selected, 2)  # Se eligen dos padres
        # Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i] = padre[0].procreate(padre[1])
        if random.random() <= mutation_chance:  # Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            population[i] = population[i].mutate(mutate_factor())

    best = population[num - 1].fitness
    for i in range(0,num-pressure2):
        if population[i].fitness == best:
            #old = population[i].fitness
            population[i] = population[i].mutate(2)
            calcularFitness(population[i])
            #print("mutating %s -%s to %s "%(i,old,population[i].fitness))

    return population
    # El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven


def mutate_factor():
    factor = 50
    if current_step > max_step - (max_step / 2):
        factor = 14
    if current_step > max_step - (max_step / 3):
        factor = 13
    if current_step > max_step - (max_step / 4):
        factor = 12
    if current_step > max_step - (max_step / 5):
        factor = 11
    if current_step > max_step - (max_step / 6):
        factor = 10
    return factor


population = crearPoblacion()  # Inicializar una poblacion
"""
print("Poblacion Inicial:\n%s" % (population))  # Se muestra la poblacion inicial
for i in population:
    print("Individuo:\n%s" % (i))  # Se muestra la poblacion inicial
    i.print()
"""
# Se evoluciona la poblacion
for i in range(max_step):
    population = selection_and_reproduction_and_mutation(population)
    current_step = current_step + 1


crap = [calcularFitness(i) for i in population]
"""
print("\nPoblacion Final:\n%s" % (population))  # Se muestra la poblacion evolucionada
for i in population:
    i.print()
print("\n\n")
"""
print("Mejor Individuo:\n")
population = sorted(population, key=lambda x: x.fitness,
                    reverse=True)

population[num - 1].print()

print("Segundo Mejor Individuo:\n")

population[num - 2].print()
