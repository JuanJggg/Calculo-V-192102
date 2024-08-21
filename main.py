import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("1024x720")
app.title("Suma y resta de matrices 192102")

def ResolMatriz(rowsm1,rowsm2,columnsm1,columnsm2):
    for widget in app.winfo_children():
        widget.destroy()
    
    fila1 = int(rowsm1)
    columna1 = int(columnsm1)
    fila2 = int(rowsm2)
    columna2 = int(columnsm2)

    for i in range(fila1):
        for j in range(columna1):
            boton = customtkinter.CTkButton(app, text=f"({i}, {j})")
            boton.grid(row=i, column=j, padx=10, pady=10)
    
    for a in range(fila2):
        for b in range(columna2):
            boton = customtkinter.CTkButton(app, text=f"({a}, {b})")
            boton.grid(row=a, column=(b+j+12), padx=10, pady=10)
                
    


def comienzo():
    label1 = customtkinter.CTkLabel(app, text="Ingresa la cantidad de filas y columnas de la primera matriz", font=("Arial",20))
    label1.place( relx = 0.5, rely = 0.35, anchor = customtkinter.CENTER)
    inputm1 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las filas", width=180)
    inputm1.place( relx = 0.5, rely = 0.4, anchor = customtkinter.CENTER)
    inputm2 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las Columnas", width=180)
    inputm2.place( relx = 0.5, rely = 0.45, anchor = customtkinter.CENTER)

    label2 = customtkinter.CTkLabel(app, text="Ingresa la cantidad de filas y columnas de la segunda matriz", font=("Arial",20))
    label2.place( relx = 0.5, rely = 0.52, anchor = customtkinter.CENTER)
    inputm3 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las filas", width=180)
    inputm3.place( relx = 0.5, rely = 0.57, anchor = customtkinter.CENTER)
    inputm4 = customtkinter.CTkEntry(app, placeholder_text="Ingresa las columnas", width=180)
    inputm4.place( relx = 0.5, rely = 0.62, anchor = customtkinter.CENTER)
    

    def empezarboton():
        rowsm1 = inputm1.get()
        columnsm1 = inputm2.get()
        rowsm2 = inputm3.get()
        columnsm2 = inputm4.get()

        if rowsm1 == rowsm2 and columnsm1 == columnsm2:
            ResolMatriz(rowsm1,rowsm2,columnsm1,columnsm2)
        else:
            alert = customtkinter.CTkToplevel(app)
            alert.title("¡Error!")
            alert.geometry("500x250")
            message = customtkinter.CTkLabel(alert, text="Para poder sumar dos matrcies deben tener igual tamaño n*n")
            message.place( relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)
            cerrar = customtkinter.CTkButton(alert, text="Volver a intentar", command=alert.destroy)
            cerrar.place( relx = 0.5, rely = 0.6, anchor = customtkinter.CENTER)

    buttom = customtkinter.CTkButton(app, text="Continuar", command=empezarboton)
    buttom.place( relx = 0.5, rely = 0.7, anchor = customtkinter.CENTER)

comienzo()

app.mainloop()