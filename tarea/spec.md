# Proposito 
un carrito de tienda de una universidad que se pueda, agregar, sacar, cuantos son, y el total de todo

# Ambiguedades decididas:
1. ¿Qué hago con cantidad negativa?
Rechazo y aviso error,No tiene sentido pedir -3 lápices.
2. ¿Al sacar, borro todo o solo algunas?
Resto la cantidad que pediste, Sacar 2 significa restar 2, no borrar todo
3. ¿El total se guarda o solo se muestra?
Se calcula y se puede usar, Para poder imprimir, enviar, o sumar después
4. 	¿Qué pasa si saco algo que no tengo?
Aviso error y no modifico el carrito, Para que no se rompa el programa ni guarde datos inválidos

# Operaciones

crear_carrito()
 Precondiciones: Ninguna.
 Postcondiciones: Devuelve un carrito nuevo sin elementos acumulados (len == 0).
 Errores: Ninguno.

agregar(carrito, producto, cantidad )
 Precondiciones: producto debe existir en el catálogo (independiente de si viene en mayúsculas o minúsculas) y cantidad > 0.
Postcondiciones:
Normaliza el nombre del producto a minúsculas.
 Si el producto ya existe en el carrito, suma cantidad al acumulado actual.
 Si no existe, crea la entrada con esa cantidad.
 Devuelve True.
Errores: Devuelve False y no modifica el carrito si:
 cantidad <= 0 (cero o negativa).
 producto no pertenece al catálogo.

sacar(carrito, producto, cantidad)
 Precondiciones: producto debe estar en el carrito y cantidad > 0. La cantidad a retirar debe ser $\le$ a la cantidad guardada.
Postcondiciones:Reduce la cantidad del producto en el carrito en cantidad unidades.Si la cantidad     resultante es $0$, elimina la clave del producto por completo del carrito (producto not in carrito).Devuelve True.
Errores: Devuelve False y no modifica el carrito si:cantidad <= 0.producto no está en el carrito.    cantidad a sacar es estrictamente mayor que la disponible.

ver_cantidades(carrito)
Precondiciones: Ninguna.
Postcondiciones: Devuelve una lista de tuplas de la forma (producto, cantidad) para todos los ítems vigentes en el carrito. Si está vacío, devuelve [].
Errores: Ninguno.

total(carrito)
Precondiciones: Ninguna.
Postcondiciones: Devuelve el costo total en formato flotante ($\ge 0.0$)
Errores: Ninguno.
# Invariantes
INV-01 (Claves válidas): Si un producto está en el carrito, su cantidad es estrictamente positiva ($\text{cantidad} > 0$).
INV-02 (Coherencia del total): Si el carrito no tiene elementos (len == 0), total(carrito) == 0.0.
INV-03 (Normalización): Todas las claves almacenadas en el carrito están únicamente en minúsculas.

# Criterios de aceptación

| ID | Criterio | Prueba que lo verifica |
|----|----------|------------------------|
| CA-01 | Un carrito nuevo no contiene ítems y su total es $0.0$|test_carrito_nuevo_esta_vacio |
| CA-02 | Agregar un producto del catálogo suma la cantidad y normaliza a minúsculas | test_agregar_normaliza_a_minusculas|
| CA-03 | Agregar cantidad $\le 0$ o un producto fuera de catálogo devuelve False | test_agregar_cantidad_cero_falla|
| CA-04 | Sacar una cantidad parcial actualiza el stock sin borrar la clave |test_sacar_producto_disponible_exitoso |
| CA-05 |Sacar exactamente el total disponible elimina la clave del carrito |test_sacar_todo_el_stock_borra_clave|
| CA-06 | Intentar sacar más unidades de las disponibles devuelve False y no altera el carrito |test_sacar_mas_que_tengo_no_modifica|
| CA-07 | total() multiplica correctamente cantidades por precio unitario manejando decimales |test_total_preciso_decimales|

# 6. Casos extremos considerados
- Agregar todo 
- Sacar todo 
- Carrito vacío nuevamente
- Múltiples ciclos de agregar/sacar
- Operar un producto no afecta a otros
