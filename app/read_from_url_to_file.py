import requests

url = "https://news.yahoo.co.jp/articles/e074ced0df948fb263e1431377a0e7e55d9e859b"  # 替换为您要读取的链接

response = requests.get(url)  # 获取链接内容

if response.status_code == 200:
    content = response.text  # 获取文本内容

    with open("app/data/output.html", "w", encoding="utf-8") as file:
        file.write(content)  # 将内容写入文件
    print("内容已保存到文件。")
else:
    print("无法访问链接。")
