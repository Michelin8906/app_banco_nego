
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from consultas import consulta_inicio_sesion
#import pymysql


class app_nego:
    def __init__(self, window):

        self.wind = window
        self.wind.geometry ("240x140+100+100")
        self.wind.title('BILLETERA VIRTUAL')

        #Creating a Frame Container
        self.frame = LabelFrame(self.wind, text = 'Iniciar Sesion')
        self.frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #name imput
        Label(self.frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(self.frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Password imput
        Label(self.frame, text = 'Password: ').grid(row = 2, column = 0)
        self.passw = Entry(self.frame, show = "*")
        self.passw.grid(row = 2, column = 1)

        #botton add Sesion
        ttk.Button(self.frame, text = 'Iniciar Sesion', command = self.Iniciar_sesion).grid(row = 3, columnspan = 2, sticky = W + E)

    def validation(self):
        return len(self.name.get()) != 0 and len(self.passw.get()) != 0 

    def Iniciar_sesion(self):
        if self.validation():
            val = consulta_inicio_sesion()
            if val:
                showinfo(title = "Login true", message = "Ingreso Correctamente")
                self.usu = self.name.get()
                self.frame.destroy()
                self.wind.geometry ("1020x650+50+20")
            else:
                showerror(title = "Login False", message = "Usuario o contraseña incorrecta")
        else:
            showerror(title = "Login False", message = "Ingresa por favor usuario o contraseña")

if __name__ == '__main__':
    window = Tk()
    application = app_nego(window)
    window.mainloop()