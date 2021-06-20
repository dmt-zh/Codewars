# Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero),
# after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words),
# and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
# Help Jonny restore the original song. "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB" => WE ARE THE CHAMPIONS MY FRIEND

def song_decoder(song):
    import re
    p = re.compile(r"[W][U][B]")
    i = p.sub(" ", song)
    return ' '.join(i.split())

print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))