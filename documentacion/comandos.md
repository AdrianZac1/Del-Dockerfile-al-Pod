# Comandos de reproducción en Windows CMD

Esta guía resume los comandos esenciales y presupone los archivos del repositorio. No es una transcripción literal de todas las pulsaciones. Ejecutar las pruebas una por una, no todos los YAML simultáneamente.

## 0. Preparación
```cmd
docker version
kubectl version
kubectl get nodes
git --version
kubectl create namespace example --dry-run=client -o yaml | kubectl apply -f -
```
## 1. Docker
Desde ej1:
```cmd
docker build -f Dockerfile.run -t container-run .
docker run container-run
docker run --name prueba-aislamiento container-run /bin/sh -c "echo hola > /opt/out.txt"
docker cp prueba-aislamiento:/opt/out.txt evidencia-out.txt
type evidencia-out.txt
```
Usar un nombre libre si el contenedor ya existe. Para observar caché, repetir build tras cambiar example.txt.

## 2–5. API y Pod
Desde thoughts-api:
```cmd
docker build -f Dockerfile.v1 -t miusuario/thoughts-api:v1 .
docker run -d -p 8000:8000 --name prueba miusuario/thoughts-api:v1
curl http://127.0.0.1:8000/
docker rm -f prueba
docker inspect miusuario/thoughts-api:v1
kubectl apply -f pod.yaml --dry-run=client
kubectl apply -f pod.yaml
kubectl get pods -n example -o wide
kubectl describe pod thoughts-api -n example
kubectl logs thoughts-api -n example
kubectl exec thoughts-api -n example -- printenv APP_VERSION
```
En otra CMD: `kubectl port-forward pod/thoughts-api 8000:8000 -n example`. Consultar curl desde la primera y detener túnel.

## 6–8. Patrones de Pods
```cmd
kubectl apply -f pod-command.yaml
kubectl logs thoughts-debug -n example
kubectl apply -f pod-args.yaml
kubectl logs thoughts-args -n example
kubectl apply -f pod-restart.yaml
kubectl describe pod thoughts-restart -n example
kubectl delete -f pod-restart.yaml
kubectl apply -f pod-sidecar.yaml
kubectl logs thoughts-con-sidecar -n example -c log-shipper
kubectl exec thoughts-con-sidecar -n example -c log-shipper -- wget -qO- http://localhost:8000/
kubectl apply -f pod-init.yaml
kubectl describe pod thoughts-con-init -n example
kubectl apply -f pod-init-error.yaml
kubectl logs thoughts-init-error -n example -c preparar-config
kubectl delete -f pod-init-error.yaml
```
Esperar a que los contenedores se creen antes de consultar logs. Las pruebas negativas requieren observar el estado antes de borrarlas.

## 9. Diagnóstico
```cmd
kubectl apply -f pod-error-imagen.yaml
kubectl describe pod thoughts-error-imagen -n example
kubectl set image pod/thoughts-error-imagen api=miusuario/thoughts-api:v1 -n example
kubectl wait --for=condition=Ready pod/thoughts-error-imagen -n example --timeout=120s
kubectl delete -f pod-error-imagen.yaml
docker build -f Dockerfile.error -t miusuario/thoughts-api:cmd-error .
kubectl apply -f pod-error-cmd.yaml
kubectl logs thoughts-error-cmd -n example
kubectl describe pod thoughts-error-cmd -n example
kubectl set image pod/thoughts-error-cmd api=miusuario/thoughts-api:v1 -n example
kubectl wait --for=condition=Ready pod/thoughts-error-cmd -n example --timeout=120s
kubectl delete -f pod-error-cmd.yaml
kubectl apply -f pod-error-command.yaml
kubectl describe pod thoughts-error-command -n example
kubectl delete -f pod-error-command.yaml
kubectl apply -f pod-command-corregido.yaml
kubectl wait --for=condition=Ready pod/thoughts-error-command -n example --timeout=120s
kubectl delete -f pod-command-corregido.yaml
kubectl apply -f pod-error-pull.yaml
kubectl describe pod thoughts-error-pull -n example
kubectl delete -f pod-error-pull.yaml
kubectl apply -f pod-pull-corregido.yaml
kubectl wait --for=condition=Ready pod/thoughts-error-pull -n example --timeout=120s
kubectl delete -f pod-pull-corregido.yaml
```
El resultado de Always depende del acceso al registro; no se registró el mensaje inicial en la práctica original.

## 10. Deployment
```cmd
kubectl delete -f pod.yaml --ignore-not-found
kubectl apply -f deployment.yaml
kubectl rollout status deployment/thoughts-api -n example
kubectl get pods -n example -l app=thoughts-api
```
Eliminar un Pod actual del Deployment por su nombre con kubectl delete pod NOMBRE -n example (sustituir NOMBRE), observar reemplazo y comprobar tres réplicas.
```cmd
docker build -t miusuario/thoughts-api:v2 .
kubectl set image deployment/thoughts-api api=miusuario/thoughts-api:v2 -n example
kubectl rollout status deployment/thoughts-api -n example
kubectl rollout history deployment/thoughts-api -n example
kubectl rollout undo deployment/thoughts-api -n example
kubectl rollout status deployment/thoughts-api -n example
```
Verificar por port-forward y curl antes y después del rollback. El manifiesto local usa v1.

## Reto final
Seguir README. Para autorrecuperación, observar `kubectl get pods -n example -l app=reto-integrador -w` en otra terminal, eliminar un Pod actual por nombre, comprobar rollout y consultar logs de preparacion y monitor. Recrear el port-forward si estaba conectado al Pod eliminado.


## Evidencia complementaria: cuatro etapas

Consultar [procedimiento de las cuatro etapas](../evidencia-final/README.md). Los manifiestos de fallo y recuperación se aplican por separado, nunca todos juntos.
