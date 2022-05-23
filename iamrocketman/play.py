from iamrocketman.params import song
import time
import random

def play_song():
    list_song = song.split(sep='&')
    print(random.choice(list_song))
    # for verse in list_song:
    #     print(verse)
    #     time.sleep(2)
