## インスタンス初期化

`repository_root/ansible`以下で実行

- 初めて接続するホストでKeyチェックを無効にする

```
export ANSIBLE_HOST_KEY_CHECKING=false
```

- パッケージインストール

```
ansible-playbook -i instances install-pkgs.yml
```
