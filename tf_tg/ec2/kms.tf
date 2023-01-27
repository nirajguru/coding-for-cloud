module "my_kms" {
  providers = {
    aws = aws.niraj
  }
  source                  = "./module_kms"
  key_alias_name          = "alias/ec2key"
  description             = "kms keys creation for ec2"
  deletion_window_in_days = 7

}