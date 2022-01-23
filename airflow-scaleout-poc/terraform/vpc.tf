### vpc
resource "aws_vpc" "airflow_demo_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "airflow_demo_vpc"
  }
}

### subnets
resource "aws_subnet" "nat_subnet_aza" {
  vpc_id            = aws_vpc.airflow_demo_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = local.azs.a

  tags = {
    Name = "nat_subnet"
  }
}

resource "aws_subnet" "airflow_subnet_aza" {
  vpc_id            = aws_vpc.airflow_demo_vpc.id
  cidr_block        = "10.0.10.0/24"
  availability_zone = local.azs.a

  tags = {
    Name = "airflow_subnet"
  }
}

resource "aws_subnet" "db_subnet_aza" {
  vpc_id            = aws_vpc.airflow_demo_vpc.id
  cidr_block        = "10.0.20.0/24"
  availability_zone = local.azs.a

  tags = {
    Name = "db_subnet"
  }
}

resource "aws_subnet" "bastion_subnet_aza" {
  vpc_id                  = aws_vpc.airflow_demo_vpc.id
  cidr_block              = "10.0.100.0/24"
  availability_zone       = local.azs.a
  map_public_ip_on_launch = true

  tags = {
    Name = "bastion_subnet"
  }
}

### internet & NAT gateway bits
resource "aws_internet_gateway" "internet_gw" {
  vpc_id = aws_vpc.airflow_demo_vpc.id

  tags = {
    Name = "internet_gw"
  }
}

resource "aws_eip" "nat_gw_eip" {
  tags = {
    Name = "nat_gw_eip"
  }
}

resource "aws_nat_gateway" "nat_gw" {
  allocation_id = aws_eip.nat_gw_eip.id
  subnet_id     = aws_subnet.nat_subnet_aza.id

  tags = {
    Name = "nat_gw"
  }
}

### routing
resource "aws_route_table" "private_routes" {
  vpc_id = aws_vpc.airflow_demo_vpc.id

  # NAT gateway 
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.nat_gw.id
  }

  tags = {
    Name = "airflow_demo_private_routes"
  }
}

resource "aws_route_table" "public_routes" {
  vpc_id = aws_vpc.airflow_demo_vpc.id

  # Internet gateway 
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.internet_gw.id
  }

  tags = {
    Name = "airflow_demo_public_routes"
  }
}

resource "aws_route_table_association" "rta_airflow_subnet" {
  subnet_id      = aws_subnet.airflow_subnet_aza.id
  route_table_id = aws_route_table.private_routes.id
}

resource "aws_route_table_association" "rta_bastion_subnet" {
  subnet_id      = aws_subnet.bastion_subnet_aza.id
  route_table_id = aws_route_table.public_routes.id
}

### security groups
resource "aws_security_group" "bastion_sg" {
  name        = "bastion_sg"
  description = "Allow public SSH from specific IPs inbound, and all traffic within VPC in/out"
  vpc_id      = aws_vpc.airflow_demo_vpc.id

  ingress {
    description = "SSH from Internet"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_internet_cidrs
  }

  ingress {
    description = "Internal VPC traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["10.0.0.0/16"]
  }

  tags = {
    Name = "bastion_sg"
  }
}
