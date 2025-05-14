# Tratamiento de datos
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Gráficos
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import style
style.use('ggplot') or plt.style.use('ggplot')

# Preprocesado y modelado
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

# Configuración warnings
import warnings
warnings.filterwarnings('ignore')

#==============================================================================================
#Importar datos
file_path = "/Users/merimacias/Downloads/subject01_walk_IK.mot"
#Para leer correctamente el archivo .mot, que contiene datos con un encabezado no estándar
with open(file_path, 'r') as file:
    lines = file.readlines()

header_end = next(i for i, line in enumerate(lines) if 'endheader' in line.lower())

#==============================================================================================
#Dataframe con el trabajaremos:
df = pd.read_csv(file_path, delim_whitespace=True, skiprows=header_end + 1)

#Varianzas
print('-------------------------')
print('Varianza de cada variable')
print('-------------------------')
df.var(axis=0)

# Separar la columna de tiempo (para conservarla si luego queremos graficar en función del tiempo)
time = df['time']
df_data = df.drop(columns=['time'])

#==============================================================================================
#Escalar los datos antes de PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_data)

# Aplicar PCA
pca = PCA()
principal_components = pca.fit_transform(scaled_data)

# Convertir resultados a DataFrame (opcional)
pca_df = pd.DataFrame(principal_components, columns=[f'PC{i+1}' for i in range(pca.n_components_)])
pca_df['time'] = time  # conservar tiempo para visualización
pca_df

#==============================================================================================
# Varianza explicada por cada componente
explained_var = pca.explained_variance_ratio_

# Mostrar en forma de tabla
for i, var in enumerate(explained_var):
    print(f"PC{i+1}: {var:.4f} ({var*100:.2f}% de la varianza)")

# Varianza acumulada
cumulative_var = np.cumsum(explained_var)
print("\nVarianza acumulada:")
for i, var in enumerate(cumulative_var):
    print(f"PC1 a PC{i+1}: {var:.4f} ({var*100:.2f}%)")

# Gráfico de varianza explicada
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(explained_var)+1), cumulative_var, marker='o', label='Varianza acumulada')
plt.bar(range(1, len(explained_var)+1), explained_var, alpha=0.5, label='Varianza individual')
plt.xticks(range(1, len(explained_var)+1))
plt.xlabel('Componente principal')
plt.ylabel('Fracción de varianza explicada')
plt.title('Varianza explicada por los componentes principales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#========================================================================================================================
# Obtener los nombres de las variables originales
original_features = df_data.columns

# Obtener los loadings (componentes)
loadings = pd.DataFrame(pca.components_.T, columns=[f'PC{i+1}' for i in range(pca.n_components_)], index=original_features)

# Mostrar cuanto contribuyen las variables al PC1
L1 = loadings['PC1'].abs().sort_values(ascending=False)
print("Contribuciones a PC1:")
print(L1)

# Barplot de las 5 mayores contribuciones a PC1
topL1 = L1.head(5)
topL1.index = topL1.index.str.replace('_', '\n')  # opcional para legibilidad
topL1.plot(kind='bar', title='Variables que más contribuyen a PC1')
plt.ylabel('Valor absoluto del loading')
plt.show()

#Análisis PC2
L2 = loadings['PC2'].abs().sort_values(ascending=False)
print("Contribuciones a PC2:")
print(L2)

topL2 = L2.head(5)
topL2.index = topL2.index.str.replace('_', '\n')
topL2.plot(kind='bar', title='Variables que más contribuyen a PC2')
plt.ylabel('Valor absoluto del loading')
plt.show()

#Análisis PC3
L3 = loadings['PC3'].abs().sort_values(ascending=False)
print("Contribuciones a PC3:")
print(L3)

topL3 = L3.head(5)
topL3.index = topL3.index.str.replace('_', '\n')
topL3.plot(kind='bar', title='Variables que más contribuyen a PC3')
plt.ylabel('Valor absoluto del loading')
plt.show()

#PC4
L4 = loadings['PC4'].abs().sort_values(ascending=False)
print("Contribuciones a PC4:")
print(L4)

topL4 = L4.head(5)
topL4.index = topL4.index.str.replace('_', '\n')
topL4.plot(kind='bar', title='Variables que más contribuyen a PC4')
plt.ylabel('Valor absoluto del loading')
plt.show()


#Proyección de los datos originales en el espacio de los dos primeros componentes principales (PC1 y PC2)
# Guardar tiempo y preparar datos
time = df['time']
df_data = df.drop(columns=['time'])

# PCA
X_scaled = StandardScaler().fit_transform(df_data)
X_pca = PCA(n_components=2).fit_transform(X_scaled)

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=time, cmap='plasma')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Proyección en PC1 vs PC2')
plt.colorbar(label='Tiempo (s)')
plt.grid(True)
plt.tight_layout()
plt.show()
