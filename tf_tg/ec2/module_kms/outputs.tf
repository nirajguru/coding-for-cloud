output "alias" {
  value = var.key_alias_name
}

output "id" {
  value = concat(aws_kms_key.this.*.id, [""])[0]
}