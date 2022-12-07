import tkinter
from threading import Thread
from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont
from Stats import Stats
from model import PhilosopherDinner

root = Tk()

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 700
hventana = 700
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry("700x1000")
#root.resizable(False,False)
root.config(bg='white')
mainFrame = Frame(root,name="mainFrame", width="1500", height="700")
mainFrame.pack()
mainFrame.config(width="1500", height="700", bg="yellow")
right_frame = tkinter.Frame(mainFrame, width="350", height="700")
left_frame = tkinter.Frame(mainFrame, width="350", height="700")
#Configuracion GRID

mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)
mainFrame.rowconfigure(4, weight=1)
mainFrame.rowconfigure(5, weight=1)
mainFrame.rowconfigure(6, weight=1)
mainFrame.rowconfigure(7, weight=1)
mainFrame.rowconfigure(8, weight=1)

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)

left_frame.rowconfigure(0, weight=1)
left_frame.rowconfigure(1, weight=1)
left_frame.rowconfigure(2, weight=1)

left_frame.columnconfigure(0, weight=1)
left_frame.columnconfigure(1, weight=1)
left_frame.columnconfigure(2, weight=1)




right_frame.grid(column=1,row=3)
left_frame.grid(column=0,row=3)
right_frame.columnconfigure(1,weight=1)
mainFrame.config(bg="white")
left_frame.config(bg="white")
right_frame.config(bg="white")

#------Variables----------------
model = PhilosopherDinner()

#------Constantes-------------
input_number_philosophers_name = "numPhilo"
input_thinking_time_name = "tmThinking"
input_meal_time_name="tmMeal"
input_simulation_time_name="tmSimulation"





def generateInputComponent(inputText, column, row, name):
    label = Label(right_frame,text=inputText)
    label.grid(column=column, row=row)
    label.config(font=("Gabriola", 14), bg="white")
    inp_philosophers_number = ttk.Entry(right_frame, justify=tkinter.CENTER,name=name)
    inp_philosophers_number.grid(column=column, row=(row+1),pady=10, padx=20)
    inp_philosophers_number.config(width=40)




def routing_stats():
    #mainFrame.pack_forget()
    philosophers_numb = int(right_frame.nametowidget(input_number_philosophers_name).get())
    thinking_time = int(right_frame.nametowidget(input_thinking_time_name).get())
    meal_time = int(right_frame.nametowidget(input_meal_time_name).get())
    total_eat_time = int(right_frame.nametowidget(input_simulation_time_name).get())
    stats = Stats(root, mainFrame, philosophers_numb=philosophers_numb, thinking_time=thinking_time,
                  meal_time=meal_time, globalClock=0, model=model)
    right_frame.destroy()
    left_frame.destroy()
    stats.set_components()
    model_theard = Thread(target=model.mySimulation, args=(philosophers_numb, meal_time, thinking_time, total_eat_time))
    model_theard.start()



fontTitle = tkfont.Font(family='Gabriola', size=25, weight='bold')
header = Label(mainFrame,text="La cena de los filosofos",justify=tkinter.CENTER,pady=15)
header.grid(row=1, column=0, columnspan=2)
header.config(font =fontTitle, bg="white")
separador=ttk.Separator(mainFrame,orient='horizontal')
separador.grid(row=2, column=0, sticky='SWE', columnspan=2)

generateInputComponent(inputText="Numero de filosofos",column=1,row=3,name=input_number_philosophers_name)
generateInputComponent(inputText="Tiempo de pensar",column=1,row=5,name=input_thinking_time_name)
generateInputComponent(inputText="Tiempo de cenar",column=1,row=7,name=input_meal_time_name)
generateInputComponent(inputText="Tiempo total de comer",column=1,row=9,name=input_simulation_time_name)
img_home = PhotoImage(file="iconSOHome.png")
photo_container = Label(left_frame,image=img_home, bg='white')
photo_container.grid(column=1,row=1)
img_play = PhotoImage(file="playButton.png")
photo_container_play = Button(right_frame,image=img_play,command=routing_stats, bg='white')
photo_container_play.grid(column=1,row=12)
#------------------------------------------------------------------------------------------------------------------------


root.mainloop()