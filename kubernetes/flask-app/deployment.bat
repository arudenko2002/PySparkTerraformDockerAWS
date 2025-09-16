kubectl delete all --all

kubectl apply -f .\nginx-flask-config.yaml
kubectl apply -f .\nginx-deployment-service.yaml
kubectl apply -f .\flask-api-deployment.yaml
kubectl rollout restart deployment nginx-deployment


kubectl port-forward svc/nginx-service 9000:9000
@REM Forwarding from 127.0.0.1:9000 -> 9000
@REM Forwarding from [::1]:9000 -> 9000
@REM Handling connection for 9000
@REM Handling connection for 9000
@REM # This command was failing many times, bad connection.  They suggested to remove "old" pods, new pods were okay
@REM # There were fixes with the config files (default.yaml and directories as the are now in nginx deployment service yaml.)
@REM best thing would be removing all pods (deployments) and building new ones
http://localhost:9000


@REM # Various useful commands
@REM # list pods
kubectl get pods -l app=nginx
@REM NAME                                READY   STATUS    RESTARTS   AGE
@REM nginx-5869d7778c-858t2              1/1     Running   0          21m
@REM nginx-deployment-84444954cd-5fnbf   1/1     Running   0          53m
kubectl get pods -l app=nginx -o wide
@REM NAME                                READY   STATUS    RESTARTS   AGE   IP          NODE             NOMINATED NODE   READINESS GATES
@REM nginx-5869d7778c-858t2              1/1     Running   0          25m   10.1.0.70   docker-desktop   <none>           <none>
@REM nginx-deployment-84444954cd-5fnbf   1/1     Running   0          58m   10.1.0.69   docker-desktop   <none>           <none>
kubectl get pods -o wide
@REM NAME                                READY   STATUS    RESTARTS   AGE     IP          NODE             NOMINATED NODE   READINESS GATES
@REM flask-deployment-7f78dd679b-p765x   1/1     Running   0          3h24m   10.1.0.55   docker-desktop   <none>           <none>
@REM nginx-5869d7778c-858t2              1/1     Running   0          42m     10.1.0.70   docker-desktop   <none>           <none>
@REM nginx-deployment-84444954cd-5fnbf   1/1     Running   0          74m     10.1.0.69   docker-desktop   <none>           <none>

@REM # delete pod
kubectl delete pod nginx-deployment-54677b4cb7-mtrqq
@REM #delete deployment (also deletes pods)
kubectl delete deployment nginx-deployment
@REM # see log of a pod
kubectl logs nginx-deployment-698b48f8c7-wvr6d
@REM #ssh to pod
kubectl exec -it nginx-5869d7778c-lgz7f -- bash
    apt update && apt install net-tools -y
    netstat -tuln

kubectl port-forward svc/flask-service 8080:8080  # 8080 from pod -> 8080 of service, and flask=api is connected to 8080, see flask-api-deployment.yaml
http://localhost:8080/pages/?page=5
http://localhost:8080/
http://localhost:8080/func/?N=1+2+3
http://localhost:8080/home/10

@REM # execute app on pod: cat /etc/nginx/conf.d/default.conf
kubectl exec -it nginx-deployment-84444954cd-5fnbf -- cat /etc/nginx/conf.d/default.conf

@REM # build docker image
@REM # Create image on Docker
docker build -t flask-api:latest .

@REM # Put image to Docker Hub
docker tag flask-api:latest your-dockerhub-username/flask-api:latest
docker push your-dockerhub-username/flask-api:latest

@REM # set image from Docker Hub
kubectl set image deployment/flask-deployment flask=arudenko2002/flask-api:latest

@REM container ot the pod:
kubectl get pod nginx-6d94789b44-kjdk9 -o jsonpath="{.spec.containers[*].name}"


#working

mlflow models serve -m models:/IrisClassifier/7 -p 1234


# with nginx
localhost:9100 → Nginx → Flask app (on port 8080 inside the pod)

Save this to a file named nginx-proxy.conf:

nginx
Copy
Edit
server {
    listen 9100;

    location / {
        proxy_pass http://flask-service:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Create the ConfigMap:

kubectl create configmap nginx-proxy-config --from-file=nginx-proxy.conf

kubectl port-forward svc/flask-service 9100:9500
Forwarding from 127.0.0.1:9100 -> 8080
Forwarding from [::1]:9100 -> 8080
Handling connection for 9100
Handling connection for 9100
Handling connection for 9100
Handling connection for 9100
Handling connection for 9100
Handling connection for 9100


