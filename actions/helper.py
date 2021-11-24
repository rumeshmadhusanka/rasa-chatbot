import json
import random
import logging
from nltk.metrics.distance import jaccard_distance


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


songs_file = "webscrape/si-songs-final.json"
songs = json.load(open(songs_file))
jaccard_dis = 0.3
logger = get_logger("actions_helper")


def get_song_by_id(id_song):
    for ins in songs:
        if ins['id'] == id_song:
            return ins['title'], ins['body'], ins['singers']


def build_index(instances):
    title_index = dict()
    body_index = dict()
    for ins in instances:
        doc_id = ins["id"]
        title_words = ins["title"].split()
        for pos in range(len(title_words)):
            if title_words[pos] in title_index:
                title_index[title_words[pos]].append((doc_id, pos))
            else:
                title_index[title_words[pos]] = [(doc_id, pos)]

        body_words = ins["body"].split()
        for pos in range(len(body_words)):
            if body_words[pos] in body_index:
                body_index[body_words[pos]].append((doc_id, pos))
            else:
                body_index[body_words[pos]] = [(doc_id, pos)]

    vocabulary = set(title_index.keys()).union(body_index.keys())

    return title_index, body_index, vocabulary


title_index, body_index, vocabulary = build_index(songs)


def songs_of_artist(artist):
    lst = []
    ori_artist = str(artist)
    artist = set(artist)
    for ins in songs:
        for singer in ins["singers"]:
            singer = set(singer)
            if jaccard_distance(singer, artist) < 0.3:
                lst.append(ins["title"])
    if len(lst) == 0:
        return ori_artist + "ගේ ගීත මා සතුව නොමැත. කරුණාකර නිවැරැදිව ලියා ඇත්දැයි බලන්න 🔤"
    string = ori_artist + "ගේ ගීත:\n"
    for i in range(len(lst)):
        string += str(i+1) + " " + lst[i]+"\n"
    return string


def get_most_popular_song():
    popular_song = ""
    max_views = 0
    for ins in songs:
        for singer in ins["singers"]:
            if max_views < ins["streams"]:
                max_views = ins["streams"]
                popular_song = ins["id"]
    title, body, singers = get_song_by_id(popular_song)
    singer_str = ""
    if len(singers) > 1:
        for i in range(len(singers) - 1):
            singer_str += singers[i] + " සහ "
    else:
        singer_str = singers[0]
    string = "මගේ ළඟ තියෙන ප්‍රසිද්ධම  සිංදුව: **" + title + "**\nමේ ගීතය ගායනා කරන්නේ " + singer_str + " විසින්.\n" + \
             "මේ ගීතය " + str(max_views) + " වාර ගණනක් අහල තියෙනවා.\n" + "** 🎵🎵🎵\n" + body + "🎵🎵🎵 **"
    return string


def most_popular_of_artist(artist):
    popular_song = ""
    max_views = 0
    ori_artist = str(artist)
    artist = set(artist)
    for ins in songs:
        for singer in ins["singers"]:
            singer = set(singer)
            if jaccard_distance(singer, artist) < 0.3:
                if max_views < ins["streams"]:
                    max_views = ins["streams"]
                    popular_song = ins["id"]
    title, body, singers = get_song_by_id(popular_song)
    out = ori_artist + " ගෙ  ජනප්‍රියම සින්දුව: " + title + " \nමෙම ගීතය " + str(
        max_views) + " වාර ගණනක් අසා තිබෙනවා\n" + \
          "** 🎵🎵🎵\n" + body + "🎵🎵🎵 **"
    return out


def suggest_song(mood):
    lst = []
    for ins in songs:
        sent = ins["sentiment"]
        if sent == mood:
            lst.append(ins)
    selected = random.choice(lst)
    title, body, singers = selected['title'], selected['body'], selected['singers']
    if len(singers) > 1:
        sing = singers[0] + " සහ " + singers[1]
    else:
        sing = singers[0]
    string = sing + " ගායනා කරන " + "**" + title + "**" + " ගීතය අහන්න\n " + "** 🎵🎵🎵\n" + body + "🎵🎵🎵 **"
    return string


# def extract_artist(message):
#     if "ගේ" in message:
#         return message.split("ගේ")[0]
#     if "ගෙ" in message:
#         return message.split("ගෙ")[0]
#     if "ගායනා" in message:
#         return message.split("ගායනා")[0]
#     if "කියපු" in message:
#         return message.split("කියපු")[0]


def match_lyrics(guess):
    guess = guess.strip().split()
    assert len(guess) > 0
    body_keys = list(body_index.keys())
    prospects = dict()
    for word in guess:
        prospects[word] = []
        for key in body_keys:
            if jaccard_distance(set(word), set(key)) < jaccard_dis:
                prospects[word].extend(body_index[key])
    # print(prospects)
    final_prospects = []
    for i in range(len(guess) - 1):
        cur_word = guess[i]
        nex_word = guess[i + 1]
        cur_data = prospects[cur_word]
        nex_data = prospects[nex_word]
        for pair in cur_data:
            s_id = pair[0]
            pos = pair[1]
            for nx_pair in nex_data:
                sn_id = nx_pair[0]
                pos_n = nx_pair[1]
                if s_id == sn_id:
                    if abs(pos_n - pos) <= 4:
                        final_prospects.append(s_id)
    if len(final_prospects) > 0:
        song_id = max(set(final_prospects), key=final_prospects.count)
        logger.debug("Final prospects: " + str(final_prospects) + " " + str(song_id))
        chosen_song = get_song_by_id(song_id)
        logger.debug("Chosen song: " + str(chosen_song))
        return get_song_by_id(song_id)
    return None


def get_matched_lyrics(guess):
    matched = match_lyrics(guess)
    if matched is None:
        return "සමාවන්න 🙁 ඔබ ඉල්ලු **" + guess + "** ගීතය මා සතුව නැත."
    title, body, singers = match_lyrics(guess)
    if len(singers) > 1:
        sing = singers[0] + " සහ " + singers[1]
    else:
        sing = singers[0]
    out = "** " + title + "** ගීතය " + sing + "  විසින් ගායනා කරන ලද්දකි.\n" + \
          "** 🎵🎵🎵\n" + body + "** 🎵🎵🎵"
    return out


if __name__ == '__main__':
    mps = get_most_popular_song()
    print(mps)
    mpsa = most_popular_of_artist("ෆන්කි ඩර්ට්")
    print(mpsa)
    ss = suggest_song("positive")
    print(ss)
    soa = songs_of_artist("ෆන්කි ඩර්ට්")
    print(soa)

    title_index, body_index, vocabulary = build_index(songs)
    # print(body_index)
    match = match_lyrics("රැස් විහිදෙන දුර අවකාසේ")
    print(match)
    # print(match)
