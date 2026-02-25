# -*- coding: utf-8 -*-
"""
PROGRAMA: RUTA MÁS CORTA
Propósito: Encontrar el camino de menor costo entre dos nodos en una red.
Autor: Javier Ayala
"""

import sys

def ruta_mas_corta(origen, destino, grafo, memo):
    """
    Retorna (costo_total, lista_de_nodos) con la ruta de menor costo
    desde 'origen' hasta 'destino' usando programación dinámica recursiva.
    Si no hay camino, retorna (float('inf'), []).
    """
    if origen == destino:
        return 0, [destino]
    if origen in memo:
        return memo[origen]

    mejor_costo = float('inf')
    mejor_ruta = []

    for vecino, costo_arista in grafo.get(origen, {}).items():
        costo_restante, ruta_restante = ruta_mas_corta(vecino, destino, grafo, memo)
        if costo_restante < float('inf'):
            costo_total = costo_arista + costo_restante
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_ruta = [origen] + ruta_restante

    memo[origen] = (mejor_costo, mejor_ruta)
    return mejor_costo, mejor_ruta


def main():
    print("=" * 60)
    print("         CALCULADORA DE RUTA MÁS CORTA")
    print("         (Programación Dinámica)")
    print("=" * 60)
    print("   Desarrollado por: Javier Ayala | https://github.com/ayalapjavier | 2026")
    print("=" * 60)
    print("Este programa encuentra el camino de menor costo")
    print("entre dos puntos (nodos) en una red.")
    print("Los nodos se nombran con letras: A, B, C, ..., Z.\n")

    # Solicitar número de nodos
    while True:
        try:
            n = int(input("¿Cuántos nodos tiene su red? (máximo 26): "))
            if 1 <= n <= 26:
                break
            else:
                print("Por favor, ingrese un número entre 1 y 26.")
        except ValueError:
            print("Debe ingresar un número entero.")

    # Generar letras
    letras = [chr(ord('A') + i) for i in range(n)]
    print(f"\nLos nodos disponibles son: {', '.join(letras)}\n")

    # Inicializar grafo
    grafo = {letra: {} for letra in letras}

    # Ingreso de aristas
    print("Ahora ingrese cada conexión (arista) con su costo.")
    print("Formato: LetraOrigen LetraDestino Costo")
    print("Ejemplo: A B 5")
    print("Para terminar, escriba 'fin'.\n")

    while True:
        entrada = input("Arista: ").strip()
        if entrada.lower() == "fin":
            break

        partes = entrada.split()
        if len(partes) != 3:
            print("Formato incorrecto. Debe ser: Origen Destino Costo")
            continue

        o, d, c = partes[0].upper(), partes[1].upper(), partes[2]

        if o not in grafo:
            print(f"El nodo {o} no existe. Válidos: {', '.join(letras)}")
            continue
        if d not in grafo:
            print(f"El nodo {d} no existe. Válidos: {', '.join(letras)}")
            continue

        try:
            costo = float(c)
            if costo < 0:
                print("El costo debe ser un número positivo.")
                continue
        except ValueError:
            print("El costo debe ser un número.")
            continue

        grafo[o][d] = costo
        print(f"Arista guardada: {o} -> {d} con costo {costo}")

    # Solicitar origen y destino
    print("\nAhora indique el punto de partida (origen) y el punto de llegada (destino).")
    while True:
        origen = input("Nodo de origen: ").strip().upper()
        if origen in grafo:
            break
        print(f"El nodo {origen} no existe. Válidos: {', '.join(letras)}")

    while True:
        destino = input("Nodo de destino: ").strip().upper()
        if destino in grafo:
            break
        print(f"El nodo {destino} no existe. Válidos: {', '.join(letras)}")

    # Calcular ruta
    memo = {}
    costo, ruta = ruta_mas_corta(origen, destino, grafo, memo)

    # Mostrar resultado
    print("\n" + "=" * 60)
    if costo < float('inf'):
        print(f"La ruta más corta desde {origen} hasta {destino} es:")
        print(" -> ".join(ruta))
        print(f"Distancia total: {costo}")
    else:
        print(f"No existe una ruta desde {origen} hasta {destino}.")
    print("=" * 60)
    
    input("\nPresione Enter para salir...")


if __name__ == "__main__":
    main()