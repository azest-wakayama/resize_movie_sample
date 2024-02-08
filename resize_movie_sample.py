import subprocess
import sys


# ファイルパスと圧縮後のファイルパス
file_path = sys.argv[1]  # ファイルパスは第1引数として受け取る
file_path = "input.mp4"
compression_file_path = "output_compressed.mp4"

# 幅と高さ
w = 1280
h = 720

# ffmpegコマンドの作成
ffmpeg_cmd = f'ffmpeg -i {file_path} -vcodec libx264 -vb 2000k -s {w}x{h} -acodec aac -ab 64k -aac_coder twoloop -pix_fmt yuv420p -movflags +faststart {compression_file_path}'

# ffmpegコマンドの実行
subprocess.run(ffmpeg_cmd, shell=True)


# 実行時下記のコマンドを実行すると.pyファイルが実行されるはず