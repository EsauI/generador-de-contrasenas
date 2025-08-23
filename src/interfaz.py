import tkinter as tk
from tkinter import messagebox
from main import validar_longitud, validar_opciones, construir_caracteres, gencontraseña, evaluar_seguridad

# Copia la contraseña al portapapeles
def copiar_al_portapapeles():
    contraseña = entry_resultado.get()
    if contraseña:
        ventana.clipboard_clear()
        ventana.clipboard_append(contraseña)
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar")

# Maneja todo el proceso de generación de contraseñas
def generar_contraseña():
    try:
        longitud_str = entry_longitud.get()

        # Validar longitud
        es_valido, mensaje = validar_longitud(longitud_str)
        if not es_valido:
            messagebox.showerror("Error", mensaje)
            return

        # Obtener opciones
        opciones = (var_mayusculas.get(), var_numeros.get(), var_simbolos.get())

        # Validar opciones
        es_valido, mensaje = validar_opciones(*opciones)
        if not es_valido:
            messagebox.showerror("Error", mensaje)
            return

        # Generar contraseña
        caracteres = construir_caracteres(*opciones)
        contraseña = gencontraseña(int(longitud_str), caracteres)

        # Análisis de seguridad
        seguridad, color = evaluar_seguridad(contraseña)

        # PRIMERO: Mostrar contraseña y análisis en pantalla
        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contraseña)
        entry_resultado.config(state="readonly")
        label_seguridad.config(text=f"Seguridad: {seguridad}", fg=color)

        # Actualizar la ventana para que se vea la contraseña
        ventana.update()

        # Pregunta si quiere copiar la contraseña
        respuesta = messagebox.askyesno("Copiar", "¿Deseas copiar la contraseña al portapapeles?")
        if respuesta:
            ventana.clipboard_clear()
            ventana.clipboard_append(contraseña)
            messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")

        # Pregunta si quiere generar otra contraseña
        otra = messagebox.askyesno("Continuar", "¿Generar otra contraseña?")
        if otra:
            # Limpia los campos para una nueva configuración
            entry_longitud.delete(0, tk.END)
            entry_longitud.insert(0, "8")
            entry_resultado.config(state="normal")
            entry_resultado.delete(0, tk.END)
            entry_resultado.config(state="readonly")
            label_seguridad.config(text="")
            # Resetea los checkboxes a valores por defecto
            var_mayusculas.set(True)
            var_numeros.set(True)
            var_simbolos.set(False)

    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {str(e)}")

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x555")
ventana.configure(bg="white")
ventana.resizable(False, False)

# Variables
var_mayusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

# Frame principal
frame_principal = tk.Frame(ventana, bg="white")
frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Frame de controles
frame_controles = tk.Frame(frame_principal, bg="white")
frame_controles.pack(fill=tk.BOTH, expand=True)

# Título principal
titulo = tk.Label(frame_controles, text="Generador de Contraseñas",
                  font=("Monaco", 18, "bold"), bg="white", fg="black")
titulo.pack(pady=(0, 30))

# Frame de configuración
frame_configuracion = tk.LabelFrame(frame_controles, text="Configuración",
                                    font=("Monaco", 12, "bold"), bg="white", fg="black")
frame_configuracion.pack(fill=tk.X, pady=(0, 20))

tk.Label(frame_configuracion, text="Longitud de la contraseña:",
         font=("Monaco", 11), bg="white", fg="black").pack(pady=(10, 5))

entry_longitud = tk.Entry(frame_configuracion, font=("Monaco", 12), justify="center", width=10)
entry_longitud.pack(pady=(0, 10))
entry_longitud.insert(0, "8")

# Opciones
opciones = tk.LabelFrame(frame_controles, text="Opciones de Caracteres",
                               font=("Monaco", 12, "bold"), bg="white", fg="black")
opciones.pack(fill=tk.X, pady=(0, 20))

tk.Checkbutton(opciones, text="✓ Incluir mayúsculas (A-Z)", variable=var_mayusculas,
               font=("Monaco", 11), bg="white", fg="black", activebackground="white").pack(anchor=tk.W, padx=10, pady=5)

tk.Checkbutton(opciones, text="✓ Incluir números (0-9)", variable=var_numeros,
               font=("Monaco", 11), bg="white", fg="black", activebackground="white").pack(anchor=tk.W, padx=10, pady=5)

tk.Checkbutton(opciones, text="✓ Incluir símbolos (!@#$%)", variable=var_simbolos,
               font=("Monaco", 11), bg="white", fg="black", activebackground="white").pack(anchor=tk.W, padx=10, pady=(5, 15))

# Frame de botones
frame_botones = tk.Frame(frame_controles, bg="white")
frame_botones.pack(pady=(0, 20))

btn_generar = tk.Button(frame_botones, text="Generar Contraseña", command=generar_contraseña,
                        font=("Monaco", 12, "bold"), bg="lightgray", fg="black",
                        padx=20, pady=10, cursor="hand2")
btn_generar.pack(side=tk.LEFT, padx=(0, 10))

btn_copiar = tk.Button(frame_botones, text="Copiar", command=copiar_al_portapapeles,
                       font=("Monaco", 12, "bold"), bg="lightgray", fg="black",
                       padx=20, pady=10, cursor="hand2")
btn_copiar.pack(side=tk.LEFT)

# Frame de resultado
resultado = tk.LabelFrame(frame_controles, text="Contraseña Generada",
                                font=("Monaco", 12, "bold"), bg="white", fg="black")
resultado.pack(fill=tk.X, pady=(0, 10))

entry_resultado = tk.Entry(resultado, font=("Monaco", 14, "bold"), justify="center",
                           state="readonly", bg="white", fg="white", relief=tk.RIDGE, bd=2)
entry_resultado.pack(pady=15, padx=10, fill=tk.X)

# Label de seguridad
label_seguridad = tk.Label(resultado, text="", font=("Monaco", 12, "bold"), bg="white")
label_seguridad.pack(pady=(0, 10))

# Iniciar la aplicación
if __name__ == "__main__":
    ventana.mainloop()
