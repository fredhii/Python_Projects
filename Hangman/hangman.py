import random

def hangman():
    word = random.choice(["pugger", "little", "tigger", "cat", "puppy", "pikachu", "love", "sweet"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 9 + 1
    guessmade = ''

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Congratulations!")
            print("ʕ •ᴥ•ʔ")
            print("You've won!")
            break
        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("\033[32m9\033[0m turns left")
                print("\033[90m  --------  \033[0m")
            if turns == 8:
                print("\033[32m8\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("     O      ")
                
            if turns == 7:
                print("\033[32m7\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("\033[93m6\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("\033[93m5\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("\033[93m4\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("    \O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("\033[91m3\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("    \O/     ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("\033[91m2\033[0m turns left")
                print("\033[90m  --------  \033[0m")
                print("    \O/ \033[90m|\033[0m   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("\033[91mLast attemp\033[0m")
                print("\033[90m  --------  \033[0m")
                print("     0\033[90m__|\033[0m   ")
                print("    /|\     ")
                print("    / \     ")
            if turns == 0:
                print("\n")
                print("           \033[31m███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀")
                print("           ██    ██ ██     ██ ██   █   ██ ██   ")
                print("           ██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀")
                print("           ██    ██ ██     ██ ██       ██ ██   ")
                print("           ███▄▄▄██ ██     ██ ██       ██ ██▄▄▄")
                print("           \n")
                print("           ███▀▀▀███ ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄ ")
                print("           ██     ██   ██  ██  ██    ██     ██ ")
                print("           ██     ██   ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀ ")
                print("           ██     ██   ██  █▀  ██    ██     ██ ")
                print("           ███▄▄▄███    ▀█▀    ██▄▄▄ ██     ██▄")
                print("                                               ")
                print("                   ██               ██         ")
                print("                 ████▄   ▄▄▄▄▄▄▄   ▄████       ")
                print("                    ▀▀█▄█████████▄█▀▀          ")
                print("                      █████████████            ")
                print("                      ██▀▀▀███▀▀▀██            ")
                print("                      ██   ███   ██            ")
                print("                      █████▀▄▀█████            ")
                print("                       ███████████             ")
                print("                   ▄▄▄██  █▀█▀█  ██▄▄▄         ")
                print("                   ▀▀██           ██▀▀         ")
                print("                     ▀▀           ▀▀           ")
                print("                  You're out of attemps\033[0m\n")
                break
                


name = input("Enter your name\n")
print("==================================")
print("          Welcome", name)
print("==================================")
print("Try to guess the work in less than 10 attemps\n")
hangman()