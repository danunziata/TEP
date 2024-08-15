import streamlit as st

from forms.contact import contact_form


#@st.experimental_dialog("Contact Me")
#def show_contact_form():
#    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/escudo_ing.png", width=150)

with col2:
    st.title("Técnicas Estadísticas con Python", anchor=False)
    st.write(
        "Autor: Ing. Daniel Anunziata"        
    )
    #if st.button("✉️ Contact Me"):
    #    pass 
    #    show_contact_form()

# --- Resumen ---
st.write("\n")
#st.subheader("", anchor=False)
st.write("""
        Python se ha consolidado como una de las herramientas más potentes y versátiles para el análisis de datos debido a su sintaxis clara, extensibilidad y una amplia gama de librerías especializadas. Esta popularidad es reflejo de su capacidad para abordar tareas complejas de análisis y visualización de datos de manera eficiente y accesible. A continuación, se detalla la motivación para utilizar Python, destacando las librerías Pandas, Streamlit, Matplotlib y PandasAI.

        1. **Pandas:** Pandas es una librería fundamental para la manipulación y el análisis de datos en Python. Su estructura de datos flexible, como el DataFrame, permite manejar grandes volúmenes de datos de manera eficiente. La capacidad de Pandas para realizar operaciones de limpieza, transformación y análisis de datos con una sintaxis intuitiva facilita la tarea de los analistas y científicos de datos. Utilizando métodos como describe(), Pandas ofrece un resumen estadístico detallado de los datos numéricos, permitiendo a los usuarios obtener rápidamente una visión general de la distribución y características de sus datos.
        2. **Matplotlib:** Matplotlib es una librería esencial para la visualización de datos en Python. Su versatilidad y capacidad para generar gráficos estáticos, animados e interactivos permiten a los usuarios crear visualizaciones detalladas y personalizadas. Con Matplotlib, es posible generar histogramas, gráficos de caja (boxplots) y otras visualizaciones cruciales para explorar y entender los datos. Estas visualizaciones no solo facilitan la interpretación de patrones y tendencias, sino que también son herramientas efectivas para comunicar resultados de manera clara y concisa.
        3. **Streamlit:** Streamlit transforma el análisis de datos en una experiencia interactiva al permitir a los usuarios construir aplicaciones web de manera rápida y sencilla. Su capacidad para crear dashboards y herramientas interactivas sin necesidad de conocimientos avanzados en desarrollo web democratiza el acceso a herramientas de análisis y visualización de datos. Con Streamlit, los usuarios pueden cargar datos, realizar análisis y visualizar resultados en tiempo real, facilitando la exploración de datos y la toma de decisiones basada en evidencia.
        4. **PandasAI:** PandasAI combina el poder de Pandas con capacidades avanzadas de inteligencia artificial para automatizar y simplificar el análisis de datos. Al integrar modelos de lenguaje natural, PandasAI permite a los usuarios realizar consultas en lenguaje natural sobre sus datos y recibir respuestas detalladas y análisis automatizados. Esta herramienta reduce la complejidad del análisis de datos, haciendo que la obtención de insights sea más accesible para aquellos sin experiencia en programación o estadística avanzada.
        5. **BambooLLM:** es un modelo de lenguaje de última generación desarrollado por PandasAI específicamente para el análisis de datos. Su diseño está orientado a mejorar la interacción entre los usuarios y sus datos mediante la interpretación y ejecución de consultas formuladas en lenguaje natural
        """)


# --- Proyecto 1 ---
st.write("\n")
st.subheader("Proyecto 1 Dashboard - Análisis Estadístico con python pandas - con datos en formato csv", anchor=False)
st.write(
    """
    Este proyecto se enfoca en el análisis estadístico básico de datos almacenados en archivos CSV. A continuación, se describen los pasos para llevar a cabo el análisis:

    1. **Seleccionar el Archivo CSV de la lista**
        - Se utilizó Python `pandas` para cargar el archivo CSV.
        - Asegurarse de que el archivo esté preordenado, con la primera fila destinada al nombre de cada columna.

    2. **Obtener Estadísticos Descriptivos:**
        - Se Calcular estadísticas descriptivas básicas, de cada columna numérica. con el método describe() de pandas
        
        El método describe() de la biblioteca pandas en Python proporciona un resumen estadístico de los datos numéricos en un DataFrame o Serie. Los estadísticos que genera por defecto son los siguientes:
            - count: El número de valores no nulos.
            - mean: La media aritmética de los valores.
            - std: La desviación estándar, que mide la dispersión de los datos.
            - min: El valor mínimo.
            - 25%: El primer cuartil (Q1), que es el valor por debajo del cual se encuentra el 25% de los datos.
            - 50%: La mediana o segundo cuartil (Q2), que es el valor por debajo del cual se encuentra el 50% de los datos.
            - 75%: El tercer cuartil (Q3), que es el valor por debajo del cual se encuentra el 75% de los datos.
            - max: El valor máximo.

    3. **Visualización de Datos:**
        - con el uso de la libreria matplotlib se crean dos graficos:
            - Histograma 
            - BoxPlot 
    """
)

# ---Proeycto 2 ---
st.write("\n")
st.subheader("Proyecto 2 Chatbot - Análisis Estadístico con python pandas ai - con datos en formato csv", anchor=False)
st.write(
    """

    Este proyecto utiliza inteligencia artificial para realizar un análisis estadístico de datos almacenados en un archivo CSV, mediante el servicio de **Pandas AI**, utilizando el modelo **BambooLLM**
    
    Los pasos para llevar a cabo el análisis son los siguientes:

    1. **Cargar el Archivo CSV que se va a analizar**
        
    2. **Crear una Cuenta en Pandas AI:**
        - Regístrate en el servicio de Pandas AI y obtén una clave API (key). (https://www.pandabi.ai/auth/sign-up)
        - Copia la clave API para usarla en las solicitudes de análisis.

    3. **Interacción con Pandas AI:**
        - Realizar preguntas en ingles sobre información de los datos cargados

    4. **Preguntas en Inglés para Pandas AI:**
        - **generate a summary of basic statistics for the dataset**
        
        - **histogram column_name**
            
        - **boxplot column_name**    
    """
)
