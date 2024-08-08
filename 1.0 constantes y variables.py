
# Constantes
# En Python, las constantes son por convención nombres en mayúsculas
PI = 3.14159
GRAVEDAD = 9.8

# Variables y asignación dinámica
# Python es un lenguaje de tipado dinámico, por lo que no necesitas declarar el tipo de una variable
edad = 30  # Entero
temperatura = 36.5  # Flotante
nombre = "Alice"  # Cadena de texto

# Cambiar el tipo de dato dinámicamente
edad = "treinta"

# Errores comunes en el nombramiento y uso de variables
# 1. Uso de palabras reservadas como nombres de variable
# int = 7  # Descomentar esta línea causaría un error de sintaxis

# 2. Empezar nombres de variables con números
# 1nombre = "Bob"  # Descomentar causaría un error de sintaxis

# 3. Uso de caracteres especiales en nombres de variable
# nombre-variable = "Carol"  # Descomentar causaría un error de sintaxis


# Operadores
# Aritméticos
# suma = edad + temperatura  # Nota: Esto es un error intencional para mostrar la asignación dinámica
diferencia = temperatura - 20
producto = 5 * temperatura
cociente = temperatura / 5

# Comparación
es_igual = temperatura == 36.5
es_diferente = edad != 30
es_mayor = temperatura > 20
es_menor = temperatura < 40

# Lógicos
resultado_and = (temperatura > 35) and (temperatura < 37)
resultado_or = (temperatura < 35) or (temperatura > 37)
resultado_not = not(temperatura == 36.5)

# Imprimir resultados de operadores y demostraciones de errores
print("Diferencia:", diferencia)
print("Producto:", producto)
print("Cociente:", cociente)
print("Es igual:", es_igual)
print("Es diferente:", es_diferente)
print("Es mayor:", es_mayor)
print("Es menor:", es_menor)
print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado NOT:", resultado_not)
