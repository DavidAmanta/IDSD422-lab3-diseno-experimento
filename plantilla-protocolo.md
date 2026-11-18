# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** David Amanta  · **Fecha:** 27/10/2026

## 1. Pregunta e hipótesis

**Pregunta**: ¿Vende más, en promedio, el producto cuando se exhibe en el pasillo principal que en su ubicación habitual?

**Hipótesis**: En 10 tiendas, durante 4 semanas, las ventas semanales promedio en USD del producto serán mayores en el pasillo principal que en la ubicación habitual.
- H₀: la diferencia media de ventas (pasillo principal − habitual) es 0.
- H₁: la diferencia media es distinta de 0.


## 2. Unidad experimental

Semana-tienda: 10 tiendas × 4 semanas = 40 unidades. Se justifica porque la ubicación se cambia semana a semana dentro de cada tienda. Para el análisis estadístico, la unidad efectiva es la tienda (n = 10 diferencias pareadas), porque las semanas de una misma tienda no son independientes.


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

- **Qué podría invalidar el diseño:** promociones simultáneas, efecto de arrastre entre semanas consecutivas, tendencia temporal no perfectamente balanceada, quiebres de stock, eventos externos locales, incumplimiento del protocolo de colocación y ciego solo parcial.

- **Qué no se podrá concluir:** que el efecto aplique a otros productos, otras tiendas o regiones, ni que se mantenga a largo plazo; tampoco el mecanismo causal, el impacto sobre productos vecinos (canibalización) ni la rentabilidad. Con solo 10 tiendas y 4 semanas, los resultados son orientativos.


## 9. Comparación en código (Python/R)

- ¿Qué grupo muestra mayor venta promedio en la plantilla?

   El grupo pasillo principal muestra la mayor venta promedio: 1335 USD frente a 1040 USD en la ubicación habitual (diferencia de 295 USD).

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?

    Con 4 filas no se puede concluir porque hay solo 2 observaciones por grupo, así que un dato atípico cambia todo el promedio, cada fila es una tienda distinta, por lo que la diferencia puede deberse a la tienda y no a la ubicación, no hay evidencia de aleatorización en la asignación, la única fila con promoción simultánea (Guayaquil Centro, 1420 USD) está en el grupo pasillo y lo infla, no hay control de temporada y finalmente no hay medida de variabilidad (desviación, IC ni p-value) para saber si la diferencia es mayor que el azar.

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?

    Le faltarían más unidades (10 tiendas × 4 semanas = 40 observaciones), que cada tienda pruebe ambas ubicaciones, para comparar dentro de la misma tienda (análisis pareado), una asignación aleatoria del orden con semilla, un control o registro de promociones, temporada, stock y afluencia; y una medida de variabilidad y una prueba estadística.

     En la simulación, esto da una diferencia media de 239.7 USD, IC 95% [166.5, 312.9] y p = 0.00004, que ya permite una conclusión más sólida.