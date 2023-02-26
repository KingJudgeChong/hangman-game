import time
import os
import random
os.system('cls')

# My introductions or entry before the game starts. It's kinda bit long though. Well just a little bit until line 46
name = input("\n \n \nEnter your name: ")
os.system('cls')

print(f" \n \n Hey {name}...")
time.sleep(1)
print(" \n \n Do you wanna get hanged?")
time.sleep(0.5)
print(" \n ...", end= '')
time.sleep(1.5)
print(" \n \n \n Like this\n \n \n")
time.sleep(2)

#photo
import tkinter as tk
root = tk.Tk()
root.title("Hangman Game!")
root.geometry("1197x732")

photo = tk.PhotoImage(file= "hang.png")

label = tk.Label(root, image= photo, width= 1197, height= 732,
bg= "black", fg= "yellow", font=('Arial',30,'bold'))
label.pack()

root.mainloop()

time.sleep(4)
print(" \n \n Sorry, I didn't mean that one.  Well anyway... \n \n")
time.sleep(4)
os.system('cls')
print("\n \n \n")
print("                              !!! WELCOME TO HANGMAN !!!\n")
print(" \n                                       ", name)
print(" \n \n                                     AHAHAHAHAHA!")
print("\n \n \n")
time.sleep(3)
os.system('cls')
print(" \n \n \n")
print("                                Let's start playing HANGMAN\n")
time.sleep(1)
print(" \n                             You only have 30 seconds to guess")
time.sleep(2)
print(" \n  \n                                 Have FUN and GOOD LUCK!!! \n \n \n")
time.sleep(1)
print("                                             3")
time.sleep(1)
print("                                             2")
time.sleep(1)
print("                                             1")
time.sleep(1)
os.system('cls')
print(" \n \n \n \n \n \n \n \n                             The BOMB has been PLANTED!!!")
time.sleep(2)
os.system('cls')

# collection given variables
def collection():
    global length_words
    global count
    global guess_this_word
    global words
    global length
    global COUNT_LIMIT
    global hang
    global starting_time
    global guessed
    global remaining_time
    global keys_used
    global start_time

    # timer, only 30 seconds.
    starting_time = 30

    # starting count for mistakes
    count = 0

    # limit for counting
    COUNT_LIMIT = 5
    
    # the words to guess inside the game
    words = [                                                                                                                           'floccinaucinihilipilification', 'incomprehensibility', 'uncopyrightable', 'hippopotomonstrosesquippedaliophobia', 'python', 'discord']
    
    # randomize the words
    guess_this_word = random.choice(words)
    
    # use to measure the length of the word
    length = len(guess_this_word)

    # for all the guessed keys, including the wrong keys
    keys_used = []
    
    # change the length into '_'
    length_words = length * '_'

    # for my time bomb 
    start_time = time.time()

    # guessed letters inside the word
    guessed = []

    # my hang collection
    hang = [ 
"\033[0;30;46m                                                                                                                                         \n"        
"\033[1;30;46m    \  |  /                          \033[2;31;41m*/+---+---+\*\033[0;30;46m                                                                                       \n"
"   \033[0;30;46m_ \033[0;30;43m     \033[0;30;46m _                         \033[2;30;41m||\033[0;30;46m         \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"     \033[0;30;43m     \033[0;30;46m                           \033[2;30;41m||\033[0;30;46m         \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"\033[0;30;44m                                     \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                   \033[2;30;42m                    \n"
"\033[0;30;44m                                    \033[0;30;43m \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m        > I believe in you.                                       \033[0;30;42m                     \n"
"\033[0;30;44m                                  \033[0;30;43m   \033[2;30;41m||\033[0;30;43m_________\033[2;30;41m||\033[0;30;43m                                                                     \033[2;30;42m                  \n"
"\033[0;30;44m                                \033[0;30;43m     \033[2;30;41m||  _____  ||\033[0;30;43m                                                                          \033[1;30;42m             \n"
"\033[0;30;44m                              \033[0;30;43m   \033[2;30;41m====||_|\033[0;30;43m     \033[2;30;41m|_||====\033[0;30;43m                                                                       \033[3;30;42m            \n"
"\033[0;30;44m                            \033[0;30;43m         \033[2;30;41m|| |\033[0;30;43m_____\033[2;30;41m| ||\033[0;30;43m                                                                              \033[0;30;42m         \n"
"\033[0;30;44m                          \033[0;30;43m       \033[2;30;41m====||_________||====\033[0;30;43m                                                                             \033[0;30;42m      \n"
"\033[0;30;44m                        \033[0;30;43m                                                                                                              \033[0;30;42m   \n \n\033[0;37;40m",  
"\033[0;30;46m                                                                                                                                         \n"        
"\033[1;30;46m    \  |  /                          \033[2;30;41m*/+---+---+\*\033[0;30;46m                                                                                       \n"
"   \033[0;30;46m_ \033[0;30;43m     \033[0;30;46m _                         \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"     \033[0;30;43m     \033[0;30;46m                           \033[2;30;41m||\033[0;30;46m         \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"\033[0;30;44m                                     \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                   \033[0;30;42m                    \n"
"\033[0;30;44m                                    \033[0;30;43m \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                  \033[0;30;42m                     \n"
"\033[0;30;44m                                  \033[0;30;43m   \033[2;30;41m||\033[0;30;43m_________\033[2;30;41m||\033[0;30;43m        > It's alright, that's only one. You can do it!              \033[2;30;42m                  \n"
"\033[0;30;44m                                \033[0;30;43m     \033[2;30;41m||  _____  ||\033[0;30;43m                                                                          \033[1;30;42m             \n"
"\033[0;30;44m                              \033[0;30;43m   \033[2;30;41m====||_|\033[0;30;43m     \033[2;30;41m|_||====\033[0;30;43m                                                                       \033[3;30;42m            \n"
"\033[0;30;44m                            \033[0;30;43m         \033[2;30;41m|| |\033[0;30;43m_____\033[2;30;41m| ||\033[0;30;43m                                                                              \033[0;30;42m         \n"
"\033[0;30;44m                          \033[0;30;43m       \033[2;30;41m====||_________||====\033[0;30;43m                                                                               \033[0;30;42m    \n"
"\033[0;30;44m                        \033[0;30;43m                                                                                                              \033[0;30;42m   \033[0;37;40m\n \n", 
"\033[0;30;46m                                                                                                                                         \n"        
"\033[1;30;46m    \  |  /                          \033[2;30;41m*/+---+---+\*\033[0;30;46m                                                                                       \n"
"   \033[0;30;46m_ \033[0;30;43m     \033[0;30;46m _                         \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"     \033[0;30;43m     \033[0;30;46m                           \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"\033[0;30;44m                                     \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                   \033[0;30;42m                    \n"
"\033[0;30;44m                                    \033[0;30;43m \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                  \033[0;30;42m                     \n"
"\033[0;30;44m                                  \033[0;30;43m   \033[2;30;41m||\033[0;30;43m_________\033[2;30;41m||\033[0;30;43m        > Knock Knock! Hang...                                       \033[2;30;42m                  \n"
"\033[0;30;44m                                \033[0;30;43m     \033[2;30;41m||  _____  ||\033[0;30;43m      I'm hanging out with someone else...                                \033[1;30;42m             \n"
"\033[0;30;44m                              \033[0;30;43m   \033[2;30;41m====||_|\033[0;30;43m     \033[2;30;41m|_||====\033[0;30;43m            HAHAHAHAHA!                                                \033[3;30;42m            \n"
"\033[0;30;44m                            \033[0;30;43m         \033[2;30;41m|| |\033[0;30;43m_____\033[2;30;41m| ||\033[0;30;43m                                                                              \033[0;30;42m         \n"
"\033[0;30;44m                          \033[0;30;43m       \033[2;30;41m====||_________||====\033[0;30;43m                                                                             \033[0;30;42m      \n"
"\033[0;30;44m                        \033[0;30;43m                                                                                                              \033[0;30;42m   \033[0;37;40m\n \n", 
"\033[0;30;46m                                                                                                                                         \n"        
"\033[1;30;46m    \  |  /                          \033[2;30;41m*/+---+---+\*\033[0;30;46m                                                                                       \n"
"   \033[0;30;46m_ \033[0;30;43m     \033[0;30;46m _                         \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"     \033[0;30;43m     \033[0;30;46m                           \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"\033[0;30;44m                                     \033[2;30;41m||\033[0;31;43m    \033[1;30;43mO\033[0;31;43m    \033[2;30;41m||\033[0;30;43m                                                                   \033[0;30;42m                    \n"
"\033[0;30;44m                                    \033[0;30;43m \033[2;30;41m||\033[0;30;43m         \033[2;30;41m||\033[0;30;43m                                                                  \033[0;30;42m                     \n"
"\033[0;30;44m                                  \033[0;30;43m   \033[2;30;41m||\033[0;30;43m_________\033[2;30;41m||\033[0;30;43m        > Whoa... I can see my head. I just realized I'm bald. Nice!\033[2;30;42m                   \n"
"\033[0;30;44m                                \033[0;30;43m     \033[2;30;41m||  _____  ||\033[0;30;43m                                                                          \033[1;30;42m             \n"
"\033[0;30;44m                              \033[0;30;43m   \033[2;30;41m====||_|\033[0;30;43m     \033[2;30;41m|_||====\033[0;30;43m                                                                       \033[3;30;42m            \n"
"\033[0;30;44m                            \033[0;30;43m         \033[2;30;41m|| |\033[0;30;43m_____\033[2;30;41m| ||\033[0;30;43m                                                                              \033[0;30;42m         \n"
"\033[0;30;44m                          \033[0;30;43m       \033[2;30;41m====||_________||====\033[0;30;43m                                                                             \033[0;30;42m      \n"
"\033[0;30;44m                        \033[0;30;43m                                                                                                              \033[0;30;42m   \033[0;37;40m\n \n", 
"\033[0;30;46m                                                                                                                                         \n"        
"\033[1;30;46m    \  |  /                          \033[2;30;41m*/+---+---+\*\033[0;30;46m                                                                                       \n"
"   \033[0;30;46m_ \033[0;30;43m     \033[0;30;46m _                         \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"     \033[0;30;43m     \033[0;30;46m                           \033[2;30;41m||\033[0;31;46m    \033[1;31;46m|\033[0;31;46m    \033[2;30;41m||\033[0;30;46m                                                                                       \n"
"\033[0;30;44m                                     \033[2;30;41m||\033[0;31;43m    \033[1;30;43mO\033[0;31;43m    \033[2;30;41m||\033[0;30;43m                                                                   \033[0;30;42m                    \n"
"\033[0;30;44m                                    \033[0;30;43m \033[2;30;41m||\033[0;30;43m   \033[1;30;43m/\033[0;30;43m\033[1;30;43m|>\033[0;30;43m   \033[2;30;41m||\033[0;30;43m                                                                  \033[0;30;42m                     \n"
"\033[0;30;44m                                  \033[0;30;43m   \033[2;30;41m||\033[0;30;43m_________\033[2;30;41m||\033[0;30;43m        > ... HEEEEEELP!!! This ain't funny..                       \033[2;30;42m                   \n"
"\033[0;30;44m                                \033[0;30;43m     \033[2;30;41m||  _____  ||\033[0;30;43m                                                                          \033[1;30;42m             \n"
"\033[0;30;44m                              \033[0;30;43m   \033[2;30;41m====||_|\033[0;30;43m     \033[2;30;41m|_||====\033[0;30;43m                                                                       \033[3;30;42m            \n"
"\033[0;30;44m                            \033[0;30;43m         \033[2;30;41m|| |\033[0;30;43m_____\033[2;30;41m| ||\033[0;30;43m                                                                              \033[0;30;42m         \n"
"\033[0;30;44m                          \033[0;30;43m       \033[2;30;41m====||_________||====\033[0;30;43m                                                                             \033[0;30;42m      \n"
"\033[0;30;44m                        \033[0;30;43m                                                                                                              \033[0;30;42m   \033[1;30;47m\n \n",
"\033[0;30;47m                                                                                                                            \n" 
"\033[0;30;47m                                     \033[1;37;40m*/+---+---+\*\033[0;30;47m                                                                          \n" 
"\033[0;30;47m                                     \033[1;37;40m||\033[0;30;47m    \033[1;30;47m|\033[0;37;47m    \033[1;37;40m||\033[0;30;47m                                                                          \n"
"\033[0;30;47m                                     \033[1;37;40m||\033[0;30;47m    \033[1;30;47m|\033[0;37;47m    \033[1;37;40m||\033[0;30;47m                                                                          \n"
"\033[0;30;47m                                     \033[1;37;40m||\033[0;30;47m    \033[1;30;47m|O\033[0;37;47m   \033[1;37;40m||\033[0;30;47m        > Ung hindi ka crush ng crush mo                                  \n"
"\033[0;30;47m                                     \033[1;37;40m||\033[0;30;47m   /|\   \033[1;37;40m||\033[0;30;47m                                                                          \n"
"\033[0;30;47m                                     \033[1;37;40m||\033[0;30;47m___/ \___\033[1;37;40m||\033[0;30;47m                     BIGTI                                                \n"
"\033[0;30;47m                                 \033[01;37;40m====||  _____  ||====\033[0;30;47m                                                                      \n"
"\033[0;30;47m                                     \033[1;37;40m||_|\033[0;30;47m     \033[1;37;40m|_||\033[0;30;47m                 AHHH WAWA IYAK                                           \n"
"\033[0;30;47m                                     \033[1;37;40m|| |\033[0;30;47m_____\033[1;37;40m| ||\033[0;30;47m                                                                          \n"
"\033[0;30;47m                                 \033[1;37;40m====||_________||====\033[0;30;47m                                                                      \n"
"\033[0;30;47m                                                                                                                            \033[1;30;47m\n \n "]    



# hangman game
def main_game():
    global length_words
    global count
    global guess_this_word
    global words
    global length
    global COUNT_LIMIT
    global hang
    global starting_time
    global guessed
    global remaining_time
    global keys_used
    global start_time 
    
    print(" \n \n ")
    print("                               :", length_words )
    guess = input(f"                               GUESS THE WORD OR HANGMAN!\n \n{hang[count]}")
    guess = guess.lower()
    
    
    # for time countdown
    time_elapsed = time.time() - start_time
    remaining_time = starting_time - int(time_elapsed)

    # conditions
    if len(guess) > 1 or guess == ' ':
        os.system('cls')
        print(" \n \n \n"
        f"                                       {remaining_time}s left. \n \n"
        "           Hey only 1 letter is allowed. Not 2 or more! AND no NUMBERS... DUMMY!!!")
    
        
    elif guess.isdigit() is True or len(guess) == 0:
        os.system('cls')
        guess = int()
        print(" \n \n \n"
        f"                                       {remaining_time}s left. \n \n"
        "                         That's not a letter. OMG! Go study KINDERGARTEN, DUMMY!!!")
        
    elif guess in guess_this_word:
        os.system('cls')
        if guess in guessed:
            print(" \n \n \n"
        f"                                       {remaining_time}s left. \n \n"
        f"                   BAAKKKAAAA!!! You already chose {guess} earlier. Try another one")
        else:
            print(" \n \n \n"
        f"                                       {remaining_time}s left. \n \n"
        "                                  Nice, another one...")

        guessed.extend([guess])
        result = [*guess_this_word]
        result2 = [*length_words]
        
        for index, word in enumerate(result):
            
            if index == len(result2):
                continue
            if word == guess:
                result2[index] = result[index]
                        
        guess_this_word = guess_this_word.replace(guess, "_")
        guess_this_word = "".join(result)
        length_words = "".join(result2)
    
    elif guess in keys_used:
        os.system('cls')
        print(" \n \n \n"
        f"                                       {remaining_time}s left. \n \n"
        f"                    BAAKKKAAAA!!! You already chose {guess} earlier. Try another one")
    # for wrong guesses
    else:
        
        count += 1
        
        if count == 1:
            os.system('cls')
            print(" \n \n \n"
            f"                                       {remaining_time}s left. \n \n"
            "                                 Wrong guess! Try again")
        
        elif count == 2:
            os.system('cls')
            print(" \n \n \n"
            f"                                       {remaining_time}s left. \n \n"
            "                                 Wrong guess!!! Again!")
        
        elif count == 3:
            os.system('cls')
            print(" \n \n \n"
            f"                                       {remaining_time}s left. \n \n"
            "                                 Wrong guess again!!!")
        
        elif count == 4:
            os.system('cls')
            print(" \n \n \n"
            f"                                       {remaining_time}s left. \n \n"
            "                        Wrong guess! YESSSS. ONE MORE AND YOU'RE DEAD\n"
            "                                      GO DIE YEAH!")
        elif count == 5:
            os.system('cls')
            print(" \n \n \n \n \n \n \n \n \n"
            f"{hang[5]}")
            pass

    #end of countdown
    end_time = time.time()
    time_taken = end_time - start_time        
    keys_used.extend([guess])        
    
    # end game conditions
    if length_words == guess_this_word or count == 5 or time_elapsed > starting_time:
        
        if length_words == guess_this_word:
            os.system('cls')
            print(" \n \n \n \n \n \n \n \n"
            "                                Congratulations!!! The WORD is \n \n",
            f"                                :  '{length_words}' \n \n" )
            print(f"                                  Your used time:   {int(time_taken)}")
            time.sleep(3)
                   
        elif count == 5:
            
            print(""
            f"                                Sorry, YOU'VE BEEN HANGED! \n \n")
            
            time.sleep(2)
            print(
            f"                            Your used time:   {int(time_taken)} \n \n ")
            time.sleep(2)
            print(f"                            The word was  :  '{guess_this_word}'")
            time.sleep(3)
                      
        elif time_elapsed > starting_time:
            os.system('cls')
            print(" \n \n \n \n \n \n \n \n"
            f"                     BOOOOOM PATAY KAAAAAA. PATAY SA KANYA YIIIIEEEE \n \n")
            time.sleep(2)
            print(" \n \n"
            f"                            Your used time:   {int(time_taken)} \n \n \n \n \n")
            time.sleep(2)
            print(f"                            The word was  :  '{guess_this_word}'")
            time.sleep(3)
            
        collection()
        replay = input(" \n \n \n  "
        "     Would you like to play again? y/n \033[1;37;40m\n \n ")   
        os.system('cls')
        
        # the game ender or the comeback
        if replay == 'y':
            
            collection()
        # if n, the game will exit, but I added some stuffs here. I can remove it later   
        elif replay == 'n':
            print(" \n \n \n")
            time.sleep(1)
            print("                                         ...\n \n")
            time.sleep(2)
            print("            TAMA YAN WAG KA NA BUMALIK, HINDI KA NAMAN NA NYA BABALIKAN. AHHH BUTI NGA...")
            time.sleep(8)
            print("The CODE is typing", end='')
            for char in "...":
                print(char, end="", flush=True)
                time.sleep(0.8)
            time.sleep(1)
            print()
            os.system('cls')
            print(" \n \n \n")
            print("                                         ...\n \n")
            print("            TAMA YAN WAG KA NA BUMALIK, HINDI KA NAMAN NA NYA BABALIKAN. AHHH BUTI NGA... \n \n")
            print("                 The CODE replies: HOY IKAW, HINDI AKO MADRAMA.")
            time.sleep(3)
            print("The CODE is typing", end='')
            for char in "...":
                print(char, end="", flush=True)
                time.sleep(0.8)
            time.sleep(1)
            print()
            os.system('cls')
            print(" \n \n \n")
            print("                                         ...\n \n")
            print("            TAMA YAN WAG KA NA BUMALIK, HINDI KA NAMAN NA NYA BABALIKAN. AHHH BUTI NGA... \n \n")
            print("                 The CODE replies: HOY IKAW, HINDI AKO MADRAMA.\n \n")
            print("                 The CODE replies: IKAW UNG NAGTYPE NIYAN, AKO PA SISISIHIN MO. BAHALA KA DYAN!\n \n \n")
            time.sleep(3)
            os.system('cls')
            print(" \n \n \n \n \n")
            print("                                            BLEH!!! ")
            time.sleep(2)
            
            print(" \n \n \n")
            print(
"                               \033[1;37m⠄  ⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄\n"
"                                ⠄  ⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄\n"
"                               ⠄ ⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄\n"
"                               ⠄ ⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄\n"
"                               ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰\n"
"                               ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤\n"
"                               ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗\n"
"                               ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄\n"
"                               ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄\n"
"                               ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆         ⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄\n"
"                               ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄\033[1;31m⣴⣿⣶⣄⠄⣴⣶⠄\033[1;37m⢀⣾⣿⣿⣿⣿⣿⣿⠃ ⠄\n"
"                               ⠄ ⠈⠻⣿⣿⣿⣿⣿⣿⡄\033[1;31m⢻⣿⣿⣿⠄⣿⣿⡀\033[1;37m⣾⣿⣿⣿⣿⣛⠛⠁  ⠄\n"
"                               ⠄   ⠈⠛⢿⣿⣿⣿⠁\033[1;31m⠞⢿⣿⣿⡄⢿⣿⡇\033[1;37m⣸⣿⣿⠿⠛⠁     ⠄\n"
"                               ⠄     ⠄⠉⠻⣿⣿⣾⣦\033[1;31m⡙⠻⣷⣾⣿⠃\033[1;37m⠿⠋⠁      ⢀⣠⣴\n"
"                               ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆\033[1;31m⣿⡿⠃\033[1;37m        ⣠⣴⣿⣿⣿\n"
)
            time.sleep(1)
            os.system('cls')
            print(" \n \n \n \n \n \n \n \n")
            exit()
        else:
            print(" \n \n \n \n \n \n \n \n  "
            "                        Sorry, the game will exit because you chose something that is not there. Thank you! \n \n \n \n \n \n \n \n \n \n")
            exit()
                        
    main_game()     
collection()                
main_game()
        
           
        




