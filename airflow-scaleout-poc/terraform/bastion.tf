### EC2 bastion host

resource "aws_instance" "bastion" {
  ami               = "ami-02af65b2d1ebdfafc" # Ubuntu Server 20.04 ARM
  instance_type     = "t4g.nano"
  availability_zone = local.azs.a
  subnet_id         = aws_subnet.bastion_subnet_aza.id
  private_ip        = "10.0.100.10"
  key_name          = aws_key_pair.aws_sandbox.id

  credit_specification {
    cpu_credits = "standard"
  }

  root_block_device {
    encrypted   = true
    kms_key_id  = data.aws_ebs_default_kms_key.current.key_arn
    volume_type = "gp3"
    volume_size = 20
  }

  volume_tags = {
    InstanceName = "airflow-demo-bastion"
  }

  tags = {
    Name = "airflow-demo-bastion"
  }
}
