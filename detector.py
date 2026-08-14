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
            conf=self.umb_conf,
            verbose=False
        )

        return resultados

    def ejecutar(self, duracion):
        camara = cv2.VideoCapture(self.fuent_vid)

        inicio = time.time()

        may_conf = {}

        while time.time() - inicio < duracion:

            ret, frame = camara.read()

            if not ret:
                break

            resultados = self.procesar_frame(frame)

            for box in resultados[0].boxes:

                clase = resultados[0].names[int(box.cls)]
                confianza = float(box.conf)

                if clase not in may_conf:
                    may_conf[clase] = confianza

                elif confianza > may_conf[clase]:
                    may_conf[clase] = confianza

            frame_mostrado = resultados[0].plot()

            cv2.imshow("Detector", frame_mostrado)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        camara.release()
        cv2.destroyAllWindows()

        return may_conf