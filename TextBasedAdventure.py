import time


def scene1():
    print("""Welcome to my adventure game!
    I think we shall start and get into the action.

    You awake within a dark and damp tavern, light muffled music fall onto your ear. The bard is still playing his 
    evening gig for the patrons. You hear your stomach growl, and then feel it. You are very hungry. As well as 
    tired. Do you get out of bed to get some food, or sleep for the rest of the night? 

    Type your choice: Stay or Leave?
     """)
    c1 = input()
    time.sleep(3)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print(
                "\nYou decided to stay in your bed, and let yourself enjoy the rest of the night to yourself. But you "
                "awoke to the smell of burning fire, and see that all around you is flames. Unable to escape, "
                "your perish "
                "in the fire.")
            ans = 'correct'
            print("\n\n")
            print("=================================YOU HAVE DIED=================================")
            print(" ================================= RESTARTING ================================")
            time.sleep(4)
            scene1()
        elif c1.upper() == "LEAVE":
            print(
                "You leave the room desiring to rid your self of your hungriness. You approach the bar maiden, "
                "and ask her for a plate of bread and soup. You wait until you get your food and begin to divulge into "
                "eating. ")
            ans = 'correct'
            scene2()
        else:
            print("ENTER THE RIGHT CHOICE! Stay or Leave? ")
            c1 = input()


def scene2():
    print("""
            While you were eating you noticed the bard start to look over at you while he was playing.
            After he was done, he approached you. He sat down at your table and asked you a question.
            'Do you know where the wild ones go?'. Confused you look at him, not answering his question.
            He then asked again, in a frustrated tone.

            Type your choice: Answer or Refuse?
    """)
    time.sleep(4)
    c1 = input()
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "ANSWER":
            print(
                """\nYou answer the bard's question. He starts to laugh, and gives you some relief from the tension. 
                He pats you on the back, and says to you "I would leave this place, it smells of burnt and rot. 
                Take the road north. And find me at my camp." The bard then left and gave you 5 gold pieces. 
                After you finished you wanted to go to bed, but were filled with a desire to scratch this curiosity.
                You left the tavern and head North up the road.
                """)
            time.sleep(4)
            print(
                """\nAfter walking up the road for some time, you found a traveling fortune teller. Her name was madam
                Eva. She gave you a tarot card, and said to keep it on you forever. You were given The Wheel of Fortune
                card.
                """)
            ans = 'correct'
            pick = "True"
        elif c1.upper() == 'REFUSE':
            print("""\nThe Bard grew angrier, after the 4th time of asking his question, he left. You finished eating
            and went to retire back into your bead. But there was something that was controlling you to move. You began
            to follow it. It lead you out of the tavern and down the road, until you meet a traveling fortune teller.
            She eagerly gave you a tarot card, and left without much word. you were given The Fool card.
            """)
            ans = 'correct'
            pick = "False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1 = input()
    time.sleep(3)
    scene3(pick)


def scene3(pick_value):
    print("""\n\nAfter receiving your card, you finally made your way to your destination. It was a camp filled with 
    musicians and actors. They were in the middle of dancing and singing, until one of them moved their way towards 
    you. It was the bard from the tavern. ) 
    """)
    time.sleep(3)
    if pick_value == "True":
        time.sleep(4)
        print("""He welcomed you with open arms. He said to you, "I knew you had a sense for adventure and curiosity. 
        I am Ricter the Ivory, a very famous bard throughout these lands. I am also a top student within a mages 
        guild titled the Mithril Academy. I noticed something about you. Something dark and terrible. Here talk with 
        me inside." """)
        time.sleep(4)
        print("""\n The Bard ushered you inside his tent. It was filled with baubles and trinkets around. In the back 
        of the tent was a mural of the bard, atop of a horse. He looked proud and happy to be there. Richter sat 
        down, and pointed for you to take a seat. He spoke thus, "There is something coming, specifically for you. 
        Whatever you have done in your life, you have not keep your tracks covered. But I am a very generous man, 
        who believes that those who have talent shall receive aid. You have it, talent. I believe this will be the 
        start of something great."
        """)
    elif pick_value == "False":
        print(""" The Bard moved you into his tent. He sat you down, and poured you a cup of tea. He spoke to you, "I am
        Richter the Ivory, I am famous around these lands, and search for talent everywhere I go. I think you were
        someone special. The problem was you didn't pass the test. You allowed your mind to be clouded and ruined it. 
        But I love to give out second chances. The other fact at hand, is there is something dark chasing you.
        Whatever you did before we meet, you must of not covered your tracks all to well. It chasing you, and wants to 
        end you. But I will help you. I believe this will be the start of something great." 
        """)


scene1()
print("\n\n")
print("=================================END OF CHAPTER 1=================================")


def CharacterScene1():
    time.sleep(3)
    print("""\n "Before we begin to work together I must know more about you, who you are, what your expertises is,stuff
    like that. Hopefully it wont take that long. First I am going to ask you what your Name is.
    """)
    time.sleep(2)
    name = input("Please Type in your Name: ")
    time.sleep(2)
    print("""\n Now that we have your name, I need to know what class are you. 
    A brute of a Warrior, wielding a sword and shield to slay your enemies and protect your allies. 
    Are you a Mage, studier of the arcane and wielder of magic. You wield powerful spells to disintegrate those who dare
    to call them selves your enemies.
    Or are you a ranger, waiting and stalking your enemies for the right time to strike. You would be very proficient in
    nature and tracking having a knack for stealth as well.

    Type your choice: Warrior, Mage, or Ranger?

    """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "WARRIOR":
            print("""\n"I knew I pegged you as a warrior. Your muscle definitely defines that. I know you must be a little
            under trained with your aspects of the warrior life. But don't worry I have a friend who can help with that.
            Go talk to Gorthug, he the brutish orc that was playing the flute when you came in. He'll get your gears into
            shape. Don't worry he shouldn't go to far."
            """)
            time.sleep(3)
            print("""\nYou left the tent and made your way to Gorthug. You approached him and saw that he was polishing
            his flute with a black wax. He looked up at you, "Your the stranger, What can I help you with Outsider?". You
            relay your interaction with Ricter, and you see his expression get excited. "Well I haven't had a sparring 
            opponent in a while. Let me go get my blade, and we will begin." You waited outside Gorthug's tent. A silent
            cold breeze started to form. It felt very nice, and a welcoming sight, until you started to smell burning wood.
            I confusion you look over and see a flame bigger then the sun itself. It spoke to you, in intangible words.
            Your eyes began to faze, and your vision went dark. Then everything went silent and still.
            """)
            ans = 'correct'
            Class = "Warrior"
        elif c1.upper() == "MAGE":
            print("""\n"Ahh, a mage. I am one myself. For many years I have studied the arts myself. I assume its been 
            awhile since you practiced the arts. Don't worry It shouldn't take long. Go ahead and create a small ball
            of light within the palm of your hand." Listing to Ricter, you began to concentrate and remember your 
            teachings. From the deep corners of your soul you begin to pull and manipulate the arcane layways. You feel
            the force begin to swell into a ball within your palm. The light begins to shine on both yours and Ricter's
            face. But you look deep into the ball, and see something ferocious. It looks back onto you, and hear it speak
            an intangible language. Your eyes begin to faze, and your vision went dark. Then everything went silent and still.
            """)
            ans = 'correct'
            Class = "Mage"
        elif c1.upper() == "RANGER":
            print("""\n"Interesting. I have only ever meet a few rangers in my life. One of them is my life long friend.
            Go find him out. He's North into the forest, hunting some boars for dinner." You left tent after giving a
            goodbye to Ricter. You headed north into the forest. You found some tracks that seemed to belong to a average
            height male. You followed it, till you heard a arrow fly pass your face.
                """)
            time.sleep(3)
            print("""\n "One more step friend and you'll find the next arrow in your crown." You relayed your information 
            about meeting Ricter to this mysterious man. "Oh, sorry about that then. Come help me with finding this singular
            that was roaming around here." You joined the man to hunt the remaining boars in the area. After some time 
            hunting with this man, he looked to you "Name is Eadwulf. Pristine game hunter, and personal catcher for the
            prince of the land. Its nice to meet you. I will take this game back to camp, you stay awhile and see if you
            can find anything else roaming." You acknowledged his request, and hunted till dawn came. But when the sun 
            arose, it was brighter and scarier than normal. It spoke to you with intangible voices. Your eyes began to
            faze, and your vision went dark. Then everything went silent and still.
            """)
            ans = 'correct'
            Class = "Ranger"
        else:
            print("ENTER THE RIGHT CHOICE! Stay or Leave? ")
            c1 = input()
    time.sleep(3)
    CharacterScene2(Class)


def CharacterScene2(Class_value):
    print("""\n\nYou awake from your dream, sweating profusely. Its been 5 years since you first started traveling with
    Ricter and his merry gang of musicians.
    """)
    time.sleep(2)
    if Class_value == "Warrior":
        time.sleep(2)
        print("This works for Warrior")
    elif Class_value == "Mage":
        time.sleep(2)
        print("This works for Mage")
    elif Class_value == "Ranger":
        time.sleep(2)
        print("This works for Ranger")


CharacterScene1()
print("\n\n")
print("=================================END OF CHAPTER 2=================================")
