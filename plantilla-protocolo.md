# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** David Amanta  · **Fecha:** 27/10/2026

## 1. Pregunta e hipótesis

El producto  en el pasillo principal, vende más en promedio que su ubicación actual, en ventas semanales durante 4 semanas.

## 2. Unidad experimental

Semana-Tienda
(**# de tiendas x # de semanas**)

- 10 tiendas x 4 semanas = 40 unidades

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicación
- **Niveles** (valores del factor): Pasillo y Habitual
- **Tratamiento** (combinación asignada): Pasillo durante una semana y ubicación habitual durante otra (grupo de control)

## 4. Grupo de control

La misma tienda, pero con el producto dispuesto en la ubicacón habitual.

## 5. Aleatorización

Sorteo de 20, tiendas a cada grupo (paralelo). 

- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta: Ventas semanales en USD
- Período de medición: 4 semanas
- Quién registra y cómo (¿ciego?): Mediante el POS, ciego (vendedor no sabría si el producto esta en principal o en habitual)

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | Clima |
| 2. | Evento Local | 
| 3. | Surtido / Stock |
| 4. | Cambios en el personal |

## 8. Limitaciones del diseño

- Pérdida de potencia por promociones
- Canibalización de las tiendas

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo muestra 1335 USD en venta frente a 1040 USD en habitual

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
No se puede concluir porque no hay ninguna afirmación real aleatoria, los datos son muy pocos (4), no tenemos control de temporada, ni promociones en el grupo pasillo y no hay medida de variabilidad.

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
