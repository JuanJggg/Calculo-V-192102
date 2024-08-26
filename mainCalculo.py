import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1024x720")
app.title("Suma y resta de matrices 192102")

def ResolMatriz(rowsm1, rowsm2, columnsm1, columnsm2):

    for widget in app.winfo_children():
        widget.destroy()
    
    entrya = []
    entryb = []

    fila1 = int(rowsm1)
    columna1 = int(columnsm1)
    fila2 = int(rowsm2)
    columna2 = int(columnsm2)

    # Crear un Frame para contener todo (opcional, pero ayuda a mantener la estructura)
    main_frame = customtkinter.CTkFrame(app)
    main_frame.grid(row=0, column=0, padx=20, pady=20)

    # Configurar la ventana o el frame principal para centrar todo
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure([0, 1, 2], weight=1)

    # Primer Frame para la primera matriz
    frame1 = customtkinter.CTkFrame(main_frame)
    frame1.grid(row=0, column=0, padx=10, pady=10)

    # Segundo Frame para la segunda matriz
    frame2 = customtkinter.CTkFrame(main_frame)
    frame2.grid(row=0, column=2, padx=10, pady=10)

    # Tercer Frame para la matriz resultante
    frame3 = customtkinter.CTkFrame(main_frame)
    frame3.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    button2 = customtkinter.CTkButton(main_frame, text="Volver a Inicio", command=comienzo)
    button2.grid(row=3, column=1, columnspan=1, padx=10, pady=1)

    for i in range(fila1):
        filaRone = []
        for j in range(columna1):
            entrada = customtkinter.CTkEntry(frame1, placeholder_text=f"({i}, {j})", placeholder_text_color="white", justify="center")
            entrada.grid(row=i, column=j, padx=5, pady=20)
            entrada.insert(0, "0")
            filaRone.append(entrada)
        entrya.append(filaRone)
    
    for a in range(fila2):
        filaRtwo = []
        for b in range(columna2):
            entrada = customtkinter.CTkEntry(frame2, placeholder_text=f"({a}, {b})", placeholder_text_color="white", justify="center")
            entrada.grid(row=a, column=b, padx=5, pady=20)
            entrada.insert(0, "0") 
            filaRtwo.append(entrada)
        entryb.append(filaRtwo)

    def leerMatriz(entries):
        """
        Convierte los valores de los campos de entrada en una matriz (lista de listas de enteros).
        """
        matriz = []
        for fila_entries in entries:
            fila = []
            for entry in fila_entries:
                try:
                    valor = int(entry.get())
                    fila.append(valor)
                except ValueError:
                    alert = customtkinter.CTkToplevel(app)
                    alert.title("¡Error!")
                    alert.geometry("500x250")
                    message = customtkinter.CTkLabel(alert, text="Todos los valores deben ser números enteros.")
                    message.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
                    cerrar = customtkinter.CTkButton(alert, text="Volver a intentar", command=alert.destroy)
                    cerrar.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
                    return None
            matriz.append(fila)
        return matriz

    def mostrar_resultado(matriz):
        for i in range(fila1):
            for j in range(columna1):
                entrada = customtkinter.CTkEntry(frame3, justify="center")
                entrada.grid(row=i, column=j, padx=5, pady=20)
                entrada.insert(0, str(matriz[i][j]))

    def sumar():
        label = customtkinter.CTkLabel(main_frame, text=" + ", font=("Arial", 24)) 
        label.grid(row=0, column=1, padx=10, pady=10)
        matriz1 = leerMatriz(entrya)
        matriz2 = leerMatriz(entryb)
        if matriz1 is not None and matriz2 is not None:
            resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columna1)] for i in range(fila1)]
            mostrar_resultado(resultado)

    def restar():
        label = customtkinter.CTkLabel(main_frame, text=" - ", font=("Arial", 24)) 
        label.grid(row=0, column=1, padx=10, pady=10)
        matriz1 = leerMatriz(entrya)
        matriz2 = leerMatriz(entryb)
        if matriz1 is not None and matriz2 is not None:
            resultado = [[matriz1[i][j] - matriz2[i][j] for j in range(columna1)] for i in range(fila1)]
            mostrar_resultado(resultado)

    button3 = customtkinter.CTkButton(main_frame, text="Sumar", command=sumar)
    button3.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    button4 = customtkinter.CTkButton(main_frame, text="Restar", command=restar)
    button4.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def comienzo():
    for widget in app.winfo_children():
        widget.destroy()
    
    label1 = customtkinter.CTkLabel(app, text="Ingresa la cantidad de filas y columnas de la primera matriz", font=("Arial", 20))
    label1.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
    inputm1 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las filas", width=180)
    inputm1.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
    inputm2 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las Columnas", width=180)
    inputm2.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

    label2 = customtkinter.CTkLabel(app, text="Ingresa la cantidad de filas y columnas de la segunda matriz", font=("Arial", 20))
    label2.place(relx=0.5, rely=0.52, anchor=customtkinter.CENTER)
    inputm3 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las filas", width=180)
    inputm3.place(relx=0.5, rely=0.57, anchor=customtkinter.CENTER)
    inputm4 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las columnas", width=180)
    inputm4.place(relx=0.5, rely=0.62, anchor=customtkinter.CENTER)
    
    def empezarboton():
        rowsm1 = inputm1.get()
        columnsm1 = inputm2.get()
        rowsm2 = inputm3.get()
        columnsm2 = inputm4.get()

        if rowsm1 == rowsm2 and columnsm1 == columnsm2:
            ResolMatriz(rowsm1, rowsm2, columnsm1, columnsm2)
        else:
            alert = customtkinter.CTkToplevel(app)
            alert.title("¡Error!")
            alert.geometry("500x250")
            message = customtkinter.CTkLabel(alert, text="Para poder sumar o restar dos matrices deben tener igual tamaño n*n")
            message.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
            cerrar = customtkinter.CTkButton(alert, text="Volver a intentar", command=alert.destroy)
            cerrar.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

    boton = customtkinter.CTkButton(app, text="Continuar", command=empezarboton)
    boton.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

comienzo()
app.mainloop()