output "eks_name" {
  value = aws_eks_cluster.this.name
}

output "eks_endpoint" {
  value = aws_eks_cluster.this.endpoint
}

output "eks_cert_auth" {
  value = aws_eks_cluster.this.certificate_authority[0].data
}

output "openid_provider_arn" {
  value = aws_iam_openid_connect_provider.this[0].arn
}

output "openid_provider_url" {
  value = aws_iam_openid_connect_provider.this[0].url
}
