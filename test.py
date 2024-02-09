import subprocess
import re
import sys


# 入力ファイルのパス
f = sys.argv[1]

# ffmpegコマンドを実行して出力を取得
output = ['ffmpeg', '-i', f]
result = subprocess.run(output, capture_output=True, text=True)
pattern = r'(\d{3,4})x(\d{3,4})'
match = re.search(pattern, result.stdout)
print(match)
# 正規表現パターンを使用して出力から必要な情報を抽出
# pattern = re.compile(r'(Stream:).*')
# matches = pattern.findall(result.stdout)
# print(matches)

# 結果を表示
# for match in matches:
#     print('情報',match)

# python test.py ./input/縦長動画サンプル.mp4