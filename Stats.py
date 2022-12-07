import time
import tkinter
from threading import Thread
from tkinter import *
from tkinter import ttk
from model import PhilosopherDinner
from PIL import ImageTk, Image


class Stats:

    def __init__(self,root,mainFrame,globalClock,thinking_time,philosophers_numb,meal_time,model:PhilosopherDinner):
        self.root = root
        self.mainFrame = mainFrame
        self.model = model
        self.up_frame = Frame(mainFrame, width=700, height=350, bg="white")
        self.down_frame = Frame(mainFrame, width=700, height=350)
        self.number_philosopher_eating = "number_philosopher_eating"
        self.number_philosopher_thinking = "number_philosopher_thinking"
        self.number_philosophers_blocked = "avg_thinking"
        self.max_hungry = "max_hungry"
        self.globalClock = int (globalClock)
        self.thinking_time = thinking_time
        self.philosophers_numb = philosophers_numb
        self.meal_time = meal_time
        self.img_play = PhotoImage(file="playButton.png")
        self.img_pause = PhotoImage(file="pauseButton.png")



    def generateInputComponent(self,inputText, column, row, name):
        label = Label(self.up_frame, text=inputText, pady=15)
        label.grid(column=column, row=row)
        label.config(font=("Gabriola", 14), bg="white")
        inp_philosophers_number = ttk.Label(self.up_frame, justify=tkinter.CENTER, background="white", name=name)
        inp_philosophers_number.grid(column=column, row=(row + 1))
        inp_philosophers_number.config(width=10,font=("Cuprum", 12))



    def set_theard(self):
        thread_start = Thread(target=self.countdown_time)
        thread_update_labels = Thread(target=self.update_labels)
        thread_start.start()
        thread_update_labels.start()


    def countdown_time(self):
        while(self.model.is_on):
            self.globalClock = self.globalClock+1
            time.sleep(1)

    def update_labels(self):
        while (self.model.is_on):
            self.up_frame.nametowidget(self.number_philosopher_thinking).config(text=self.model.controller.view.calculateStatePhiloshoping(self.model.statesPhilosophos))
            self.up_frame.nametowidget(self.number_philosopher_eating).config(text=self.model.controller.view.calculateStateEating(self.model.statesPhilosophos))
            self.up_frame.nametowidget(self.number_philosophers_blocked).config(text=self.model.controller.view.calculateStateHungry(self.model.statesPhilosophos))
            self.up_frame.nametowidget(self.max_hungry).config(text=self.globalClock)
            time.sleep(1)

    def onclickPlay(self):
        self.model.controller.showTimeEat(self.model.timeEat)
        self.model.controller.showTimePhilosophizing(self.model.timePhilosophizing)
        self.model.controller.showTimeHungry(self.model.timeHungry)
        self.model.controller.showTimeWaiting(self.model.timeWaiting)
        self.model.controller.showPlots()
        #time.sleep(5)
        self.down_frame.grid_forget()
        frameGraficas = Frame(self.mainFrame)
        frameGraficas.grid(row=3)
        photo =PhotoImage(file="playButton.png")
        myi = Image.open("graficas.png")
        myi = myi.resize((640,440), Image.ANTIALIAS)
        myi = ImageTk.PhotoImage(myi)
        label = Label(frameGraficas, text="resultados", image=myi)
        label.grid(row=3)
        self.root.update_idletask()








    def set_components(self):
        self.up_frame.grid(row=2)
        self.down_frame.grid(row=3)
        self.generateInputComponent(inputText="Filosofos pensando:", column=1, row=2, name=self.number_philosopher_thinking)
        self.generateInputComponent(inputText="Filosofos comiendo:", column=1, row=4, name=self.number_philosopher_eating)
        self.generateInputComponent(inputText="Filosofos bloqueados", column=2, row=4, name=self.number_philosophers_blocked)
        self.generateInputComponent(inputText="Tiempo de ejecución", column=2, row=2, name=self.max_hungry)
        grafic_button = Button(self.down_frame,text="Graficas",command=self.onclickPlay)
        grafic_button.grid(row=1)
        self.labelGraphics = Label(self.down_frame)
        self.labelGraphics.grid(row=2)
        self.set_theard()




