#TRABAJO INTEGRADOR FINAL
Sarría, Juan Pablo
Valenti, Laura
Ventura, María Rosa
Analista Funcional de Sistemas Informáticos
Gestión de Software 1
1° 3°
Prof. Grimaldi, Carina
Año 2026


##ACTIVIDAD
Sistema de cobro de una cafetería y validación de contraseña.
Una cafetería desea automatizar el proceso de registro de pedidos diarios.
Cada cliente puede pedir uno o más productos del menú.
Especificaciones del Sistema:
El programa se organiza en dos módulos independientes que garantizan la seguridad y el correcto flujo operacional del negocio:
Módulo 1: Autenticación de Operadores (Seguridad)
1. El usuario debe ingresar una PIN/clave numérica de seguridad de 4 dígitos (por ejemplo, "2026").
2. El sistema debe controlar el acceso por un límite máximo de 3 intentos.
3. Si agota los intentos sin acertar, el programa emitirá un mensaje de bloqueo y terminará de forma segura.
Módulo 2: Carga y Procesamiento del pedido del cliente.
Descripción Lógica y Estructura del Módulo de Cobro.
Para cada cliente, registrar cuántos productos compró y el tipo de producto y su precio.
1. Ciclo de Atención Continua.
• Calcular el total a pagar por cada cliente.
• Aplicar un descuento del 10% si el total supera los $25000.
• Al final del día, mostrar:
• El total de ingresos de la cafetería.
• La cantidad total de clientes y la cantidad que recibieron descuento.
Criterio de parada: La atención a clientes continúa hasta que el operador
ingresa una clave especial de cierre (por ejemplo, la palabra "FIN" o el código "0").
2. Registro e Inspección de Productos por Cliente.
Para cada cliente que llega a la caja:
Definición de cantidad: El sistema solicita la cantidad total de tipos de productos distintos que el cliente llevará.
Nombre/Tipo de producto: Cadena de texto normalizada mediante métodos de cadenas como .upper() o .strip() para evitar discrepancias por mayúsculas o minúsculas.
Precio unitario: Valor numérico de punto flotante (float).
Cantidad de unidades: Valor entero (int).
Si el operador introduce accidentalmente texto en lugar de números o valores menores/iguales a cero, la excepción es capturada, emitiendo un mensaje de error y solicitando el dato nuevamente sin que el sistema falle.
5. Totalización, Medio de Pago y Formato de Salida.
Selección de método de pago: Permite seleccionar el medio de pago (Efectivo, Tarjeta, Transferencia).
Emisión del ticket: Presenta en consola el resumen detallado del pedido y el monto total final formateado a dos cifras decimales mediante f-strings (f"${total:.2f}")