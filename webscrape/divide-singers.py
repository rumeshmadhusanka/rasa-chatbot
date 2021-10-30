import json
from random import randrange

data = open("si-songs.json")
data = json.load(data)
new_data = []
out_file = open("si-songs-final.json", "w")
for d in data:
    ins = dict()
    ins["title"] = d["title"]
    ins["body"] = d["body"].replace("\n\r\n", "\n").replace("\r\n", "\n").replace(".", " ")
    singers = d["singer"].split("සමග")
    singers = [' '.join(i.strip().split()) for i in singers]
    ins["singers"] = singers
    ins["streams"] = randrange(5000, 50000, 100)
    new_data.append(ins)

json.dump(new_data, out_file, ensure_ascii=False, indent=4)
