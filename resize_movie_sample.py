import subprocess
import sys
import re

# 圧縮用にサイズをアスペクト比に合わせてサイズ変更
def resize_movie(file_path):
  movie_width, movie_height = get_video_sizes(file_path)
  ratio_w, ratio_h = calculation_aspect_ratio(movie_width, movie_height)
  aspect_ratio = ratio_w / ratio_h  # 初期のアスペクト比を計算
  MAX_WIDTH = 1920
  MAX_HEIGHT = 1080

#　横1920、縦1080以下の場合はそのままのサイズで返す
  if movie_width <= MAX_WIDTH and movie_height <= MAX_HEIGHT:
    aspect_ratio = ratio_w / ratio_h
    return movie_width, movie_height
# 縦長動画の場合
  elif movie_width <= movie_height:     
     resize_width = MAX_HEIGHT * aspect_ratio
     return resize_width ,MAX_HEIGHT
  else:
      resize_height = MAX_WIDTH / aspect_ratio
      if resize_height < MAX_HEIGHT:
        return MAX_WIDTH, resize_height
      else:
        while resize_height >= MAX_HEIGHT:
            MAX_WIDTH -= 1
            resize_height = MAX_WIDTH / aspect_ratio
        return MAX_WIDTH, resize_height

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
# w = 1080
# h = 608

# # ffmpegコマンドの作成
# compression_file_path = f"./output/{w}_{h}_.mp4"
# ffmpeg_cmd = f'ffmpeg -i {file_path} -vcodec libx264 -vb 2000k -s {w}x{h} -acodec aac -ab 64k -aac_coder twoloop -pix_fmt yuv420p -movflags +faststart {compression_file_path}'

# # ffmpegコマンドの実行
subprocess.run(ffmpeg_cmd, shell=True)


# 実行時下記のコマンドを実行すると.pyファイルが実行されるはず
# python resize_movie_sample.py ./input/1080_608_.mp4