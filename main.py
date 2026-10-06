import json

# PRODUCTOS
productos = [
    {"nombre": "Café", "precio": 8000.00},
    {"nombre": "Factura", "precio": 6000.00},
    {"nombre": "Exprimido", "precio": 10000.00},
    {"nombre": "Licuado", "precio": 20000.00}
]


# MÓDULO 1: AUTENTICACIÓN DE OPERADORES
def autenticar_operador():
    """Valida el inicio de sesión"""
    pin_correcto = "2026"
    intentos_maximos = 3

    for intento in range(1, intentos_maximos + 1):
        pin_ingresado = input(f"Ingrese PIN de seguridad (Intento {intento} de {intentos_maximos}): ").strip()
        if pin_ingresado == pin_correcto:
            print("\n[OK] Ingreso correcto \n")
            return True
        else:
            intentos_restantes = intentos_maximos - intento
            if intentos_restantes > 0:
                print(f"[ERROR] PIN incorrecto. Intentos restantes: {intentos_restantes}\n")

    print("\n[BLOQUEADO] No hay más intentos.")
    return False


# MÓDULO 2: CARGA Y PROCESAMIENTO DEL PEDIDO DEL CLIENTE
def leer_numero_valido(mensaje, tipo=int, minimo=1):
    """Garantiza la captura de excepciones (try/except) para entradas numéricas."""
    while True:
        try:
            entrada = input(mensaje).strip()
            valor = tipo(entrada)
            if valor < minimo:
                print(f"[ERROR] El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("[ERROR] Ingrese una opción correcta.")

def generar_codigo_pedido(contador):
    """Genera un código correlativo para el pedido (ej. P-001)."""
    return f"P-{contador:03d}"

def registrar_pedido(pedidos_dia, contador_pedidos):
    """Registra un nuevo pedido seleccionando productos del menú predefinido."""
    codigo = generar_codigo_pedido(contador_pedidos)
    print(f"\n Número de pedido: {codigo}")

    cant_tipos = leer_numero_valido(
        "Ingrese la cantidad de tipos de productos distintos a llevar: ",
        tipo=int,
        minimo=1
    )

    productos_pedido = []
    subtotal = 0.0

    for i in range(1, cant_tipos + 1):
        print(f"\n Producto {i} de {cant_tipos}")
        print("Seleccione los productos:")
        for idx, prod in enumerate(productos, start=1):
            print(f"{idx}. {prod['nombre']} (${prod['precio']:.2f})")

        # Selección del producto
        while True:
            opcion_prod = leer_numero_valido(
                f"Seleccione producto (1-{len(productos)}): ",
                tipo=int,
                minimo=1
            )
            if opcion_prod <= len(productos):
                producto_elegido = productos[opcion_prod - 1]
                break
            print(f"[ERROR] Opción inválida. Ingrese un número entre 1 y {len(productos)}.")

        cantidad = leer_numero_valido(
            f"Ingrese cantidad de '{producto_elegido['nombre']}': ",
            tipo=int,
            minimo=1
        )

        nombre_prod = producto_elegido["nombre"].strip().upper()
        precio_unitario = producto_elegido["precio"]
        monto = precio_unitario * cantidad
        subtotal += monto

        productos_pedido.append({
            "nombre": nombre_prod,
            "precio_unitario": precio_unitario,
            "cantidad": cantidad,
            "monto": monto
        })

    # Descuento 
    descuento = 0.0
    recibio_descuento = False
    if subtotal > 25000:
        descuento = subtotal * 0.10
        recibio_descuento = True

    total_final = subtotal - descuento

    # Selección de medio de pago
    print("\nSeleccione Medio de Pago:")
    print("1. Efectivo")
    print("2. Tarjeta")
    print("3. Transferencia")
    op_pago = input("Ingrese opción seleccionada: ").strip()
    match op_pago:
        case "1": medio_pago = "Efectivo"
        case "2": medio_pago = "Tarjeta"
        case "3": medio_pago = "Transferencia"
        case _:
            print("[ADVERTENCIA] Opción inválida. Se asignará 'Efectivo' por defecto.")
            medio_pago = "Efectivo"

    nuevo_pedido = {
        "codigo": codigo,
        "productos": productos_pedido,
        "subtotal": subtotal,
        "descuento": descuento,
        "recibio_descuento": recibio_descuento,
        "total": total_final,
        "medio_pago": medio_pago
    }

    pedidos_dia.append(nuevo_pedido)
    print(f"\n Pedido {codigo} registrado con éxito. Total a pagar: ${total_final:.2f}")
    return contador_pedidos + 1

def generar_ticket(pedidos_dia):
    """Muestra el detalle del último pedido cobrado."""
    if not pedidos_dia:
        print("[INFO] Aún no se han registrado pedidos en la jornada.")
        return

    ultimo_pedido = pedidos_dia[-1]

    print(f"Código de Pedido: {ultimo_pedido['codigo']}")
    for prod in ultimo_pedido["productos"]:
        print(f"{prod['cantidad']}x {prod['nombre']} @ ${prod['precio_unitario']:.2f} c/u = ${prod['monto']:.2f}")
    print(f"Subtotal: ${ultimo_pedido['subtotal']:.2f}")
    if ultimo_pedido["recibio_descuento"]:
        print(f"Descuento (10%):-${ultimo_pedido['descuento']:.2f}")
    print(f"TOTAL FINAL: ${ultimo_pedido['total']:.2f}")
    print(f"Medio de Pago: {ultimo_pedido['medio_pago']}")

def generar_reporte(pedidos_dia, nombre_archivo="reporte.json"):
    """Muestra el reporte de fin de jornada y guarda los datos en un JSON."""
    total_ingresos = sum(p["total"] for p in pedidos_dia)
    clientes_descuento = sum(1 for p in pedidos_dia if p["recibio_descuento"])

    print("REPORTE DE CIERRE DEL DÍA")
    print(f"Total de ingresos de la cafetería: ${total_ingresos:.2f}")
    print(f"Cantidad total de clientes: {len(pedidos_dia)}")
    print(f"Clientes que tuvieron descuento: {clientes_descuento}")

    datos_exportar = {
        "total_ingresos": total_ingresos,
        "total_clientes": len(pedidos_dia),
        "clientes_con_descuento": clientes_descuento,
        "historial_pedidos": pedidos_dia
    }

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos_exportar, f, indent=4, ensure_ascii=False)
        print(f"\n Reporte generado ok en '{nombre_archivo}'.")
    except IOError as e:
        print(f"Error: {e}")


# ESTRUCTURA PRINCIPAL DEL PROGRAMA
def main():
    if not autenticar_operador():
        return

    pedidos_dia = []
    contador_pedidos = 1

    while True:
        print("\n1. Registrar nuevo pedido de cliente")
        print("2. Generar ticket de la última venta")
        print("0. Finalizar jornada y generar reporte")

        opcion = input("Seleccione una opción: ").strip().upper()

        match opcion:
            case "1":
                contador_pedidos = registrar_pedido(pedidos_dia, contador_pedidos)
            case "2":
                generar_ticket(pedidos_dia)
            case "0":
                generar_reporte(pedidos_dia)
                print("Sistema finalizado.")
                break
            case _:
                print("[ERROR] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()