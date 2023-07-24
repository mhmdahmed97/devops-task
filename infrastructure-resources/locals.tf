locals {
  vpc_azs = ["us-east-1a", "us-east-1b"]
  # vpc_private_subnets = ["10.0.0.0/19", "10.0.32.0/19"]
  vpc_public_subnets = ["10.0.64.0/19", "10.0.96.0/19"]

  # vpc_private_subnet_tags = {
  #   "kubernetes.io/role/internal-elb"                    = 1
  #   "kubernetes.io/cluster/test-project-arm-eks-cluster" = "owned"
  # }

  vpc_public_subnet_tags = {
    "kubernetes.io/role/elb"                             = 1
    "kubernetes.io/cluster/test-project-arm-eks-cluster" = "owned"
  }

  eks_version = "1.27"
  eks_name    = "test-project-arm-eks-cluster"
  node_groups = {
    intellirentv2_nodes = {
      ami_type       = "AL2_ARM_64"
      capacity_type  = "ON_DEMAND"
      instance_types = ["t4g.small"]
      scaling_config = {
        desired_size = 3
        max_size     = 3
        min_size     = 0
      }
    }
  }
}
