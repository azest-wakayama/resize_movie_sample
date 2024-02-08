import subprocess
import sys

# compression_file_path = "./output/output_compressed.mp4"
def get_video_sizes(file_path):
    input_ffmpeg_cmd = ['ffmpeg', '-i', file_path]  # 例としてFFmpegコマンドをリスト形式で渡す
    result = subprocess.run(input_ffmpeg_cmd, capture_output=True, text=True)
    output = result.stderr
    lines = output.split('\n')
    for line in lines:
        if 'Stream #0:0' in line:
            tokens = line.split(',')[2].strip().split()[0]
            width, height = map(int, tokens.split('x'))
            return width, height
    return None, None

file_path = sys.argv[1]
print(file_path)
width, height = get_video_sizes(file_path)
print('縦:', height)
print('横:', width)







# input_ffmpeg_cmd = ['ffmpeg', '-i', file_path]
# try:
#     result = subprocess.run(input_ffmpeg_cmd, capture_output=True, text=True)
#     output = result.stderr
#     lines = output.split('\n')
#     for line in lines:
#         if 'Stream #0:0' in line:
#             tokens = line.split(',')[2].strip().split()[0]
#             width, height = map(int, tokens.split('x'))
#             print('縦:',height)
#             print('横:',width)
#             break
# except Exception as e:
#     print("エラー:", e)

# # 幅と高さ
# w = 800
# h = 720

# # ffmpegコマンドの作成
# ffmpeg_cmd = f'ffmpeg -i {file_path} -vcodec libx264 -vb 2000k -s {w}x{h} -acodec aac -ab 64k -aac_coder twoloop -pix_fmt yuv420p -movflags +faststart {compression_file_path}'

# # ffmpegコマンドの実行
# subprocess.run(ffmpeg_cmd, shell=True)


# 実行時下記のコマンドを実行すると.pyファイルが実行されるはず
# python resize_movie_sample.py ./input/横長動画サンプル.mp4