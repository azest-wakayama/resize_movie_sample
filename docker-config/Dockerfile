# イメージ
FROM amazonlinux:2

# 基本的なパッケージの更新とApacheのインストール
RUN yum -y update && \
    yum -y install httpd

# EPELリポジトリを追加し、追加のパッケージをインストール
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum -y install ffmpeg python3

# Pythonのパッケージ管理ツールpipのインストール
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

# 必要なPythonパッケージのインストール
RUN pip install numpy scipy matplotlib

# コンテナが起動したときに実行するコマンドを指定します（オプション）
CMD ["httpd", "-D", "FOREGROUND"]
