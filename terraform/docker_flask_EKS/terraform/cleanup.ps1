param (
    [string]$VpcId = "vpc-00c21b7276ad9a7e0"  # <-- replace with your VPC ID
)

Write-Host "Checking for Elastic IPs in VPC: $VpcId"

$eips = aws ec2 describe-addresses `
    --filters "Name=domain,Values=vpc" `
    --query "Addresses[*].{AllocId:AllocationId,AssocId:AssociationId}" `
    --output json | ConvertFrom-Json

if ($eips.Count -gt 0) {
    foreach ($eip in $eips) {
        $allocId = $eip.AllocId
        $assocId = $eip.AssocId

        if ($assocId -and $assocId -ne $null) {
            Write-Host "Disassociating Elastic IP ($allocId) with AssociationId $assocId"
            aws ec2 disassociate-address --association-id $assocId
        }

        Write-Host "Releasing Elastic IP $allocId"
        aws ec2 release-address --allocation-id $allocId
    }
} else {
    Write-Host "No Elastic IPs found"
}

Write-Host "Checking for NAT Gateways in VPC: $VpcId"

$nats = aws ec2 describe-nat-gateways `
    --filter "Name=vpc-id,Values=$VpcId" `
    --query "NatGateways[*].NatGatewayId" `
    --output text

if ($nats) {
    foreach ($natId in $nats.Split()) {
        Write-Host "Deleting NAT Gateway: $natId"
        aws ec2 delete-nat-gateway --nat-gateway-id $natId
    }

    Write-Host "Waiting for NAT Gateways to delete..."
    aws ec2 wait nat-gateway-deleted --nat-gateway-ids $nats
    Write-Host "NAT Gateways deleted"
} else {
    Write-Host "No NAT Gateways found"
}

Write-Host "Running terraform destroy"
terraform destroy -auto-approve