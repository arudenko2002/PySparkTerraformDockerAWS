@REM aws ec2 describe-addresses --region us-east-1
@REM terraform state rm 'module.eks.module.eks_managed_node_group[\"default\"].aws_eks_node_group.this[0]'
@REM terraform destroy -auto-approve

@REM aws eks delete-nodegroup  --cluster-name flask-app-cluster --nodegroup-name "default-20250824022411671400000001" --region us-east-1

@REM aws eks wait nodegroup-deleted  --cluster-name flask-app-cluster --nodegroup-name "default-20250824022411671400000001" --region us-east-1

terraform destroy -target=aws_eks_cluster.flask-app-cluster

terraform state list | grep internet_gateway
terraform destroy -target="module.vpc.aws_internet_gateway.this[0]"

aws ec2 describe-nat-gateways --filter "Name=vpc-id,Values=vpc-00c21b7276ad9a7e0" --query "NatGateways[*].{ID:NatGatewayId,State:State,Subnet:SubnetId}" --output table

# find IGW
aws ec2 describe-internet-gateways `
  --filters "Name=attachment.vpc-id,Values=vpc-00c21b7276ad9a7e0" `
  --query "InternetGateways[*].InternetGatewayId" `
  --output table

aws ec2 detach-internet-gateway --internet-gateway-id igw-023be49bd44532b8b --vpc-id vpc-00c21b7276ad9a7e0
# An error occurred (DependencyViolation) when calling the DetachInternetGateway operation: Network vpc-00c21b7276ad9a7e0 has some mapped public address(es). Please unmap those public address(es) before detaching the gateway.
aws ec2 delete-internet-gateway --internet-gateway-id igw-023be49bd44532b8b
# An error occurred (DependencyViolation) when calling the DeleteInternetGateway operation: The internetGateway 'igw-023be49bd44532b8b' has dependencies and cannot be deleted.

@REM  344 aws ec2 describe-network-interfaces --network-interface-ids eni-04a31a5d1e7c71baf --query "NetworkInterfaces[*].{ID:NetworkInterfaceId,Status:Status,Attachment:Attachment.InstanceId,Description:Description}" --output table
@REM  345 aws elbv2 describe-load-balancers --names acefb641d00c04fbc828c961e45dab75 --output table
@REM  346 aws ec2 describe-network-interfaces --network-interface-ids eni-04a31a5d1e7c71baf --query "NetworkInterfaces[*].Attachment" --output json

@REM  348 aws elbv2 describe-load-balancers --names acefb641d00c04fbc828c961e45dab75
@REM  356 aws ec2 detach-network-interface --attachment-id eni-attach-01e8e71452fe5b0e6
@REM  357 aws elbv2 describe-load-balancers --query "LoadBalancers[?VpcId=='vpc-00c21b7276ad9a7e0'].[LoadBalancerName,Type,DNSName]" --output table
@REM  360 aws ec2 detach-network-interface --attachment-id eni-04a31a5d1e7c71baf
@REM  361 aws elbv2 describe-load-balancers --query "LoadBalancers[?VpcId=='vpc-00c21b7276ad9a7e0'].[LoadBalancerName,Type,LoadBalancerArn]" --output table
@REM  363 aws ec2 delete-network-interface --network-interface-id eni-04a31a5d1e7c71baf
@REM  364 terraform  destroy

