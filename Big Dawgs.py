import time
from threading import Thread, Lock
import sys
lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Wait a minute, get it how you live it", 0.05),
        ("Ten toes in when we standin' on business", 0.06),
        ("I'm a big stepper, underground methods", 0.06),
        ("Top-notch hoes get the most, not the lesser", 0.07),
        ("Straight terror, product of your errors", 0.06),
        ("Pushing culture, baby, got that product you can't measure", 0.045),
        ("Trendsetter, the one who get her wetter", 0.06),
    ]
    delays = [0.2, 2.1, 4.1, 6.37, 8.6, 10.73, 15.4] 

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
