terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# --- VPC, Subnets, and Security Groups ---
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  name = "flask-eks-vpc"
  cidr = "10.0.0.0/16"
  azs = ["${var.aws_region}a", "${var.aws_region}b"]
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  enable_nat_gateway = false
  map_public_ip_on_launch = true  # Add this line
}

# --- EKS Cluster ---
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.3"
  cluster_name    = "flask-app-cluster"
  cluster_version = "1.28"
  subnet_ids      = module.vpc.public_subnets
  vpc_id          = module.vpc.vpc_id

    # Add these lines
  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true
  cluster_endpoint_public_access_cidrs = ["104.172.226.106/32"]

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.micro"]
      min_size       = 1
      max_size       = 3
      desired_size   = 2
    }
  }
}

# --- ECR Repository ---
resource "aws_ecr_repository" "flask_repo" {
  name = "flask-app"
  force_delete = true
}

output "cluster_name" {
  value = module.eks.cluster_name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.flask_repo.repository_url
}

