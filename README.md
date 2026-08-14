# doev_yolo

Respuestas sobre el trabajo:
- Si no detecta nada, el programa devuelve un mensaje "No se encontró ningún objeto."
- La salida va a la consola al finalizar la ejecución de la cámara.
- Elegí que imprima solo al final de la ejecución, guarda el umbral de confianza mas grande y lo imprime al final junto con la clase de objeto que encontró. Me parece una forma mas limpia y cómoda para utilizar el programa.
- Si la cámara está ocupada no encontrará resultados o no permitirá usarla, no fuerza a utilizarla. Dará el mensaje de que no se encontraron objetos.


 El programa cuenta con un mensaje de WARNING inicial que aparece si tenés una sola cámara, para sacarlo debía importar otra librería así que decidí dejarlo para cumplir con los requisitos. Es un mensaje de opencv-python que, si tenes mas de 2 cámaras no te aparecerá.


 https://github.com/lunawillhu/doev_yolo.git
 gh repo clone lunawillhu/doev_yolo
