from statistics import Statistics

class Controller:
    def __init__(self):
        self.view = Statistics()

    def showTimeEat(self, listPhilosophers):
        self.view.plot1TimeEat(listPhilosophers)
        self.view.calculateMin(listPhilosophers)
        self.view.calculateMax(listPhilosophers)
        self.view.calculateAverage(listPhilosophers)

    def showTimePhilosophizing(self,listPhilosophizing):
        self.view.plotTimePhilosophizing(listPhilosophizing)
        self.view.calculateMinPhilosophizing(listPhilosophizing)
        self.view.calculateMaxPhilosophizing(listPhilosophizing)
        self.view.calculateAveragePhilosophizing(listPhilosophizing)
    def showTimeHungry(self,listHungry):
        self.view.plotTimeHungry(listHungry)
        self.view.calculateMinHungry(listHungry)
        self.view.calculateMaxHungry(listHungry)
        self.view.calculateAverageHungry(listHungry)
    def showTimeWaiting(self, listWaiting):
        self.view.plotTimeWaiting(listWaiting)
        self.view.calculateMinWaiting(listWaiting)
        self.view.calculateMaxWaiting(listWaiting)
        self.view.calculateAverageWaiting(listWaiting)
    def showPlots(self):
        self.view.showPlots()