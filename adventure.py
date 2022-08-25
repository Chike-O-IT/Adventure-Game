import time

name = input("What is your name? ")
print("Welcome", name, "to your grand adventure!!")
time.sleep(2)

answer = input("You come to a dirt road at the end and you can go left or right. Which way do you choose? ").lower()

if answer == "left":
    time.sleep(2)
    answer = input("You have now come to river. Enter walk to walk around it or swim to swim through it. ").lower()
    if answer == "walk":
        time.sleep(2)
        print("Along your walk, you encounter a bear eating honey. He hasn't noticed you yet.")
        time.sleep(2)
        answer = input("What do you? Enter hide or keep walking. ").lower()
        if answer == "hide":
            time.sleep(2)
            print("The bear finishes and walks away. You've survived!")
            time.sleep(2)
            print("The End")
        elif answer == "keep walking":
            time.sleep(2)
            print("The bear sees you. He immediately attacks you.")
            time.sleep(2)
            print("You got the bear's eye, but this only enrages the beast furthur.")
            time.sleep(2)
            print("You did not survive.....")
            time.sleep(2)
            print("The End")
    elif answer == "swim":
        time.sleep(2)
        print("The waves are rough but you've made it to the other side. You see a house in the distance. It looks like yours.")
        time.sleep(2)
        print("As you get closer, you see another figure in the distance.")
        time.sleep(2)
        print("It is your family. Welcoming you with open arms.")
        time.sleep(2)
        print("You are home.")
        time.sleep(2)
        print("The End")
    else:
        print("Not a valid option")

elif answer == "right":
    time.sleep(2)
    print("You are now at a bridge. Looks a little shaky, but you should be able to cross it.")
    time.sleep(2)
    print("However, you see tools nearby. This might take a while and the sun is going down.")
    time.sleep(2)
    answer = input("What do you do? Enter risk or fix. ").lower()
    if answer == "risk":
        time.sleep(2)
        print("You start crossing the bridge slowly.")
        time.sleep(2)
        print("A few boards fall away and you lose you balance, but quickly regain it.")
        time.sleep(2)
        print("You've crossed the bridge successfully!")
        time.sleep(2)
        print("You see your home and run to it.")
        time.sleep(2)
        print("You climb in bed. Goodnight.")
        time.sleep(2)
        print("The End")
    elif answer == "fix":
        time.sleep(2)
        print("You take the rest of the day to fix the bridge.")
        time.sleep(2)
        print("Exhaustion sets in and you camp out for the night")
        time.sleep(2)
        print("A group of bandits see your fire and decide to check it out.")
        time.sleep(2)
        print("You fight bravely, but the exhaustion from fixing the bridge has left you weak.")
        time.sleep(2)
        print("You did not survive....")
        time.sleep(2)
        print("The End")
    else:
        print("Not a valid option.")


else:
    print("Not a valid option.")