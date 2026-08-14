from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    inicio = 0
    final = len(nums) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if nums[medio] == target:
            return medio
        elif nums[medio] < target:
            inicio = medio + 1
        else:
            final = medio - 1

    return inicio

if __name__ == "__main__":
    numeros = [1, 3, 5, 6]
    objetivo = 5

    posicion = searchInsert(nums=numeros, target=objetivo)
    print(f"El objetivo: {objetivo}, en el array: {numeros}, se introduce en la posicion: {posicion}.")