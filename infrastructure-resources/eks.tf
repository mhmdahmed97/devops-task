module "eks" {
  source = "./modules/eks"

  eks_version = local.eks_version
  eks_name    = local.eks_name
  subnet_ids  = module.vpc.public_subnet_ids
  node_groups = local.node_groups
}
