import cv2
from ultralytics import YOLO
import time

# Menu del modelo 
while True:
    modelo = input("Ingrese el modelo de YOLO: ")

    try:
        model = YOLO(modelo, task="detect")
        break
    except Exception:
        print("El modelo no es válido. Intente nuevamente.\n")

# Menu de las camaras disponibes con una funcion
ncams = 0
def buscar_camaras(ncams):
    camaras = []

    for i in range(10):
        camara = cv2.VideoCapture(i)

        if camara.isOpened():
            camaras.append(i)
            camara.release()
            ncams = ncams+1


    return camaras, ncams
camaras = buscar_camaras()

print("Camaras disponiblles:", ncams)

if ncams>0:
    for i in range(camaras):
        print(f"[{i}] Camara {i}")
else:
    print("Conecte una camara e intente nuevamente.")
    exit()

cam = input("Ingrese el numero de la camara que desea utilizar: ")
camara = cv2.VideoCapture(cam)

# Menu de tiempo de repeticion del bucle
duracion = float(input("Cuantos minutos debe durar el detector? "))
duracion = duracion * 60

# Solicitando umbral de confianza
umb_conf = float(
    input("Ingrese el umbral de confianza (0.0 - 1.0): ")
)

inicio = time.time()


# Inicio del bucle

#while time.time() - inicio < duracion:

#    frame = camara.read()

#    resultados = model(frame)

#    frame = resultados[0].plot()

#    cv2.imshow("YOLO", frame)





detector = Detector(
    modelo,
    camara,
    umb_conf
)

########################################seguir################################################
