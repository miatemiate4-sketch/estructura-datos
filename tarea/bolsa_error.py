# carrito_spec.py (documentación del TAD)
"""
TAD: Carrito de Compras

OPERACIONES:
1. crear_carrito() -> Carrito
   - Crea un carrito vacío

2. agregar(carrito, producto, cantidad) -> bool
   - Agrega X unidades de un producto
   - Retorna True si exitoso, False si falla
   - Precondiciones: producto debe existir en catálogo, cantidad > 0

3. sacar(carrito, producto, cantidad) -> bool
   - Qita X unidades de un producto
   - Retorna True si pudo, False si no hay suficiente

4. cuantos(carrito, producto) -> int
   - Devuelve cuántas unidades hay de un producto

5. total(carrito) -> float
   - Devuelve el monto total a pagar

6. ver_cantidades(carrito) -> list[(producto, cantidad)]
   - Devuelve lista de todos los productos y cantidades
"""
# test_carrito.py
import pytest


def test_creacion_carrito_vacio():
    """Un carrito nuevo está vacío"""
    carrito = crear_carrito()
    assert total(carrito) == 0.0
    assert len(carrito) == 0

def test_agregar_producto_valido():
    """Puedo agregar un producto existente"""
    carrito = crear_carrito()
    resultado = agregar(carrito, "lapiz", 3)
    assert resultado == True
    assert cuantos(carrito, "lapiz") == 3

def test_agregar_producto_inexistente():
    """No puedo agregar producto que no existe"""
    carrito = crear_carrito()
    resultado = agregar(carrito, "remera", 1)
    assert resultado == False
    assert cuantos(carrito, "remera") == 0

def test_agregar_cantidad_negativa():
    """No puedo agregar cantidad negativa"""
    carrito = crear_carrito()
    resultado = agregar(carrito, "lapiz", -5)
    assert resultado == False

def test_sacar_producto_disponible():
    """Puedo sacar si tengo suficientes"""
    carrito = crear_carrito()
    agregar(carrito, "lapiz", 5)
    resultado = sacar(carrito, "lapiz", 2)
    assert resultado == True
    assert cuantos(carrito, "lapiz") == 3

def test_sacar_sin_stock():
    """No puedo sacar más de lo que tengo"""
    carrito = crear_carrito()
    agregar(carrito, "lapiz", 2)
    resultado = sacar(carrito, "lapiz", 5)
    assert resultado == False
    assert cuantos(carrito, "lapiz") == 2  # No debe cambiar

def test_total_calculo_correcto():
    """El total suma precio × cantidad"""
    carrito = crear_carrito()
    agregar(carrito, "lapiz", 2)     # 2 × 2.50 = 5.00
    agregar(carrito, "cuaderno", 3)  # 3 × 8.00 = 24.00
    assert total(carrito) == 29.00

def test_cuanto_hay_de_cada_uno():
    """Puedo ver todas las cantidades"""
    carrito = crear_carrito()
    agregar(carrito, "lapiz", 5)
    agregar(carrito, "cuaderno", 3)
    cantidades = ver_cantidades(carrito)
    assert ("lapiz", 5) in cantidades
    assert ("cuaderno", 3) in cantidades