import cv2
import streamlit as st
import av
import numpy as np
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer

# Carga el modelo pre-entrenado para la detección de rostros y emociones
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_model = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt',
    'fer2013_mini_XCEPTION.102-0.66.hdf5'
)

# Lista de etiquetas de emociones
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

# Clase para procesar el video y realizar la detección de emociones en cada cuadro
class EmotionDetector(VideoProcessorBase):
    def __init__(self):
        super().__init__()
    
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Convierte el cuadro de video a una imagen en formato OpenCV
        image = frame.to_ndarray(format="bgr24")
        
        # Detecta rostros en la imagen
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Procesa cada rostro detectado
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(face, (48, 48))
            face = face.astype("float") / 255.0
            face = np.expand_dims(face, axis=0)
            face = np.expand_dims(face, axis=0)

            # Realiza la predicción de emociones
            emotion_model.setInput(face)
            preds = emotion_model.forward()
            emotion_index = np.argmax(preds[0])

            # Obtiene la etiqueta de la emoción y la muestra en la imagen
            emotion_label = EMOTIONS[emotion_index]
            cv2.putText(
                image,
                emotion_label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                2,
                cv2.LINE_AA
            )
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        return av.VideoFrame.from_ndarray(image, format="bgr24")

# Configura la interfaz de Streamlit
def main():
    st.title("Detección de emociones en tiempo real")
    st.write("Utilizando Streamlit-WebRTC y OpenCV")

    # Inicia la transmisión de video y procesa los cuadros con la clase EmotionDetector
    webrtc_ctx = webrtc_streamer(
        key="emotion-detection",
        mode=1,
        video_processor_factory=EmotionDetector,
    )

    if webrtc_ctx.video_processor:
        st.write("**Transmisión de video en tiempo real**")
        st.write("La detección de emociones se aplicará a los rostros detectados.")
    else:
        st.write("Esperando la transmisión de video...")

if __name__ == "__main__":
    main()
