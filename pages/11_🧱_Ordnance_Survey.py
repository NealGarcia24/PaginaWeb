import cv2
import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np


# Cargar el modelo de detección de emociones preentrenado
model = load_model('path/to/your/model.h5')

# Definir las etiquetas de las emociones
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


# Función para preprocesar la imagen
def preprocess_image(image):
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Redimensionar la imagen a 48x48
    resized = cv2.resize(gray, (48, 48))
    # Expandir las dimensiones de la imagen para que coincida con el formato de entrada del modelo (1 canal)
    resized = np.expand_dims(resized, axis=-1)
    # Normalizar la imagen
    normalized = resized / 255.0
    # Devolver la imagen preprocesada
    return normalized


# Función para detectar emociones en el rostro
def detect_emotions(face):
    # Preprocesar la imagen
    processed = preprocess_image(face)
    # Realizar la predicción utilizando el modelo
    prediction = model.predict(np.expand_dims(processed, axis=0))[0]
    # Obtener la emoción con mayor probabilidad
    max_index = np.argmax(prediction)
    emotion = emotions[max_index]
    # Devolver la emoción detectada y la probabilidad correspondiente
    return emotion, prediction[max_index]


# Configurar la aplicación Streamlit
st.title('Detección de emociones en tiempo real')

# Crear el objeto de captura de video
video_capture = cv2.VideoCapture(0)

# Ejecutar la aplicación en bucle hasta que se interrumpa
while True:
    # Leer un fotograma del video
    ret, frame = video_capture.read()

    # Si no se pudo leer el fotograma, salir del bucle
    if not ret:
        break

    # Obtener las dimensiones del fotograma
    height, width, _ = frame.shape

    # Dibujar un rectángulo en el fotograma para mostrar el área de detección
    cv2.rectangle(frame, (100, 100), (width - 100, height - 100), (0, 255, 0), 2)

    # Obtener el área de interés (ROI) dentro del rectángulo
    roi = frame[100:height - 100, 100:width - 100]

    # Si hay una ROI válida
    if roi.shape[0] > 0 and roi.shape[1] > 0:
        # Detectar emociones en la ROI
        emotion, probability = detect_emotions(roi)

        # Escribir la emoción detectada y la probabilidad en el fotograma
        cv2.putText(frame, f'{emotion} ({probability:.2f})', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                    cv2.LINE_AA)

    # Mostrar el fotograma en la aplicación Streamlit
    st.image(frame, channels='BGR')

# Liberar el objeto de captura de video
video_capture.release()
