import os

# Creando la lista de archivos en el directorio del proyecto
lista_archivo = [archivo for archivo in os.listdir() if os.path.isfile(archivo) and archivo.split(
    ".")[-1] and archivo.split(".")[-1] != "ipynb" and archivo.split(".")[-1] != "py"]

# Creando lista de tipos unicos de archivos
lista_tipos_unicos = {tipo.split(".")[-1] for tipo in lista_archivo if tipo.split(
    ".")[-1] != "ipynb" and tipo.split(".")[-1] != "py"}


# Creando las carpetas de los firentes tipos de archivos

for tipo in lista_tipos_unicos:
    if not os.path.isdir(tipo):
        os.mkdir(tipo)
        print(f"La carpeta '{tipo}' fue creada con exito.")
    else:
        print(f"La carpeta '{tipo}' ya existe.")

# Moviendo los archivos a sus correspondientes carpetas

for archivo in lista_archivo:
    carpeta_destino = archivo.split(".")[-1]
    origen = os.path.join(os.getcwd(), archivo)
    destino = os.path.join(os.getcwd(), carpeta_destino, archivo)
    print(f"Archivo '{archivo}' -> Carpeta '{carpeta_destino}'")
    os.rename(origen, destino)
