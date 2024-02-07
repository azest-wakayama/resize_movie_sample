# readme

# CPUの制限を行い、zip化された複数のファイルをまとめて圧縮する機能

***
## 環境
 - Amazon Linux2
 - Apache2.4
***

## 手順
~~~bash
# コンテナの立ち上げ
$ docker compose up --build -d

# 起動中のコンテナプロセスを確認
$ docker ps

# コンテナ内にログイン
$ docker exec -it コンテナ名 /bin/bash

# input/logsディレクトリにログを圧縮したいログを配置

# zip_compression.shの実行
$ ./zip_compression.sh

# outputディレクトリに圧縮されたzipファイルが出力される

# コンテナを停止する
$ docker compose down
~~~


# 　CPU Limitのインストールの参考記事

- ▽EPEL レポジトリを有効にするためには
  - 　https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/add-repositories.html
- ▽CPU limitの使用方法、導入について
  - https://ubunlog.com/ja/cpulimit-limita-cpu-proceso/