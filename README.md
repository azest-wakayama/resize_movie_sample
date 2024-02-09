# readme

# 動画をアスペクト比合わせかつ、1920×1080に納め出力

***
## 環境
 - ubuntu20.4
 - Apache2.4
 - Python 3.10
***

## 手順
~~~bash
# コンテナの立ち上げ
$ docker compose up --build -d

# 起動中のコンテナプロセスを確認
$ docker ps

# コンテナ内にログイン
$ docker exec -it コンテナ名 /bin/bash

# inputディレクトリに圧縮したい動画を格納

# ffmpegコマンドを実行
$ python resize_movie_sample.py ./input/縦長動画サンプル.mp4

# outputディレクトリにアスペクト比に合わせたリサイズした動画が出力される

# コンテナを停止する
$ docker compose down
~~~