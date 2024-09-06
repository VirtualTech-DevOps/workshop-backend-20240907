locals {
  ips = join("\n", [for k, v in nifcloud_instance.workshop : v.public_ip])
}

output "ansible_inventory" {
  description = "ansible-playbookで指定するインベントリーを出力"
  value       = <<EOT
[all]
${local.ips}
EOT
}

# output "ssh_command" {
#   description = "SSHコマンドの例を出力"
#   value       = <<EOT

# ssh -l root ${nifcloud_instance.workshop.public_ip} -i path/to/secret_key
# EOT
# }
