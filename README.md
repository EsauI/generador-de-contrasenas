# Generador de Contraseñas

---

## 📋 **DATOS DEL PROYECTO**

- **Nombre del Proyecto:** El impacto de las nuevas tecnologías en la sociedad: visualización del futuro.
- **Proyecto:** Generador de Contraseñas
- **Autor:** Esaul

---

## 🎯 **OBJETIVO DEL PROGRAMA**

Desarrollar una aplicación que genere contraseñas seguras y aleatorias, evaluando su nivel de seguridad. El objetivo es demostrar como se puede mejorar la seguridad digital y proteger la información confidencial de los usuarios.

---

## ⚙️ **Principales Funcionalidades DEL Codigo**

### **1. main.py**

#### **Validación de Entrada:**
- `validar_longitud(longitud_str)`: Verifica que la longitud esté entre 4 y 50 caracteres
- `validar_opciones(mayusculas, numeros, simbolos)`: Asegura que al menos una opción esté seleccionada

#### **Generación de Contraseñas:**
- `construir_caracteres(mayusculas, numeros, simbolos)`: Construye el conjunto de caracteres disponibles
- `gencontraseña(longitud, caracteres)`: Genera contraseña usando `secrets` para máxima seguridad
  - Utiliza `secrets.choice()` para selección criptográficamente segura
  - Garantiza al menos un carácter de cada tipo seleccionado
  - Mezcla aleatoriamente los caracteres generados

#### **Evaluación de Seguridad:**
- `evaluar_seguridad(contraseña)`: Sistema de puntos que evalúa:
  - Longitud (2 puntos por ≥8 caracteres, 1 punto adicional por ≥12)
  - Diversidad de caracteres (1 punto por tipo: minúsculas, mayúsculas, números, 2 puntos por símbolos)
  - Clasificación: Débil (≤3 puntos), Media (4-5 puntos), Fuerte (≥6 puntos)

### **2. interfaz.py**

#### **Diseño de la Interfaz:**
- Ventana principal de 400x555 píxeles
- Campo de entrada numérica para longitud
- Checkboxes para selección de tipos de caracteres

#### **Funcionalidades Avanzadas:**
- `generar_contraseña()`: Proceso completo de validación, generación y evaluación
- `copiar_al_portapapeles()`: Copia automática con confirmación visual
- Diálogos informativos usando `messagebox`
- Restablecimiento automático para generar múltiples contraseñas

---

## **Como Funciona el Programa**

### **Flujo Principal:**
1. **Entrada del Usuario:** Selecciona longitud y tipos de caracteres
2. **Validación:** El sistema verifica que los parámetros sean válidos
3. **Construcción:** Se crea el conjunto de caracteres disponibles
4. **Generación:** Algoritmo seguro produce la contraseña
5. **Evaluación:** Se calcula y muestra el nivel de seguridad
6. **Presentación:** Contraseña se muestra con código de colores
7. **Utilidad:** Usuario puede copiar al portapapeles

---

## **Instrucciones de uso**

### **Ejecución:**
1. Descarga los archivos `main.py` e `interfaz.py`
2. Ejecuta el comando: `python interfaz.py`
3. La aplicación se abrirá automáticamente

### **Uso de la Aplicación:**
1. Configura la longitud de la contraseña entre 4-50 caracteres
2. Selecciona los tipos de caracteres que desea incluir
3. Hacer clic en Generar Contraseña
4. Observa el nivel de seguridad indicado por colores
5. Copia la contraseña al portapapeles
