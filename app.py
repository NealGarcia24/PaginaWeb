import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Hola Bienvenid@ !!!
    - Creado por Neal Garcia
    """
)

st.sidebar.title("Colegio Los Pinos")
st.sidebar.info(
    """
    Aplicación web como herramienta para detectar la depresion en alumnos de secundaria del colegio Los Pinos
    """
)

st.title("MoodUP!!!
            Bienvenid@s")

st.markdown(
    """
    Bienvenidos a nuestra página de detección de depresión para alumnos de secundaria del Colegio Los Pinos!
    En esta página, nos dedicamos a brindar apoyo y herramientas para la detección temprana de la depresión en los 
    alumnos de secundaria del Colegio Los Pinos. Nuestro objetivo principal es promover la salud mental y ayudar 
    a los estudiantes a reconocer los signos y síntomas de la depresión, así como a buscar el apoyo necesario.

    """
)

st.info("Haga clic en el menú de la barra lateral izquierda para navegar por las difentes pestañas")

st.subheader("Sabemos que hablar sobre la depresión puede resultar difícil, y muchos adolescentes pueden 
sentirse solos o incomprendidos. Queremos que sepan que no están solos. Aquí encontrarán información valiosa, 
recursos útiles y la posibilidad de conectarse con profesionales capacitados que los escucharán y les brindarán 
el apoyo que necesitan.")

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
