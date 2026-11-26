# Guion final — cuatro etapas

Duración objetivo 2:55, cortes propuestos y no medidos. Priorizar las cuatro grabaciones nuevas; conservar los tres videos anteriores como evidencia complementaria.

| Tiempo | Mostrar | Narración |
|---|---|---|
| 00:00–00:08 | Título y proyecto | Después de completar los ejercicios previos, desarrollé una evidencia en cuatro etapas. |
| 00:08–00:38 | app.py, Dockerfile, build, etiqueta | Creé una aplicación Flask con mi nombre, hora del servidor y ruta healthz. Utilicé Python Alpine, las instrucciones requeridas y una etiqueta con mi apellido. Corregí la codificación y la extensión del Dockerfile. La construcción tomó 4.4 segundos. |
| 00:38–01:13 | run, curl, logs, exec, stats, edición local y comparación | La imagen es la plantilla y el contenedor su instancia. Publiqué el puerto 9091, comprobé ambas rutas, consulté registros y recursos e ingresé al contenedor. Modifiqué un archivo local sin alterar la imagen ni el contenedor. |
| 01:13–01:45 | namespace, YAML, apply, wait, describe | En Docker Desktop creé el namespace k8s-avalos y un Pod mediante YAML con recursos y readinessProbe. La imagen estaba disponible localmente. Tres comprobaciones iniciales fallaron, pero el Pod quedó listo sin reinicios. |
| 01:45–02:45 | wide, describe, logs -f, exec, port-forward, navegador, apply fallo, eventos, monitor 200, apply recuperación, ambos Running | Consulté los Pods, eventos y registros en tiempo real, ingresé al contenedor y accedí desde el navegador. Utilicé una etiqueta inexistente para provocar ErrImageNeverPull. Los eventos identificaron la causa y el monitor confirmó respuestas HTTP 200 del Pod principal durante las pruebas. Corregí el YAML y recuperé el segundo Pod sin eliminarlo. Ambos quedaron disponibles y sin reinicios. |
| 02:45–02:55 | GitHub y resultado | Documenté los ejercicios, errores de comandos, configuración, conexión e imágenes, y sus soluciones. Así comprendí el ciclo completo de Docker y Kubernetes. |

Tras publicar, mostrar GitHub. El registro histórico contiene 32 incidencias, incluidas advertencias y pruebas controladas: consultar registro-incidencias.md para el detalle completo. No afirmar disponibilidad ininterrumpida ni balanceo. Verificar visualmente todos los comandos solicitados y cronometrar la narración antes de exportar. Los tiempos exactos de los clips fuente están pendientes de inspección.
