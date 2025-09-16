# Find your public IP address: A quick way to do this is by visiting a website like
# checkip.amazonaws.com
# in your browser.
# aws eks describe-cluster --name flask-app-cluster --query "cluster.resourcesVpcConfig"
# aws eks update-cluster-config --region us-east-1 --name flask-app-cluster --resources-vpc-config endpointPublicAccess=true,publicAccessCidrs=104.172.226.106/32
# aws eks describe-cluster --name flask-app-cluster --query "cluster.status"
# aws eks update-kubeconfig --region us-east-1 --name flask-app-cluster
# aws autoscaling describe-auto-scaling-groups --query "AutoScalingGroups[?contains(AutoScalingGroupName, 'flask-app-cluster')].Instances[].LifecycleState"
# kubectl apply -f deployment.yaml
# kubectl apply -f service.yaml
# !!!!!!!
# kubectl get svc flask-app-service
aws autoscaling describe-auto-scaling-groups --query "AutoScalingGroups[?Tags[?Key=='eks:cluster-name' && Value=='flask-app-cluster']].AutoScalingGroupName" --output text

aws eks describe-nodegroup --cluster-name flask-app-cluster --nodegroup-name default --query "nodegroup.status"

terraform state rm 'module.eks.module.eks_managed_node_group[\"default\"].aws_eks_node_group.this[0]'

kubectl get pods -o wide
