from tkinter import *
from tkinter import ttk
import pymysql


class FinanzApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("FinanzApp")
        self.ventana.geometry("1360x700+0+0")
        self.ventana.resizable(False, False)

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


        # Entrada de tipo entero Saldo Actual
        self.saldo = IntVar()
        txt_saldo_actual = Entry(Manage_Frame, textvariable=self.saldo, font=("Consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_saldo_actual.grid(row=1, column=1, pady=10, padx=20, sticky="w")






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
        self.descripcion = StringVar()
        txt_descripcion = Text(Manage_Frame, width=30, height=4, font=("Consolas", 10, "bold"), bd=5, relief=GROOVE)
        txt_descripcion.grid(row=7, column=1, pady=10, padx=20, sticky="w")

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
        lbl_search = Label(Detail_Frame, text="Buscar por", bg="black", fg="white", font=("Consolas", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # combobox de busqueda que tenga los valores de tipo, categoria y subcategoria y fecha
        combo_search = ttk.Combobox(Detail_Frame, font=("Consolas", 13, "bold"), state="readonly", width=10)
        combo_search['values'] = ("Tipo", "Categoria", "Subcategoria", "Fecha")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        # Entrada de busqueda
        txt_search = Entry(Detail_Frame, font=("Consolas", 10, "bold"), bd=5, relief=GROOVE, width=20)
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
        Finanzas_table = ttk.Treeview(Table_Frame, columns=("tipo", "categoria", "subcategoria", "monto", "fecha", "descripcion"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Finanzas_table.xview)
        scroll_y.config(command=Finanzas_table.yview)
        Finanzas_table.heading("tipo", text="Tipo")
        Finanzas_table.heading("categoria", text="Categoria")
        Finanzas_table.heading("subcategoria", text="Subcategoria")
        Finanzas_table.heading("monto", text="Monto")
        Finanzas_table.heading("fecha", text="Fecha")
        Finanzas_table.heading("descripcion", text="Descripcion")
        Finanzas_table['show'] = 'headings'
        Finanzas_table.column("tipo", width=100)
        Finanzas_table.column("categoria", width=100)
        Finanzas_table.column("subcategoria", width=100)
        Finanzas_table.column("monto", width=100)
        Finanzas_table.column("fecha", width=100)
        Finanzas_table.column("descripcion", width=100)
        Finanzas_table.pack(fill=BOTH, expand=1)





ventana = Tk()
app = FinanzApp(ventana)
ventana.mainloop()