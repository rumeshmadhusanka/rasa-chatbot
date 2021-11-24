import json
import random

file = open("si-songs-final.json")
data = json.load(file)
st = set()
for ins in data:
    singers = ins["singers"]
    for s in singers:
        st.add(s)
    # song = ins['title']
    # st.add(song)
rest = ["සින්දුවේ ලිරික්ස් මොනවද?", "සින්දුවේ ලිරික්ස් ?", "සින්දුවේ ලිරික්ස් හොයල දෙන්න", "ගීතයේ ලිරික්ස් මොනවද?",
        "ගීතයේ පදවැල කුමක්ද"]
song_singer = ["ගේ සින්දු මොනවාද?","ගෙ ගීත මොනවාද?","ගායනා කළ ගීත මොනවාද?","කියපු සින්දු මොනවාද?"]
most_pop = ["ගේ ජනප්‍රියම සින්දුව මොකක්ද?","ගෙ ජනප්‍රියම ගීතය මොකක්ද?","ප්‍රසිද්ධම ගීතය කුමක්ද",
            "ගේ ප්‍රසිද්ධම සින්දුව මොකක්ද?"]
i = ""
song_lyr = "- [" + i + "](song) " + random.choice(rest)
for i in st:
    ln = str(len(i))
    popu = "- [" + i + ']{"entity":"artist","start":0,"end":' + ln + '} ' + random.choice(most_pop)
    print(popu)
