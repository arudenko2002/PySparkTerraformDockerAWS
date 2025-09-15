#complete cleanup steps

# 1. Delete k8s resources first (so LoadBalancers get deprovisioned automatically):

kubectl delete -f deployment.yaml
kubectl delete -f service.yaml


#2. Run terraform destroy in your project folder:

terraform destroy


#Check for leftovers:
#aws ecr describe-repositories → delete manually if still there:

aws ecr delete-repository --repository-name flask-app --force

# aws ec2 describe-load-balancers → confirm no orphan ELBs.
# aws ec2 describe-network-interfaces → confirm no dangling ENIs.