# TRABAJO INTEGRADOR FINAL

* **Carrera:** Analista Funcional de Sistemas Informáticos
* **Materia:** Gestión de Software 1 (1° 3°)
* **Profesora:** Prof. Grimaldi, Carina
* **Integrantes:**
  * Sarría, Juan Pablo
  * Valenti, Laura
  * Ventura, María Rosa
* **Año:** 2026

---

## 📌 DESCRIPCIÓN DE LA ACTIVIDAD

### Sistema de Cobro de una Cafetería y Validación de Contraseña

Una cafetería desea automatizar el proceso de registro de pedidos diarios. Cada cliente puede pedir uno o más productos del menú.

---

## ⚙️ ESPECIFICACIONES DEL SISTEMA

El programa se organiza en dos módulos independientes que garantizan la seguridad y el correcto flujo operacional del negocio:

### 🔐 Módulo 1: Autenticación de Operadores (Seguridad)
1. **PIN de Acceso:** El usuario debe ingresar una clave/PIN numérica de seguridad de 4 dígitos (por ejemplo, `"2026"`).
2. **Control de Intentos:** El sistema controla el acceso permitiendo un límite máximo de **3 intentos**.
3. **Bloqueo Seguro:** Si el operador agota los intentos sin acertar, el programa emite un mensaje de bloqueo y termina su ejecución de forma segura.

---

### ☕ Módulo 2: Carga y Procesamiento del Pedido del Cliente

#### 1. Descripción Lógica y Estructura del Módulo de Cobro
Para cada cliente atendido, el sistema registra la cantidad de tipos de productos, la descripción de cada uno, su precio y las unidades compradas.

* **Ciclo de Atención Continua:**
  * Calcula el total individual a pagar por cliente.
  * Aplica un **descuento del 10%** automático si el total de la compra supera los **$25.000**.
  * **Criterio de Parada:** La atención a clientes continúa de forma ininterrumpida hasta que el operador ingresa una clave especial de cierre (palabra `"FIN"` o código `"0"`).
  * **Cierre de Jornada:** Al finalizar el día, se visualizan las métricas globales:
    * Total de ingresos recopilados por la cafetería.
    * Cantidad total de clientes atendidos.
    * Cantidad de clientes que recibieron descuento.
    * Exportación opcional de los datos registrados a un archivo estructurado `JSON`.

#### 2. Registro e Inspección de Productos por Cliente
Para cada cliente que llega a la caja se solicita:
* **Definición de Cantidad:** Solicitud de la cantidad total de tipos de productos distintos que llevará el cliente.
* **Nombre/Tipo de Producto:** Cadena de texto normalizada mediante métodos como `.upper()` y `.strip()` para evitar discrepancias por mayúsculas, minúsculas o espacios accidentales.
* **Precio Unitario:** Valor numérico de punto flotante (`float`).
* **Cantidad de Unidades:** Valor entero (`int`).
* **Manejo de Excepciones (`try/except`):** Si el operador introduce texto accidentalmente en campos numéricos o ingresa valores menores/iguales a cero, la excepción es capturada emitiendo un mensaje de advertencia y volviendo a solicitar el dato sin interrupciones ni fallos en el sistema.

#### 3. Totalización, Medio de Pago y Formato de Salida
* **Selección de Método de Pago:** Permite elegir el canal de cobro entre **Efectivo**, **Tarjeta** o **Transferencia**.
* **Emisión del Ticket:** Presenta en la consola de comandos el resumen detallado de la compra con su desglose de productos y el monto final formateado a dos decimales mediante *f-strings* (ej. `f"${total:.2f}"`).

---

## 🛠️ TECNOLOGÍAS UTILIZADAS
* **Lenguaje:** Python 3.x
* **Estructuras de Datos:** Listas (`list`), Diccionarios (`dict`)
* **Control de Flujo:** Bucle `while`, estructuras condicionales `if/else` y `match/case`
* **Persistencia de Datos:** Módulo integrado `json`