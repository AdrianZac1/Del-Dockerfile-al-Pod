# Guion del video — Del Dockerfile al Pod

Duración objetivo: 2:55; margen de cinco segundos. Los intervalos son una propuesta de edición, no tiempos medidos de narración. Ajustar pausas al grabar.

| Tiempo | Mostrar | Narración |
|---|---|---|
| 00:00–00:10 | Título y carpeta del reto | En esta práctica integré los conocimientos adquiridos sobre Docker y Kubernetes para desplegar y recuperar automáticamente un microservicio. |
| 00:10–00:30 | app.py, requirements.txt, Dockerfile | Desarrollé una API con Python y Flask que devuelve su estado, versión, entorno y nombre del host. Configuré sus dependencias, puerto 9090 y variable de entorno inicial mediante el Dockerfile. |
| 00:30–00:55 | Build, docker run, curl dev | Construí la imagen en 4.3 segundos, aprovechando la caché de Docker. Después ejecuté el contenedor y comprobé que respondiera correctamente en JSON con el entorno de desarrollo. |
| 00:55–01:40 | YAML, apply, monitor, logs Init y Sidecar | Trasladé la misma imagen a Kubernetes mediante un Deployment con dos réplicas. Cada Pod contiene un Init Container que simula la preparación durante tres segundos, una API Flask y un Sidecar que consulta la aplicación mediante localhost cada diez segundos. También incorporé una comprobación HTTP de disponibilidad. |
| 01:40–02:05 | Pods 2/2, curl prod, logs | Kubernetes sobrescribió la variable de entorno de dev a prod sin reconstruir la imagen. Verifiqué las dos réplicas, los registros de ambos contenedores y el acceso mediante port-forward. En ejercicios previos aprendí a resolver errores de conexión manteniendo el túnel en otra terminal. |
| 02:05–02:30 | Borrado rs545, nuevo 9zhqz, SuccessfulCreate | Eliminé intencionalmente un Pod. El ReplicaSet creó automáticamente su reemplazo con una nueva dirección IP. Comprobé que se ejecutaran nuevamente su inicialización, API y monitoreo, y que las dos réplicas estuvieran disponibles. |
| 02:30–02:45 | GitHub, README, carpetas | Organicé los ejercicios, resultados e incidencias en un repositorio para documentar el proceso y facilitar su reproducción. |
| 02:45–02:55 | Resultado final | Con esta práctica comprendí cómo construir, configurar, diagnosticar y recuperar aplicaciones mediante Docker y Kubernetes. |

**Importante:** grabar el segmento GitHub solo después de publicar. Utilizar los clips reales 01_Reto_Final_Docker, 02_Reto_Final_Kubernetes y 03_Reto_Final_Autorrecuperacion. No afirmar disponibilidad ininterrumpida ni balanceo de carga. El video debe concentrarse en el reto final, según la interpretación acordada de la indicación del profesor.
