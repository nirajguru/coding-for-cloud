variable "key_alias_name" {
  description = "This is the key alias"
  type        = string

}

variable "description" {
  description = "my kms key"
  type        = string

}

variable "deletion_window_in_days" {
  default     = 7
  type        = number
  description = "default deletion period"

}