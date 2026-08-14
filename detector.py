# Importaciones
import cv2
from ultralytics import YOLO
# yolo26n.pt

# Camara de YOLO
class Detector:
    
    def __init__(self, modelo, fuent_vid, umb_conf, duracion):
        self.modelo = YOLO(modelo)
        self.fuent_vid = fuent_vid
        self.umb_conf = umb_conf
        self.duracion = duracion

