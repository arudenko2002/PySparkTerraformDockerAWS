aws eks update-kubeconfig --region us-east-1 --name flask-eks
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
@REM returns XXXXXXXXX - url of the service
@REM XXXXXXXX
@REM return "hello world!"
@REM XXXXXXXX/home/10
@REM returns { "data":100}
@REM XXXXXXXX/func/?N=1+2+3
@REM returns { 6 }
@REM XXXXXXXX/api/?urls=L1+L2+L3
@REM returns {L1:1, L2:2, L3:3}