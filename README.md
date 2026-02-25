# 🧭 Calculadora de Ruta Más Corta

**Encuentra el camino de menor costo entre dos puntos en una red.**  
Diseñado especialmente para estudiantes y profesionales de **arquitectura y urbanismo**, pero útil para cualquier persona que trabaje con redes y optimización.
Pueden resolverlo manualmente con GRAFOS. 

---

## 📌 ¿Qué hace este programa?

Permite modelar una red de nodos (representados con letras de la **A** a la **Z**) y conexiones con costos (distancias, tiempos, etc.). Luego, calcula la ruta más corta desde un origen hasta un destino, mostrando tanto la secuencia de nodos como el costo total.

**Ejemplo de uso:**  
Si ingresas los nodos A, B, C, D y las conexiones:
- A → B con costo 2
- A → C con costo 4
- B → C con costo 1
- B → D con costo 7
- C → D con costo 3

Y pides la ruta de **A a D**, el programa responderá:  
`A → B → C → D` con un costo total de **6**.

---

## ✨ Características

- ✅ En español
- ✅ Para nodos se usan las letras mayúsculas (hasta 26 nodos de la A a la Z).
- ✅ Verificado (Si hay errores, lo pueden corregir o cambiar)
- ✅ Algoritmo de **programación dinámica recursiva con memoización**.
- ✅ Se puede ejecutar como script Python o como archivo `.exe` (sin necesidad de instalar Python).
- ✅ ANEXO: comprimido `.rar` del programa

---

## 🧱 Aplicaciones en arquitectura y urbanismo

- Diseño de **circulaciones peatonales y vehiculares** en edificios.
- Planificación de **rutas óptimas** en tejidos urbanos.
- Optimización de **redes de servicios** (agua, energía, telecomunicaciones).
- Evaluación de **recorridos de evacuación** en caso de emergencias.
- Los que impliquen un esquema de redes en cualquier ámbito

---

## 🚀 Cómo usarlo

### Opción 1: Con Python instalado
1. Guarda el archivo `ruta_corta.py`.
2. Abre una terminal en la carpeta donde lo guardaste.
3. Ejecuta:
   ```bash
   python 01_ruta_corta.py
