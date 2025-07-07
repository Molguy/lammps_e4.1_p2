# lammps_e4.1_p2
El log de la simulación no fue arrojado, pero en cambio se tiene una respuesta en la terminal del ejemplo 4.1 parte 2 que tambien sirve para revisar su ejecucion.

Tambien fueron agregados los textos de respuesta que fueron usados como lo indicaba el ejercicio: 

    lmp_serial < input.dat
    
Aclarando que en este punto se decidio usar la herramienta venv para ejecutar scripts auxiliares
    
    python3 -m venv venv
.
    
    source venv/bin/activate
.

    python3 adcn.py && adcg.py
(A este punto se mostrara la respuesta de adcn.py en la terminal y la grafica de adcg.py en una ventana)

_Ejemplo:_

Moleculas mas cercanas al COM de la molécula 26:

Molecula 9 → distancia = 3.01 Å

Molecula 3 → distancia = 3.28 Å

.
    
    deactivate
(Legando a este punto ya deberia estar desactivada la herramienta)

.
    
    ovito 1.1a.xyz

