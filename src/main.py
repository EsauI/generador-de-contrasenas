import secrets
import string

#Valida que la longitud sea un número válido
def validar_longitud(longitud_str):
    try:
        longitud = int(longitud_str)
        if longitud < 4:
            return False, "La longitud mínima es 4"
        if longitud > 50:
            return False, "La longitud máxima es 50"
        return True, ""
    except ValueError:
        return False, "Ingresa un número válido"

def validar_opciones(mayusculas, numeros, simbolos):
    if not (mayusculas or numeros or simbolos):
        return False, "Selecciona al menos una opción"
    return True, ""

# Construye el conjunto de caracteres según las opciones seleccionadas
def construir_caracteres(mayusculas, numeros, simbolos):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%"
    return caracteres

# Genera la contraseña con los parámetros especificados
def gencontraseña(longitud, caracteres):
    # Para longitudes pequeñas
    if longitud <= 2:
        return ''.join(secrets.choice(caracteres) for _ in range(longitud))

    # Para longitudes mayores, garantizar al menos un carácter de cada tipo
    contraseña = []
    tipos = [string.ascii_lowercase]

    # Determinar qué tipos están disponibles
    if any(c in string.ascii_uppercase for c in caracteres):
        tipos.append(string.ascii_uppercase)
    if any(c in string.digits for c in caracteres):
        tipos.append(string.digits)
    if any(c in "!@#$%" for c in caracteres):
        tipos.append("!@#$%")

    # Agregar al menos un carácter de cada tipo disponible
    for tipo in tipos[:longitud]:
        contraseña.append(secrets.choice(tipo))

    # Completar con caracteres aleatorios
    while len(contraseña) < longitud:
        contraseña.append(secrets.choice(caracteres))

    # Mezclar
    secrets.SystemRandom().shuffle(contraseña)

    return ''.join(contraseña)

#Evalúa la seguridad de la contraseña
def evaluar_seguridad(contraseña):
    puntos = 0
    longitud = len(contraseña)
    # Puntos por longitud
    if longitud >= 8:
        puntos += 2
    if longitud >= 12:
        puntos += 1
    # Puntos por tipos de caracteres
    if any(c.islower() for c in contraseña):
        puntos += 1
    if any(c.isupper() for c in contraseña):
        puntos += 1
    if any(c.isdigit() for c in contraseña):
        puntos += 1
    if any(c in "!@#$%" for c in contraseña):
        puntos += 2
    # Clasificar fortaleza
    if puntos <= 3:
        return "Débil", "#ff4444"
    elif puntos <= 5:
        return "Media", "#ff8800"
    else:
        return "Fuerte", "#00aa00"
