# Registro de incidencias

| ID | Tipo | Hallazgo y resolución |
|---|---|---|
| 001 | Accidental | Kubernetes sin conexión localhost:8080; configurar clúster en Docker Desktop. |
| 002 | Accidental | Ruta escrita como comando; usar cd /d. |
| 003 | Accidental | FROM/RUN/COPY escritos en CMD; crear Dockerfile mediante echo. |
| 004 | Advertencia | JSONArgsRecommended; se conservó CMD original del ejercicio. |
| 005 | Accidental | Campos YAML introducidos como comandos; escribir manifiesto. |
| 006 | Accidental | Mensaje No resources found copiado como comando; distinguir salida de instrucciones. |
| 007 | Accidental | Curl no conecta con port-forward; abrir túnel en CMD separado. |
| 008 | Advertencia | Servidor Flask de desarrollo; adecuado para demostración, no producción. |
| 009 | Advertencia | flask.__version__ obsoleto; alternativa importlib.metadata.version. |
| 010 | Accidental | Logs de Pod no creado tras dry-run; aplicar manifiesto. |
| 011 | Controlado | Always reinicia tarea finalizada; CrashLoopBackOff; eliminar Pod de prueba. |
| 012 | Controlado | Init exit 1; API no inicia; eliminar prueba. |
| 013 | Accidental | Llave adicional antes de kubectl; retirar carácter. |
| 014 | Esperado | Logs de API bloqueada por Init devuelven BadRequest. |
| 015 | Controlado | Imagen v9 inexistente con Never; cambiar a v1. |
| 016 | Esperado | Logs no disponibles antes de iniciar contenedor. |
| 017 | Controlado | CMD ap.py inexistente, exit 2; restaurar v1. |
| 018 | Limitación | No se recuperaron logs --previous; diagnóstico mediante logs actuales. |
| 019 | Controlado | pyhton inexistente, exit 127; corregir a python y recrear. |
| 020 | Accidental | YAML del Deployment copiado a CMD; usar archivo y kubectl. |
| 021 | Advertencia | Rollback no actualiza anotación last-applied; conservar manifiesto v1 y sincronizar cuando corresponda. |
| 022 | Informativo | Favicon 404; ruta no implementada, API principal HTTP 200. |
| 023 | Accidental | cd ..( produjo ruta inexistente; regresar con cd /d. |
| 024 | Accidental | Ruta relativa duplicada para YAML; reescribir desde raíz y validar. |
| 025 | Accidental | .gitignore y documentacion dentro de thoughts-api; mover a raíz. |

Todas las incidencias accidentales quedaron corregidas. Los fallos controlados son ejercicios de diagnóstico y no defectos pendientes del reto. La advertencia Flask y el favicon pueden repetirse. El mensaje inicial del ejercicio 9D no quedó registrado; sí se comprobó su recuperación.


## Evidencia complementaria: cuatro etapas

| ID | Tipo | Hallazgo y resolución |
|---|---|---|
| 026 | Advertencia | Git avisó de conversión LF/CRLF; el commit anterior se completó. |
| 027 | Accidental | Caracteres incorrectos en CMD; usar chcp 65001. |
| 028 | Accidental | Dockerfile.txt; renombrar a Dockerfile. |
| 029 | Accidental | Respuesta HTTP copiada como comando; ejecutar curl y distinguir salida. |
| 030 | Advertencia | Tres fallos iniciales de readiness por conexión rechazada; esperar disponibilidad. Se resolvió sin reinicios. |
| 031 | Controlado | Imagen avalos-9.9 inexistente con Never; aplicar pod-recuperado.yaml con avalos-1.0. |
| 032 | Accidental | ls-1 no reconocido; corregir a ls -l. |

Total histórico: 32 incidencias, advertencias y observaciones. Los fallos controlados no son defectos pendientes. El servidor Flask continúa siendo de desarrollo.
