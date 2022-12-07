import argparse
import threading
import time
import random
import datetime
from Controller import Controller


class PhilosopherDinner:

    def __init__(self):
        self.statephilosopher = None
        self.list_philosopher = []
        self.QUANTITY_PHILOSOPHER = 0
        self.EAT_TIME = 0
        self.TOTAL_EAT_TIME = 0
        self.TIME_TO_PHILOSOPHIZE = 0
        self.SIMULATION_START_TIME=datetime.datetime.now()
        self.is_on = True
        self.timeEat= {}
        self.timePhilosophizing = {}
        self.timeHungry={}
        self.timeWaiting = {}
        self.statesPhilosophos={}

        self.STATE_PHILOSOPHING = "F"
        self.HUNGRY_STATE = "H"
        self.EATING_STATE = "E"
        self.controller = Controller()

    def grabChopsticks(self,id_philosopher):
        """Trata de tomar los palillos izquierdo y derecho (en ese orden) y
        devuelve True si ha podido adquirir ambos y False de lo contrario"""

        left_toothpick = self.list_philosopher[id_philosopher]
        rigth_toothpick = self.list_philosopher[(id_philosopher - 1) % self.QUANTITY_PHILOSOPHER]

        left_toothpick.acquire()

        if rigth_toothpick.acquire(blocking=False):
            return True
        else:
            left_toothpick.release()
            return False


    def freeChipsticks(self,id_philosopher):
        """Liberación de los palillos adyacentes al filosofo"""
        self.list_philosopher[id_philosopher].release()
        self.list_philosopher[(id_philosopher - 1) % self.QUANTITY_PHILOSOPHER].release()


    def startSimulation(self,id_philosopher):
        """Función que va ejecutar cada filosofo(hilo)"""

        total_time_eating = 0

        while total_time_eating < self.TOTAL_EAT_TIME:
            if self.grabChopsticks(id_philosopher):
                # Limpiar los intentos, ya que ya ha terminado de comer
                if total_time_eating == 0:
                    self.timeWaiting[id_philosopher] = (datetime.datetime.now()-self.SIMULATION_START_TIME).seconds
                # Acción de comer
                time_eat = min(self.EAT_TIME, self.TOTAL_EAT_TIME - total_time_eating)
                total_time_eating += time_eat
                print(f"[+] Filosofo {id_philosopher} comiendo [{time_eat} seg.]")
                self.statephilosopher[id_philosopher] = self.EATING_STATE
                self.statesPhilosophos[id_philosopher] = self.EATING_STATE
                time.sleep(total_time_eating)
                self.freeChipsticks(id_philosopher)

                # Filosofar
                self.statephilosopher[id_philosopher] = self.STATE_PHILOSOPHING
                self.statesPhilosophos[id_philosopher] = self.STATE_PHILOSOPHING
                time_philosophize = random.uniform(0, self.TIME_TO_PHILOSOPHIZE)
                self.timePhilosophizing[id_philosopher] += time_philosophize
                print(f"[*] Filosofo {id_philosopher} filosofando[{time_philosophize:.2f} seg.]")
                time.sleep(time_philosophize)
            else:
                self.statephilosopher[id_philosopher] = self.HUNGRY_STATE
                self.statesPhilosophos[id_philosopher] = self.HUNGRY_STATE
                tiempo_reintentar = random.uniform(0, 3)
                self.timeHungry[id_philosopher] += tiempo_reintentar
                print(f"[ ] Filosofo {id_philosopher} esperando tenedores"
                    f"[{tiempo_reintentar:.2f} seg.]")
                time.sleep(tiempo_reintentar)
        print(f"el filosofo {id_philosopher} termino de comer")
        timeUse = datetime.datetime.now()-self.SIMULATION_START_TIME
        print("Se demoro", (datetime.datetime.now()-self.SIMULATION_START_TIME).seconds)

        self.timeEat[id_philosopher] = timeUse.seconds

    def allThreadAlive(self,threadList):
        result = False
        for y in threadList:
            actualThread = y
            if actualThread.is_alive():
                result=True

        return result

    def mySimulation(self, quantity_philosophers: int, eat_time: int, time_philosophize: int, total_eat_time: int):
        self.SIMULATION_START_TIME = datetime.datetime.now()
        self.QUANTITY_PHILOSOPHER = quantity_philosophers
        self.EAT_TIME = eat_time
        self.TOTAL_EAT_TIME = total_eat_time
        self.TIME_TO_PHILOSOPHIZE = time_philosophize

        self.statephilosopher = self.QUANTITY_PHILOSOPHER * [self.STATE_PHILOSOPHING]

        # Inicialización de lista de filosofos
        for _ in range(self.QUANTITY_PHILOSOPHER):
            self.list_philosopher.append(threading.RLock())

        list_thread = []
        for i in range(self.QUANTITY_PHILOSOPHER):
            new_thread = threading.Thread(target=self.startSimulation, args=(i,))
            self.timeEat[i]=0
            self.timePhilosophizing[i]=0
            self.timeHungry[i]=0
            self.timeWaiting[i]=0
            self.statesPhilosophos[i]=0
            list_thread.append(new_thread)

        # Iniciar ejecución de los hilos
        for hilo in list_thread:
            hilo.start()


        # Esperar a que terminen todos los hilos
        for hilo in list_thread:
            hilo.join()

        print("Termino todo")

    #controller = Controller()
    #controller.showTimeEat(timeEat)
    #controller.showTimePhilosophizing(timePhilosophizing)
    #controller.showTimeHungry(timeHungry)
    #controller.showTimeWaiting(timeWaiting)
    #controller.showPlots()

# dineer = PhilosopherDinner()
# dineer.mySimulation()



