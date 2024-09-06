# ワークショップの実行環境構築手順

ワークショップで参加者に配布するVM環境を構築する手順を記載します。

## 1. ディレクトリを指定してDev Containerを起動

次の手順を実行してDev Containerを起動します。

1. VSCodeの左下の「><」をクリックしてコマンドパレットを開く
2. 「Reopen in Container」を選択する
3. 「ワークショップ環境構築用」を選択する

## 2. 環境構築で使用するSSH鍵をホスト側からコピー

1. ホスト側で`~/.ssh/id_rsa`の鍵をコピーする
2. Dev Containerのターミナルで`.devcontainer/ssh/id_rsa`にコピーした値を貼り付けて保存

**ホスト側で秘密鍵をコピーする方法**

```shell
cat ~/.ssh/id_rsa | pbcopy
```

## 3. ワークショップ用のVMを作成

- インスタンスの起動は[terraform](terraform/README.md)
- 起動したインスタンスのセットアップは[ansible](ansible/README.md)

## 4. GitHubの公開鍵を登録

参加者のGitHubの公開鍵を登録します。\
`<VMのIPアドレス>`と`<参加者のGitHubID>`を置き換えてからコマンドを実行します。\
`<VMのIPアドレス>`は[terraform](terraform/README.md)で作成したVMのIPアドレスです。\
参加者ごとにそれぞれ異なるVM向けに実行してください。

```shell
ssh root@<VMのIPアドレス> -i ../ "curl https://github.com/<参加者のGitHubID>.keys >> /root/.ssh/authorized_keys"
```

## 5. GitHubのリポジトリに参加者を追加

```shell
REPO_NAME={{ここに追加先のリポジトリ名を入力}}
INVITE_GITHUB_ID={{ここに招待するGitHub IDを入力}}
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /repos/VirtualTech-DevOps/${REPO_NAME}/collaborators/${INVITE_GITHUB_ID} \
  -f permission='write'
```

## その他

<details>
<summary>手動でツールをインストールする場合</summary>

**バージョン管理ツール**

```
brew install asdf
```

**実行ツール**

```
asdf plugin add ansible-base
asdf plugin add terraform
asdf install
```
</details>
