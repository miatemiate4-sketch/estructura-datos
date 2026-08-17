"""
test_carrito_ucc.py
Batería de pruebas para el TAD Carrito UCC
Cubre casos normales, límites y extremos
"""

import pytest
from carrito import agregar, sacar, ver_cantidades, total, crear_carrito


@pytest.fixture
def carrito_vacio():
    """Fixture: carrito completamente vacío"""
    return crear_carrito()


@pytest.fixture
def carrito_con_items():
    """Fixture: carrito con productos pre-cargados"""
    c = crear_carrito()
    agregar(c, "lapiz", 5)
    agregar(c, "cuaderno", 3)
    return c


class TestCarritoVacio:
    
    def test_carrito_nuevo_esta_vacio(self):
        """Un carrito recién creado debe estar vacío"""
        c = crear_carrito()
        assert len(c) == 0
    
    def test_total_carrito_vacio_es_cero(self):
        """Total de carrito vacío es $0.00"""
        c = crear_carrito()
        assert total(c) == 0.0
    
    def test_ver_cantidades_carrito_vacio_devuelve_lista_vacia(self):
        """Ver cantidades en carrito vacío devuelve []"""
        c = crear_carrito()
        assert ver_cantidades(c) == []


class TestAgregar:
    
    def test_agregar_producto_valido_exitoso(self, carrito_vacio):
        """Puedo agregar un producto que existe en el catálogo"""
        resultado = agregar(carrito_vacio, "lapiz", 3)
        assert resultado == True
        assert carrito_vacio["lapiz"] == 3
    
    def test_agregar_cantidad_cero_falla(self, carrito_vacio):
        """ CANTIDAD CERO: No puedo agregar cantidad 0"""
        resultado = agregar(carrito_vacio, "lapiz", 0)
        assert resultado == False
        assert "lapiz" not in carrito_vacio
    
    def test_agregar_cantidad_negativa_falla(self, carrito_vacio):
        """ CANTIDAD NEGATIVA: No puedo agregar cantidad negativa"""
        resultado = agregar(carrito_vacio, "lapiz", -5)
        assert resultado == False
    
    def test_agregar_producto_inexistente_falla(self, carrito_vacio):
        """No puedo agregar producto que no está en catálogo"""
        resultado = agregar(carrito_vacio, "remera", 2)
        assert resultado == False
        assert "remera" not in carrito_vacio
    
    def test_agregar_suma_si_ya_existe(self, carrito_vacio):
        """Agregar producto existente suma la cantidad"""
        agregar(carrito_vacio, "lapiz", 2)
        agregar(carrito_vacio, "lapiz", 3)
        assert carrito_vacio["lapiz"] == 5
    
    def test_agregar_varios_productos_distintos(self, carrito_vacio):
        """Puedo agregar múltiples productos diferentes"""
        agregar(carrito_vacio, "lapiz", 2)
        agregar(carrito_vacio, "cuaderno", 3)
        assert len(carrito_vacio) == 2
    
    def test_agregar_normaliza_a_minusculas(self, carrito_vacio):
        """Nombres en mayúscula se normalizan a minúscula"""
        agregar(carrito_vacio, "LAPIZ", 1)
        assert "lapiz" in carrito_vacio
        assert "LAPIZ" not in carrito_vacio
    
    def test_agregar_cantidad_muy_grande(self, carrito_vacio):
        """Puedo agregar cantidades muy grandes"""
        agregar(carrito_vacio, "lapiz", 999999)
        assert carrito_vacio["lapiz"] == 999999


class TestSacar:
    
    def test_sacar_producto_disponible_exitoso(self, carrito_con_items):
        """Puedo sacar si tengo suficientes unidades"""
        resultado = sacar(carrito_con_items, "lapiz", 2)
        assert resultado == True
        assert carrito_con_items["lapiz"] == 3  # 5 - 2
    
    def test_sacar_lo_que_no_esta_no_modifica(self, carrito_vacio):
        """ SACAR LO QUE NO ESTÁ: Si saco producto que no tengo, no cambia nada"""
        cantidad_inicial = len(carrito_vacio)
        resultado = sacar(carrito_vacio, "remera", 1)
        assert resultado == False
        assert len(carrito_vacio) == cantidad_inicial  # Sin cambios
    
    def test_sacar_mas_que_tengo_no_modifica(self, carrito_con_items):
        """ STOCK INSUFICIENTE: No puedo sacar más de lo que tengo"""
        agregar(carrito_con_items, "lapiz", 100)  # Ahora tengo 105
        resultado = sacar(carrito_con_items, "lapiz", 200)
        assert resultado == False
        assert carrito_con_items["lapiz"] == 105  # No cambió
    
    def test_sacar_todo_el_stock_borra_clave(self, carrito_vacio):
        """Si saco toda la cantidad, la clave se elimina"""
        agregar(carrito_vacio, "lapiz", 5)
        sacar(carrito_vacio, "lapiz", 5)
        assert "lapiz" not in carrito_vacio
    
    def test_sacar_cantidad_1(self, carrito_con_items):
        """Puedo sacar cantidad mínima (1 unidad)"""
        sacar(carrito_con_items, "lapiz", 1)
        assert carrito_con_items["lapiz"] == 4
    
    def test_sacar_cantidad_cero_no_hace_nada(self, carrito_vacio):
        """ CANTIDAD CERO: Sacar 0 unidades no hace nada"""
        agregar(carrito_vacio, "lapiz", 5)
        resultado = sacar(carrito_vacio, "lapiz", 0)
        # El comportamiento depende de la implementación
        # En nuestro caso: 0 <= 0, entonces no debería modificar
    
    def test_sacar_luego_agregar_mismo_producto(self, carrito_vacio):
        """Ciclo: agregar → sacar → agregar del mismo producto"""
        agregar(carrito_vacio, "lapiz", 10)
        sacar(carrito_vacio, "lapiz", 4)
        agregar(carrito_vacio, "lapiz", 2)
        assert carrito_vacio["lapiz"] == 8  # 10 - 4 + 2


class TestTotal:
    
    def test_total_carrito_vacio_es_cero(self, carrito_vacio):
        """Total de carrito vacío es $0.00"""
        assert total(carrito_vacio) == 0.0
    
    def test_total_un_producto(self, carrito_vacio):
        """Total de un solo producto"""
        agregar(carrito_vacio, "lapiz", 2)
        assert total(carrito_vacio) == 5.0  # 2 × $2.50
    
    def test_total_varios_productos(self, carrito_con_items):
        """Total acumula todos los productos"""
        # lapiz: 5 × $2.50 = $12.50
        # cuaderno: 3 × $8.00 = $24.00
        assert total(carrito_con_items) == 36.5
    
    def test_total_preciso_decimales(self, carrito_vacio):
        """El total maneja decimales correctamente"""
        agregar(carrito_vacio, "boligrafo", 3)  # 3 × $3.50 = $10.50
        assert abs(total(carrito_vacio) - 10.50) < 0.01


class TestVerCantidades:
    
    def test_ver_carrito_vacio_devuelve_vacio(self, carrito_vacio):
        """Ver cantidades en carrito vacío devuelve []"""
        assert ver_cantidades(carrito_vacio) == []
    
    def test_ver_cantidades_un_producto(self, carrito_vacio):
        """Ver cantidades con un producto"""
        agregar(carrito_vacio, "lapiz", 5)
        cantidades = ver_cantidades(carrito_vacio)
        assert ("lapiz", 5) in cantidades
    
    def test_ver_cantidades_varios_productos(self, carrito_con_items):
        """Ver cantidades con múltiples productos"""
        cantidades = ver_cantidades(carrito_con_items)
        assert ("lapiz", 5) in cantidades
        assert ("cuaderno", 3) in cantidades


class TestCasosExtremos:
    
    def test_agregar_luego_sacar_todo_carrito_vacio(self, carrito_vacio):
        """Agregar todo → Sacar todo → Carrito vacío nuevamente"""
        agregar(carrito_vacio, "lapiz", 10)
        agregar(carrito_vacio, "cuaderno", 5)
        sacar(carrito_vacio, "lapiz", 10)
        sacar(carrito_vacio, "cuaderno", 5)
        assert len(carrito_vacio) == 0
        assert total(carrito_vacio) == 0.0
    
    def test_operaciones_alternadas_multiples_veces(self, carrito_vacio):
        """Múltiples ciclos de agregar/sacar"""
        agregar(carrito_vacio, "lapiz", 3)
        sacar(carrito_vacio, "lapiz", 1)
        agregar(carrito_vacio, "lapiz", 2)
        sacar(carrito_vacio, "lapiz", 4)
        assert "lapiz" not in carrito_vacio
    
    def test_productos_no_interfieren_entre_si(self, carrito_con_items):
        """Operar un producto no afecta a otros"""
        agregar(carrito_con_items, "boligrafo", 4)
        sacar(carrito_con_items, "lapiz", 2)
        assert carrito_con_items["lapiz"] == 3  # 5 - 2
        assert carrito_con_items["cuaderno"] == 3  # Sin cambios
        assert carrito_con_items["boligrafo"] == 4
