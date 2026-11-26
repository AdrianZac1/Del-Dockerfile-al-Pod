# Resultados de ejecución

| Ejercicio | Evidencia observada |
|---|---|
| 0 | Nodo docker-desktop Ready; namespace example Active; Git main inicializado. |
| 1 | Alpine: construcción 10.5 s y 3.5 s tras modificar example.txt; RUN reutilizado. Archivo interno recuperado con docker cp: hola. |
| 2 | Flask thoughts-api:v1; construcción 19.4 s y 1 s con caché; HTTP JSON versión v1. |
| 3 | Imagen local caceb91f3e1a; APP_VERSION=v1; comando python app.py. |
| 4 | pod.yaml validado mediante dry-run; sin crear recursos. |
| 5 | Pod Running 1/1, cero reinicios; IP 10.1.0.6; HTTP versión v1-desde-yaml; directorio /opt/code. |
| 6 | Flask 3.0.3 y programa hola completados; política Always produjo dos reinicios y CrashLoopBackOff incluso con salida 0. |
| 7 | Sidecar BusyBox, volumen emptyDir compartido; 2/2 Running; tres peticiones HTTP exitosas y comunicación localhost. |
| 8 | Init generó APP_VERSION=v1-init; salida 0, aproximadamente seis segundos; prueba negativa exit 1, tres reinicios, API bloqueada. |
| 9A | ErrImageNeverPull con v9 inexistente; cambio a v1 recuperó el Pod. |
| 9B | Python no encontró ap.py; salida 2, CrashLoopBackOff; restauración v1 exitosa. |
| 9C | Comando pyhton inexistente, salida 127, cinco reinicios; corrección y HTTP exitoso. |
| 9D | Corrección de política a Never: 1/1 Running y HTTP v1. No se conservó evidencia del mensaje inicial de error. |
| 10 | Deployment 3/3; borrado de Pod y reemplazo automático; v2 construida en 4.5 s; rolling update y rollback a v1 verificados por HTTP. |
| Reto A | Imagen reto:1.0 ID 7d461c0651dc, construcción 4.3 s, HTTP 200, ENTORNO=dev. |
| Reto B | Deployment 2/2; cuatro contenedores permanentes listos, dos Init completados en tres segundos cada uno, HTTP prod, cero reinicios. |
| Reto C | Pod rs545 (10.1.0.31) eliminado; ReplicaSet creó 9zhqz (10.1.0.32); Pod 9p7jm conservado. Dos réplicas listas y HTTP prod. |

## Tiempos de construcción
Los tiempos son los reportados por Docker, no mediciones controladas. Ejercicio 1: reducción 66.7%; ejercicio 2: reducción 94.8%. La caché y la disponibilidad previa de imágenes influyen en los resultados.

## Estado final
Thoughts API 3/3 y reto-integrador 2/2. Siete Pods Running y dos Completed en la última inspección general. La posterior auditoría confirmó ambos Deployments disponibles. La edad del Pod nuevo (58 s) no es el tiempo de recuperación.

## Mantenimiento del repositorio
La imagen cmd-error fue reconstruida en 2.5 s, ID 3c3385f254f3. Se corrigió pod-error-cmd.yaml para referenciarla y se verificó el manifiesto mediante dry-run y el comando incorrecto mediante docker inspect. La prueba negativa original no se repitió.


## Evidencia complementaria: cuatro etapas

| Etapa | Resultado observado |
|---|---|
| 1 | Flask 3.0.3; Python Alpine; imagen miapp:avalos-1.0, ID ffccfd552413; build 4.4 s; disco 108 MB, contenido 26.2 MB. |
| 2 | Puerto local 9091 hacia 9090; HTTP 200; CPU 0.02%, memoria 21.18 MiB, 0.56%, un proceso en la muestra; modificación local no alteró imagen ni contenedor. |
| 3 | Docker Desktop Kubeadm; namespace k8s-avalos; imagen local confirmada por eventos; Pod 1/1 Running, IP 10.1.0.44, cero reinicios. Requests 100m/64Mi, limits 250m/128Mi. |
| 4 | Pod miapp-fallo con imagen inexistente: ErrImageNeverPull, 26 ocurrencias y 12 Failed reportadas. Pod principal respondió HTTP 200 durante las comprobaciones. Corrección mediante apply, sin borrar el Pod ni reconstruir imagen. |
| Final | Ambos Pods 1/1 Running, cero reinicios, IP 10.1.0.44 y 10.1.0.45. Deployments originales reto-integrador 2/2 y thoughts-api 3/3. |

El Pod defectuoso fue creado a las 18:37:46 y su contenedor corregido inició a las 18:43:23 (hora local), intervalo de 5 min 37 s que incluye el diagnóstico. No es una medición exclusiva de recuperación. Las peticiones exitosas demuestran aislamiento del fallo en las comprobaciones, no disponibilidad continua ni balanceo. El contenedor temporal de Docker fue eliminado conservando la imagen; se observó exit 137 al detenerlo, sin determinar la causa exacta.
