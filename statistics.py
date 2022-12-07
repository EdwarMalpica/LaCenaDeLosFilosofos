import time

import matplotlib.pyplot as plt


class Statistics:
    def __init__(self):
        print("Estadisticas")
        self.fig, self.ax = plt.subplots(2, 2)
        self.fig.set_size_inches(10, 8)
        plt.subplots_adjust(left=0.125, bottom=0.2, right=0.9, top=0.9, wspace=0.5, hspace=1)
        self.xLabelTimeTotal = "Filosofos\n\n Estadisticas:\n"
        self.xLabelTimePhilososophing = "Filosofos\n\n Estadisticas:\n"
        self.xLabelTimeHungry = "Filosofos\n\n Estadisticas:\n"
        self.xLabelTimeWaiting = "Filosofos\n\n Estadisticas:\n"

    def plot1TimeEat(self, listPhilosophers):
        self.ax[0, 0].bar(listPhilosophers.keys(), listPhilosophers.values(), color="green")
        self.ax[0, 0].set_title("Tiempo total de cada filosofo")
        self.ax[0, 0].set(xlabel="Filosos", ylabel="Tiempo(s)")

    def calculateMin(self, listPhilosophers):
        value = min(listPhilosophers.values())
        key = ""
        for keys in listPhilosophers:
            if listPhilosophers[keys] == value:
                key = keys
        self.xLabelTimeTotal += f"El filosofo {key} se demoro menos con {value} s\n"

    def calculateMax(self, listPhilosophers):
        value = max(listPhilosophers.values())
        key = ""
        for keys in listPhilosophers:
            if listPhilosophers[keys] == value:
                key = keys
        self.xLabelTimeTotal += f"El filosofo {key} se demoro mas con {value} s\n"

    def calculateAverage(self, listPhilosophers):
        mean = sum(listPhilosophers.values()) / len(listPhilosophers.values())
        self.xLabelTimeTotal += f"El promedio de tiempo empleado es de {mean} s\n"

    def plotTimePhilosophizing(self, listPhilosophizing):
        self.ax[1, 0].bar(listPhilosophizing.keys(), listPhilosophizing.values(), color="green")
        self.ax[1, 0].set_title("Tiempo total Filosofando")
        self.ax[1, 0].set(xlabel="Filosos", ylabel="Tiempo(s)")

    def calculateMinPhilosophizing(self, listPhilosophizing):
        value = min(listPhilosophizing.values())
        key = ""
        for keys in listPhilosophizing:
            if listPhilosophizing[keys] == value:
                key = keys
        self.xLabelTimePhilososophing += f"El filosofo {key} Filosofo menos con {value} s\n"

    def calculateMaxPhilosophizing(self, listPhilosophizing):
        value = max(listPhilosophizing.values())
        key = ""
        for keys in listPhilosophizing:
            if listPhilosophizing[keys] == value:
                key = keys
        self.xLabelTimePhilososophing += f"El filosofo {key} Filosofo mas con {value} s\n"

    def calculateAveragePhilosophizing(self, listPhilosophizing):
        mean = sum(listPhilosophizing.values()) / len(listPhilosophizing.values())
        self.xLabelTimePhilososophing += f"El promedio de tiempo Filosofando es de {mean} s\n"

    def plotTimeHungry(self, listHungry):
        self.ax[0, 1].bar(listHungry.keys(), listHungry.values(), color="green")
        self.ax[0, 1].set_title("Tiempo total con hambre")
        self.ax[0, 1].set(xlabel="Filosos", ylabel="Tiempo(s)")

    def calculateMinHungry(self, listHungry):
        value = min(listHungry.values())
        key = ""
        for keys in listHungry:
            if listHungry[keys] == value:
                key = keys
        self.xLabelTimeHungry += f"El filosofo {key} tuvo menos tiempo hambre con {value} s\n"

    def calculateMaxHungry(self, listHungry):
        value = max(listHungry.values())
        key = ""
        for keys in listHungry:
            if listHungry[keys] == value:
                key = keys
        self.xLabelTimeHungry += f"El filosofo {key} tuvo mas tiempo hambre con {value} s\n"

    def calculateAverageHungry(self, listHungry):
        mean = sum(listHungry.values()) / len(listHungry.values())
        self.xLabelTimeHungry += f"El promedio de tiempo con hambre es de {mean} s\n"

    def plotTimeWaiting(self, listWaiting):
        self.ax[1, 1].bar(listWaiting.keys(), listWaiting.values(), color="green")
        self.ax[1, 1].set_title("Tiempo de espera")
        self.ax[1, 1].set(xlabel="Filosos", ylabel="Tiempo(s)")

    def calculateMinWaiting(self, listWaiting):
        value = min(listWaiting.values())
        key = ""
        for keys in listWaiting:
            if listWaiting[keys] == value:
                key = keys
        self.xLabelTimeWaiting += f"El filosofo {key} espero menos tiempo con {value} s\n"

    def calculateMaxWaiting(self, listWaiting):
        value = max(listWaiting.values())
        key = ""
        for keys in listWaiting:
            if listWaiting[keys] == value:
                key = keys
        self.xLabelTimeWaiting += f"El filosofo {key} espero mas tiempo con {value} s\n"

    def calculateAverageWaiting(self, listWaiting):
        mean = sum(listWaiting.values()) / len(listWaiting.values())
        self.xLabelTimeWaiting += f"El promedio de tiempo esperando es de {mean} s\n"

    def showPlots(self):
        self.ax[0, 0].set(xlabel=self.xLabelTimeTotal, ylabel="Tiempo(s)")
        self.ax[0, 0].grid()
        self.ax[1, 0].set(xlabel=self.xLabelTimePhilososophing, ylabel="Tiempo(s)")
        self.ax[1, 0].grid()
        self.ax[0, 1].set(xlabel=self.xLabelTimeHungry, ylabel="Tiempo(s)")
        self.ax[0, 1].grid()
        self.ax[1, 1].set(xlabel=self.xLabelTimeWaiting, ylabel="Tiempo(s)")
        self.ax[1, 1].grid()
        plt.savefig('graficas.png')
        time.sleep(2)


    def calculateStatePhiloshoping(self, listStates):
        c = 0
        for state in listStates:
            if listStates[state] == "F":
                c += 1
        return c

    def calculateStateHungry(self, listStates):
        c = 0
        for state in listStates:
            if listStates[state] == "H":
                c += 1
        return c

    def calculateStateEating(self, listStates):
        c = 0
        for state in listStates:
            if listStates[state] == "E":
                c += 1
        return c


