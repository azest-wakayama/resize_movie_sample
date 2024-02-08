# ベースイメージを指定
FROM ubuntu:latest

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    apache2

# デフォルトのPythonをPython 3に設定
RUN ln -s /usr/bin/python3 /usr/bin/python

# 作業ディレクトリを設定
WORKDIR /app

# Dockerコンテナが起動した際に実行されるコマンドを設定
CMD ["apache2ctl", "-D", "FOREGROUND"]