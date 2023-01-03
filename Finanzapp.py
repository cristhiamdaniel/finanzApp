from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class FinanzApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("FinanzApp")
        self.ventana.geometry("1360x700+0+0")
        self.ventana.resizable(False, False)

        # Variables
        self.id = IntVar()


        title = Label(self.ventana, text="Sistema de finanzas personales", font=("Consolas", 40, "bold"), bg="black",
                      fg="white", bd=10, relief=RAISED)
        title.pack(side=TOP)

        ################################## Marco de registros ##################################
        Manage_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="black")
        Manage_Frame.place(x=20, y=100, width=520, height=580)

        m_title = Label(Manage_Frame, text="Control de Finanzas", font=("Consolas", 30, "bold"), bg="white", fg="red")
        m_title.grid(row=0, columnspan=2, pady=20)

        ################################## SALDO ##################################

        # Etiqueta Saldo Actual
        lbl_saldo_actual = Label(Manage_Frame, text="Saldo Actual", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_saldo_actual.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Boton de Saldo Actual
        self.saldo = 450900
        btn_saldo_actual = Button(Manage_Frame, text=f"{self.saldo} cop", font=("Consolas", 15, "bold"), bg="white", fg="red", command=self.mostrar_saldo)
        btn_saldo_actual.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        '''
        # Entrada de tipo entero Saldo Actual
        self.saldo = IntVar()
        txt_saldo_actual = Entry(Manage_Frame, textvariable=self.saldo, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_saldo_actual.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        '''

        ################################## TIPO ##################################
        # Etiqueta Tipo
        lbl_tipo = Label(Manage_Frame, text="Tipo", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_tipo.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        # Combobox Tipo = [Ingreso Fijo, Ingreso Variable, Gasto Fijo, Gasto Variable]
        self.tipo = StringVar()
        combo_tipo = ttk.Combobox(Manage_Frame, textvariable=self.tipo, font=("Consolas", 13, "bold"), state="readonly")
        combo_tipo['values'] = ("Ingreso Fijo", "Ingreso Variable", "Gasto Fijo", "Gasto Variable")
        combo_tipo.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        ################################## CATEGORIA Y SUBCATEGORIA ##################################

        '''
        Para las etiquetas de "Categoria" y "Subcategoria" se debe hacer un combobox.
        
        El valor de "Categoria" depende del valor de "Tipo".
        
        # Si tipo = Ingreso Fijo, Categoria = [Salario]
        # Si tipo = Ingreso Variable, Categoria = [Extras]
        # Si tipo = Gasto Fijo, Categoria = [Vivienda, Servicios, Deudas, Deporte, Ahorro]
        # Si tipo = Gasto Variable, Categoria = [Alimentacion, Transporte, Diversion, Salud, Mesadas, Aseo, Apoyo, Otros]
        
        El valor de "Subcategoria" depende del valor de "Categoria".
        
        # Si categoria = Salario, Subcategoria = [Gobierno, Universidad]
        # Si categoria = Extras, Subcategoria = [Trading, Judicial]
        # Si categoria = Vivienda, Subcategoria = [Arriendo, Ama de casa]
        # Si categoria = Servicios, Subcategoria = [Agua, Luz, Gas, Internet, Celular]
        # Si categoria = Deudas, Subcategoria = [Copebis, Davivienda]
        # Si categoria = Deporte, Subcategoria = [Gimnasio, Futbol, Otros]
        # Si categoria = Ahorro, Subcategoria = [Copebis Karla, Copebis Daniel, Otros]
        # Si categoria = Educacion, Subcategoria = [Doctorado, Jardin]
        # Si categoria = Alimentacion, Subcategoria = [Mercado, Restaurantes, Otros]
        # Si categoria = Transporte, Subcategoria = [Gasolina, Transporte Publico, Otros]
        # Si categoria = Diversion, Subcategoria = [Viajes, Otros]
        # Si categoria = Salud, Subcategoria = [Medicamentos, Citas, Otros]
        # Si categoria = Mesadas, Subcategoria = [Daniel, Karla, Nicolas]
        # Si categoria = Aseo, Subcategoria = [Casa, Ropa, Automovil, Otros]
        # Si categoria = Apoyo, Subcategoria = [Daniel, Karla, Otros]
        # Si categoria = Otros, Subcategoria = [Otros]
        
        Si se cambia un valor de "Tipo", "Categoria" y "Subcategoria" deben limpiar.
        
        Si se cambia un valor de "Categoria", "Subcategoria" debe limpiar.
        
        '''

        lbl_categoria = Label(Manage_Frame, text="Categoria", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_categoria.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.categoria = StringVar()
        combo_categoria = ttk.Combobox(Manage_Frame, textvariable=self.categoria, font=("Consolas", 13, "bold"), state="readonly")
        combo_categoria['values'] = []
        combo_categoria.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_subcategoria = Label(Manage_Frame, text="Subcategoria", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_subcategoria.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.subcategoria = StringVar()
        combo_subcategoria = ttk.Combobox(Manage_Frame, textvariable=self.subcategoria, font=("Consolas", 13, "bold"), state="readonly")
        combo_subcategoria['values'] = []
        combo_subcategoria.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        def change_tipo(event):
            if self.tipo.get() == "Ingreso Fijo":
                combo_categoria['values'] = ("Salario")
            elif self.tipo.get() == "Ingreso Variable":
                combo_categoria['values'] = ("Extras")
            elif self.tipo.get() == "Gasto Fijo":
                combo_categoria['values'] = ("Vivienda", "Servicios", "Deudas", "Deporte", "Ahorro")
            elif self.tipo.get() == "Gasto Variable":
                combo_categoria['values'] = ("Alimentacion", "Transporte", "Diversion", "Salud", "Mesadas", "Aseo", "Apoyo", "Otros")
            else:
                combo_categoria['values'] = []
            self.categoria.set("")
            self.subcategoria.set("")

        def change_categoria(event):
            if self.categoria.get() == "Salario":
                combo_subcategoria['values'] = ("Gobierno", "Universidad")
            elif self.categoria.get() == "Extras":
                combo_subcategoria['values'] = ("Trading", "Judicial")
            elif self.categoria.get() == "Vivienda":
                combo_subcategoria['values'] = ("Arriendo", "Ama de casa")
            elif self.categoria.get() == "Servicios":
                combo_subcategoria['values'] = ("Agua", "Luz", "Gas", "Internet", "Celular")
            elif self.categoria.get() == "Deudas":
                combo_subcategoria['values'] = ("Copebis", "Davivienda")
            elif self.categoria.get() == "Deporte":
                combo_subcategoria['values'] = ("Gimnasio", "Futbol", "Otros")
            elif self.categoria.get() == "Ahorro":
                combo_subcategoria['values'] = ("Copebis Karla", "Copebis Daniel", "Otros")
            elif self.categoria.get() == "Educacion":
                combo_subcategoria['values'] = ("Doctorado", "Jardin")
            elif self.categoria.get() == "Alimentacion":
                combo_subcategoria['values'] = ("Mercado", "Restaurantes", "Otros")
            elif self.categoria.get() == "Transporte":
                combo_subcategoria['values'] = ("Gasolina", "Transporte Publico", "Otros")
            elif self.categoria.get() == "Diversion":
                combo_subcategoria['values'] = ("Viajes", "Otros")
            elif self.categoria.get() == "Salud":
                combo_subcategoria['values'] = ("Medicamentos", "Citas", "Otros")
            elif self.categoria.get() == "Mesadas":
                combo_subcategoria['values'] = ("Daniel", "Karla", "Nicolas")
            elif self.categoria.get() == "Aseo":
                combo_subcategoria['values'] = ("Casa", "Ropa", "Automovil", "Otros")
            elif self.categoria.get() == "Apoyo":
                combo_subcategoria['values'] = ("Daniel", "Karla", "Otros")
            elif self.categoria.get() == "Otros":
                combo_subcategoria['values'] = ("Otros")
            else:
                combo_subcategoria['values'] = []
            self.subcategoria.set("")

        combo_tipo.bind("<<ComboboxSelected>>", change_tipo)
        combo_categoria.bind("<<ComboboxSelected>>", change_categoria)

        ################################## MONTO ##################################
        # Etiqeta de Monto
        lbl_monto = Label(Manage_Frame, text="Monto", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_monto.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        # Entrada de Monto de tipo entero
        self.monto = IntVar()
        txt_monto = Entry(Manage_Frame, textvariable=self.monto, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_monto.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        ################################## FECHA ##################################

        # Etiqeta de Fecha
        lbl_fecha = Label(Manage_Frame, text="Fecha dd/mm/aa", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_fecha.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        # Entrada de Fecha de tipo fecha
        self.fecha = StringVar()
        txt_fecha = Entry(Manage_Frame, textvariable=self.fecha, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_fecha.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        ################################## DESCRIPCION ##################################

        # Etiqeta de Descripcion
        lbl_descripcion = Label(Manage_Frame, text="Descripcion", font=("Consolas", 15, "bold"), bg="black", fg="white")
        lbl_descripcion.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        # Texto de Descripcion
        #self.descripcion = StringVar()
        self.txt_descripcion = Text(Manage_Frame, width=30, height=4, font=("Consolas", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_descripcion.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        ################################## BOTONES ##################################

        # FRAME DE BOTONES
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="blue")
        btn_Frame.place(x=15, y=510, width=430)

        # Boton de Agregar
        Addbtn = Button(btn_Frame, text="Agregar", width=7).grid(row=0, column=0, padx=10, pady=10)
        # Boton de Actualizar
        updatebtn = Button(btn_Frame, text="Actualizar", width=7).grid(row=0, column=1, padx=10, pady=10)
        # Boton de Borrar
        deletebtn = Button(btn_Frame, text="Borrar", width=7).grid(row=0, column=2, padx=10, pady=10)
        # Boton de Limpiar
        clearbtn = Button(btn_Frame, text="Limpiar", width=7).grid(row=0, column=3, padx=10, pady=10)


        ################################## Marco de consulta ##################################
        Detail_Frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="black")
        Detail_Frame.place(x=560, y=100, width=780, height=580)

        ################################## busqueda ##################################
        self.buscar_por = StringVar()
        self.buscar_txt = StringVar()

        lbl_search = Label(Detail_Frame, text="Buscar por", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # combobox de busqueda que tenga los valores de tipo, categoria y subcategoria y fecha
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.buscar_por, font=("Consolas", 13, "bold"), state="readonly", width=10)
        combo_search['values'] = ("Tipo", "Categoria", "Subcategoria", "Fecha")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        # Entrada de busqueda
        txt_search = Entry(Detail_Frame, textvariable=self.buscar_txt, font=("Consolas", 10, "bold"), bd=5, relief=GROOVE, width=20)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        # Boton de busqueda
        searchbtn = Button(Detail_Frame, text="Buscar", width=7, pady=5).grid(row=0, column=3, padx=10, pady=10)
        # Boton de mostrar todo
        showallbtn = Button(Detail_Frame, text="Mostrar todo", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        ################################## Tabla de consulta ##################################
        # Tabla de consulta
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Finanzas_table = ttk.Treeview(Table_Frame, columns=("Id", "Tipo", "Categoria", "Subcategoria", "Monto", "Fecha", "Descripcion"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Finanzas_table.xview)
        scroll_y.config(command=self.Finanzas_table.yview)
        self.Finanzas_table.heading("Id", text="Id")
        self.Finanzas_table.heading("Tipo", text="Tipo")
        self.Finanzas_table.heading("Categoria", text="Categoria")
        self.Finanzas_table.heading("Subcategoria", text="Subcategoria")
        self.Finanzas_table.heading("Monto", text="Monto")
        self.Finanzas_table.heading("Fecha", text="Fecha")
        self.Finanzas_table.heading("Descripcion", text="Descripcion")
        self.Finanzas_table['show'] = 'headings'
        self.Finanzas_table.column("Id", width=50)
        self.Finanzas_table.column("Tipo", width=100)
        self.Finanzas_table.column("Categoria", width=100)
        self.Finanzas_table.column("Subcategoria", width=100)
        self.Finanzas_table.column("Monto", width=100)
        self.Finanzas_table.column("Fecha", width=100)
        self.Finanzas_table.column("Descripcion", width=100)
        self.Finanzas_table.pack(fill=BOTH, expand=1)



    def mostrar_saldo(self):
        # Crea la ventana emergente
        saldo_window = Toplevel()
        saldo_window.title("Saldo Actual")

        # Crea un marco para colocar los widgets
        Manage_Frame = Frame(saldo_window)
        Manage_Frame.pack(fill="both", expand=True)

        # Crea las etiquetas y cajas de texto
        lbl_efectivo = Label(Manage_Frame, text="Efectivo:")
        lbl_efectivo.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        txt_efectivo = Entry(Manage_Frame)
        txt_efectivo.grid(row=0, column=1, padx=10, pady=5)

        lbl_davivienda_k = Label(Manage_Frame, text="Davivienda Karla:")
        lbl_davivienda_k.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        txt_davivienda_k = Entry(Manage_Frame)
        txt_davivienda_k.grid(row=1, column=1, padx=10, pady=5)

        lbl_davivienda_d = Label(Manage_Frame, text="Davivienda Daniel:")
        lbl_davivienda_d.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        txt_davivienda_d = Entry(Manage_Frame)
        txt_davivienda_d.grid(row=2, column=1, padx=10, pady=5)

        lbl_nequi_k = Label(Manage_Frame, text="Nequi Karla:")
        lbl_nequi_k.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        txt_nequi_k = Entry(Manage_Frame)
        txt_nequi_k.grid(row=3, column=1, padx=10, pady=5)

        lbl_nequi_d = Label(Manage_Frame, text="Nequi Daniel :")
        lbl_nequi_d.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        txt_nequi_d = Entry(Manage_Frame)
        txt_nequi_d.grid(row=4, column=1, padx=10, pady=5)

        lbl_billetera = Label(Manage_Frame, text="Billetera V:")
        lbl_billetera.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        txt_billetera = Entry(Manage_Frame)
        txt_billetera.grid(row=5, column=1, padx=10, pady=5)

        lbl_total = Label(Manage_Frame, text="Total:")
        lbl_total.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        txt_total = Entry(Manage_Frame)
        txt_total.grid(row=6, column=1, padx=10, pady=5)

        # Asigna valores a las cajas de texto
        txt_efectivo.insert(0, "0")
        txt_davivienda_k.insert(0, "0")
        txt_davivienda_d.insert(0, "0")
        txt_nequi_k.insert(0, "0")
        txt_nequi_d.insert(0, "0")
        txt_billetera.insert(0, "0")

        # boton para mostrar el total
        btn_total = Button(Manage_Frame, text="Total")
        btn_total.grid(row=7, column=1, sticky="e", padx=10, pady=5)

















    '''
    def mostrar_saldo(self):
        self.saldo = 0
        self.saldo = self.saldo + self.monto
        self.lbl_saldo.config(text=self.saldo)

        

    def agregar_montos(self):
        if self.tipo_var.get() == "" or self.categoria_var.get() == "" or self.subcategoria_var.get() == "" or self.monto_var.get() == "" or self.fecha_var.get() == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
        else:
            con = pymysql.connect(host="localhost", user="root", password="Alejo263.", database="finanzApp")
            cur = con.cursor()
            cur.execute("insert into finanzas values(%s,%s,%s,%s,%s,%s,%s)", (
                self.tipo_var.get(),
                self.categoria_var.get(),
                self.subcategoria_var.get(),
                self.monto_var.get(),
                self.fecha_var.get(),
                self.descripcion_txt.get('1.0', END),
                self.id_var.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Exito", "Registro agregado exitosamente")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Alejo263.", database="finanzApp")
        cur = con.cursor()
        cur.execute("select * from montos")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Finanzas_table.delete(*self.Finanzas_table.get_children())
            for row in rows:
                self.Finanzas_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.tipo_var.set("")
        self.categoria_var.set("")
        self.subcategoria_var.set("")
        self.monto_var.set("")
        self.fecha_var.set("")
        self.descripcion_txt.delete("1.0", END)
        self.id_var.set("")




    def get_cursor(self, ev):
        cursor_row = self.Finanzas_table.focus()
        contents = self.Finanzas_table.item(cursor_row)
        row = contents['values']
        #print(row)


        self.tipo.set(row[0])
        self.categoria.set(row[1])
        self.subcategoria.set(row[2])
        self.monto.set(row[3])
        self.fecha.set(row[4])
        self.txt_descripcion.delete("1.0", END)
        self.txt_descripcion.insert(END, row[5])
        self.id = row[6]


    def update_data(self):
        conexion = pymysql.connect(host="localhost", user="root", password="Alejo263.", database="finanzApp")
        cursor = conexion.cursor()
        cursor.execute("UPDATE montos SET tipo=%s, categoria=%s, subcategoria=%s, monto=%s, fecha=%s, descripcion=%s WHERE id=%s",
                          (self.tipo.get(),
                            self.categoria.get(),
                            self.subcategoria.get(),
                            self.monto.get(),
                            self.fecha.get(),
                            self.txt_descripcion.get("1.0", END),
                            self.id()))
        conexion.commit()
        self.fetch_data()
        self.clear()
        conexion.close()

        # Agrega el registro
        messagebox.showinfo("FinanzApp", "Registro actualizado con exito")

    def delete_data(self):
        conexion = pymysql.connect(host="localhost", user="root", password="Alejo263.", database="finanzApp")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM montos WHERE id=%s", self.id)

        conexion.commit()
        self.fetch_data()
        self.clear()
        conexion.close()

        # Agrega el registro
        messagebox.showinfo("FinanzApp", "Registro eliminado con exito")

    def search_data(self):
        conexion = pymysql.connect(host="localhost", user="root", password="Alejo263.", database="finanzApp")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM montos WHERE " + str(self.buscar_por.get()) + " LIKE '%" + str(self.buscar_txt.get()) + "%'")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Finanzas_table.delete(*self.Finanzas_table.get_children())
            for row in rows:
                self.Finanzas_table.insert('', END, values=row)
            conexion.commit()
        conexion.close()
    '''


ventana = Tk()
app = FinanzApp(ventana)
ventana.mainloop()