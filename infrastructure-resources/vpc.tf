module "vpc" {
  source = "./modules/vpc/"

  azs = local.vpc_azs
  # private_subnets = local.vpc_private_subnets
  public_subnets = local.vpc_public_subnets

  # private_subnet_tags = local.vpc_private_subnet_tags
  public_subnet_tags = local.vpc_public_subnet_tags
}
