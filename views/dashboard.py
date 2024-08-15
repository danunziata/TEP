import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Título del dashboard
st.title("Dashboard de Análisis Estadístico de Datos por Categoría")

# Selección de archivo
data_dir = "data"  # Directorio donde se encuentran los archivos CSV
file_options = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
file_options = sorted(file_options)  # Ordenar los archivos por nombre

selected_file = st.selectbox("Selecciona el archivo CSV a analizar", file_options)

# Cargar el archivo CSV seleccionado
if selected_file:
    file_path = os.path.join(data_dir, selected_file)
    df = pd.read_csv(file_path)

    # Mostrar datos del archivo completo
    st.write("### Datos del dataset")
    st.dataframe(df)
    
    # Estadísticas descriptivas generales
    st.write("### Estadísticas Descriptivas Generales")
    st.write(df.describe())

    # Verificar columnas categóricas
    categorical_columns = df.select_dtypes(include='object').columns
    if len(categorical_columns) > 0:
        st.write("### Análisis por Categoría")
        
        # Selección de la categoría
        selected_category = st.selectbox(f"Selecciona una categoría para análisis", categorical_columns)
        selected_category_value = st.selectbox(f"Selecciona un valor de la categoría {selected_category}", df[selected_category].unique())
        df_category = df[df[selected_category] == selected_category_value]

        if not df_category.empty:
            st.write(f"**Análisis para la categoría: {selected_category_value}**")
            st.write(df_category.describe())

            # Selección de columna de datos numéricos
            numeric_columns = df_category.select_dtypes(include='number').columns
            if len(numeric_columns) > 0:
                selected_column = st.selectbox("Selecciona la columna de datos para graficar", numeric_columns)

                # Histogramas por categoría
                st.write(f"#### Histograma de {selected_column} para {selected_category_value}")
                fig, ax = plt.subplots()
                df_category[selected_column].hist(ax=ax, bins=20)
                ax.set_title(f'Histograma de {selected_column} para {selected_category_value}')
                ax.set_xlabel(selected_column)
                ax.set_ylabel('Frecuencia')
                st.pyplot(fig)

                # Gráficos de caja (boxplots) por categoría
                st.write(f"#### Gráfico de Caja (Boxplot) de {selected_column} para {selected_category_value}")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.boxplot(data=df_category[selected_column], ax=ax)
                ax.set_title(f'Gráfico de Caja para {selected_column} y {selected_category_value}')
                st.pyplot(fig)
            else:
                st.write("No hay columnas numéricas para graficar.")
    else:
        st.write("El dataset no contiene columnas categóricas para análisis.")
else:
    st.write("Por favor, selecciona un archivo CSV para comenzar el análisis.")
