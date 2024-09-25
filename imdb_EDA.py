import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Ruta y carga del CSV con Pandas
path = "./imdb_top_1000.csv"
data = pd.read_csv(path)

# Averiguo el numero de filas y columnas del csv
print("La estructura de este data set es de: {} filas y {} columnas".format(data.shape[0], data.shape[1]))

#La primera ojeada del data para conocer los nombres de las columnas
data.head(3)