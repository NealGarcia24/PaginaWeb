import streamlit as st


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

# Customize page title
st.title("MoodUP!!! Bienvenid@s")

st.markdown(
    """
    Bienvenidos a nuestra página de detección de depresión para alumnos de secundaria del Colegio Los Pinos!
    En esta página, nos dedicamos a brindar apoyo y herramientas para la detección temprana de la depresión en los 
    alumnos de secundaria del Colegio Los Pinos. Nuestro objetivo principal es promover la salud mental y ayudar 
    a los estudiantes a reconocer los signos y síntomas de la depresión, así como a buscar el apoyo necesario.

    """
)

st.header("Acerca de MoodUp")

st.markdown (
"""
Sabemos que hablar sobre la depresión puede resultar difícil, y muchos adolescentes pueden 
sentirse solos o incomprendidos. Queremos que sepan que no están solos. Aquí encontrarán información valiosa, 
recursos útiles y la posibilidad de conectarse con profesionales capacitados que los escucharán y les brindarán 
el apoyo que necesitan.

"""

)
def main():
   
    # Agregar una imagen desde una URL
    st.subheader("Colegio 80892 LOS PINOS")
    url = "https://1.bp.blogspot.com/-sCobWggbKhY/XQfyHdL3hwI/AAAAAAABQN4/jMxT1znQlsov4xDT67CHngSGTxzFLvy9QCLcBGAs/s1600/ie-80892-los-pinos.jpg"
    st.image(url, caption='Imagen del frontis colegio', use_column_width=True)

if __name__ == '__main__':
    main()
