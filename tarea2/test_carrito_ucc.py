# test_carrito_ucc.py
import pytest
from carrito_dist import CarritoDist
from carrito_lista import CarritoLista

class ElementoNoEncontradoError(Exception):
    """Excepción lanzada cuando se intenta sacar un elemento inexistente."""
    pass


# Las MISMAS pruebas corren contra las DOS implementaciones
@pytest.fixture(params=[CarritoDist, CarritoLista])
def Carrito(request):
    return request.param


def test_carrito_vacio(Carrito):
    """CA-01: un carrito recién creado está vacío."""
    c = Carrito()
    assert c.tamaño() == 0
    assert not c.existe("lapiz")


def test_agregar_producto_valido(Carrito):
    """CA-02: agregar un producto que existe en el catálogo."""
    c = Carrito()
    resultado = c.agregar("lapiz", 3)
    assert resultado == True
    assert c.cantidad("lapiz") == 3


def test_agregar_cantidad_cero_falla(Carrito):
    """CA-03: no puedo agregar cantidad 0."""
    c = Carrito()
    resultado = c.agregar("lapiz", 0)
    assert resultado == False


def test_agregar_cantidad_negativa_falla(Carrito):
    """CA-04: no puedo agregar cantidad negativa."""
    c = Carrito()
    resultado = c.agregar("lapiz", -5)
    assert resultado == False


def test_agregar_producto_inexistente_falla(Carrito):
    """CA-05: no puedo agregar producto que no está en catálogo."""
    c = Carrito()
    resultado = c.agregar("remera", 2)
    assert resultado == False


def test_agregar_suma_si_ya_existe(Carrito):
    """CA-06: agregar producto existente suma la cantidad."""
    c = Carrito()
    c.agregar("lapiz", 2)
    c.agregar("lapiz", 3)
    assert c.cantidad("lapiz") == 5


def test_agregar_varios_productos_distintos(Carrito):
    """CA-07: puedo agregar múltiples productos diferentes."""
    c = Carrito()
    c.agregar("lapiz", 2)
    c.agregar("cuaderno", 3)
    # productos distintos = 2, no unidades totales = 5
    assert len(c.productos()) == 2  # ← Cambiar tamaño() por productos()
    assert c.total() == 36.5         # 2×2.50 + 3×8.00 = 5 + 24 = 29 (ajustar según cálculo)

def test_agregar_normaliza_a_minusculas(Carrito):
    """CA-08: nombres en mayúscula se normalizan a minúscula."""
    c = Carrito()
    c.agregar("LAPIZ", 1)
    assert c.cantidad("lapiz") == 1
    assert c.existe("lapiz")        # ✅ "lapiz" SÍ existe (normalizado)
    assert not c.existe("LAPIZ")    # ✅ "LAPIZ" NO existe
    
def test_sacar_producto_disponible_exitoso(Carrito):
    """CA-09: puedo sacar si tengo suficientes unidades."""
    c = Carrito()
    c.agregar("lapiz", 5)
    resultado = c.sacar("lapiz", 2)
    assert resultado == True
    assert c.cantidad("lapiz") == 3


def test_sacar_inexistente(Carrito):
    """CA-10: sacar un elemento inexistente no modifica el carrito."""
    c = Carrito()
    cantidad_inicial = c.tamaño()
    resultado = c.sacar("remera", 1)
    assert resultado == False
    assert c.tamaño() == cantidad_inicial


def test_sacar_mas_que_tengo_no_modifica(Carrito):
    """CA-11: no puedo sacar más de lo que tengo."""
    c = Carrito()
    c.agregar("lapiz", 5)
    resultado = c.sacar("lapiz", 200)
    assert resultado == False
    assert c.cantidad("lapiz") == 5


def test_sacar_todo_el_stock_borra_elemento(Carrito):
    """CA-12: si saco toda la cantidad, el elemento se elimina."""
    c = Carrito()
    c.agregar("lapiz", 5)
    c.sacar("lapiz", 5)
    assert not c.existe("lapiz")


def test_sacar_cantidad_1(Carrito):
    """CA-13: puedo sacar cantidad mínima (1 unidad)."""
    c = Carrito()
    c.agregar("lapiz", 5)
    c.sacar("lapiz", 1)
    assert c.cantidad("lapiz") == 4


def test_sacar_cantidad_cero_no_hace_nada(Carrito):
    """CA-14: sacar 0 unidades no hace nada."""
    c = Carrito()
    c.agregar("lapiz", 5)
    resultado = c.sacar("lapiz", 0)
    assert resultado == False
    assert c.cantidad("lapiz") == 5


def test_total_carrito_vacio_es_cero(Carrito):
    """CA-15: total de carrito vacío es $0.00."""
    c = Carrito()
    assert c.total() == 0.0


def test_total_un_producto(Carrito):
    """CA-16: total de un solo producto."""
    c = Carrito()
    c.agregar("lapiz", 2)
    assert c.total() == 5.0  # 2 × $2.50


def test_total_varios_productos(Carrito):
    """CA-17: total acumula todos los productos."""
    c = Carrito()
    c.agregar("lapiz", 5)
    c.agregar("cuaderno", 3)
    assert c.total() == 36.5


def test_total_preciso_decimales(Carrito):
    """CA-18: el total maneja decimales correctamente."""
    c = Carrito()
    c.agregar("boligrafo", 3)
    assert abs(c.total() - 10.50) < 0.01


def test_ciclo_agregar_sacar_mismo_producto(Carrito):
    """CA-19: ciclo: agregar → sacar → agregar del mismo producto."""
    c = Carrito()
    c.agregar("lapiz", 10)
    c.sacar("lapiz", 4)
    c.agregar("lapiz", 2)
    assert c.cantidad("lapiz") == 8


def test_productos_no_interfieren_entre_si(Carrito):
    """CA-20: operar un producto no afecta a otros."""
    c = Carrito()
    c.agregar("lapiz", 5)
    c.agregar("cuaderno", 3)
    c.agregar("boligrafo", 4)
    c.sacar("lapiz", 2)
    assert c.cantidad("lapiz") == 3
    assert c.cantidad("cuaderno") == 3
    assert c.cantidad("boligrafo") == 4


def test_inv_tamaño_es_suma_cantidades(Carrito):
    """INV-01: el tamaño es la suma de todas las cantidades."""
    c = Carrito()
    c.agregar("lapiz", 5)
    c.agregar("cuaderno", 3)
    c.agregar("boligrafo", 4)
    assert c.tamaño() == c.cantidad("lapiz") + c.cantidad("cuaderno") + c.cantidad("boligrafo")