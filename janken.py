from random import randint
hands = {0:"✊",1:"✌",2:"✋"}
rules = {(0,0):"あいこ", (0,1):"勝ち", (0,2):"負け", (1,0):"負け", (1,1):"あいこ", (1,2):"勝ち", (2,0):"勝ち", (2,1):"負け", (2,2):"あいこ"}

while True:
    chands = randint(0,2)
    uhands = input("0:グー,1:チョキ,2:パー,3:おわり")
    if uhands == "3":
        break
    if uhands not in ("0","1","2"):
        continue
    uhands = int(uhands)
    print(hands[uhands] , hands[chands])
    print(rules[(uhands,chands)])