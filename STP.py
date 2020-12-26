#
#!0 -> steen
#!1 -> papier
#!2 -> schaar

#!ALERT, voordat we beginnen wil ik eerst bij nadrukken dat de random import nodig zal-
#!zijn voor de randomiser methode en de time import gaan gebruiken voor een paar seconden pauze zodat hij niet- 
#!de while loop als een spam alles uitprint maar tussen pauzes neemt
#geimporteerde items die we later gebruiken in onze code
import random
import time

#variable voor speler een input en speler 2 word auto "Bot"
AssignOne = input("Player one is: ")
PlayerOne =  AssignOne
PlayerTwo = "Bot"

#variable voor aantal gewonnen rondes die worden dus automatisch naar een 0 gezet
WinsHuman = 0
WinsBot = 0

#variable voor keuzes die ik later ga gebruiken voor tekst opmaak #!(Deze variables hoefden niet toegevoegd te worden maar ik wilde het zo gebruiken)
schaar = "Scissors"
steen = "Rock"
papier = "Paper"

#de spelers worden hier geprint in de console zodat de persoon die de code runt ziet wie er allemaal spelen
print("=========================================")
print("Players: " + PlayerOne + ", " + PlayerTwo)
print("=========================================")

#While loop gaat loopen door de keuzes tot dat er iemand 5 keer heeft gewonnen en dan stop de while loop
while WinsBot < 5 and WinsHuman < 5:

    #hier word de randomizer methode ingevoerd en helemaal bovenaan zie je welke getal welke voorwerop inhoudt
    KeuzeHuman = random.randint(0,2)
    KeuzeBot = random.randint(0,2)

    #elke combinatie worden hier na gecheckt dus als de randomizer een 
    # 1, 1 als keuze heeft geraakt dan gaat hij de hele while loop doorheen tot 
    # dat hij de if statement van 1, 1 heeft gevonden
    if KeuzeHuman == 2:
        if KeuzeBot == 2:
            print (PlayerOne + " chose, " + schaar)
            print (PlayerTwo + " chose, " + schaar)
            print("Both of you have scissors. It's a tie")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 1:
            print (PlayerOne + " chose, " + schaar)
            print (PlayerTwo + " chose, " + papier)
            WinsHuman = WinsHuman + 1
            print (PlayerOne + ", won this round. He has won",WinsHuman, "rounds")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 0:
            print (PlayerOne + " chose, " + schaar)
            print (PlayerTwo + " chose, " + steen)
            WinsBot = WinsBot + 1
            print (PlayerTwo + ", won this round. He has won",WinsBot, "rounds")
            print("======================================")
            time.sleep(4)

    elif KeuzeHuman == 1:
        if KeuzeBot == 2:
            print (PlayerOne + " chose, " + papier)
            print (PlayerTwo + " chose, " + schaar)
            WinsBot = WinsBot + 1
            print (PlayerTwo + ", won this round. He has won",WinsBot, "rounds")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 1:
            print (PlayerOne + " chose, " + papier)
            print (PlayerTwo + " chose, " + papier)
            print("Both of you have paper. It's a tie")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 0:
            print (PlayerOne + " chose, " + papier)
            print (PlayerTwo + " chose, " + steen)
            WinsHuman = WinsHuman + 1
            print (PlayerOne + ", won this round. He has won",WinsHuman, "rounds")
            print("======================================")
            time.sleep(4)

    elif KeuzeHuman == 0:
        if KeuzeBot == 2:
            print (PlayerOne + " chose, " + steen)
            print (PlayerTwo + " chose, " + schaar)
            WinsHuman = WinsHuman + 1
            print (PlayerOne + ", won this round. He has won",WinsHuman, "rounds")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 1:
            print(PlayerOne + " chose, " + steen)
            print(PlayerTwo + " chose, " + papier)
            WinsBot = WinsBot + 1
            print (PlayerTwo + ", won this round. He has won",WinsBot, "rounds")
            print("======================================")
            time.sleep(4)

        elif KeuzeBot == 0:
            print (PlayerOne + " chose, " + steen)
            print (PlayerTwo + " chose, " + steen)
            print("Both of you have stone. It's a tie")
            print("======================================")
            time.sleep(4)

if WinsHuman > WinsBot:
    print(PlayerOne + ", has won " ,WinsHuman, " rounds " + "vs" ,WinsBot)

elif WinsBot > WinsHuman:
    print(PlayerTwo + ", has won " ,WinsBot, " rounds " + "vs" ,WinsHuman)


#?print(random.randint(1, 3))