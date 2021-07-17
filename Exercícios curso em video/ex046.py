from time import sleep
import emoji
import playsound
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(emoji.emojize('BOOOOOOOOOOOOOM!!! :fire: :fire: :fire:', use_aliases=True))
playsound._playsoundWin('ex021.mp3')
