# comparacion_experimento.R — Comparación de grupos (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/comparacion_experimento.R

# TODO 1: carga plantillas/registro_experimento.csv (read.csv)
# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
#         (aggregate)
# TODO 3: imprime el número de registros por grupo (table)
# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
df <- read.csv("plantillas/registro_simulacion.csv", stringsAsFactors = FALSE)

print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))