variable "instance_type" {
  description = "インスタンスタイプ"
  type        = string
  default     = "small"
}

variable "instance_name_prefix" {
  description = "インスタンス名プレフィックス. 1-15文字 [0-9a-zA-Z]"
  type        = string
  default     = "workshop"
}

variable "instances" {
  description = "インスタンス数"
  type        = number
  default     = 1
}

variable "key_name" {
  description = "管理者用SSH公開鍵名"
  type        = string
  default     = "workshopadmin"
}

variable "admin_pubkey" {
  description = "管理者用SSH公開鍵(RSA base64 encoded)"
  type        = string
}
