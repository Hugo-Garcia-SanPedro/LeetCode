from typing import List

class Solution:
    def solucionNQueens(self, n: int) -> List[List[str]]:
        # Primero creamos el tablero
        resultado = []
        tablero = [["."] * n for i in range(n)]

        # Funcion de backtracking
        def backtracking(fila):
            # Paso base
            if fila == n:
                copia = ["".join(fila) for fila in tablero]
                resultado.append(copia)
                return

            # Resto de posibilidades
            for columna in range(n):
                if self.esSeguro(fila, columna, tablero):
                    # Primero colocamos la ficha
                    tablero[fila][columna] = "Q"
                    # Segundo llamamos a la funcion backtracking
                    backtracking(fila + 1)
                    # Por ultimo se deshace el movimiento
                    tablero[fila][columna] = "."

            backtracking(0)
            return resultado

    def esSeguro(self, f: int, c: int, tablero):
        # Comprobamls las filas
        fila = f - 1
        while fila >= 0:
            if tablero[fila][c] == "Q":
                return False
            fila = fila - 1

        # Comprobamos las columnas
        columna = c - 1
        fila = f - 1
        while columna >= 0 and fila >= 0:
            if tablero[fila][columna] == "Q":
                return False
            fila = fila - 1
            columna = columna - 1

        # Comprobamos las diagonales
        fila = f - 1
        columna = c + 1
        while fila >= 0 and columna < len(tablero):
            if tablero[fila][columna] == "Q":
                return False
            fila = fila - 1
            columna = columna + 1

        return True

if __name__ == "__main__":
    solucion = Solution()
    n = 5
    tablero = solucion.solucionNQueens(n=n)
    print(tablero)
