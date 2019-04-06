# github-webhook

## 概要
個人開発(4人)で進めているプロジェクトがありますが、モチベーションを上げるためにissueのclose、プルリクマージされた際に自動でツイートするようにしたい。

## 構成
GitHubのwebhook → API Gateway → Lambda

## ライブラリ手順
Lambdaのため、プロジェクトにライブラリを入れる。
※ライブラリはフォルダ直下に置く必要がある
```
$ pip3 install requests requests_oauthlib -t .
```
