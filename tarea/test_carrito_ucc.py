# test_carrito_ucc.py
import pytest

def get_functions(impl_name):
    """Devuelve todas las funciones necesarias para una implementación."""
    if impl_name == "dist":
        from carrito_dist import agregar, sacar, ver_cantidades, total, crear_carrito
    else:
        from carrito_lista import agregar, sacar, ver_cantidades, total, crear_carrito
    return crear_carrito, agregar, sacar, ver_cantidades, total

@pytest.fixture(params=["dist", "list"], ids=lambda x: f"implementacion_{x}")
def impl_name(request):
    """Nombre de la implementación a probar."""
    return request.param

@pytest.fixture
def carrito_funcs(impl_name):
    """Devuelve las funciones de la implementación seleccionada."""
    return get_functions(impl_name)

@pytest.fixture
def carrito_vacio(carrito_funcs):
    """Carrito vacío para pruebas."""
    crear_carrito, _, _, _, _ = carrito_funcs
    return crear_carrito()

@pytest.fixture
def carrito_con_items(carrito_funcs):
    """Carrito con productos pre-cargados."""
    crear_carrito, agregar, _, _, _ = carrito_funcs
    c = crear_carrito()
    agregar(c, "lapiz", 5)
    agregar(c, "cuaderno", 3)
    return c

class TestCarritoVacio:
    
    def test_carrito_nuevo_esta_vacio(self, carrito_vacio):
        """Un carrito recién creado debe estar vacío"""
        assert len(carrito_vacio) == 0
    
    def test_total_carrito_vacio_es_cero(self, carrito_vacio, carrito_funcs):
        """Total de carrito vacío es $0.00"""
        _, _, _, _, total = carrito_funcs
        assert total(carrito_vacio) == 0.0
    
    def test_ver_cantidades_carrito_vacio_devuelve_lista_vacia(self, carrito_vacio, carrito_funcs):
        """Ver cantidades en carrito vacío devuelve []"""
        _, _, _, ver_cantidades, _ = carrito_funcs
        assert ver_cantidades(carrito_vacio) == []


class TestAgregar:
    
    def test_agregar_producto_valido_exitoso(self, carrito_vacio, carrito_funcs):
        """Puedo agregar un producto que existe en el catálogo"""
        _, agregar, _, _, _ = carrito_funcs
        resultado = agregar(carrito_vacio, "lapiz", 3)
        assert resultado == True
        assert carrito_vacio["lapiz"] == 3
    
    def test_agregar_cantidad_cero_falla(self, carrito_vacio, carrito_funcs):
        """CANTIDAD CERO: No puedo agregar cantidad 0"""
        _, agregar, _, _, _ = carrito_funcs
        resultado = agregar(carrito_vacio, "lapiz", 0)
        assert resultado == False
    
    def test_agregar_cantidad_negativa_falla(self, carrito_vacio, carrito_funcs):
        """CANTIDAD NEGATIVA: No puedo agregar cantidad negativa"""
        _, agregar, _, _, _ = carrito_funcs
        resultado = agregar(carrito_vacio, "lapiz", -5)
        assert resultado == False
    
    def test_agregar_producto_inexistente_falla(self, carrito_vacio, carrito_funcs):
        """No puedo agregar producto que no está en catálogo"""
        _, agregar, _, _, _ = carrito_funcs
        resultado = agregar(carrito_vacio, "remera", 2)
        assert resultado == False
    
    def test_agregar_suma_si_ya_existe(self, carrito_vacio, carrito_funcs):
        """Agregar producto existente suma la cantidad"""
        _, agregar, _, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 2)
        agregar(carrito_vacio, "lapiz", 3)
        assert carrito_vacio["lapiz"] == 5
    
    def test_agregar_varios_productos_distintos(self, carrito_vacio, carrito_funcs):
        """Puedo agregar múltiples productos diferentes"""
        _, agregar, _, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 2)
        agregar(carrito_vacio, "cuaderno", 3)
        assert len(carrito_vacio) == 2
    
    def test_agregar_normaliza_a_minusculas(self, carrito_vacio, carrito_funcs):
        """Nombres en mayúscula se normalizan a minúscula"""
        _, agregar, _, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapizgit ", 1)
        assert "lapiz" in carrito_vacio
        assert "LAPIZ" not in carrito_vacio
    
    def test_agregar_cantidad_muy_grande(self, carrito_vacio, carrito_funcs):
        """Puedo agregar cantidades muy grandes"""
        _, agregar, _, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 999999)
        assert carrito_vacio["lapiz"] == 999999


class TestSacar:
    
    def test_sacar_producto_disponible_exitoso(self, carrito_con_items, carrito_funcs):
        """Puedo sacar si tengo suficientes unidades"""
        _, _, sacar, _, _ = carrito_funcs
        resultado = sacar(carrito_con_items, "lapiz", 2)
        assert resultado == True
        assert carrito_con_items["lapiz"] == 3
    
    def test_sacar_lo_que_no_esta_no_modifica(self, carrito_vacio, carrito_funcs):
        """SACAR LO QUE NO ESTÁ: Si saco producto que no tengo, no cambia nada"""
        _, _, sacar, _, _ = carrito_funcs
        cantidad_inicial = len(carrito_vacio)
        resultado = sacar(carrito_vacio, "remera", 1)
        assert resultado == False
        assert len(carrito_vacio) == cantidad_inicial
    
    def test_sacar_mas_que_tengo_no_modifica(self, carrito_con_items, carrito_funcs):
        """STOCK INSUFICIENTE: No puedo sacar más de lo que tengo"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_con_items, "lapiz", 100)
        resultado = sacar(carrito_con_items, "lapiz", 200)
        assert resultado == False
        assert carrito_con_items["lapiz"] == 105
    
    def test_sacar_todo_el_stock_borra_clave(self, carrito_vacio, carrito_funcs):
        """Si saco toda la cantidad, la clave se elimina"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 5)
        sacar(carrito_vacio, "lapiz", 5)
        assert "lapiz" not in carrito_vacio
    
    def test_sacar_cantidad_1(self, carrito_con_items, carrito_funcs):
        """Puedo sacar cantidad mínima (1 unidad)"""
        _, _, sacar, _, _ = carrito_funcs
        sacar(carrito_con_items, "lapiz", 1)
        assert carrito_con_items["lapiz"] == 4
    
    def test_sacar_cantidad_cero_no_hace_nada(self, carrito_vacio, carrito_funcs):
        """CANTIDAD CERO: Sacar 0 unidades no hace nada"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_vacio, "Lapiz", 5)
        resultado = sacar(carrito_vacio, "lapiz", 0)
        assert resultado == False
        assert carrito_vacio["lapiz"] == 5
    
    def test_sacar_luego_agregar_mismo_producto(self, carrito_vacio, carrito_funcs):
        """Ciclo: agregar → sacar → agregar del mismo producto"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 10)
        sacar(carrito_vacio, "lapiz", 4)
        agregar(carrito_vacio, "lapiz", 2)
        assert carrito_vacio["lapiz"] == 8


class TestTotal:
    
    def test_total_carrito_vacio_es_cero(self, carrito_vacio, carrito_funcs):
        """Total de carrito vacío es $0.00"""
        _, _, _, _, total = carrito_funcs
        assert total(carrito_vacio) == 0.0
    
    def test_total_un_producto(self, carrito_vacio, carrito_funcs):
        """Total de un solo producto"""
        _, agregar, _, _, total = carrito_funcs
        agregar(carrito_vacio, "lapiz", 2)
        assert total(carrito_vacio) == 5.0
    
    def test_total_varios_productos(self, carrito_con_items, carrito_funcs):
        """Total acumula todos los productos"""
        _, _, _, _, total = carrito_funcs
        assert total(carrito_con_items) == 36.5
    
    def test_total_preciso_decimales(self, carrito_vacio, carrito_funcs):
        """El total maneja decimales correctamente"""
        _, agregar, _, _, total = carrito_funcs
        agregar(carrito_vacio, "boligrafo", 3)
        assert abs(total(carrito_vacio) - 10.50) < 0.01


class TestVerCantidades:
    
    def test_ver_carrito_vacio_devuelve_vacio(self, carrito_vacio, carrito_funcs):
        """Ver cantidades en carrito vacío devuelve []"""
        _, _, _, ver_cantidades, _ = carrito_funcs
        assert ver_cantidades(carrito_vacio) == []
    
    def test_ver_cantidades_un_producto(self, carrito_vacio, carrito_funcs):
        """Ver cantidades con un producto"""
        _, agregar, _, ver_cantidades, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 5)
        cantidades = ver_cantidades(carrito_vacio)
        assert ("lapiz", 5) in cantidades
    
    def test_ver_cantidades_varios_productos(self, carrito_con_items, carrito_funcs):
        """Ver cantidades con múltiples productos"""
        _, _, _, ver_cantidades, _ = carrito_funcs
        cantidades = ver_cantidades(carrito_con_items)
        assert ("lapiz", 5) in cantidades
        assert ("cuaderno", 3) in cantidades


class TestCasosExtremos:
    
    def test_agregar_luego_sacar_todo_carrito_vacio(self, carrito_vacio, carrito_funcs):
        """Agregar todo → Sacar todo → Carrito vacío nuevamente"""
        _, agregar, sacar, _, total = carrito_funcs
        agregar(carrito_vacio, "lapiz", 10)
        agregar(carrito_vacio, "cuaderno", 5)
        sacar(carrito_vacio, "lapiz", 10)
        sacar(carrito_vacio, "cuaderno", 5)
        assert len(carrito_vacio) == 0
        assert total(carrito_vacio) == 0.0
    
    def test_operaciones_alternadas_multiples_veces(self, carrito_vacio, carrito_funcs):
        """Múltiples ciclos de agregar/sacar"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_vacio, "lapiz", 3)
        sacar(carrito_vacio, "lapiz", 1)
        agregar(carrito_vacio, "lapiz", 2)
        sacar(carrito_vacio, "lapiz", 4)
        assert "lapiz" not in carrito_vacio
    
    def test_productos_no_interfieren_entre_si(self, carrito_con_items, carrito_funcs):
        """Operar un producto no afecta a otros"""
        _, agregar, sacar, _, _ = carrito_funcs
        agregar(carrito_con_items, "boligrafo", 4)
        sacar(carrito_con_items, "lapiz", 2)
        assert carrito_con_items["lapiz"] == 3
        assert carrito_con_items["cuaderno"] == 3
        assert carrito_con_items["boligrafo"] == 4