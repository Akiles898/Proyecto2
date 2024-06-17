# Nombre del archivo de entrada y salida
archivo_entrada = 'cristiano.txt'
archivo_salida = 'resumen.txt'

# Inicializar contadores
contador_letras = 0
contador_espacios = 0

# Leer el archivo de entrada y contar letras y espacios
try:
    with open(archivo_entrada, 'r') as file:
        contenido = file.read()
        for caracter in contenido:
            if caracter.isalpha():  # Verifica si es una letra
                contador_letras += 1
            elif caracter.isspace():  # Verifica si es un espacio
                contador_espacios += 1
except FileNotFoundError:
    print(f"El archivo '{archivo_entrada}' no se encontró.")
    exit()

# Escribir el resumen en el archivo de salida
try:
    with open(archivo_salida, 'w') as file:
        file.write(f"Cantidad de letras: {contador_letras}\n")
        file.write(f"Cantidad de espacios: {contador_espacios}\n")
    print(f"Se ha generado el archivo '{archivo_salida}' con el resumen.")
except IOError:
    print(f"No se pudo escribir en el archivo '{archivo_salida}'.")
