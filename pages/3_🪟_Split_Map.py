import cv2
import numpy as np
import streamlit as st
import streamlit_webrtc as webrtc
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


# Cargar el modelo de detección de emociones
model = load_model('model_v6_23.hdf5')


# Mapeo de las etiquetas de emociones
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


# Función para predecir la emoción en una imagen
def predict_emotion(image):
    # Preprocesamiento de la imagen
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (48, 48))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    
    # Realizar la predicción
    predictions = model.predict(image)[0]
    emotion_index = np.argmax(predictions)
    emotion = emotion_labels[emotion_index]
    
    return emotion


# Función para procesar los frames del video
def process_frame(frame):
    # Detección de emociones en el frame
    emotion = predict_emotion(frame)
    
    # Mostrar la imagen con la emoción detectada
    cv2.putText(frame, emotion, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    st.image(frame, channels="BGR")
    

# Configuración de la interfaz de Streamlit
st.title('Detección de Emociones en Tiempo Real')

# Crear la instancia del elemento de video
webrtc_ctx = webrtc.StreamerRTC()

# Configurar el procesamiento de frames del video
webrtc_ctx.add_processor(process_frame)

# Iniciar el streaming de video en tiempo real
webrtc_ctx.start()

# Mostrar el elemento de video en Streamlit
webrtc_ctx.video_renderer()
