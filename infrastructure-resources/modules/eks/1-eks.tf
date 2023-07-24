resource "aws_iam_role" "eks_iam_role" {
  name = "eks-service-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "eks_iam_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_iam_role.name
}

resource "aws_eks_cluster" "this" {
  name     = var.eks_name
  version  = var.eks_version
  role_arn = aws_iam_role.eks_iam_role.arn
  vpc_config {
    endpoint_private_access = false
    endpoint_public_access  = true

    subnet_ids = var.subnet_ids
  }

  depends_on = [aws_iam_role_policy_attachment.eks_iam_policy_attachment]

  tags = {
    Name = "${var.eks_name}"
  }
}

