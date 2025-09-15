output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public[0].id  # good for EC2
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id  # good for ALB
}