# Importaciones
import cv2
from ultralytics import YOLO
import time
# yolo26n.pt

# Detector con yolo y cv2
class Detector:
    
    def __init__(self, modelo, fuent_vid, umb_conf):
        self.modelo = YOLO(modelo)
        self.fuent_vid = fuent_vid
        self.umb_conf = umb_conf


    def procesar_frame(self, frame):
        resultados = self.modelo(
            frame,
            conf=self.umb_conf
        )

        return resultados

    def ejecutar(self, duracion):
            camara = cv2.VideoCapture(self.fuente_video)
            
            inicio = time.time()

            while time.time() - inicio < duracion:
                ret, frame = camara.read()

                if not ret:
                    break

                resultados = self.procesar_frame(frame)
                ult_resultado = resultados

                frame = resultados[0].plot()

                cv2.imshow("Detector", frame)

                return ult_resultado
