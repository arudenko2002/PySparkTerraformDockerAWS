@REM kubectl get nodes
@REM kubectl get pods -A
@REM kubectl create deployment nginx --image=nginx
@REM kubectl expose deployment nginx --port=9000 --type=NodePort
@REM kubectl get service nginx

echo kubectl delete deployment nginx
echo kubectl delete service nginx
kubectl get deployments
kubectl get services
kubectl get pods
kubectl describe pod nginx-5869d7778c-l6tpd
kubectl get all
echo kubectl delete all --all

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl proxy

kubectl describe pod nginx-5869d7778c-l6tpd

kubectl get serviceaccounts -n kube-system
kubectl get secrets -n kube-system

rem kubectl describe secret kubernetes-dashboard-key-holder -n kube-system

netstat -aon | findstr :8001
taskkill /PID 12345 /F

kubectl apply -f dashboard-admin-sa-secret.yaml

kubectl describe secret dashboard-admin-sa-token -n kubernetes-dashboard

eyJhbGciOiJSUzI1NiIsImtpZCI6IkQwTE5jZmxNNklwV19LSGVsYTA5eEhsNXpTa19NNmE3c2hPM3pIdEpqUnMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tc2EtdG9rZW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluLXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiN2E3YjM0Y2ItMDcyYy00NGI0LWE5MDktNDEzZWQ1NTMzNDYyIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbi1zYSJ9.VcpqjOeSkWnoDpGX6AKy9HPTqC9XaHrjLDQQAjTfTYTrrjz-0nbwdSU-GLkVDA8mJ3aAB6S38lahcPFh-YnNGdhS3qLdDzRyFjvGvCPLbbpjpiOdNfInpZbp7M3U6j4funGDsqQZhWnNkePUAm14iGFUHT2oxXmgbqAhAuTkOd3YzdD2TL1XMvvNZKn6AOkkCg7ho6AwZTyAYfcO39W04trGAWg7MyYpn6NmgGRhXy1qjaUI0QUS22sMEKCSgHdBC2ybbIqBxQZSqskX_bF2tuWf-IiZdHhLEK3_ygXul9x2FiHONEV0TSlTVWTtP1EJaV4T0eyasB5IWkmLiU2HVQ

eyJhbGciOiJSUzI1NiIsImtpZCI6IkQwTE5jZmxNNklwV19LSGVsYTA5eEhsNXpTa19NNmE3c2hPM3pIdEpqUnMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tc2EtdG9rZW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluLXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiN2E3YjM0Y2ItMDcyYy00NGI0LWE5MDktNDEzZWQ1NTMzNDYyIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbi1zYSJ9.VcpqjOeSkWnoDpGX6AKy9HPTqC9XaHrjLDQQAjTfTYTrrjz-0nbwdSU-GLkVDA8mJ3aAB6S38lahcPFh-YnNGdhS3qLdDzRyFjvGvCPLbbpjpiOdNfInpZbp7M3U6j4funGDsqQZhWnNkePUAm14iGFUHT2oxXmgbqAhAuTkOd3YzdD2TL1XMvvNZKn6AOkkCg7ho6AwZTyAYfcO39W04trGAWg7MyYpn6NmgGRhXy1qjaUI0QUS22sMEKCSgHdBC2ybbIqBxQZSqskX_bF2tuWf-IiZdHhLEK3_ygXul9x2FiHONEV0TSlTVWTtP1EJaV4T0eyasB5IWkmLiU2HVQ

  # generate access token # automatically it is not generated when admin account is created
  72 kubectl apply -f dashboard-admin-sa-secret.yaml
  73 kubectl describe secret dashboard-admin-sa-token -n kubernetes-dashboard
  76 kubectl get secrets -n kubernetes-dashboard
  77 kubectl describe secret dashboard-admin-sa-token -n kubernetes-dashboard
  78 kubetl proxy
  79 kubectl proxy
  80 kubectl proxy --port=8002
  81 kubectl describe secret dashboard-admin-sa-token -n kubernetes-dashboard
  85 kubectl -n kubernetes-dashboard get secret | findstr dashboard-admin-sa
  87 kubectl -n kubernetes-dashboard describe secret dashboard-admin-sa-token

(.venv) PS C:\Users\AlexR\PycharmProjects\pythonProject\kubernetes> kubectl apply -f nginx-deployment.yaml
deployment.apps/nginx-deployment created
(.venv) PS C:\Users\AlexR\PycharmProjects\pythonProject\kubernetes> kubectl port-forward svc/nginx-service 9000:9000


Forwarding from 127.0.0.1:9000 -> 80
Forwarding from [::1]:9000 -> 80
Handling connection for 9000


# Create image on Docker
docker build -t flask-api:latest .

# Put image to Docker Hub
docker tag flask-api:latest your-dockerhub-username/flask-api:latest
docker push your-dockerhub-username/flask-api:latest

# set image from Docker Hub
kubectl set image deployment/flask-deployment flask=arudenko2002/flask-api:latest

# apply kubernetes pod described in flask-api-deployment.yaml
kubectl apply -f .\flask-api-deployment.yaml

# restart pod
kubectl rollout restart deployment flask-deployment

# list pods
kubectl get pods -l app=flask-api -o wide

# execute task from pod:
kubectl exec -it flask-deployment-c9479d46f-hmr4w  -- curl -v "http://flask-service:8080/pages/?page=5"
# or run local API for the flask-deployment-c9479d46f-hmr4w pod :
kubectl exec -it flask-deployment-c9479d46f-hmr4w  -- curl -v "http://localhost:8080/pages/?page=5"

# follow logs on the pod
kubectl logs -f flask-deployment-bf846c77-fjx96

# port forward by nginx from 9000 to 8080
kubectl port-forward svc/nginx-service 9000:kube

#list all pods
kubectl get pods --all-namespaces

@REM   27 kubectl describe secret bootstrap-token-abcdef -n kube-system
@REM   28 kubectl describe secret kubernetes-dashboard-token-abcde -n kube-system
@REM   29 kubectl describe secret kubernetes-dashboard-key-holder -n kube-system
@REM   30 kubectl describe secret secret/kubernetes-dashboard-key-holder -n kube-system
@REM   31 kubectl get secrets -n kube-system
@REM   32 .\kubectl_cmd.bat
@REM   33 kubectl get pods -n kubernetes-dashboard
@REM   34 kubectl get svc -n kubernetes-dashboard
@REM   35 kubectl proxy
@REM   36 netstat -aon | findstr :8001
@REM   37 taskkill /PID 38272 /F
@REM   38 kubectl proxy
@REM   39 kubectl proxy --port=8002

@REM kubectl delete all --all

kubectl get deployments
kubectl get services
kubectl get pods
kubectl get all
kubectl describe pod nginx-5869d7778c-l6tpd

kubectl get pods -l app=flask-api
NAME                                READY   STATUS    RESTARTS   AGE
flask-api-6f84d5cf4b-mxpdw          1/1     Running   0          150m
flask-deployment-5cd899cc4b-hx7np   1/1     Running   0          49m

# ssh to pod:
kubectl exec -it flask-api-6f84d5cf4b-mxpdw -- /bin/sh

# get endpoints with port:
kubectl get endpoints flask-service

kubectl exec -it nginx-6d94789b44-9t4nq -- cat /etc/nginx/nginx.conf
kubectl exec -it nginx-deployment-86c8459b98-n5ttq -- cat /etc/nginx/nginx.conf


@REM kubectl delete pod nginx-6d94789b44-g2gg5
@REM kubectl apply -f .\nginx-flask-2.yaml
@REM kubectl apply -f .\nginx-deployment-service.yaml
@REM kubectl get pods -l app=nginx
@REM kubectl exec -it <new-nginx-pod-name> -- cat /etc/nginx/nginx.conf
@REM kubectl exec -it nginx-6d94789b44-9t4nq -- cat /etc/nginx/nginx.conf
@REM kubectl exec -it nginx-deployment-86c8459b98-n5ttq -- cat /etc/nginx/nginx.conf

ifconfig

kubectl get nodes
kubectl get pods -A
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=9000 --type=NodePort
kubectl get service nginx

http://localhost:9000

#Dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl proxy
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/


Try these:
kubectl get deployments
kubectl get services
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl delete deployment nginx (to clean up)

kubectl get serviceaccounts -n kube-system
kubectl get secrets -n kube-system

kubectl describe secret <secret-name> -n kube-system
kubectl describe secret kubernetes-dashboard-token-abcde -n kube-system

kubectl create serviceaccount dashboard-admin-sa -n kube-system

kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=kube-system:dashboard-admin-sa
kubectl get secret -n kube-system $(kubectl get serviceaccount dashboard-admin-sa -n kube-system -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode

#get token:
  18 kubectl -n kubernetes-dashboard get secret | findstr dashboard-admin-sa
  19 kubectl describe secret dashboard-admin-sa-token -n kubernetes-dashboard
http://localhost:8002/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

#  To run flask we need to run
kubectl port-forward pod/nginx-deployment-55597497f7-pr8fn 9000:9000
#  To function we need to run proxy
kubectl proxy --port=8002

#  To run Dashboard we tried to delete old replica set (rs) then old pod, but it rerun it on and on.
kubectl get rs
kubectl delete rs nginx-6d94789b44
#  delete old pod
kubectl get pods -l app=nginx, CrashLoopBackOff is on
kubectl delete pod nginx-6d94789b44-pmhwj
#  delete old deployment (called nginx)
kubectl get deployments
kubectl delete deployment nginx
#  The old replicas stopped being recreated
Token:
eyJhbGciOiJSUzI1NiIsImtpZCI6IkQwTE5jZmxNNklwV19LSGVsYTA5eEhsNXpTa19NNmE3c2hPM3pIdEpqUnMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tc2EtdG9rZW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluLXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiN2E3YjM0Y2ItMDcyYy00NGI0LWE5MDktNDEzZWQ1NTMzNDYyIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbi1zYSJ9.VcpqjOeSkWnoDpGX6AKy9HPTqC9XaHrjLDQQAjTfTYTrrjz-0nbwdSU-GLkVDA8mJ3aAB6S38lahcPFh-YnNGdhS3qLdDzRyFjvGvCPLbbpjpiOdNfInpZbp7M3U6j4funGDsqQZhWnNkePUAm14iGFUHT2oxXmgbqAhAuTkOd3YzdD2TL1XMvvNZKn6AOkkCg7ho6AwZTyAYfcO39W04trGAWg7MyYpn6NmgGRhXy1qjaUI0QUS22sMEKCSgHdBC2ybbIqBxQZSqskX_bF2tuWf-IiZdHhLEK3_ygXul9x2FiHONEV0TSlTVWTtP1EJaV4T0eyasB5IWkmLiU2HVQ

kubectl get nodes -o wide
k u b e c t l   p o r t - f o r w a r d   s v c / n g i n x - s e r v i c e   9 0 0 0 : 9 0 0 0  
 