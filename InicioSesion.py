import pymysql
from tkinter import *
from tkinter import messagebox
from Finanzapp import FinanzApp
from credencialesMYSQL import *
from tkinter import PhotoImage
import urllib.request

class InicioSesion:
    '''
    Clase para la ventana de inicio de sesion
    '''
    def __init__(self):
        '''
        Constructor
        '''
        #------------------VENTANA------------------#
        self.ventana = Tk()
        self.ventana.title("finanzApp")
        self.ventana.geometry("350x400")
        self.ventana.resizable(0,0)
        self.ventana.config(bg="gainsboro")

        # Logo
        with urllib.request.urlopen("https://cdn-icons-png.flaticon.com/512/2167/2167780.png") as url:
            self.image_data = url.read()
        self.logo = PhotoImage(data=self.image_data)
        self.logo = self.logo.subsample(3)
        self.logo_label = Label(self.ventana, image=self.logo)
        self.logo_label.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        #------------------CAJAS DE TEXTO------------------#

        # Caja de texto para el nombre de usuario
        self.etiqueta1 = Label(self.ventana, text="Nombre de usuario", bg="black", fg="white")
        self.etiqueta1.grid(row=1, column=0, padx=10, pady=10)
        self.caja1 = Entry(self.ventana, width=20)
        self.caja1.grid(row=1, column=1, padx=10, pady=10)

        # Caja de texto para la contraseña
        self.etiqueta2 = Label(self.ventana, text="Contraseña", bg="black", fg="white")
        self.etiqueta2.grid(row=2, column=0, padx=10, pady=10)
        self.caja2 = Entry(self.ventana, width=20, show="*")
        self.caja2.grid(row=2, column=1, padx=10, pady=10)

        # Pie de pagina
        self.etiqueta3 = Label(self.ventana, text="Created by @MundoBitCol", bg="black", fg="white")
        self.etiqueta3.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        #------------------BOTONES------------------#

        # Boton para iniciar sesion
        self.boton1 = Button(self.ventana, text="Iniciar Sesión", command=self.validar)
        self.boton1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.ventana.mainloop()

    #------------------FUNCIONES------------------#
    def validar(self):
        '''
        Funcion para validar el inicio de sesion
        :return: None
        '''
        # Obtener los datos de las cajas de texto
        nombre = self.caja1.get()
        contrasenia = self.caja2.get()
        # Conectar a la base de datos
        conexion = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_user, contrasenia FROM usuarios")
        datos = cursor.fetchall()
        conexion.close()
        # Validar los datos
        for i in datos:
            if nombre == i[0] and contrasenia == i[1]:
                usuario = self.caja1.get()
                self.ventana.destroy()
                FinanzApp(usuario)
                return
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        # Limpiar las cajas de texto
        self.caja1.delete(0, END)
        self.caja2.delete(0, END)
        self.caja1.focus()

if __name__ == "__main__":
    InicioSesion()


