import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")  # 下载所需的数据（仅需要运行一次）

# 读取文件内容
file_path = "app/data/output.html"  # 替换为你的文件路径
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# 分词并统计token数量
tokens = word_tokenize(content)
token_count = len(tokens)

print("Token count:", token_count)
