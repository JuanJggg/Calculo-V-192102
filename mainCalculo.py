import customtkinter

# Configuración de la apariencia de la interfaz (modo oscuro y tema verde)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Creación de la ventana principal con tamaño 1024x720 y título
app = customtkinter.CTk()
app.geometry("1024x720")
app.title("Suma y resta de matrices 192102")


def ResolMatriz(rowsm1, rowsm2, columnsm1, columnsm2):
    # Limpiar la pantalla al cambiar de función
    for widget in app.winfo_children():
        widget.destroy()
    
    # Lista donde se almacenarán las entradas de las dos matrices
    entrya = []
    entryb = []

    # Convertir las entradas de filas y columnas a números enteros
    fila1 = int(rowsm1)
    columna1 = int(columnsm1)
    fila2 = int(rowsm2)
    columna2 = int(columnsm2)

    # Crear un contenedor principal (opcional, pero organiza mejor los elementos)
    main_frame = customtkinter.CTkFrame(app)
    main_frame.grid(row=0, column=0, padx=20, pady=20)

    # Configurar el contenedor principal para centrar todo
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure([0, 1, 2], weight=1)

    # Crear una sección para la primera matriz
    frame1 = customtkinter.CTkFrame(main_frame)
    frame1.grid(row=0, column=0, padx=10, pady=10)

    # Crear una sección para la segunda matriz
    frame2 = customtkinter.CTkFrame(main_frame)
    frame2.grid(row=0, column=2, padx=10, pady=10)

    # Crear una sección para mostrar el resultado
    frame3 = customtkinter.CTkFrame(main_frame)
    frame3.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Botón para regresar a la pantalla inicial
    button2 = customtkinter.CTkButton(main_frame, text="Volver a Inicio", command=comienzo)
    button2.grid(row=3, column=1, columnspan=1, padx=10, pady=1)

    # Crear los campos de entrada para la primera matriz
    for i in range(fila1):
        filaRone = []  # Lista para almacenar cada fila de entradas
        for j in range(columna1):
            # Crear una entrada con texto de marcador de posición indicando la posición
            entrada = customtkinter.CTkEntry(frame1, placeholder_text=f"({i}, {j})", placeholder_text_color="white", justify="center")
            entrada.grid(row=i, column=j, padx=8, pady=20)
            entrada.insert(0,"0")  # Insertar un valor inicial de 0
            filaRone.append(entrada)  # Agregar la entrada a la lista de la fila
        entrya.append(filaRone)  # Agregar la fila completa a la matriz

    # Crear los campos de entrada para la segunda matriz
    for a in range(fila2):
        filaRtwo = []  # Lista para almacenar cada fila de entradas
        for b in range(columna2):
            # Crear una entrada con texto de marcador de posición indicando la posición
            entrada = customtkinter.CTkEntry(frame2, placeholder_text=f"({a}, {b})", placeholder_text_color="white", justify="center")
            entrada.grid(row=a, column=b, padx=5, pady=20)
            entrada.insert(0,"0")  # Insertar un valor inicial de 0
            filaRtwo.append(entrada)  # Agregar la entrada a la lista de la fila
        entryb.append(filaRtwo)  # Agregar la fila completa a la matriz

    # Función para convertir los valores de entrada en una lista (matriz)
    def leerMatriz(entries):
        matriz = []  # Lista para almacenar la matriz completa
        for fila_entries in entries:
            fila = []  # Lista para cada fila
            for entry in fila_entries:
                try:
                    valor = float(entry.get())  # Intentar convertir el valor a número
                    fila.append(valor)  # Agregar el valor a la fila
                except ValueError:  # Si no es un número, mostrar un mensaje de error
                    alert = customtkinter.CTkToplevel(app)
                    alert.title("¡Error!")
                    alert.geometry("800x250")
                    message = customtkinter.CTkLabel(alert, text="Todos los valores deben ser números enteros o decimales.")
                    message.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
                    cerrar = customtkinter.CTkButton(alert, text="Volver a intentar", command=alert.destroy)
                    cerrar.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
                    return None  # Detener la ejecución si hay un error
            matriz.append(fila)  # Agregar la fila completa a la matriz
        return matriz  # Devolver la matriz completa

    # Función para mostrar el resultado en el tercer frame
    def mostrar_resultado(matriz):
        for i in range(fila1):
            for j in range(columna1):
                entrada = customtkinter.CTkEntry(frame3, justify="center")
                entrada.grid(row=i, column=j, padx=5, pady=20)
                entrada.insert(0, f"{matriz[i][j]:.4f}")  # Mostrar el resultado con 4 decimales

    # Función para sumar las matrices
    def sumar():
        # Mostrar un signo de "+" en el centro
        label = customtkinter.CTkLabel(main_frame, text=" + ", font=("Arial", 24)) 
        label.grid(row=0, column=1, padx=10, pady=10)
        matriz1 = leerMatriz(entrya)  # Leer los valores de la primera matriz
        matriz2 = leerMatriz(entryb)  # Leer los valores de la segunda matriz
        if matriz1 is not None and matriz2 is not None:
            # Sumar las dos matrices
            resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(columna1)] for i in range(fila1)]
            mostrar_resultado(resultado)  # Mostrar el resultado

    # Función para restar las matrices
    def restar():
        # Mostrar un signo de "-" en el centro
        label = customtkinter.CTkLabel(main_frame, text=" - ", font=("Arial", 24)) 
        label.grid(row=0, column=1, padx=10, pady=10)
        matriz1 = leerMatriz(entrya)  # Leer los valores de la primera matriz
        matriz2 = leerMatriz(entryb)  # Leer los valores de la segunda matriz
        if matriz1 is not None and matriz2 is not None:
            # Restar las dos matrices
            resultado = [[matriz1[i][j] - matriz2[i][j] for j in range(columna1)] for i in range(fila1)]
            mostrar_resultado(resultado)  # Mostrar el resultado

    # Botón para ejecutar la función de sumar
    button3 = customtkinter.CTkButton(main_frame, text="Sumar", command=sumar)
    button3.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Botón para ejecutar la función de restar
    button4 = customtkinter.CTkButton(main_frame, text="Restar", command=restar)
    button4.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Función que se ejecuta al inicio de la aplicación
def comienzo():
    # Limpiar la pantalla de widgets anteriores
    for widget in app.winfo_children():
        widget.destroy()
    
    # Etiquetas y entradas para que el usuario ingrese las dimensiones de las matrices
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
    inputm4 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las Columnas", width=180)
    inputm4.place(relx=0.5, rely=0.62, anchor=customtkinter.CENTER)

    # Botón para continuar y enviar los tamaños de las matrices ingresadas
    button = customtkinter.CTkButton(app, text="Continuar",command=lambda: ResolMatriz(inputm1.get(), inputm3.get(), inputm2.get(), inputm4.get()))
    button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


# Ejecutar la función de inicio al abrir la aplicación
comienzo()

# Iniciar el bucle principal de la ventana
app.mainloop()