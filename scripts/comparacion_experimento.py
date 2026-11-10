# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import json

import pandas as pd
import numpy as np

df = pd.read_csv("plantillas/registro_experimento.csv")
print(df.head())

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion 
print("\n")
print(df.groupby("ubicacion")["ventas_producto"].mean())

# TODO 3: imprime el número de registros por grupo (value_counts)\
print("\n")
print( df["ubicacion"].value_counts())

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
print("\n")
print("Interpretación:")
print("Con solo 4 filas de datos, no se puede concluir que haya una diferencia significativa entre las ubicaciones, ya que la muestra es demasiado pequeña para representar la población. Se necesitaría un tamaño de muestra mayor y un análisis estadístico más robusto para poder hacer afirmaciones confiables sobre las diferencias en ventas entre ubicaciones.")


# DISENIO DE EXPERIMENTO
tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte", 
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"]

semanas = [1, 2, 3, 4] 

#Sorteo de la condicion inicial
rng = np.random.default_rng(1234597)  # Semilla para reproducibilidad
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

filas = []
for tienda, cond in zip(tiendas, primera):
   otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
   for s in semanas:
         filas.append({"tienda": tienda, 
                       "semana": s,
                       "ubicacion": cond if s%2 == 1 else otra})

diseno = pd.DataFrame(filas)

#Simulacion de la ejecucion
rng = np.random.default_rng(1234598)  # Semilla para reproducibilidad
efecto_tienda = dict(zip(tiendas, rng.normal(1100, 120, len(tiendas)))) 
efecto_semana = {1: 0, 2: 30, 3: 60, 4: 90}  
diseno["ventas_producto"] = (
     diseno["tienda"].map(efecto_tienda) +
     diseno["semana"].map(efecto_semana) + 
     (diseno["ubicacion"] == "pasillo_principal")*220 +
     rng.normal(0, 90, len(diseno))
 ).round(0).astype(int)

#Promocion simultanea registrada
diseno["promocion_simultanea"] = "no"

diseno.loc[(diseno["tienda"]== "Guayaquil Centro") & (diseno["semana"] == 1), "promocion_simultanea"] = "si"
diseno.loc[diseno["promocion_simultanea"] == "si", "ventas_producto"] += 180

diseno.to_csv("plantillas/resultado_simulacion.csv", index=False)

#Analisis pareado: una fila por tienda con sus condiciones 
piv = diseno.groupby(["tienda", "ubicacion"])["ventas_producto"].mean().unstack()
piv["diferencia"] = piv["pasillo_principal"] - piv["habitual"]

media = piv["diferencia"].mean()
dev = piv["diferencia"].std(ddof=1)

print("\n")
print("Promedio de la diferencia de ventas entre ubicaciones:", media)
print("Desviación estándar de la diferencia de ventas entre ubicaciones:", dev)

