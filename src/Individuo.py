import random


class Individuo:
    mutate_min = -1
    mutate_max = 1
    min = 0
    max = 500

    """
    Representa un individuo/solucion
    """

    def __init__(self):
        self.Ore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fitness = 0
        self.volumen = 0
        self.Minerales = [0, 0, 0, 0, 0, 0, 0, 0]
        self.mineralFalta = 0
        self.mineralSobra = 0
        self.Ore[0] = random.randint(self.min, self.max)  # Veldespar
        self.Ore[1] = random.randint(self.min, self.max)  # Scordite
        self.Ore[2] = random.randint(self.min, self.max)  # Pyroxeres
        self.Ore[3] = random.randint(self.min, self.max)  # Plagioclase
        self.Ore[4] = random.randint(self.min, self.max)  # Omber
        self.Ore[5] = random.randint(self.min, self.max)  # Kernite
        self.Ore[6] = random.randint(self.min, self.max)  # Jaspet
        self.Ore[7] = random.randint(self.min, self.max)  # Hemorphite
        self.Ore[8] = random.randint(self.min, self.max)  # Hedbergite
        self.Ore[9] = random.randint(self.min, self.max)  # Gneiss
        self.Ore[10] = random.randint(self.min, self.max)  # DarkOchre
        self.Ore[11] = random.randint(self.min, self.max)  # Spodumain
        self.Ore[12] = random.randint(self.min, self.max)  # Crokite
        self.Ore[13] = random.randint(self.min, self.max)  # Bistot
        self.Ore[14] = random.randint(self.min, self.max)  # Arkonor
        self.Ore[15] = random.randint(self.min, self.max)  # Mercoxit



    def mutate_amount(self, mutate_factor):
        """
        if self.mineralFalta > 0 and self.mineralSobra >0:
            amount = random.randint(self.mutate_min * mutate_factor, self.mutate_max * mutate_factor)
        elif self.mineralFalta > 0:
            amount = random.randint(1, self.mutate_max * mutate_factor)
        elif self.mineralSobra > 0:
            amount = random.randint(self.mutate_min * mutate_factor, 1)
        else:
        """
        amount = random.randint(self.mutate_min * mutate_factor, self.mutate_max * mutate_factor)
        return amount

    def mutate(self, mutate_factor):
        for i in range(16):
            self.Ore[i] = self.Ore[i] + (self.mutate_amount(mutate_factor))
            self.Ore[i] = self.Ore[i] if self.Ore[i] >= 0 else 0
        return self

    def procreate(self, parent):
        child = Individuo()


        for i in range(16):
            switch2 = random.randint(1, 3)
            if (switch2 == 1):
                child.Ore[i] = self.Ore[i]
            elif (switch2 == 2):
                child.Ore[i] = parent.Ore[i]
            elif (switch2 == 3):
                child.Ore[i] = round((parent.Ore[i] + self.Ore[i])/2)
        return child

    def print(self):
        print("----------------------")
        print("Individuo : %s - Fitnes: %s" % (self.__hash__(), self.fitness))
        print("\n** Ores **")
        print("Veldespar : %s" % (self.Ore[0]))
        print("Scordite : %s" % (self.Ore[1]))
        print("Pyroxeres : %s" % (self.Ore[2]))
        print("Plagioclase : %s" % (self.Ore[3]))
        print("Omber : %s" % (self.Ore[4]))
        print("Kernite : %s" % (self.Ore[5]))
        print("Jaspet : %s" % (self.Ore[6]))
        print("Hemorphite : %s" % (self.Ore[7]))
        print("Hedbergite : %s" % (self.Ore[8]))
        print("Gneiss : %s" % (self.Ore[9]))
        print("DarkOchre : %s" % (self.Ore[10]))
        print("Spodumain : %s" % (self.Ore[11]))
        print("Crokite : %s" % (self.Ore[12]))
        print("Bistot : %s" % (self.Ore[13]))
        print("Arkonor : %s" % (self.Ore[14]))
        print("Mercoxit : %s" % (self.Ore[15]))
        print("\n** Minerales **")
        print(" Tritanium: %s" % (self.Minerales[0]))
        print("Pyerite: %s" % (self.Minerales[1]))
        print("Mexallon: %s" % (self.Minerales[2]))
        print("Isogen: %s" % (self.Minerales[3]))
        print("Nocxium: %s" % (self.Minerales[4]))
        print("Megacyte: %s" % (self.Minerales[5]))
        print("Zydrine: %s" % (self.Minerales[6]))
        print("Morphite: %s" % (self.Minerales[7]))
        print("\nMinerales que faltan :%s" % (self.mineralFalta))
        print("\nMinerales que Sobran :%s" % (self.mineralSobra))
        print("\nVolumen :%s" % (self.volumen))
        print("----------------------")
