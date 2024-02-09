import subprocess
import sys
import re

# 圧縮用にサイズをアスペクト比に合わせてサイズ変更
def resize_movie(file_path):
  movie_width, movie_height = get_video_sizes(file_path)
  ratio_w, ratio_h = calculation_aspect_ratio(movie_width, movie_height)
  aspect_ratio = ratio_w / ratio_h
#　横1920、縦1080以下の場合はそのままのサイズで返す
  if movie_width <= 1920 and movie_height <= 1080:
    return movie_width, movie_height
# 縦長動画の場合
  elif movie_width <= movie_height:     
     resize_height = 1080
     resize_width = resize_height * aspect_ratio
     return resize_width ,resize_height
  else:
      resize_width = 1920
      resize_height = resize_width * aspect_ratio
      return resize_width ,resize_height

# ビデオサイズを取得する
def get_video_sizes(file_path):
    input_ffmpeg_cmd = ['ffmpeg', '-i', file_path]
    result = subprocess.run(input_ffmpeg_cmd, capture_output=True, text=True)
    output = result.stderr
    lines = output.split('\n')
    for line in lines:
        if 'Stream #0:0' in line:
            matches = re.search(r'(\d{3,4})x(\d{3,4})', line)
            if matches:
                width = int(matches.group(1))
                height = int(matches.group(2))
                return width, height
    return None, None


# 最大公約数を求める
def gcb(width, height):
    while height:
        width, height = height, width % height
    return width

#　アスペクト比を求める 横/最大公約数 : 縦/最大公約数
def calculation_aspect_ratio(width, height):
    gcb_value = gcb(width, height)
    ratio_w = width / gcb_value
    ratio_h = height / gcb_value
    return ratio_w, ratio_h


     

#   ratio_w, ratio_h = calculation_aspect_ratio(movie_width, movie_height)

file_path = sys.argv[1]
resize_width, resize_height = resize_movie(file_path)

print('幅',resize_width)
print('高さ',resize_height)
# # 幅と高さ
# w = 800
# h = 720

# # ffmpegコマンドの作成
# compression_file_path = "./output/output_compressed.mp4"
# ffmpeg_cmd = f'ffmpeg -i {file_path} -vcodec libx264 -vb 2000k -s {w}x{h} -acodec aac -ab 64k -aac_coder twoloop -pix_fmt yuv420p -movflags +faststart {compression_file_path}'

# # ffmpegコマンドの実行
# subprocess.run(ffmpeg_cmd, shell=True)


# 実行時下記のコマンドを実行すると.pyファイルが実行されるはず
# python resize_movie_sample.py ./input/横長動画サンプル.mp4