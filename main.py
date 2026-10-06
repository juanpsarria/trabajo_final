#CLAVE DE INICIO

clave = "2026"
intentos = 0

#PRODUCTOS Y PRECIOS
productos = [
    {"nombre":"cafe","precio":8000.00},
    {"nombre":"factura","precio":6000.00},
    {"nombre":"exprimido","precio":10000.00},
    {"nombre":"licuado","precio":20000.00}
]

#REGISTRO DE VENTA
def generar_codigo_venta(contador):
    """genera un codigo correlativo para la venta(p-001)."""
    return f"p-{contador:03d}"

def registrar_venta(contador_venta):
    """registra una nueva venta en la cola de espera."""
    print ("\n---registrar nueva venta---")
    print ("\n Ingresar 1 para agregar cafe")
    print ("\n Ingresar 2 para agregar facturas")
    print ("\n Ingresar 3 para agregar exprimido")
    print ("\n Ingresar 4 para agregar licuado")
    while True: 
        try: 
            producto = input ("Ingrese el pedido")
        except ValueError:  
            print ("ERROR.- Producto invalido")
            continue
        match producto: 
            case "1": 
                cantidad = int(input ("Ingresar la cantidad"))
            case "2": 
                antidad = int(input ("Ingresar la cantidad"))
            case "3": 
                cantidad = int(input ("Ingresar la cantidad"))
            case "4": 
                cantidad = int(input ("Ingresar la cantidad"))
            case _:
                print("NO existe producto.")

        codigo = generar_codigo_venta(contador_venta)

        nuevo_pedido = {
            "codigo": codigo,
            "productos": {"producto": producto}, 
            "cantidad": producto.cantidad
        }

#MENU DE OPCIONES
def menu():
    while True:
        print("\n INGRESE OPCIÓN 1 PARA REGITRAR VENTA")
        print("\n INGRESE OPCIÓN 2 PARA GENERAR TICKET")
        print("\n INGRESE 0 PARA FINALIZAR Y GENERAR REPORTE")
    
        try: 
            opcion = int(input(" INGRESE OPCIÓN A REALIZAR: "))
        except ValueError:
            print("DEBES INGRESAR UNA OPCIÓN CORRECTA.")
            continue

        match opcion:
            case 1:
                print("registro vta")
                registrar_venta(generar_codigo_venta())
            case 2:
                print("ticket ok")
            case 3:
                print("reporte ok")
            case _:
                print("OPCIÓN NO DISPONIBLE. INGRESA 1, 2 O 3.")
        

#INICIO DE SESION
while intentos < 4:
    ingreso = input("Ingrese la clave: ")
    if ingreso == clave:
        print("INICIO DE SESIÓN CORRECTO")
        menu()
        break
    else:
        intentos += 1
        if intentos == 3:
            print("USUARIO BLOQUEADO.")
            break
        else:
            print(f"CLAVE INVÁLIDA. TE QUEDAN {3 - intentos} INTENTO/S")
