# put into AWS config our kubernettes setup
aws eks update-kubeconfig --name flask-app-cluster --region us-east-1
kubectl get nodes
# add our configs to AWS config for kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods -o wide
kubectl describe pod flask-app-7c54bd9855-4xzq2
# get service url to use with browser
kubectl get svc flask-app-service
# should work
