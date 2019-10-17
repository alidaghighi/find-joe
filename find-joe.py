


# class bcolors:
#     HEADER = "\033[95m"
#     OKBLUE = "\033[94m"
#     OKGREEN = "\033[92m"
#     WARNING = "\033[93m"
#     FAIL = "\033[91m"
#     ENDC = "\033[0m"
#     CLEAR = "\x1b[2J\x1b[H"

#     def disable(self):
#         self.HEADER = ""
#         self.OKBLUE = ""
#         self.OKGREEN = ""
#         self.WARNING = ""
#         self.FAIL = ""
#         self.ENDC = ""


# class FindJoe:
#     def __init__(self, load=None):
#         self.newGame = None
#         if load:
#             load_file = open(load)
#             loaded = load_file.read()
#             loaded = loaded.split("\n")
#             self.newGame = False
#             print(loaded)
#         else:
#             self.newGame = True





# ***
# Quick note: type the number or type your choice compeletly! (number is much easier! 
# ¯\_( ͡° ͜ʖ ͡°)_/¯)
# ***
import time
import sys
import random

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
CLEAR = '\x1b[2J\x1b[H'
SAVE_DIR = "."

cuts = None
ankle = None
sprainedWrist = None
inHouse = 0
inBathroom = 0
pee = 1
poop = 1

def typePrint(m):
    l = list(m)
    for i in range(0, len(l)):
        print(l[i], end='', flush=True)
        time.sleep(0.02)
    print()


def house():  # House
    global cuts
    global ankle
    global sprainedWrist
    global inHouse
    inHouse = 1

    typePrint("\nYou step into the hallway, ready for the day!")
    typePrint("You need to go downstairs and make some food.")
    time.sleep(1)
    while inHouse == 1:
        randomChance = random.randint(0, 10)
        typePrint("\nHow will you get down?\nSteps    Railing    Window")
        options = input()
        if options.upper() == "STEPS":
            typePrint("\nYou walk down the stairs.")
            kitchen()
        elif options.upper() == "RAILING":
            typePrint("You slide down the railing. Why not have a little fun?")
            time.sleep(0.8)
            typePrint("You've never done this before, and you don't know how.\n")
            time.sleep(1)
            if randomChance >= 5:
                typePrint("You slide down nicely, satisfied with your attempt.")
                kitchen()
            elif randomChance < 5:
                typePrint("You fall off of the railing and sprain your wrist.\n")
                time.sleep(2)
                typePrint("Great job.\n")
                time.sleep(1)
                typePrint("You walk to the kitchen, gritting your teeth to withstand the pain of your wrist.")
                sprainedWrist = 1
                kitchen()
        elif options.upper() == "WINDOW":
            typePrint("You walk up to the window.\nDive    Climb")
            options = input()
            if options.upper() == "DIVE":
                typePrint("\nYou rear up, getting ready to dive...")
                time.sleep(2)
                if randomChance >= 6:
                    typePrint("\nYou ace it! You break through the window and end on a roll from the two story drop.")
                    time.sleep(2.5)
                    typePrint("You look up at the broken window, realizing that it wasn't the best idea to do that.")
                    time.sleep(2)
                    typePrint("..Whatever.")
                    time.sleep(1)
                    typePrint("You enter the house from the back door, because you always forget to lock it.")
                    time.sleep(3)
                    kitchen()

                elif randomChance < 6:
                    typePrint("\nYou fail the dive, ending up with a lot of cuts on your skin from the broken glass.")
                    time.sleep(2.5)
                    typePrint("You writhe in pain on the ground for a bit, and then pick yourself up.")
                    time.sleep(2)
                    cuts = 1
                    typePrint("You enter the house from the back door, because you always forget to lock it.")
                    time.sleep(3)
                    kitchen()

            elif options.upper() == "CLIMB":
                typePrint("\nYou walk up to the window, release the lock, and open it.")
                time.sleep(0.8)
                typePrint("You start to climb out...")
                time.sleep(1)

                if randomChance >= 4:
                    typePrint("You safely climb down.")
                    time.sleep(0.7)
                    typePrint("You enter the house from the back door, because you always forget to lock it.")
                    time.sleep(1)
                    kitchen()

                if randomChance < 4:
                    typePrint("You slip and twist your ankle from the fall.")
                    time.sleep(1.2)
                    ankle = 1
                    typePrint("You hobble into the house from the back door, because you always forget to lock it.")
                    time.sleep(1)
                    kitchen()
            else:
                typePrint("Wrong move!\nTry again!")
        else:
            typePrint("Wrong move!\nTry again!")


def makeEgg():
    randomChances = random.randint(0, 10)
    global makeEggs
    makeEggs = 1
    global pan
    pan = 0
    global stove
    stove = 0
    global egg
    egg = 0
    global options
    while makeEggs == 1:
        typePrint("You want to make an egg. What do you need to do?\nEgg  -  Stove  -  Pan  -  Oil")
        options = input()

        if options.upper() == "EGG":

            if egg == 1 or egg == -1:

                typePrint("Pour the egg?\nYes    No")
                options = input()

                if options.upper() == "NO" and pan == 0:
                    typePrint("Right, you haven't put the pan on yet!")

                elif options.upper() == "YES" and pan == 0:
                    typePrint(
                        "You pour the egg on the stove. You forgot the pan. It seeps through the burner, and your egg is now ruined.")
                    makeEggs = 0
                

                elif options.upper() == "NO" and pan == 1:
                    typePrint("You don't pour the egg on the pan.")

                elif options.upper() == "YES" and pan == 1:
                    typePrint("You pour the egg on the pan.")
                else:
                    typePrint("Wrong move!\nTry again!")
                    continue
                if stove == 1:
                    typePrint("It sizzles and starts to coagulate.")



            elif egg == 0:
                typePrint("You attempt to crack the egg and pour it into a bowl...")
                time.sleep(2)
                if randomChances >= 4:
                    typePrint("You successfully crack the egg.")
                    time.sleep(1.5)
                    egg = 1


                elif randomChances < 4:
                    typePrint(
                        "You apply an excessive amount of force and slam the egg into the bowl.\nThere is now a bunch of egg shell mixed in with your egg.")
                    time.sleep(3)
                    egg = -1


        elif options.upper() == "STOVE":

            if stove == 1:
                typePrint("You turn the stove off")
                stove = 0

            elif stove == 0:
                typePrint("You turn the stove on")
                stove = 1


        elif options.upper() == "PAN":

            if pan == 1:
                typePrint("You take the pan off of the stove.")
                pan = 0

            elif pan == 0:
                typePrint("You place the pan on the stove.")
                pan = 1
        else:
            typePrint("Wrong move!\nTry again!")


def kitchen():  # Kitchen

    global randomChance
    randomChance = random.randint(0, 10)

    global makeBacon
    makeBacon = 1
    global makeToast
    makeToast = 1
    global makeCereal
    makeCereal = 1

    inKitchen = 1
    typePrint("You enter the kitchen.")
    time.sleep(1)
    while inKitchen == 1:
        typePrint("What should you eat?\nEgg    Bacon    Toast    Cereal")
        options = input()

        if options.upper() == "EGG":
            makeEgg()
        else:
            typePrint("I'm still working on story line! Till now you can just go with Egg!  ಠᴗಠ")


def bathroom():
    global inBathroom
    inBathroom = 1
    global pee
    global poop
    typePrint("\nYou step into the bathroom\n")
    while inBathroom == 1:
        time.sleep(1.5)
        typePrint(WARNING + "What you want to do?\nShower    Toilet    Sink    Door\n" + ENDC)
        options = input()
        if options.upper() == "SHOWER":
            typePrint("\nNow you are going to take a shower")
            time.sleep(1.5)
            typePrint("\n.")
            time.sleep(0.5)
            typePrint("\n.")
            time.sleep(0.5)
            typePrint("\n.")
            time.sleep(1.5)
            typePrint("\nUse your imagination about these moments!" + OKBLUE + "I can't describe it more for families sake!" + ENDC)
        elif options.upper() == "TOILET":
            time.sleep(1.5)
            typePrint(WARNING + "What you want to do?\nPee    Poop\n" + ENDC)
            options = input()
            if options.upper() == "POOP":
                if poop > 0:
                    time.sleep(2.5)
                    typePrint(OKGREEN + "     (   )  \n  (   ) (   \n   ) _   )  \n    ( \_    \n  _(_\ \)__ \n (____\___))" + ENDC)
                    time.sleep(1.5)
                    poop -= 1
                    typePrint("Done!")
                else:
                    typePrint("You need to eat something to poop!\nyou can't generate it out of nothing! ಠ_ಠ")
            elif options.upper() == "PEE":
                if pee > 0:
                    typePrint(OKGREEN + "        _  \n       ( } \n ====  /\\\\ \n |  | / /\\\\\n |__|_L_==n\n   L(   ) |\n    (___) L\n" + ENDC)
                    time.sleep(1.5)
                    pee -= 1
                    typePrint("Done! \nP.S. I did my best for these ASCII arts 	¯\_( ͡° ͜ʖ ͡°)_/¯")
                else:
                    typePrint("You need to drink something!\nyou can't generate it out of nothing! ಠ_ಠ")
            else:
                typePrint(FAIL + "Wrong move!\nTry again!" + ENDC)
        elif options.upper() == "SINK":
            typePrint(WARNING + "\nNow you are fron of the sink. \nYour options are...\nUse water    Use mirror" + ENDC)
            options = input()
            if options.upper() == "USE WATER":
                typePrint("\nNow you are using water tap to wash your hands!\nUse your imagination for sound ofwater •ᴗ•")
                time.sleep(2.5)
            elif options.upper() == "USE MIRROR":
                typePrint("\nYou are looking at your face and wondering...\n")
                time.sleep(0.5)
                typePrint(FAIL + "WHAT" + ENDC)
                time.sleep(0.5)
                typePrint(FAIL + "THE" + ENDC)
                time.sleep(0.5)
                typePrint(FAIL + "HELL!" + ENDC)
                time.sleep(2.5)
                typePrint(OKBLUE + "⊂_ヽ \n　 ＼＼ \n　 ＼＼ \n　　 ＼( ͡° ͜ʖ ͡°) \n　　　 >　⌒ヽ \n　　　/ 　 へ＼ \n　　 /　　/　＼＼ \n 　　 ﾚ　ノ　　 ヽ_つ \n　　/　/ \n　 /　/| \n　(　(ヽ \n　|　|、＼ \n　| 丿 ＼ ⌒) \n　| |　　) / \nノ )　　Lﾉ \n(_／ \n" + ENDC)
                time.sleep(2.5)
            else:
                typePrint(FAIL + "Wrong move!\nTry again!" + ENDC)
        elif options.upper() == "DOOR":
            inBathroom = 0
            typePrint("You are going back to the bedroom")
            bedroom()
        else:
            typePrint(FAIL + "Wrong move!\nTry again!" + ENDC)

def bedroom():  # Bedroom
    global sleptIn
    sleptIn = 0
    inBedroom = 1
    global wearSuit
    wearSuit = 0
    global wearPajamas
    wearPajamas = 0
    global wearDenim
    wearDenim = 0
    global wearNothing
    wearNothing = 0
    global windowOpen
    windowOpen = 0

    while inBedroom == 1:
        time.sleep(1.5)
        typePrint(WARNING + "\nYour options are...\nCloset    Bed    Window    Bathroom    Door" + ENDC)
        options = input()

        if options.upper() == "CLOSET":  # Bedroom Closet
            typePrint("\nYou head over to your walk-in closet." + WARNING + "Should you get dressed?\nYes    No" + ENDC)
            options = input()

            if options.upper() == "YES":
                typePrint(WARNING + "\nWhat should you wear?\nSuit    Pajamas    Denim" + ENDC)
                options = input()

                if options.upper() == "SUIT":
                    typePrint("\nYou're feeling fancy, so you put on your favorite suit and tie.")
                    wearSuit = 1
                    wearPajamas = 0
                    wearDenim = 0
                    wearNothing = 0

                elif options.upper() == "PAJAMAS":
                    typePrint("\nYou're feeling lazy, so you put on some loose pajamas.")
                    wearSuit = 0
                    wearPajamas = 1
                    wearDenim = 0
                    wearNothing = 0

                elif options.upper() == "DENIM":
                    typePrint("\nYou're feeling ordinary, so you put on some jeans and a shirt.")
                    wearSuit = 0
                    wearPajamas = 0
                    wearDenim = 1
                    wearNothing = 0

            elif options.upper() == "NO":

                if wearSuit == 0 and wearPajamas == 0 and wearDenim == 0:
                    typePrint("You walk out of the closet, wearing nothing but your underwear.")
                    wearNothing = 1

                elif wearNothing == 0:
                    typePrint("You walk out of the closet.")
        



        elif options.upper() == "BED":  # Bedroom Bed
            typePrint(WARNING + "\nYou go back to bed. Sleep?\nYes    No" + ENDC)
            options = input()

            if options.upper() == "YES":

                def sleeping():
                    time.sleep(2)
                    typePrint(".")
                    time.sleep(0.7)
                    typePrint(".")
                    time.sleep(0.7)
                    typePrint(".\n")
                    time.sleep(1.5)

                if sleptIn == 0:
                    typePrint("You go back to bed.")
                    sleeping()
                    typePrint("You wake up a couple of hours later.")
                    sleptIn = 1

                elif sleptIn == 1:
                    typePrint("You lie in bed, but fail to fall asleep.")

                elif sleptIn == -1:
                    typePrint("Despite refusing earlier, you decide to sleep. Just a little nap...")
                    sleeping()
                    typePrint("You wake up a couple of hours later.")
                    sleptIn = 1
            elif options.upper() == "NO":

                if sleptIn == 0:
                    typePrint("You probably shouldn't sleep, as tempting as it looks.")
                    sleptIn = -1
                elif sleptIn == 1:
                    typePrint("You decide not to. You've already slept enough, better not waste time!")



        elif options.upper() == "WINDOW":  # Bedroom Window

            if windowOpen == 0:

                typePrint(WARNING + "\nYou walk to the window. Open it?\nYes    No" + ENDC)
                options = input()

                if options.upper() == "YES":
                    typePrint("You decide to let the cool breeze in.")
                    windowOpen = 1

                elif options.upper() == "NO":
                    typePrint("You leave it closed.")
                    windowOpen = 0


            elif windowOpen == 1:
                typePrint(WARNING + "\nYou walk to the opened window. Close it?\nYes    No" + ENDC)
                options = input()
                if options.upper() == "YES":
                    typePrint("You regret your decision to open the window, and close it.")
                    windowOpen = -1

                elif options.upper() == "NO":
                    typePrint("You leave it open.")


            elif windowOpen == -1:
                typePrint(WARNING + "\nYou walk to the closed window. Re-open it?\nYes    No" + ENDC)
                options = input()
                if options.upper() == "YES":
                    typePrint("\nYou re-open the window, welcoming the breeze back in.")
                    windowOpen = 1

                elif options.upper() == "NO":
                    typePrint("\nYou leave it closed.")


        elif options.upper() == "DOOR":  # Bedroom Door
            typePrint(WARNING + "\nExit your room?\nYes    No" + ENDC)
            options = input()

            if options.upper() == "YES":
                inBedroom = 0
                house()

            elif options.upper().lower == "NO":
                typePrint("\nYou take some more time to get ready for the day.")
        
        elif options.upper() == "BATHROOM":  # Bedroom Door
            inBedroom = 0
            bathroom()

        else:
            typePrint(FAIL + "Wrong move!\nTry again!" + ENDC)
        
        


# Prologue
typePrint(
        """
  ______ _____ _   _ _____         _  ____  ______ 
 |  ____|_   _| \ | |  __ \       | |/ __ \|  ____|
 | |__    | | |  \| | |  | |      | | |  | | |__   
 |  __|   | | | . ` | |  | |  _   | | |  | |  __|  
 | |     _| |_| |\  | |__| | | |__| | |__| | |____ 
 |_|    |_____|_| \_|_____/   \____/ \____/|______|
        """
        )
time.sleep(2)
typePrint("To pick options, type the word. Ignore parentheses.\n")
time.sleep(2)
# typePrint(WARNING + "Continue[Yes]?\nYes    No\n" + ENDC)

typePrint(
            """
        1. New Game
        2. Load (Not working so don't try)
        3. Help (Maybe later)
        3. Credit (Oh come on!)
        4. Exit
        """
        )
options = input()
if options.lower() == "exit":
    typePrint(FAIL + "Shutting down." + ENDC)
    time.sleep(0.5)
    typePrint(FAIL + "." + ENDC)
    time.sleep(0.5)    
    typePrint(FAIL + "." + ENDC)
    time.sleep(0.5)    
    typePrint(FAIL + "." + ENDC)
    time.sleep(0.5)    
    typePrint(FAIL + "." + ENDC)
    time.sleep(0.5)    
    typePrint(FAIL + "." + ENDC)
    time.sleep(0.5)
    print(CLEAR) 
    exit(0)


time.sleep(2)
print("\n\n\n")
typePrint("This game is a comedy text-based adventure, based on the Loss comic. Yep, it's that bad.\n")
time.sleep(2)
typePrint(FAIL + "Your actions actually do have consequences.\n" + ENDC)
typePrint("You wake up in a bed, not knowing where or who you are...\n")
time.sleep(2.5)
typePrint("You slowly raise yourself out of bed.\n")
time.sleep(2)
bedroom()
