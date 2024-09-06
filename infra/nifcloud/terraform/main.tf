provider "nifcloud" {}

resource "nifcloud_instance" "workshop" {
  count = var.instances

  image_id = data.nifcloud_image.ubuntu.image_id

  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }

  instance_id   = "${var.instance_name_prefix}${count.index}"
  instance_type = var.instance_type

  key_name = nifcloud_key_pair.root.key_name

  accounting_type = "2"
}

data "nifcloud_image" "ubuntu" {
  image_name = "Ubuntu Server 22.04 LTS"
}

resource "nifcloud_key_pair" "root" {
  key_name   = var.key_name
  public_key = var.admin_pubkey
}
