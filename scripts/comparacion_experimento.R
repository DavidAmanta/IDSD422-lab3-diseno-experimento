# comparacion_experimento.R — Comparación de grupos (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/comparacion_experimento.R

# TODO 1: carga plantillas/registro_experimento.csv (read.csv)
df <- read.csv("plantillas/registro_experimento.csv", stringsAsFactors = FALSE)
print(head(df))

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
#         (aggregate)
print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))
# TODO 3: imprime el número de registros por grupo (table)
print(table(df$ubicacion))
# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
cat("\nInterpretación:\n")
cat("Con 4 filas no hay aleatorización real, ni medida de variabilidad (desviación, IC),",
    "y la promoción simultánea en Guayaquil Centro (pasillo) infla ese promedio.\n")
cat("Faltarían más unidades, comparación pareada por tienda, control de temporada y promociones, y una prueba estadística.\n")


# Simulacion de 40 filas
sim <- read.csv("plantillas/resultado_simulacion.csv", stringsAsFactors = FALSE)
media_tienda <- tapply(sim$ventas_producto, list(sim$tienda, sim$ubicacion), mean)
dif <- media_tienda[, "pasillo_principal"] - media_tienda[, "habitual"]
cat("\nDiferencia media:", mean(dif), " | Desv. est.:", sd(dif), "\n")

prueba <- t.test(media_tienda[, "pasillo_principal"],
                 media_tienda[, "habitual"], paired = TRUE)
cat("IC 95%: [", prueba$conf.int[1], ",", prueba$conf.int[2], "]\n")
cat("p-value:", prueba$p.value, "\n")