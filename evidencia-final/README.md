# Evidencia final: Del Dockerfile al Pod

Ejecutar desde esta carpeta, en Windows CMD. Se requiere Docker Desktop con Kubernetes activo y acceso a imágenes locales. En la práctica se utilizó Kubeadm; en Kind o Minikube se debe importar la imagen mediante el mecanismo correspondiente.

## 1. Construcción
```cmd
chcp 65001
type app.py
type requirements.txt
type Dockerfile
docker build -t miapp:avalos-1.0 .
docker images miapp
docker history miapp:avalos-1.0
```
La aplicación devuelve nombre, hora UTC, versión y host en `/`; `/healthz` responde 200.

## 2. Contenedor
```cmd
docker run -d -p 127.0.0.1:9091:9090 --name miapp-prueba miapp:avalos-1.0
curl http://127.0.0.1:9091/
curl -i http://127.0.0.1:9091/healthz
docker logs miapp-prueba
docker exec -it miapp-prueba /bin/sh
```
Dentro del shell: `pwd`, `ls -l`, `cat app.py`, `exit`.
```cmd
docker stats --no-stream miapp-prueba
copy app.py app.py.bak
echo.>>app.py
echo # PRUEBA_AISLAMIENTO_LOCAL>>app.py
type app.py
docker exec miapp-prueba cat /opt/code/app.py
docker run --rm --entrypoint cat miapp:avalos-1.0 /opt/code/app.py
curl -i http://127.0.0.1:9091/healthz
copy /y app.py.bak app.py
fc /b app.py app.py.bak
del app.py.bak
docker stop miapp-prueba
docker rm miapp-prueba
docker images miapp
```
La imagen es la plantilla empaquetada; el contenedor es una instancia ejecutable. La edición local no modifica lo empaquetado sin reconstruir ni montar archivos.

## 3. Pod
```cmd
kubectl get nodes
kubectl apply -f namespace.yaml --dry-run=client
kubectl apply -f namespace.yaml
kubectl apply -f pod.yaml --dry-run=client
kubectl apply -f pod.yaml
kubectl wait --for=condition=Ready pod/miapp-avalos -n k8s-avalos --timeout=120s
kubectl describe pod miapp-avalos -n k8s-avalos
```
La política Never y los eventos confirman acceso a la imagen local. La readinessProbe comprueba /healthz.

## 4. Operación y diagnóstico
```cmd
kubectl get pods -n k8s-avalos -o wide
kubectl describe pod miapp-avalos -n k8s-avalos
kubectl get events -n k8s-avalos --sort-by=.metadata.creationTimestamp
start "Kubernetes Logs" cmd /k kubectl logs -f miapp-avalos -n k8s-avalos
kubectl exec -it miapp-avalos -n k8s-avalos -- /bin/sh
```
Dentro: `pwd`, `ls -l`, `cat app.py`, `hostname`, `python --version`, `wget -qO- http://127.0.0.1:9090/healthz`, `exit`.
```cmd
start "Kubernetes Port Forward" cmd /k kubectl port-forward pod/miapp-avalos 9091:9090 -n k8s-avalos
curl -i http://127.0.0.1:9091/healthz
start http://127.0.0.1:9091/
start http://127.0.0.1:9091/healthz
start "Monitor HTTP" cmd /k monitor-http.cmd
kubectl apply -f pod-fallo.yaml
kubectl get pods -n k8s-avalos -o wide
kubectl describe pod miapp-fallo -n k8s-avalos
kubectl get events -n k8s-avalos --field-selector involvedObject.name=miapp-fallo
curl -i http://127.0.0.1:9091/healthz
kubectl apply -f pod-recuperado.yaml
kubectl wait --for=condition=Ready pod/miapp-fallo -n k8s-avalos --timeout=120s
kubectl get pods -n k8s-avalos -o wide
kubectl logs --tail=10 miapp-fallo -n k8s-avalos
kubectl exec miapp-fallo -n k8s-avalos -- wget -qO- http://127.0.0.1:9090/healthz
curl -i http://127.0.0.1:9091/healthz
kubectl get deployments -n example
```
Los dos manifiestos de diagnóstico describen el mismo Pod. Aplicar en el orden indicado, no usar `kubectl apply -f .`. Si se repite la prueba con el Pod ya recuperado, el manifiesto de fallo vuelve a cambiar su imagen. Mantener el túnel del Pod principal abierto durante las consultas. La prueba no utiliza un Service ni demuestra alta disponibilidad ante fallos del nodo. Flask es un servidor de desarrollo.
