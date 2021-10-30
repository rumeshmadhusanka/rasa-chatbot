import json
from random import randrange

data = open("si-songs.json")
data = json.load(data)
new_data = []
out_file = open("si-songs-final.json", "w")


def predict_sentiment(singers):
    for singer in singers:
        if "ෆන්කි" in singer or "භාතිය" in singer:
            return "positive"
    return "negative"


i = 1
for d in data:
    ins = dict()
    ins["id"] = i
    ins["title"] = d["title"]
    ins["body"] = d["body"].replace("\n\r\n", "\n").replace("\r\n", "\n").replace(".", " ")
    singers = d["singer"].split("සමග")
    singers = [' '.join(i.strip().split()) for i in singers]
    ins["singers"] = singers
    ins["streams"] = randrange(5000, 50000, 100)
    ins["sentiment"] = predict_sentiment(singers)
    new_data.append(ins)
    i += 1

json.dump(new_data, out_file, ensure_ascii=False, indent=4)
