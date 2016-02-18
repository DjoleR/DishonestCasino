from Die import LoadedDie
from Die import FairDie
from Viterbi import Viterbi
from random import randint


# Initiation of the problem 
ld = LoadedDie()
ld.on = True
fd = FairDie()
fd.on = False

seqeunce = ""
dice = ""

# Generating 100 rolls 
for i in range(0,101):
    if ld.on:
        seqeunce += str(ld.roll())
        dice += "L"
        if ld.switch():
            ld.on = False
            fd.on = True
        continue

    if fd.on:
        seqeunce += str(fd.roll())
        dice += "F"
        if fd.switch():
            fd.on = False
            ld.on = True
        continue


print("Sequence: " + seqeunce)
print("States  : " + dice)
# Running Viterbi decoding
v = Viterbi()
print("Decoding: " + v.Decode(seqeunce))