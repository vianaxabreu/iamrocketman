from iamrocketman.params import song
import time


list_song = song.split(sep='&')
for verse in list_song:
    print(verse)
    time.sleep(2)
