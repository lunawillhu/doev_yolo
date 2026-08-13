# Importaciones
import cv2
from ultralytics import YOLO
# yolo26n.pt

# Camara de YOLO
class detector(cam,mod, bucle):
    def __init__(self, modelo, fuent_vid, umb_conf):
        self.modelo = modelo
        self.fuent_vid = fuent_vid
        self.umb_conf = umb_conf

