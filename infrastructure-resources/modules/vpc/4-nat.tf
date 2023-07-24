# resource "aws_eip" "this" {
#   vpc = true
# }

# resource "aws_nat_gateway" "this" {
#   allocation_id = aws_eip.this.id
#   subnet_id     = aws_subnet.public[0].id

#   depends_on = [aws_internet_gateway.this]
# }
