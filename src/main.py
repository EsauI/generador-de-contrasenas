import secrets
import string
from tkinter import messagebox


#Valida que la longitud sea un número válido
def validar_longitud(longitud_str):
    try:
        longitud = int(longitud_str)
        if longitud < 4:
            return False, #La longitud mínima es 4
        if longitud > 50:
            return False, #La longitud máxima es 50
        return True, ""
    except ValueError:
        return False, "Ingresa un número válido"

#Genera una contraseña aleatoria
def generar_contraseña(longitud_str):
    try:
        # Validar longitud
        es_valido, mensaje = validar_longitud(longitud_str)
        if not es_valido:
            messagebox.showerror("Error", mensaje)
            return None
        
        longitud = int(longitud_str)
        
        # Usar todos los tipos de caracteres
        caracteres = (string.ascii_lowercase + 
                     string.ascii_uppercase + 
                     string.digits + 
                     "!@#$%&*")
        
        # Genera una contraseña completamente aleatoria
        contraseña = ''
        for i in range(longitud):
            contraseña += secrets.choice(caracteres)
        
        return contraseña
        
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {str(e)}")
        return None
