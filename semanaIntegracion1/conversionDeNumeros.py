"""
Conversión de Números:
Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.
"""


CONTROL = True
while CONTROL:
    # Paso 1: Validar el número y las bases
    numero = input("Ingrese un número: ")
    base_origen = input("Ingrese la base de origen (2, 10): ")
    base_destino = input("Ingrese la base de destino (2, 10): ")
    if numero.isdigit() and int(numero) >= 0 and (base_origen.isdigit() and (base_origen == "2" or base_origen == "10")) and (base_destino.isdigit() and (base_destino == "2" or base_destino == "10")):
        CONTROL = False
    else:
        print(f'El número "{numero}", la base de origen {base_origen}, o la base de destino {base_destino} no son válidas.')

# Paso 2: convertir string a int
base_origen = int(base_origen)
base_destino = int(base_destino)
deci = int(numero, base_origen)

# Paso 3: convertir a decimal o binario
if numero == "" or numero == "0":
    deci = 0
if base_destino == 2:
    binario =  bin(deci)[2:]
    print(f"El número {numero} en base {base_origen} es {binario} en base 2.")  
elif base_destino == 10:
    deci = deci
    print(f"El número {numero} en base {base_origen} es {deci} en base 10.")
else:
    print("Base de destino no válida. Debe ser 2, 10.")