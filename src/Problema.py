import Individuo


class Problema:
    Ores = [
        [0.1, 415, 0, 0, 0, 0, 0, 0, 0],  # Veldespar
        [0.15, 346, 173, 0, 0, 0, 0, 0, 0],  # Scordite
        [0.3, 351, 25, 50, 0, 5, 0, 0, 0],  # Pyroxeres
        [0.35, 107, 213, 107, 0, 0, 0, 0, 0],  # Plagioclase
        [0.6, 800, 100, 0, 85, 0, 0, 0, 0],  # Omber
        [1.2, 134, 0, 267, 134, 0, 0, 0, 0],  # Kernite
        [2, 0, 0, 350, 0, 75, 0, 8, 0],  # Jaspet
        [3, 2200, 0, 0, 100, 120, 0, 15, 0],  # Hemorphite
        [3, 0, 1000, 0, 200, 100, 0, 19, 0],  # Hedbergite
        [5, 0, 2200, 2400, 300, 0, 0, 0, 0],  # Gneiss
        [8, 10000, 0, 0, 1600, 120, 0, 0, 0],  # DarkOchre
        [16, 56000, 12050, 2100, 450, 0, 0, 0, 0],  # Spodumain
        [16, 21000, 0, 0, 0, 760, 0, 135, 0],  # Crokite
        [16, 0, 12000, 0, 0, 0, 100, 450, 0],  # Bistot
        [16, 22000, 0, 2500, 0, 0, 320, 0, 0],  # Arkonor
        [40, 0, 0, 0, 0, 0, 0, 0, 300]]  # Mercoxit

    def __init__(self, Tritanium, Pyerite, Mexallon, Isogen, Nocxium, Megacyte, Zydrine, Morphite):
        self.minerales = [0, 0, 0, 0, 0, 0, 0, 0]
        self.minerales[0] = Tritanium
        self.minerales[1] = Pyerite
        self.minerales[2] = Mexallon
        self.minerales[3] = Isogen
        self.minerales[4] = Nocxium
        self.minerales[5] = Megacyte
        self.minerales[6] = Zydrine
        self.minerales[7] = Morphite

    def CalculateFitness(self, individuo):
        individuo.volumen = 0
        for i in range(16):
            individuo.volumen += self.Ores[i][0] * individuo.Ore[i]

        individuo.Minerales = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(16):
            for j in range(8):
                individuo.Minerales[j] += individuo.Ore[i] * self.Ores[i][j + 1]
        mineralFalta = 0
        for i in range(8):
            mineralFalta += (self.minerales[i] - individuo.Minerales[i]) if self.minerales[i] > individuo.Minerales[
                i] else 0
        individuo.mineralFalta = mineralFalta;
        mineralSobra = 0
        for i in range(8):
            mineralSobra += (individuo.Minerales[i] - self.minerales[i]) if self.minerales[i] < individuo.Minerales[
                i] else 0
        individuo.mineralSobra = mineralSobra;
        individuo.fitness = individuo.volumen + ((individuo.mineralFalta + 1) ^ 2) + ((individuo.mineralSobra + 1)/100)
        return individuo.fitness
