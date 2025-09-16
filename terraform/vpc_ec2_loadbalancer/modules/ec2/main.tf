resource "aws_instance" "web" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  subnet_id     = var.subnet_id

  tags = {
    Name = "WebServer"
  }
}

output "instance_id" {
  value = aws_instance.web.id
}