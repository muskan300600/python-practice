def game():
    return 64

score=game()
with open("highscore.txt")as f:
    highscore=f.read()

    if highscore=="":
        with open("highscore.txt","w"):
         f.write(str(score))

    elif int(highscore)<score:
        with open("highscore.txt","w"):
         f.write(str(score))


   

