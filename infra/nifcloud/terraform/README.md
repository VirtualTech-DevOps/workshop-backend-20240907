## インスタンス起動

`repository_root/terraform`以下で実行

- nifcloudを操作するためのクレデンシャルを設定

```
export NIFCLOUD_DEFAULT_REGION=jp-east-1
export NIFCLOUD_ACCESS_KEY_ID=CHANGEME
export NIFCLOUD_SECRET_ACCESS_KEY=CHANGEME
```

- Terraformの設定

設定ファイルを作る

```
cp terraform.tfvars{.example,}
```

rootに登録するSSH公開鍵の設定

```
cat path/to/id_rsa.pub | base64 | tr -d '\n' | pbcopy
vi terraform.tfvars
```

コピーした公開鍵を`admin_pubkey`の値にペースト

- Terraform初期化、Plan作成

```
terraform init
terraform plan
```

- インスタンス起動

```
terraform apply
```

- Ansibleで使用するインベントリー生成

```
terraform output -raw ansible_inventory > ../ansible/instances
```

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.5.0 |
| <a name="requirement_nifcloud"></a> [nifcloud](#requirement\_nifcloud) | ~> 1.9.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_nifcloud"></a> [nifcloud](#provider\_nifcloud) | 1.9.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [nifcloud_instance.workshop](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/instance) | resource |
| [nifcloud_key_pair.root](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/key_pair) | resource |
| [nifcloud_image.ubuntu](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/data-sources/image) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_admin_pubkey"></a> [admin\_pubkey](#input\_admin\_pubkey) | 管理者用SSH公開鍵(RSA base64 encoded) | `string` | n/a | yes |
| <a name="input_instance_name_prefix"></a> [instance\_name\_prefix](#input\_instance\_name\_prefix) | インスタンス名プレフィックス. 1-15文字 [0-9a-zA-Z] | `string` | `"workshop"` | no |
| <a name="input_instance_type"></a> [instance\_type](#input\_instance\_type) | インスタンスタイプ | `string` | `"small"` | no |
| <a name="input_instances"></a> [instances](#input\_instances) | インスタンス数 | `number` | `1` | no |
| <a name="input_key_name"></a> [key\_name](#input\_key\_name) | 管理者用SSH公開鍵名 | `string` | `"workshopadmin"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ansible_inventory"></a> [ansible\_inventory](#output\_ansible\_inventory) | ansible-playbookで指定するインベントリーを出力 |
<!-- END_TF_DOCS -->
