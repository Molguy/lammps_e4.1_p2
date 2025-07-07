Ejemplo 4.1 - Cálculo del centro de masa (COM/cdm) del etanol y hexano

En la carpeta deben estar los siguientes archivos:
 a) input.dat
 b) pairparameters.dat
 c) structure.dat

1. Ejecutar el programa usando:
 a) export OMP_NUM_THREADS=$(nproc)
 b) lmp_serial < input.dat
 c) ó lammps < input.dat (Homebrew)

2. Identificar los últimos 3 valores de ecom.txt y hcom.txt, los cuales están en vertical, corresponden a las posiciones x-y-z del centro de masa.

3. Utilizar los 3 últimos valores de ecom.txt y hcom.txt y agregalos en 1.1.xyz en un mismo renglón acuerdo a la posición e edita la linea 4 de acuerdo a su agregado:

29*

id     mol    type        x        y          z 
128     9      2       4.27961   6.6102    4.25556
.
.
.
281    26      7          e1?         e2?         e3?
282    26      7          h1?         h2?         h3?

4. Abrir 1.1a.xyz en OVITO para visualizar COM de las moléculas, para mejorar la visualización modifica el display radius y selecciona a sobresalir la partícula 7…

5. Identificar los sitios cercanos a COM de cada molécula
	- se decidio crear un script con ayuda de IA para encontrar los mas cercanos mediante cálculos -

EXT. Abre el archivo adcn.py (analizador de cercanía numérica) como un documento de texto para editar la linea 4 y proceder a ejecutar (con venv instalado más las utilerías pip) en comando con:
 a) python3 -m venv venv
 b) source venv/bin/activate
	- en un nuevo folder llamado venv se guardara el registros y utilerías descargadas con pip -
 c) python3 adcn.py
	- se arroja el resultado en la linea de comandos -
	- en caso de terminar o salir, escribe " deactivate " 

OPT. Abre el archivo adcg.py (analizador de cercania grafica) como un documento de texto para editar la linea 10 y ejecutar (en caso de haber desactivado venv, repita el inciso a y b del paso anterior)
 a) python3 adcg.py
	- se generara una ventana con un grafico representativo
 b) deactivate

Visualiza su estructura
  ovito 1.1a.xyz
