from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    inicio = 0
    final = len(nums)

    while inicio <= final:
        medio = inicio + (final - inicio) // 2
        if nums[medio] == target:
            return nums[medio]
        elif nums[medio] < target:
            inicio = nums[medio] + 1
        else:
            final = nums[medio] - 1

if __name__ == "__main__":
    numeros = [1, 3, 4, 6]
    objetivo = 4

    posicion = searchInsert(nums=numeros, target=objetivo)
    print(f"El objetivo: {objetivo}, en el array: {numeros}, se introduce en la posicion: {posicion}.")