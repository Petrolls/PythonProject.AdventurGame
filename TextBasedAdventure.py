import time


def scene1():
    print("""Welcome to my adventure game!
    I think we shall start and get into the action.

    You awake within a dark and damp tavern, light muffled music fall onto 
    your ear. The bard is still playing his evening gig for the patrons. You 
    hear your stomach growl, and then feel it. You are very hungry. As well 
    as tired. Do you get out of bed to get some food, or sleep for the rest 
    of the night? 

    Type your choice: Stay or Leave?
     """)
    c1 = input()
    time.sleep(2.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print("""\nYou decided to stay in your bed, and let yourself 
            enjoy the rest of the night to yourself. But you awoke to the 
            smell of burning fire, and see that all around you is flames. 
            Unable to escape, your perish in the fire. 
            """)
            ans = 'correct'
            print("\n\n")
            print("====================YOU HAVE DIED=========================")
            print(" =================== RESTARTING ========================")
            time.sleep(2.5)
            scene1()
        elif c1.upper() == "LEAVE":
            print("""You leave the room desiring to rid your self of your 
            hungriness. You approach the bar maiden, and ask her for a plate 
            of bread and soup. You wait until you get your food and begin to 
            divulge into eating. 
            """)
            ans = 'correct'
            scene2()
        else:
            print("ENTER THE RIGHT CHOICE! Stay or Leave? ")
            c1 = input()


def scene2():
    time.sleep(2.5)
    print("""While you were eating you noticed the bard start to look over 
    at you while he was playing. After he was done, he approached you. He 
    sat down at your table and asked you a question. 'Do you know where the 
    wild ones go?'. Confused you look at him, not answering his question. He 
    then asked again, in a frustrated tone. 

    Type your choice: Answer or Refuse?
    """)
    time.sleep(2.5)
    c1 = input()
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "ANSWER":
            time.sleep(2.5)
            print("""\nYou answer the bard's question. He starts to laugh, 
            and gives you some relief from the tension. He pats you on the 
            back, and says to you "I would leave this place, it smells of 
            burnt and rot. Take the road north. And find me at my camp." The 
            bard then left and gave you 5 gold pieces. After you finished 
            you wanted to go to bed, but were filled with a desire to 
            scratch this curiosity. You left the tavern and head North up 
            the road. 
            """)
            time.sleep(2.5)
            print("""\nAfter walking up the road for some time, you found a 
            traveling fortune teller. Her name was madam Eva. She gave you a 
            tarot card, and said to keep it on you forever. You were given 
            The Wheel of Fortune card. 
            """)
            ans = 'correct'
            pick = "True"
        elif c1.upper() == 'REFUSE':
            time.sleep(2.5)
            print("""\nThe Bard grew angrier, after the 4th time of asking 
            his question, he left. You finished eating and went to retire 
            back into your bead. But there was something that was 
            controlling you to move. You began to follow it. It lead you out 
            of the tavern and down the road, until you meet a traveling 
            fortune teller. She eagerly gave you a tarot card, and left 
            without much word. you were given The Fool card. 
            """)
            ans = 'correct'
            pick = "False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1 = input()
    time.sleep(3)
    scene3(pick)


def scene3(pick_value):
    time.sleep(2.5)
    print("""\n\nAfter receiving your card, you finally made your way to 
    your destination. It was a camp filled with musicians and actors. They 
    were in the middle of dancing and singing, until one of them moved their 
    way towards you. It was the bard from the tavern. 
    """)
    time.sleep(2.5)
    if pick_value == "True":
        time.sleep(2.5)
        print("""\n\nHe welcomed you with open arms. He said to you, "I knew 
        you had a sense for adventure and curiosity. I am Ricter the Ivory, 
        a very famous bard throughout these lands. I am also a top student 
        within a mages guild titled the Mithril Academy. I noticed something 
        about you. Something dark and terrible. Here talk with me inside." 
        """)
        time.sleep(2.5)
        print("""\n\nThe Bard ushered you inside his tent. It was filled 
        with baubles and trinkets around. In the back of the tent was a 
        mural of the bard, atop of a horse. He looked proud and happy to be 
        there. Richter sat down, and pointed for you to take a seat. He 
        spoke thus, "There is something coming, specifically for you. 
        Whatever you have done in your life, you have not keep your tracks 
        covered. But I am a very generous man, who believes that those who 
        have talent shall receive aid. You have it, talent. I believe this 
        will be the start of something great." 
        """)
    elif pick_value == "False":
        print("""\nThe Bard moved you into his tent. He sat you down, 
        and poured you a cup of tea. He spoke to you, "I am Richter the 
        Ivory, I am famous around these lands, and search for talent 
        everywhere I go. I think you were someone special. The problem was 
        you didn't pass the test. You allowed your mind to be clouded and 
        ruined it. But I love to give out second chances. The other fact at 
        hand, is there is something dark chasing you. Whatever you did 
        before we meet, you must of not covered your tracks all to well. It 
        chasing you, and wants to end you. But I will help you. I believe 
        this will be the start of something great." 
        """)


def CharacterScene1():
    time.sleep(3)
    print("""\n"Before we begin to work together I must know more about you, 
    who you are, what your expertises is,stuff like that. Hopefully it wont 
    take that long. First I am going to ask you what your Name is. 
    """)
    time.sleep(2.5)
    input("Please Type in your Name: ")
    time.sleep(2.5)
    print("""\nNow that we have your name, I need to know what class are 
    you. A brute of a Warrior, wielding a sword and shield to slay your 
    enemies and protect your allies. Are you a Mage, studier of the arcane 
    and wielder of magic. You wield powerful spells to disintegrate those 
    who dare to call them selves your enemies. Or are you a ranger, waiting 
    and stalking your enemies for the right time to strike. You would be 
    very proficient in nature and tracking having a knack for stealth as well. 

    Type your choice: Warrior, Mage, or Ranger?

    """)
    c1 = input()
    time.sleep(2.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "WARRIOR":
            print("""\n"I knew I pegged you as a warrior. Your muscle 
            definitely defines that. I know you must be a little under 
            trained with your aspects of the warrior life. But don't worry I 
            have a friend who can help with that. Go talk to Gorthug, 
            he the brutish orc that was playing the flute when you came in. 
            He'll get your gears into shape. Don't worry he shouldn't go to 
            far." 
            """)
            time.sleep(2.5)
            print("""\nYou left the tent and made your way to Gorthug. You 
            approached him and saw that he was polishing his flute with a 
            black wax. He looked up at you, "Your the stranger, What can I 
            help you with Outsider?". You relay your interaction with 
            Ricter, and you see his expression get excited. "Well I haven't 
            had a sparring opponent in a while. Let me go get my blade, 
            and we will begin." You waited outside Gorthug's tent. A silent 
            cold breeze started to form. It felt very nice, and a welcoming 
            sight, until you started to smell burning wood. I confusion you 
            look over and see a flame bigger then the sun itself. It spoke 
            to you, in intangible words. Your eyes began to faze, and your 
            vision went dark. Then everything went silent and still. 
            """)
            ans = 'correct'
            Class = "Warrior"
        elif c1.upper() == "MAGE":
            print("""\n"Ahh, a mage. I am one myself. For many years I have 
            studied the arts myself. I assume its been awhile since you 
            practiced the arts. Don't worry It shouldn't take long. Go ahead 
            and create a small ball of light within the palm of your hand." 
            Listing to Ricter, you began to concentrate and remember your 
            teachings. From the deep corners of your soul you begin to pull 
            and manipulate the arcane layways. You feel the force begin to 
            swell into a ball within your palm. The light begins to shine on 
            both yours and Ricter's face. But you look deep into the ball, 
            and see something ferocious. It looks back onto you, and hear it 
            speak an intangible language. Your eyes begin to faze, and your 
            vision went dark. Then everything went silent and still. 
            """)
            ans = 'correct'
            Class = "Mage"
        elif c1.upper() == "RANGER":
            print("""\n"Interesting. I have only ever meet a few rangers in 
            my life. One of them is my life long friend. Go find him out. 
            He's North into the forest, hunting some boars for dinner." You 
            left tent after giving a goodbye to Ricter. You headed north 
            into the forest. You found some tracks that seemed to belong to 
            a average height male. You followed it, till you heard a arrow 
            fly pass your face. 
            """)
            time.sleep(2.5)
            print("""\n"One more step friend and you'll find the next arrow 
            in your crown." You relayed your information about meeting 
            Ricter to this mysterious man. "Oh, sorry about that then. Come 
            help me with finding this singular that was roaming around 
            here." You joined the man to hunt the remaining boars in the 
            area. After some time hunting with this man, he looked to you 
            "Name is Eadwulf. Pristine game hunter, and personal catcher for 
            the prince of the land. Its nice to meet you. I will take this 
            game back to camp, you stay awhile and see if you can find 
            anything else roaming." You acknowledged his request, and hunted 
            till dawn came. But when the sun arose, it was brighter and 
            scarier than normal. It spoke to you with intangible voices. 
            Your eyes began to faze, and your vision went dark. Then 
            everything went silent and still. 
            """)
            ans = 'correct'
            Class = "Ranger"
        else:
            print("INCORRECT! Type your choice: Warrior, Mage, or Ranger? ")
            c1 = input()
    time.sleep(2.5)
    CharacterScene2(Class)


def CharacterScene2(Class_value):
    print("""\n\nYou awake from your dream, sweating profusely. Its been 5 
    years since you first started traveling with Ricter and his merry gang 
    of musicians. 
    """)
    time.sleep(2.5)
    if Class_value == "Warrior":
        time.sleep(2.5)
        print("""\nThe air of the planes hit your face. Its a chill 
        afternoon, the sun slowly setting in the distance. You have just 
        finished a training session with your companion Gorthug. He went to 
        go some supper and drinks for the both of you about an hour ago. You 
        see someone off in the distance, coming towards you; about a mile 
        off. You quickly recognize it to be Gorthug. But there seems to be 4 
        or 5 other shadows flanking him. After watching them approach, 
        Gorthug extends his welcome towards you, "They are here for you, 
        they said they have something that can help you. Careful, they are 
        not the friendly type." Gorthug pointed towards a wound on his 
        chest, seems to be a stab wound. The party that followed Gorthug 
        approaches you. The one in the middle gestures at you, 
        "I am Alucard. I am looking for someone who is capable in with that 
        of slaying and fighting. I heard wind of your name, and decided to 
        try my luck. If you were to help us on are quest, you will be 
        greatly rewarded. I am hunting my father. He is an evil man who has 
        fallen even deeper into the dark. You must be familiar with his 
        name, Dracula. Will you Help". 

        Will you help Alucard on his quest: Yes or No?
        """)
        time.sleep(2.5)
        c1 = input()
        ans = 'incorrect'
        while ans == 'incorrect':
            if c1.upper() == "YES":
                time.sleep(2.5)
                print("""\nAlucard's eyes lit up with excitement. "Aw yes, 
                I knew you were a promising candidate. We have weapons and 
                gold to help. I assume you are very diverse with most weapon 
                types, we have a most powerful weapon for you. I call it the 
                morning star whip. It belonged to my friend years ago, 
                now it shall belong to you. We leave now, take your stuff 
                and lets go." You, entranced by his offer, go back to camp 
                and give your goodbyes to Gorthag. You gathered your 
                belongings and headed on the road with this new found group. 
                """)
            ans = 'correct'
            time.sleep(2.5)
            print("=====================END OF CHAPTER 2=====================")
            time.sleep(2.5)
            WarriorScene()
            if c1.upper() == "NO":
                time.sleep(2.5)
                print("""\n "That is a shame. I would leave this place as 
                quickly as you could. Dangers await, they only attack at 
                night. Trust my word." The man left with his group in a 
                hurry, none turning to look back at you. 


                Later that night, you were awoken to the sound of an 
                infernal growl. You were adjoined by a hugh behemoth of a 
                demon. Its jaw rang low, and its eyes were every fire red. 
                Gorthag had already awoken, and was in the mist of getting 
                you your weapon. The demon attack, but Gorthug was able to 
                stop it from killing you, by putting his body in its grasp. 
                Gorthug meet his end, but he tossed you your weapon. You 
                were beseech by rage and started to attack this monster. It 
                let go of Gorthug, and started to fight you. You were unable 
                to kill this demon, and in the end; You lost your life. 
                """)
                ans = 'correct'
                time.sleep(2)
                print("====================YOU HAVE DIED====================")
                time.sleep(2)
                print(" ================== RESTARTING ======================")
                time.sleep(2)
                CharacterScene2("Warrior")
    elif Class_value == "Mage":
        time.sleep(2)
        print("""\nYou are currently deep within a deep nordic ruins trying
        to find something called the "Arkenstone". It is said that the stone
        is filled with magic and energy that can catapult the world into 
        the next age. You decided to go alone on this journey, knowing
        you are very capable within your own experstise with magic.
        But you are at a crossroads deep within the cavern. Ahead of you
        is a small light about a mile deep, but there is a dark chamber that
        leads to your right, which you have no understanding where that
        leads too.

        Do you head North towards the light, or East into the dark?
        (Type North or East)
        """)
        time.sleep(2.5)
        c1 = input()
        ans = 'incorrect'
        while ans == 'incorrect':
            if c1.upper() == "EAST":
                time.sleep(2.5)
                print("""\nHeading down the East path, you are meet, with 
                damp mildew that reaches your nose. But after walking down
                this path for what seemed to be multiple hours, you are 
                approached with a silver lake, with the faintest hint of
                moonlight hitting it.

                There is a mound of land within the middle of this lake.
                And there rest a singular flower, that illuminates the chamber
                within.

                You beggin approaching the flower, and start to swim over. Once there
                the flower begings to enchant you. And you pluck it. But then bellows of
                roars fill the chamber. And a dragon, green reptilic skin meets your eyes.
                """)
            ans = 'correct'
            time.sleep(2.5)
            print("=====================END OF CHAPTER 2=====================")
            time.sleep(2.5)
            MageScene()
            if c1.upper() == "NORTH":
                time.sleep(2.5)
                print("""\nYou head towards the light, and see that it was a campfire.
                You begin to search around, and find out that there was someone here
                not long ago. As you begin to put the pieces together. You feel a blade
                on your neck a voice falls onto your ears, "So your thinking, why does
                this have to happen to me. Well wrong place wrong time buddy, cant trust
                a soul, even you. Goodbye".

                You feel a sharp pain and then a dark voids fall beneath you.
                """)
                ans = 'correct'
                time.sleep(2)
                print("====================YOU HAVE DIED====================")
                time.sleep(2)
                print(" ==================RESTARTING======================")
                time.sleep(2)
                CharacterScene2("Mage")
    elif Class_value == "Ranger":
        time.sleep(2)
        print("This works for Ranger")


def WarriorScene():
    time.sleep(2.5)
    print("""\nFor years, you and Alucard have been traveling the land 
    fighting the evil forces of Dracula. Recently you have made your way to 
    his castle, Ravenloft. Conjoined with the forces of Ritcher of Alucard, 
    you have pushed your way into his chambers. 
    """)
    time.sleep(2.5)
    print("""\nHere you face down the man himself, Dracula. A everlasting 
    gloom fills the space around you. A calm look from dracula, stares down 
    upon you. It is only you within his chamber. He shows his hands, daggers 
    form within his hand. He charges at you. 

    You are equipped with a shield, and the morning star whip.

    Do you attack or block?
    """)
    c1 = input()
    time.sleep(2.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "ATTACK":
            time.sleep(2.5)
            print("""\nYou whip the morning star at Dracula. He defects the 
            attack initially. But you pull down onto the whip allowing it to 
            strike Dracula within the chest. It seems to be fatal enough of 
            a blow, and he falls onto one knee. 
            """)
            time.sleep(2.5)
            print("""\nYou approach him, his calm face look up at you. 
            "Finish your destiny. Along have you awaited this. I have tried 
            at every corner to stop you, but it seems the mistress of fate 
            is cruel in her own way. But before you end my life, promise my 
            that you will tell Alucard of my last words. Tell him 'Your 
            mother lies east. Atop the ruby mountains.' That is all I have 
            to say, Good night Fel Slayer. 

            Do you kill or Spare Dracula?
            """)
            c1 = input()
            time.sleep(2.5)
            ans = 'incorrect'
            while ans == 'incorrect':
                if c1.upper() == "KILL":
                    print("""\nYou reel back the morning star whip and 
                    attack Dracula, ending him with a final blow. You see 
                    his body started to disperse into this black mist, 
                    until Richter rusher up behind you, and using fire magic 
                    to completely destroy the soul of Dracula. 

                    You two share a glance and he ask you "So, what will you 
                    do now." 
                    """)
                    time.sleep(2.5)
                    print("""\nYears pass, and you have been labeled the hero 
                    of the realm. Your deeds have landed you your own 
                    castle, and have started your own mercenary company. You 
                    and Gorthag continue to go onto adventures with each 
                    other. You have saved the day.
                    """)
                    ans = 'correct'
                    time.sleep(2.5)
                    print("=============YOU GOT THE GOOD ENDING==============")
                    time.sleep(2.5)
                    print("=============THANK YOU FOR PLAYING===============")
                    time.sleep(2.5)
                    print("===========RESTARTING FROM THE START=============")
                    time.sleep(2.5)
                    scene1()
                if c1.upper() == "SPARE":
                    print("""\nYou find pity in the man’s last words to you. 
                    You reel back the morning star, but you slack the line. 
                    Dracula stares at you. “You are a honorable man, 
                    but I am one of the dead’s chosen. Killing me would have 
                    been the right choice. I do take sorrow in what I am 
                    about to do." 

                    Dracula teleports behind you, and you feel the sharp 
                    pain of his teeth sink into your neck. You have been 
                    turned, now an undead servant for lord Dracula. At this 
                    time, both Alucard and Richter have made their way into 
                    the chamber of Dracula, and now his forever faithful 
                    servant. 

                    You are commanded to attack the two and do so without 
                    hesitation. You slay your old companions, standing over 
                    their bodies, you are the victor. 
                    """)
                    time.sleep(2.5)
                    print("""\nYears pass, and you have been the chosen 
                    champion of Lord Dracula. You have lead hordes of evil 
                    to take over the world. You stand at the top, but below 
                    your lord. You life is now his, forever commanded to do 
                    his bidding. 
                    """)
                    ans = 'correct'
                    time.sleep(2.5)
                    print("========YOU GOT THE BAD ENDING========")
                    time.sleep(2.5)
                    print("========THANK YOU FOR PLAYING=========")
                    time.sleep(2.5)
                    print("======RESTARTING FROM THE START=======")
                    time.sleep(2.5)
                    scene1()
        elif c1.upper() == 'BLOCK':
            time.sleep(2.5)
            print("""\nYou raise your silver crest blocking Dracula Attack. 
            He reels back in and strikes again. But your defense is strong. 
            You leverage another block, and have a shot to strike him. You 
            take the shot and it impales him. At the same time, both Alucard 
            and Richter flank you. They see you have struct him, and follow 
            up with you. Alucard uses his heirloom sword, and Richter use 
            his pyrokinesis. Together the three of you were able to slay and 
            destroy the soul of Dracula. 

            Alucard looks over at you, "Its over then. No more misery or 
            bloodshed, we have finally done it. I wish there was more to 
            help with my friend. But this is were we say our goodbyes.
            """)
            time.sleep(2.5)
            print("""\nYears pass, and you have been labeled the hero of the 
            realm. Your deeds have landed you your own castle, and have 
            started your own mercenary company. You and Gorthag continue to 
            go onto adventures with each other. You have saved the day.
            """)
            ans = 'correct'
            time.sleep(2.5)
            print(
                "==================YOU GOT THE GOOD ENDING==================")
            time.sleep(2.5)
            print(
                "====================THANK YOU FOR PLAYING===================")
            time.sleep(2.5)
            print(
                "==================RESTARTING FROM THE START=================")
            time.sleep(2.5)
            scene1()
        else:
            print("Wrong Input! Enter Attack or Block: ")
            c1 = input()


def MageScene():
    time.sleep(2.5)
    print("""\nThe Dragon looks down upon you, it chest bellowed up.
    "I AM ALAZATHOR, THE BREAKER OF CHAINS AND REDEMER OF HUMANITY.
    You have stumbled upon this chamber, what does thou seek?
    Answer with honest truth, for if you refuse, I will meet
    you with justice that I deemed worthy. Answer Mortal!"

    Do you Answer or Refuse?
    """)
    c1 = input()
    time.sleep(2.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "ANSWER":
            time.sleep(2.5)
            print("""\n"Ahh, looking for the Arkenstone, a mighty artifact.
            Only once has it been weilded by a mortal like yourself. An old
            dwarf king, he became made with power, and the source of his corruption
            was the stone its self. My internal question, will you be able to strike
            off this corruption. I have but one other question that you need to answer.
            For if one were to answer this right, they will achive the stone and bring
            greatness to this world. If one were to answer wrong, the stone they will recieve.
            But they will spread a great darkness around this world. A herald of pure chaos
            and death." 
            """)
            time.sleep(2.5)
            print("""\n"So now the Question. A long time ago, a farmer worked hard to maitain
            a peacful life for his family. He wasnt rich, but that didnt matter to him. He had
            love and was loved by those around him. But a king, made with power wanted his land. 
            It would be benefical for him, so he sent his army and murdered the family. The Farmer
            was out that night. He went to harvest some herbs. He found his dead family, and was broken
            will grief and rage."

            "He spent the next years plotting his vengence, and amassed a mighty group of heros
            and warriors that would fight for him. The farmer slew the king, and took his throne."

            "My question to you, was what he did the right course of action?"

            Answer his question, Yes or No: 
            """)
            c1 = input()
            time.sleep(2.5)
            ans = 'incorrect'
            while ans == 'incorrect':
                if c1.upper() == "YES":
                    print("""\n"Ah, you truly understand the world. That ever action has
                    a consequence. That no matter how lowely or mighty one is, that they will
                    meet their fate with the force of justice. You have proved yourself to wield
                    this stone with the might of a king. You will sheperd this world in its new age.
                    Take flight and remeber that you are a champion of Justice."

                    Alazathor raises it right claw, and manifest this glowing ehteral stone, of blue and purple stars.
                    He hands it to you, and with a bright flash, he dissapears. But the stone speaks to you.
                    And your able to learn all of its secrets.
                    """)
                    time.sleep(2.5)
                    print("""\nYears pass, and you have launched the world to the next age. You have become
                    supreme emperor of the lands, and have ammased countless citadels to promote peace and tranquility.
                    Everyone is happy, and you have made the world a better place.
                    """)
                    ans = 'correct'
                    time.sleep(2.5)
                    print("=============YOU GOT THE GOOD ENDING==============")
                    time.sleep(2.5)
                    print("=============THANK YOU FOR PLAYING===============")
                    time.sleep(2.5)
                    print("===========RESTARTING FROM THE START=============")
                    time.sleep(2.5)
                    scene1()
                if c1.upper() == "NO":
                    print("""\n"That saddens me. My your reign be ever short, and thou people be ever viligent."

                    Alazathor raises it right claw, and manifest this glowing ehteral stone, of blue and purple stars.
                    He hands it to you, and with a bright flash, he dissapears. But the stone speaks to you.
                    And your able to learn all of its secrets. 
                    """)
                    time.sleep(2.5)
                    print("""\nYears passed, and you have become the supreme tyrant of the lands. You have bent the knee, of
                    anyone who has resisted your rule. becoming mad with power, those who were closet with you, have turned.
                    Branding them traitors they fought against you. And in the end, you were the one who succumbed.
                    """)
                    ans = 'correct'
                    time.sleep(2.5)
                    print("========YOU GOT THE BAD ENDING========")
                    time.sleep(2.5)
                    print("========THANK YOU FOR PLAYING=========")
                    time.sleep(2.5)
                    print("======RESTARTING FROM THE START=======")
                    time.sleep(2.5)
                    scene1()
        elif c1.upper() == 'REFUSE':
            time.sleep(2.5)
            print("""\n"Interesting, I have not found a mortal to have gone against my will.
            Justice is a fickled thing, I have long been her champion for many milenia. You are
            free from her shackles i sense. I will make you my champion, and together we will free
            this world from Justice's prison.
            """)
            time.sleep(2.5)
            print("""\nAlazathor raises it right claw, and manifest this glowing ehteral stone, of blue and purple stars.
            He hands it to you, and with a bright flash. The stone speaks to you.And your able to learn all of its secrets.
            Alazathor takes you into his wing, and the two of you, use the power of the Arkenstone for the good of all humanity.

            You have become a demigod, serving the champion of Justice. With your powers you oversee the world, and step in
            when needed. You become hope for children and many men alike. Your name is whispered in the streets, as their silent savior.
            You have becomed legend, and your stories will never die.
            """)
            ans = 'correct'
            time.sleep(2.5)
            print(
                "==================YOU GOT THE GOOD ENDING==================")
            time.sleep(2.5)
            print(
                "====================THANK YOU FOR PLAYING===================")
            time.sleep(2.5)
            print(
                "==================RESTARTING FROM THE START=================")
            time.sleep(2.5)
            scene1()
        else:
            print("Wrong Input! Enter Answer or Refuse: ")
            c1 = input()


scene1()
print("\n\n")
print("=========================END OF CHAPTER 1=========================")

CharacterScene1()
