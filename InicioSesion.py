'''
Interfaz en tkinter que pida al usuario ingresar sus datos:
Nombre de usuario y contraseña.

Esos datos se deben validar con las columnas:
nombre_user y contrasenia de la tabla usuarios de la base de datos finanzApp.

Si son correctos, se debe mostrar un mensaje de bienvenida al usuario. y se debe lanzar
la interfaz del archivo FinanzApp.py

Si son incorrectos, se debe mostrar un mensaje de error y se debe volver a pedir los datos.
'''

import pymysql
from tkinter import *
from tkinter import messagebox
from Finanzapp import FinanzApp
from credencialesMYSQL import *

class InicioSesion:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("finanzApp")
        self.ventana.geometry("350x150")
        self.ventana.resizable(0,0)
        self.ventana.config(bg="gray")

        self.etiqueta1 = Label(self.ventana, text="Nombre de usuario", bg="black", fg="white")
        self.etiqueta1.grid(row=0, column=0, padx=10, pady=10)
        self.caja1 = Entry(self.ventana, width=20)
        self.caja1.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta2 = Label(self.ventana, text="Contraseña",  bg="black", fg="white")
        self.etiqueta2.grid(row=1, column=0, padx=10, pady=10)
        self.caja2 = Entry(self.ventana, width=20, show="*")
        self.caja2.grid(row=1, column=1, padx=10, pady=10)

        self.boton1 = Button(self.ventana, text="Iniciar Sesión", command=self.validar)
        self.boton1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.ventana.mainloop()

    def validar(self):
        nombre = self.caja1.get()
        contrasenia = self.caja2.get()
        conexion = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_user, contrasenia FROM usuarios WHERE nombre_user = %s AND contrasenia = %s", (nombre, contrasenia))
        resultado = cursor.fetchall()
        if resultado:
            messagebox.showinfo("Bienvenido", "Bienvenido {}".format(nombre))
            self.ventana.destroy()
            FinanzApp()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.caja1.delete(0, END)
            self.caja2.delete(0, END)
            self.caja1.focus()

if __name__ == "__main__":
    InicioSesion()


