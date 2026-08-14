# doev_yolo
---------------------------------------------------------------------------------------

# Clonar el repositorio:

git clone https://github.com/lunawillhu/doev_yolo.git

Entrar en la carpeta:
cd doev_yolo

Crear la máquina virtual:
python -m venv .venv

Activar el entorno virtual en Windows:
.venv\Scripts\activate

Instalar las dependencias:
pip install -r requirements.txt

# El programa solicita:

1. El modelo de YOLO que se desea utilizar, ejemplo yolo26n.pt.
2. La cámara que se desea utilizar.
3. La duración de la detección en minutos.
4. El umbral de confianza deseado.

Durante la ejecución se muestra la cámara con las detecciones
realizadas por YOLO.

Al finalizar el tiempo establecido, o luego de presionar "q", se muestran en la consola las
clases detectadas y el mayor umbral de confianza que se obtuvo para cada una.
Si no se detectó ningún objeto, se informa en la consola.

---------------------------------------------------------------------------------------

Respuestas sobre el trabajo:
- Si no detecta nada, el programa devuelve un mensaje "No se encontró ningún objeto."
- La salida va a la consola al finalizar la ejecución de la cámara.
- Elegí que imprima solo al final de la ejecución, guarda el umbral de confianza mas grande y lo imprime al final junto con la clase de objeto que encontró. Me parece una forma mas limpia y cómoda para utilizar el programa.
- Si la cámara está ocupada no encontrará resultados o no permitirá usarla, no fuerza a utilizarla. Dará el mensaje de que no se encontraron objetos.


 El programa cuenta con un mensaje de WARNING inicial que aparece si tenés una sola cámara, para sacarlo debía importar otra librería así que decidí dejarlo para cumplir con los requisitos. Es un mensaje de opencv-python que, si tenes mas de 2 cámaras no te aparecerá.

