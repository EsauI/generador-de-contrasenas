import tkinter as tk
from main import generar_contraseña

# Ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("350x300")


#Maneja la generación de contraseña y actualiza la interfaz
def generador():
    longitud_str = entry_longitud.get()
    contraseña = generar_contraseña(longitud_str)
    
    if contraseña is not None:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contraseña)

# Título
titulo = tk.Label(ventana, text="Generador seguro de Contraseñas", font=("Arial", 14, "bold"))
titulo.pack(pady=15)

# Campo para ingresar la longitud
label_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)

entry_longitud = tk.Entry(ventana, justify="center", font=("Arial", 12))
entry_longitud.pack(pady=5)
entry_longitud.insert(0, "12")  # Valor por defecto

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generador, 
                         font=("Arial", 11), bg="#4CAF50", fg="black", pady=5)
boton_generar.pack(pady=15)

# Campo para mostrar resultado
entry_resultado = tk.Entry(ventana, font=("Arial", 12), justify="center", width=40)
entry_resultado.pack(pady=10)

# Iniciar la aplicación
if __name__ == "__main__":
    ventana.mainloop()
