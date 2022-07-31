from tkinter import *

OptionList = [
    "Selecciona una opcion", "Italia", "Hawaii", "Tres quesos", "Chocomenta", "Dopamina", "Cajetosa", "De la casa"
] 

app = Tk()

app.geometry('910x390')

variable = StringVar(app)
variable.set(OptionList[0])

opt = OptionMenu(app, variable, *OptionList)
opt.config(width=50)
opt.pack()

app.mainloop()