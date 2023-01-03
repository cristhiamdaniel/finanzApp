from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from credencialesMYSQL import *

def mensaje():
    '''
    Función que permite salir de la aplicación
    :return: None
    '''
    answer = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if(answer == "yes"):
        ventana.destroy()

class FinanzApp:
    def __init__(self, ventana):
        '''
        Constructor de la clase FinanzApp
        :param ventana: ventana principal de la aplicación
        '''

        # Configuración de la ventana
        self.ventana = ventana
        self.ventana.title("FinanzApp")
        self.ventana.geometry("1370x700+0+0")
        self.ventana.resizable(False, False)
        self.saldo_inicial = 500000 # Saldo inicial de la cuenta

        # Titulo de la ventana
        title = Label(self.ventana, text="FinanzApp", bd=10, relief=GROOVE, font=("Consolas", 20, "bold"), bg="black", fg="white")
        title.pack(side=TOP)

        # Boton para salir de la aplicación
        Exit_btn = Button(ventana, text="Salir", command=mensaje, font=("Consolas", 10, "bold"), bg="black", fg="white")
        Exit_btn.place(x=1300, y=0)

        # Variables: Id, Tipo, Categoria, Subcategoria, Monto, Fecha, Descripcion, saldo, busqueda
        self.id_var = IntVar()
        self.tipo_var = StringVar()
        self.categoria_var = StringVar()
        self.subcategoria_var = StringVar()
        self.monto_var = IntVar()
        self.fecha_var = StringVar()
        self.saldo = IntVar()
        self.buscar_por = StringVar()
        self.buscar_txt = StringVar()

        # Caja de texto que muestre el saldo actual, se inicia con 500000 y se actualizara con cada movimiento
        self.saldo.set(500000)
        self.saldo_actual = Label(self.ventana, text="Su saldo actual es: $", font=("Consolas", 15, "bold"), bg="black", fg="white")
        self.saldo_actual.place(x=20, y=50)
        self.saldo_actual = Label(self.ventana, textvariable=self.saldo, font=("Consolas", 15, "bold"), bg="white", fg="black")
        self.saldo_actual.place(x=300, y=50)

        # Boton para actualizar saldo
        btn_actualizar_saldo = Button(self.ventana, text="Actualizar saldo", font=("Consolas", 15, "bold"), bg="white", fg="black", command=self.actualizar_saldo)
        btn_actualizar_saldo.place(x=1000, y=50)

        ############################ Marco para manejar las finanzas ############################
        # Creación del marco
        Manage_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="black")
        Manage_Frame.place(x=20, y=100, width=500, height=580)

        # Titulo del marco
        m_title = Label(Manage_Frame, text="Control de Finanzas", bg="black", fg="white", font=("Consolas", 25, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # -> Etiquetas

        # Etiqueta para Id
        lbl_roll = Label(Manage_Frame, text="Id", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Tipo
        lbl_tipo = Label(Manage_Frame, text="Tipo", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_tipo.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Categoria
        lbl_categoria = Label(Manage_Frame, text="Categoria", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_categoria.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Subcategoria
        lbl_subcategoria = Label(Manage_Frame, text="Subcategoria", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_subcategoria.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Monto
        lbl_monto = Label(Manage_Frame, text="Monto", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_monto.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Fecha
        lbl_fecha = Label(Manage_Frame, text="Fecha dd/mm/aa", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_fecha.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta para Descripcion
        lbl_descripcion = Label(Manage_Frame, text="Descripcion", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_descripcion.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        # -> Widgets

        # Id
        txt_roll = Label(Manage_Frame, textvariable=self.id_var, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE, width=10)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Tipo
        combo_tipo = ttk.Combobox(Manage_Frame, textvariable=self.tipo_var, font=("Consolas", 15, "bold"), state="readonly")
        combo_tipo['values'] = ("IngFijo", "IngVariable", "EgrFijo", "EgrVariable")
        combo_tipo.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # Categoria
        combo_categoria = ttk.Combobox(Manage_Frame, textvariable=self.categoria_var, font=("Consolas", 15, "bold"), state="readonly")
        combo_categoria['values'] = []
        combo_categoria.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Subcategoria
        combo_subcategoria = ttk.Combobox(Manage_Frame, textvariable=self.subcategoria_var, font=("Consolas", 15, "bold"), state="readonly")
        combo_subcategoria['values'] = []
        combo_subcategoria.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # -> Funciones para Combobox Tipo - Categoria - Subcategoria

        def change_tipo(event):
            if self.tipo_var.get() == "IngFijo":
                combo_categoria['values'] = ("Salario")
            elif self.tipo_var.get() == "IngVariable":
                combo_categoria['values'] = ("Extras")
            elif self.tipo_var.get() == "EgrFijo":
                combo_categoria['values'] = ("Vivienda", "Servicios", "Deudas", "Deporte", "Ahorro")
            elif self.tipo_var.get() == "EgrVariable":
                combo_categoria['values'] = ("Alimentacion", "Transporte", "Diversion", "Salud", "Mesadas", "Aseo", "Apoyo", "Otros")
            else:
                combo_categoria['values'] = []
            self.categoria_var.set("")
            self.subcategoria_var.set("")

        def change_categoria(event):
            if self.categoria_var.get() == "Salario":
                combo_subcategoria['values'] = ("Gobierno", "Universidad")
            elif self.categoria_var.get() == "Extras":
                combo_subcategoria['values'] = ("Trading", "Judicial")
            elif self.categoria_var.get() == "Vivienda":
                combo_subcategoria['values'] = ("Arriendo", "Ama de casa")
            elif self.categoria_var.get() == "Servicios":
                combo_subcategoria['values'] = ("Agua", "Luz", "Gas", "Internet", "Celular")
            elif self.categoria_var.get() == "Deudas":
                combo_subcategoria['values'] = ("Copebis", "Davivienda")
            elif self.categoria_var.get() == "Deporte":
                combo_subcategoria['values'] = ("Gimnasio", "Futbol", "Otros")
            elif self.categoria_var.get() == "Ahorro":
                combo_subcategoria['values'] = ("Copebis Karla", "Copebis Daniel", "Otros")
            elif self.categoria_var.get() == "Educacion":
                combo_subcategoria['values'] = ("Doctorado", "Jardin")
            elif self.categoria_var.get() == "Alimentacion":
                combo_subcategoria['values'] = ("Mercado", "Restaurantes", "Otros")
            elif self.categoria_var.get() == "Transporte":
                combo_subcategoria['values'] = ("Gasolina", "Transporte Publico", "Otros")
            elif self.categoria_var.get() == "Diversion":
                combo_subcategoria['values'] = ("Viajes", "Otros")
            elif self.categoria_var.get() == "Salud":
                combo_subcategoria['values'] = ("Medicamentos", "Citas", "Otros")
            elif self.categoria_var.get() == "Mesadas":
                combo_subcategoria['values'] = ("Daniel", "Karla", "Nicolas")
            elif self.categoria_var.get() == "Aseo":
                combo_subcategoria['values'] = ("Casa", "Ropa", "Automovil", "Otros")
            elif self.categoria_var.get() == "Apoyo":
                combo_subcategoria['values'] = ("Daniel", "Karla", "Otros")
            elif self.categoria_var.get() == "Otros":
                combo_subcategoria['values'] = ("Otros")
            else:
                combo_subcategoria['values'] = []
            self.subcategoria_var.set("")

        combo_tipo.bind("<<ComboboxSelected>>", change_tipo)
        combo_categoria.bind("<<ComboboxSelected>>", change_categoria)

        # Monto
        txt_monto = Entry(Manage_Frame, textvariable=self.monto_var, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_monto.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Fecha
        txt_fecha = Entry(Manage_Frame, textvariable=self.fecha_var, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_fecha.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Descripcion
        self.txt_descripcion = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.txt_descripcion.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        ############################ Marco para los botones ############################

        # Creación del marco
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="black")
        btn_Frame.place(x=15, y=500, width=470)

        # Boton para agregar
        addbtn = Button(btn_Frame, text="Agregar", width=8, command=self.agregar_montos).grid(row=0, column=0, padx=10, pady=10)

        # Boton para actualizar
        updatebtn = Button(btn_Frame, text="Actualizar", width=8, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)

        # Boton para borrar
        deletebtn = Button(btn_Frame, text="Borrar", width=8, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)

        # Boton para limpiar
        clearbtn = Button(btn_Frame, text="Limpiar", width=8, command=self.clear).grid(row=0, column=3, padx=10, pady=10)



        ############################ Marco para los registros ############################

        # Creación del marco
        Detail_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="black")
        Detail_Frame.place(x=530, y=100, width=820, height=580)

        # Etiqueta buscar por
        lbl_search = Label(Detail_Frame, text="Buscar por", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # Widet para buscar por
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.buscar_por,width=10, font=("Consolas", 15, "bold"), state="readonly")
        combo_search['values'] = ("Tipo", "Categoria", "Subcategoria", "Fecha")
        combo_search.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # Entry para buscar por
        txt_search = Entry(Detail_Frame, textvariable=self.buscar_txt, width=20, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        # Boton para buscar
        searchbtn = Button(Detail_Frame, width=7, text="Buscar", command=self.buscar_data).grid(row=0, column=3, padx=10, pady=10)

        # Boton para mostrar todos
        showallbtn = Button(Detail_Frame, width=8, text="Mostrar todo", command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        ############################ Marco para la tabla ############################

        # Creación del marco
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=70, width=800, height=500)

        # Scrollbar para la tabla
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Finanzas_table = ttk.Treeview(Table_Frame, columns=("id", "tipo", "categoria", "subcategoria", "monto", "fecha", "descripcion"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Finanzas_table.xview)
        scroll_y.config(command=self.Finanzas_table.yview)
        self.Finanzas_table.heading("id", text="Id")
        self.Finanzas_table.heading("tipo", text="Tipo")
        self.Finanzas_table.heading("categoria", text="Categoria")
        self.Finanzas_table.heading("subcategoria", text="Subcategoria")
        self.Finanzas_table.heading("monto", text="Monto")
        self.Finanzas_table.heading("fecha", text="Fecha")
        self.Finanzas_table.heading("descripcion", text="Descripcion")
        self.Finanzas_table['show'] = 'headings'
        self.Finanzas_table.column("id", width=50)
        self.Finanzas_table.column("tipo", width=100)
        self.Finanzas_table.column("categoria", width=100)
        self.Finanzas_table.column("subcategoria", width=100)
        self.Finanzas_table.column("monto", width=100)
        self.Finanzas_table.column("fecha", width=100)
        self.Finanzas_table.column("descripcion", width=150)
        self.Finanzas_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        self.Finanzas_table.pack(fill=BOTH, expand=1)

    def agregar_montos(self):
        if self.tipo_var.get() == "" or self.categoria_var.get() == "" or self.subcategoria_var.get() == "" or self.monto_var.get() == "" or self.fecha_var.get() == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
        else:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            cur.execute("INSERT INTO Amount values(%s, %s, %s, %s, %s, %s, %s)",
                        (self.id_var.get(),
                            self.tipo_var.get(),
                            self.categoria_var.get(),
                            self.subcategoria_var.get(),
                            self.monto_var.get(),
                            self.fecha_var.get(),
                            self.txt_descripcion.get('1.0', END)
                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

            messagebox.showinfo("FinanzApp", "Registro agregado exitosamente")

    def fetch_data(self):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        cur.execute("SELECT * FROM Amount")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Finanzas_table.delete(*self.Finanzas_table.get_children())
            for row in rows:
                self.Finanzas_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        counter = 1
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        cur.execute("SELECT * FROM Amount")
        rows = cur.fetchall()
        for row in rows:
            counter += 1
        self.id_var.set(counter + 1)
        self.tipo_var.set("")
        self.categoria_var.set("")
        self.subcategoria_var.set("")
        self.monto_var.set("")
        self.fecha_var.set("")
        self.txt_descripcion.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Finanzas_table.focus()
        contents = self.Finanzas_table.item(cursor_row)
        row = contents['values']
        #print(row)
        self.id_var.set(row[0])
        self.tipo_var.set(row[1])
        self.categoria_var.set(row[2])
        self.subcategoria_var.set(row[3])
        self.monto_var.set(row[4])
        self.fecha_var.set(row[5])
        self.txt_descripcion.delete("1.0", END)
        self.txt_descripcion.insert(END, row[6])

    def update_data(self):
        if self.tipo_var.get() == "" or self.categoria_var.get() == "" or self.subcategoria_var.get() == "" or self.monto_var.get() == "" or self.fecha_var.get() == "":
            messagebox.showerror("Error", "Seleccione un registro")
        else:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            cur.execute("UPDATE Amount SET tipo=%s, categoria=%s, subcategoria=%s, monto=%s, fecha=%s, descripcion=%s WHERE id=%s",
                        (self.tipo_var.get(),
                            self.categoria_var.get(),
                            self.subcategoria_var.get(),
                            self.monto_var.get(),
                            self.fecha_var.get(),
                            self.txt_descripcion.get('1.0', END),
                            self.id_var.get()
                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

            messagebox.showinfo("FinanzApp", "Registro actualizado exitosamente")

    def delete_data(self):
        if self.tipo_var.get() == "" or self.categoria_var.get() == "" or self.subcategoria_var.get() == "" or self.monto_var.get() == "" or self.fecha_var.get() == "":
            messagebox.showerror("Error", "Seleccione un registro")
        else:
            con = pymysql.connect(host=host, user=user, password=password, database=database)
            cur = con.cursor()
            cur.execute("DELETE FROM Amount WHERE id=%s", self.id_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("FinanzApp", "Registro eliminado exitosamente")

    def buscar_data(self):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        cur.execute("SELECT * FROM Amount WHERE "+str(self.buscar_por.get())+" LIKE '%"+str(self.buscar_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Finanzas_table.delete(*self.Finanzas_table.get_children())
            for row in rows:
                self.Finanzas_table.insert('', END, values=row)
            con.commit()
        con.close()

    def actualizar_saldo(self):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        cur.execute("SELECT monto FROM Amount WHERE tipo = 'IngFijo' OR tipo = 'IngVariable'")
        rows = cur.fetchall()
        ingresos = 0
        for row in rows:
            ingresos = ingresos + row[0]
        cur.execute("SELECT monto FROM Amount WHERE tipo = 'EgrFijo' OR tipo = 'EgrVariable'")
        rows = cur.fetchall()
        egresos = 0
        for row in rows:
            egresos = egresos + row[0]

        saldo = self.saldo_inicial + ingresos - egresos
        self.saldo.set(saldo)
        con.commit()
        con.close()

        messagebox.showinfo("FinanzApp", "Saldo actualizado exitosamente")

# Inicio de la aplicación
ventana = Tk()
app = FinanzApp(ventana)
ventana.mainloop()
