# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** David Amanta  · **Fecha:** 27/10/2026

## 1. Pregunta e hipótesis

**Pregunta**: ¿Vende más, en promedio, el producto cuando se exhibe en el pasillo principal que en su ubicación habitual?

**Hipótesis**: En 10 tiendas, durante 4 semanas, las ventas semanales promedio en USD del producto serán mayores en el pasillo principal que en la ubicación habitual.
- H₀: la diferencia media de ventas (pasillo principal − habitual) es 0.
- H₁: la diferencia media es mayor que 0.


## 2. Unidad experimental

Semana-tienda: 10 tiendas × 4 semanas = 40 unidades. Se justifica porque la ubicación se cambia semana a semana dentro de cada tienda. Para el análisis estadístico, la unidad efectiva es la tienda (n = 10 diferencias pareadas), porque las semanas de una misma tienda no son independientes.

- 10 tiendas x 4 semanas = 40 unidades

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicación del producto
- **Niveles** (valores del factor): Pasillo principal y Habitual
- **Tratamiento** (combinación asignada): Pasillo principal durante una semana y ubicación habitual durante otra (grupo de control)

## 4. Grupo de control

La misma tienda en las semanas en que el producto está en su ubicación habitual. Sirve de referencia y elimina las diferencias entre tiendas (tamaño, clientela).

## 5. Aleatorización

Se sortea, para cada una de las 10 tiendas, qué ubicación recibe en la semana 1 (pasillo principal u habitual) en las semanas siguientes se alterna. El sorteo hace que la asignación no dependa de ninguna característica de la tienda ni de la semana, por lo que los factores desconocidos (clima, afluencia, tendencia de ventas, eventos locales) quedan repartidos al azar entre ambas ubicaciones en lugar de favorecer a una. Así, una diferencia sistemática de ventas puede atribuirse con mayor confianza a la ubicación y no a esos factores. La semilla (1234597) hace el sorteo reproducible.

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
