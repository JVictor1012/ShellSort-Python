import random
import time


def numeros(tam, min, max):
    return [random.randint(min, max) for _ in range(tam)]

def shellShort(lista):
    tamanho = len(lista)
    h = tamanho // 2

    while h > 0:
      
        for i in range(h, tamanho):
            atual = lista[i]
            j = i
            while j >= h and lista[j - h] > atual:
                lista[j] = lista[j - h]
                j -= h
            lista[j] = atual
        h //= 2


#array = [5, 6, 7, 10, 56, 94, 3, 0, 25, 9] # 10 numeros

array = numeros(500000, 1, 100000) #500 mil números


print("Array antes da ordenação:")
print(array[:10], "...", array[-10:], "\n")


tempo_inicio = time.time()

shellShort(array)

tempo_fim = time.time()
tempo_total = tempo_fim - tempo_inicio

print("Array ordenado:")
print(array[:10], "...", array[-10:], "\n")

print("Tempo de ordenação :", tempo_total, "segundos")
