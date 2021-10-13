import json
from collections import OrderedDict

file = open("si-songs.json")
di = json.load(file)
content = OrderedDict()
count = 0
for item in di:
    i = item['title'].strip()
    i += item['body'].strip().strip().replace('\r\n', " ").replace('\n\r\n', ' ').replace("//", " ").replace("(", " ") \
        .replace(")", " ").replace("-", " ")
    i += item['singer'].strip()
    tokens = i.split()
    for token in tokens:
        count += 1
        if token in content:
            content[token] += 1
        else:
            content[token] = 1

out = open("word-count.json", "w")
content = {k: v for k, v in sorted(content.items(), key=lambda item: item[1], reverse=True)}
json.dump(content, out, ensure_ascii=False, indent=4)
print(" total tokens:", count)  # 60602
