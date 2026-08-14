import cv2
from ultralytics import YOLO
from detector import Detector

# Menu del modelo 
while True:
    modelo = input("Ingrese el modelo de YOLO: ")

    try:
        model = YOLO(modelo, task="detect")
        break
    except Exception:
        print("El modelo no es válido. Intente nuevamente.\n")

# Menu de las camaras disponibes con una funcion

def buscar_camaras():
    camaras = []
    ncams = 0
    for i in range(3):
        camara = cv2.VideoCapture(i)

        if camara.isOpened():
            camaras.append(i)
            camara.release()
            ncams = ncams+1


    return camaras, ncams
camaras, ncams = buscar_camaras()

print("Camaras disponiblles:", ncams)

if ncams>0:
    for i, camara in enumerate(camaras):
        print(f"[{i}] Camara {i}")
else:
    print("Conecte una cámara e intente nuevamente.")
    exit()

opcion = int(input("Ingrese el numero de la cámara que desea utilizar: "))
cam = camaras[opcion]

# Tiempo de ejecucion

duracion = float(input("Cuantos minutos debe durar el detector? "))
tiempo = duracion*60

# Umbral de confianza
umb_conf = float(input("Ingrese el umbral de confianza (0.0 - 1.0): "))

# Comienzo

print("Sonría :)")
print("Para salir presione 'q'")
detector1 = Detector(modelo, cam, umb_conf)


resultados = detector1.ejecutar(tiempo)

if resultados:

    print("\nResultados:")

    for clase, confianza in resultados.items():
        print(f"{clase}: {confianza:.2f}")

else:

    print("\nNo se encontró ningún objeto.")