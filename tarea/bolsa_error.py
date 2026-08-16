# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html

class ElementoNoEncontradoError(Exception):
    """El elemento solicitado no está en la bolsa."""


class BolsaLista:
    """Bolsa implementada sobre una lista: un elemento por cada aparición.

    Complejidad:
        agregar  -> O(1)
        sacar    -> O(n)
        cuantos  -> O(n)
        tamaño   -> O(1)
        contiene -> O(n)
    """

    def __init__(self):
        self._elementos = []

    def agregar(self, elemento):
        """Agrega UNA aparición del elemento a la bolsa. O(1)"""
        self._elementos.append(elemento)

    def sacar(self, elemento):
        """Saca UNA aparición del elemento.
        Si no existe, lanza ElementoNoEncontradoError. O(n)
        """
        for i in range(len(self._elementos)):
            if self._elementos[i] == elemento:
                self._elementos.pop(i)
                return
        raise ElementoNoEncontradoError(f"'{elemento}' no está en la bolsa")

    def cuantos(self, elemento):
        """Devuelve cuántas veces aparece el elemento. O(n)"""
        contador = 0
        for e in self._elementos:
            if e == elemento:
                contador += 1
        return contador

    def tamaño(self):
        """Devuelve la cantidad total de elementos. O(1)"""
        return len(self._elementos)

    def contiene(self, elemento):
        """Devuelve True si el elemento está en la bolsa. O(n)"""
        return elemento in self._elementos

    def __len__(self):
        return self.tamaño()

    def __repr__(self):
        return f"BolsaLista({self._elementos!r})"


# ================================================
# 🧪 PRUEBAS
# ================================================
if __name__ == "__main__":
    bolsa = BolsaLista()

    # --- Agregar ---
    bolsa.agregar("lapiz")
    bolsa.agregar("lapiz")
    bolsa.agregar("cuaderno")
    print(bolsa)                    # BolsaLista(['lapiz', 'lapiz', 'cuaderno'])

    # --- Cuántos ---
    print(bolsa.cuantos("lapiz"))    # 2
    print(bolsa.cuantos("cuaderno"))# 1
    print(bolsa.cuantos("mochila"))# 0

    # --- Tamaño ---
    print(bolsa.tamaño())            # 3
    print(len(bolsa))                # 3

    # --- Contiene ---
    print(bolsa.contiene("lapiz"))   # True
    print(bolsa.contiene("mochila"))# False

    # --- Sacar ---
    bolsa.sacar("lapiz")             # Saca UN solo lápiz
    print(bolsa)                     # BolsaLista(['lapiz', 'cuaderno'])
    print(bolsa.cuantos("lapiz"))   # 1

    # --- Sacar algo que no existe ---
    try:
        bolsa.sacar("mochila")
    except ElementoNoEncontradoError as e:
        print(e)                     # 'mochila' no está en la bolsa
    