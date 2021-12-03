__author = 'Ethan Franklin'
import time
#Im importing the time function to use as a way to delay messages.

def scene1():
#We define the first scene
    print("""
    Welcome to my adventure game!
    I think we shall start and get into the action.

    You awake within a dark and damp tavern, light muffled music fall onto 
    your ear. The bard is still playing his evening gig for the patrons. You 
    hear your stomach growl, and then feel it. You are very hungry. As well 
    as tired. Do you get out of bed to get some food, or sleep for the rest 
    of the night? 

    Type your choice: Stay or Leave?
     """)
    c1 = input()
    #We assign c1 to our input for our print message above
    time.sleep(2.5)
    #Time function delaying operation from instantly happening
    ans = 'incorrect'
    #We set "ans" to incorrect to start the while loop
    while ans == 'incorrect':
    #while loop starts
        if c1.upper() == "STAY":
        #If innput is any array of "STAY" it runs the statement
            print("""\n
            You decided to stay in your bed, and let yourself 
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
            #Now we load the first scene again, restarting it from the top, so we dont have to keep re-running the program.
        elif c1.upper() == "LEAVE":
        #If innput is any array of "LEAVE" it runs the statement
            print("""\n
            You leave the room desiring to rid your self of your 
            hungriness. You approach the bar maiden, and ask her for a plate 
            of bread and soup. You wait until you get your food and begin to 
            divulge into eating.
            """)
            ans = 'correct'
            scene2()
            #Now we load scene two, because we had the right choice.
        else:
            print("ENTER THE RIGHT CHOICE! Stay or Leave? ")
            c1 = input()
        #Here it will re run the while loop if anything other then Stay or Leave is typed.


def scene2():
    time.sleep(2.5)
    print("""\n
    While you were eating you noticed the bard start to look over 
    at you while he was playing. After he was done, he approached you. He 
    sat down at your table and asked you a question. 'Do you know where the 
    wild ones go?'. Confused you look at him, not answering his question. He 
    then asked again, in a frustrated tone. 

    Type your choice: Answer or Refuse?
    """)
    time.sleep(2.5)
    c1 = input()
    #We assign c1 to our input for our print message above
    ans = 'incorrect'
    #Start the While Loop
    while ans == 'incorrect':
        if c1.upper() == "ANSWER":
            time.sleep(2.5)
            print("""\n
            You answer the bard's question. He starts to laugh, 
            and gives you some relief from the tension. He pats you on the 
            back, and says to you "I would leave this place, it smells of 
            burnt and rot. Take the road north. And find me at my camp." The 
            bard then left and gave you 5 gold pieces. After you finished 
            you wanted to go to bed, but were filled with a desire to 
            scratch this curiosity. You left the tavern and head North up 
            the road. 
            """)
            time.sleep(2.5)
            print("""\n
            After walking up the road for some time, you found a 
            traveling fortune teller. Her name was madam Eva. She gave you a 
            tarot card, and said to keep it on you forever. You were given 
            The Wheel of Fortune card. 
            """)
            ans = 'correct'
            pick = "True"
            #Here we assign a value which we will call later on the next scene def.
        elif c1.upper() == 'REFUSE':
            time.sleep(2.5)
            print("""\n
            The Bard grew angrier, after the 4th time of asking 
            his question, he left. You finished eating and went to retire 
            back into your bead. But there was something that was 
            controlling you to move. You began to follow it. It lead you out 
            of the tavern and down the road, until you meet a traveling 
            fortune teller. She eagerly gave you a tarot card, and left 
            without much word. you were given The Fool card. 
            """)
            ans = 'correct'
            pick = "False"
            #Here we assign a value which we will call later on the next scene def.
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1 = input()
        #Here it will re run the while loop if anything other then Stay or Leave is typed.
    time.sleep(3)
    scene3(pick)
    #Now we run our scene with the inner function set.


def scene3(pick_value):
    time.sleep(2.5)
    print("""\n
    After receiving your card, you finally made your way to 
    your destination. It was a camp filled with musicians and actors. They 
    were in the middle of dancing and singing, until one of them moved their 
    way towards you. It was the bard from the tavern. 
    """)
    time.sleep(2.5)
    if pick_value == "True":
    #Here we load the value we assigned in the earlier scene
        time.sleep(2.5)
        print("""\n
        He welcomed you with open arms. He said to you, "I knew 
        you had a sense for adventure and curiosity. I am Ricter the Ivory, 
        a very famous bard throughout these lands. I am also a top student 
        within a mages guild titled the Mithril Academy. I noticed something 
        about you. Something dark and terrible. Here talk with me inside." 
        """)
        time.sleep(2.5)
        print("""\n
        The Bard ushered you inside his tent. It was filled 
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
    #Here we load the value we assigned in the earlier scene
        print("""\n
        The Bard moved you into his tent. He sat you down, 
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
    time.sleep(2.5)
    print("========END OF CHAPTER 1========")
    CharacterScene1()
    #Now we load the next scene, because we had the right choice.


def CharacterScene1():
    time.sleep(2.5)
    print("""\n
    "Before we begin to work together I must know more about you, 
    who you are, what your expertises is, stuff like that. Hopefully it wont 
    take that long. First I am going to ask you what your Name is. 
    """)
    time.sleep(2.5)
    input("Please Type in your Name: ")
    time.sleep(2.5)
    print("""\n
    Now that we have your name, I need to know what class are 
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
    #In this while loop, we are asking for multiple variables, in which we will call onto later
        if c1.upper() == "WARRIOR":
            print("""\n
            "I knew I pegged you as a warrior. Your muscle 
            definitely defines that. I know you must be a little under 
            trained with your aspects of the warrior life. But don't worry I 
            have a friend who can help with that. Go talk to Gorthug, 
            he the brutish orc that was playing the flute when you came in. 
            He'll get your gears into shape. Don't worry he shouldn't go to 
            far." 
            """)
            time.sleep(2.5)
            print("""\n
            You left the tent and made your way to Gorthug. You 
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
            #Setting up the Variable
        elif c1.upper() == "MAGE":
            print("""\n
            "Ahh, a mage. I am one myself. For many years I have 
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
            #Setting up the Variable.
        elif c1.upper() == "RANGER":
            print("""\n
            "Interesting. I have only ever meet a few rangers in 
            my life. One of them is my life long friend. Go find him out. 
            He's North into the forest, hunting some boars for dinner." You 
            left tent after giving a goodbye to Ricter. You headed north 
            into the forest. You found some tracks that seemed to belong to 
            a average height male. You followed it, till you heard a arrow 
            fly pass your face. 
            """)
            time.sleep(2.5)
            print("""\n
            "One more step friend and you'll find the next arrow 
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
            #Setting up the Variable.
        else:
            print("INCORRECT! Type your choice: Warrior, Mage, or Ranger? ")
            c1 = input()
        #Here it will re run the while loop if anything other then Stay or Leave is typed.
    time.sleep(2.5)
    CharacterScene2(Class)
    #We load our next def scene with the inner function class, which we just defined.


def CharacterScene2(Class_value):
    print("""\n
    You awake from your dream, sweating profusely. Its been 5 
    years since your first encounter with Ricter and his merry gang 
    of musicians. 
    """)
    time.sleep(2.5)
    if Class_value == "Warrior":
    #Here we load the "Warrior" Class value.
        time.sleep(2.5)
        print("""\n
        The air of the planes hit your face. Its a chill 
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
        #Now we set up a while loop in side the if loop.
            if c1.upper() == "YES":
                time.sleep(2.5)
                print("""\n
                Alucard's eyes lit up with excitement. "Aw yes, 
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
                print("===================END OF CHAPTER 2===================")
                time.sleep(2.5)
                WarriorScene()
                #Now We load the Warrior Scene
            elif c1.upper() == "NO":
                time.sleep(2.5)
                print("""\n
                "That is a shame. I would leave this place as 
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
                #Here we load back the same scene back to the warrior value
            else:
                print("INCORRECT! Type your choice: Warrior, Mage, or Ranger?")
                c1 = input()
            #Here it will re run the while loop if anything other then Stay or Leave is typed
    elif Class_value == "Mage":
    #Here we load the "Mage" Class value
        time.sleep(2)
        print("""\n
        You are currently deep within a deep nordic ruins trying
        to find something called the "Arkenstone". It is said that the stone
        is filled with magic and energy that can catapult the world into 
        the next age. You decided to go alone on this journey, knowing
        you are very capable within your own expertise with magic.
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
                print("""\n
                Heading down the East path, you are meet, with 
                damp mildew that reaches your nose. But after walking down
                this path for what seemed to be multiple hours, you are 
                approached with a silver lake, with the faintest hint of
                moonlight hitting it.

                There is a mound of land within the middle of this lake.
                And there rest a singular flower, that illuminates the chamber
                within.

                You begin approaching the flower, and start to swim over. 
                Once there the flower begins to enchant you. And you pluck 
                it. But then bellows of roars fill the chamber. And a 
                dragon, green reptilian skin meets your eyes. 
                """)
                ans = 'correct'
                time.sleep(2.5)
                print("==================END OF CHAPTER 2==================")
                time.sleep(2.5)
                MageScene()
                #Now we load the Mage scene
            elif c1.upper() == "NORTH":
                time.sleep(2.5)
                print("""\n
                You head towards the light, and see that it was a 
                campfire. You begin to search around, and find out that 
                there was someone here not long ago. As you begin to put the 
                pieces together. You feel a blade on your neck a voice falls 
                onto your ears, "So your thinking, why does this have to 
                happen to me. Well wrong place wrong time buddy, cant trust 
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
                #Here we load back the same scene back to the warrior value
            else:
                print("INCORRECT! Type your choice: Warrior, Mage, or Ranger?")
                c1 = input()
            #Here it will re run the while loop if anything other then Stay or Leave is typed.
    elif Class_value == "Ranger":
    #Now we load the Ranger Class value.
        time.sleep(2)
        print("""\n
        The sea breeze hits your nose, and the distance sound of
        seagulls fall down on your ear. The boat your on begins to rock.
        Used to the sway, you avoid the sickness. You have been traveling
        with captain Hugo for some time with your friend Ulysses. As you scan
        around the top deck you see Ulysses comes up from behind you.
        "Hey, captain wants to know if you'll stay guard tonight. Joseph,
        got some scurry and wont be able to stand up for some time. It'll
        mean a lot to him."

        Do you take Joseph Night watch? (Type Yes or No)
        """)
        time.sleep(2.5)
        c1 = input()
        ans = 'incorrect'
        while ans == 'incorrect':
            if c1.upper() == "YES":
                time.sleep(2.5)
                print("""\n
                "Thank you. Captain has been very paranoid 
                recently. Talks of mutiny are coming from the Revelry. The 
                plank king is said to want the head of hugo. But hopefully 
                these are rumours. Still you see anything strange tonight, 
                don't hesitate to act upon it." 

                You go ahead and situate yourself to oversee the boat 
                tonight. You are stationed within the Reverly, a "Capital" 
                of sorts. Its a den of thieves and pirates, but it has been 
                home to you and Ulysses for some time. The lord of the 
                reverly, The Plank King; Is a scary individual. He has shown 
                to have a stern and easy-to-provoke attitude. There has 
                been talks of a mutiny against your captain, and rumours are 
                the Plank king wants him dead himself. 

                As your thoughts are combining in your head. You begin to 
                look around. Closer to midnight, you hear it first before 
                you see it. But a group of 5 cloaked individuals have been 
                moving 3 barrels onto the ship deck. Then they light a 
                match, but before they are able to exploded the gunpowder 
                barrels, you shoot their hands in quick retaliation. 

                They begin to run away, but not before they start to yell 
                out loud. Lights come down deep from the reverly. Cannon 
                shots, and a mob of pirates approach. The sound has awoken 
                the crew that you belong too. And Ulysses comes bering bad 
                news, "Assassins killed Captain, tried to stop it. Was too 
                slow. But its true, this is the Plank King's doing. Im not 
                leaving till he is dead." 

                Agreeing with your friend, the two of you gather the rest of 
                the crews, and begin to counter the forces of the plank 
                king. 
                """)
                ans = 'correct'
                time.sleep(2.5)
                print("==================END OF CHAPTER 2==================")
                time.sleep(2.5)
                RangerScene()
                #We now load the Ranger Scene
            elif c1.upper() == "NO":
                time.sleep(2.5)
                print("""\n
                "Well that is a shame. Ill find someone else. Its 
                getting a little late, why don't you get some rest. Were 
                gonna need you tomorrow." 

                You listen to your friends word, and get go and get some 
                rest for the night. Sleep comes easy to you. Its been 
                sometime since you been on the boat, and your eyes begin to 
                feel very. As your sleep takes you, you see a vision of a 
                bright light. Until minutes later you awaken to the sound of 
                an explosion. And a flaming bar of wood hits you. It ends up 
                pinning you down, unable to move. You see the water level 
                begin to rise, until it succumbs you within it. You drift 
                into the void. Until your life leaves your body. 
                """)
                ans = 'correct'
                time.sleep(2)
                print("====================YOU HAVE DIED====================")
                time.sleep(2)
                print(" ==================RESTARTING======================")
                time.sleep(2)
                CharacterScene2("Ranger")
                #Here we load back the same scene back to the ranger value
            else:
                print("INCORRECT! Type your choice: Warrior, Mage, or Ranger?")
                c1 = input()
            #Here it will re run the while loop if anything other then Stay or Leave is typed.

def WarriorScene():
    time.sleep(2.5)
    print("""\n
    For years, you and Alucard have been traveling the land 
    fighting the evil forces of Dracula. Recently you have made your way to 
    his castle, Ravenloft. Conjoined with the forces of Ritcher of Alucard, 
    you have pushed your way into his chambers. 
    """)
    time.sleep(2.5)
    print("""\n
    Here you face down the man himself, Dracula. A everlasting 
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
            print("""\n
            You whip the morning star at Dracula. He defects the 
            attack initially. But you pull down onto the whip allowing it to 
            strike Dracula within the chest. It seems to be fatal enough of 
            a blow, and he falls onto one knee. 
            """)
            time.sleep(2.5)
            print("""\n
            You approach him, his calm face look up at you. 
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
                    print("""\n
                    You reel back the morning star whip and 
                    attack Dracula, ending him with a final blow. You see 
                    his body started to disperse into this black mist, 
                    until Richter rusher up behind you, and using fire magic 
                    to completely destroy the soul of Dracula. 

                    You two share a glance and he ask you "So, what will you 
                    do now." 
                    """)
                    time.sleep(2.5)
                    print("""\n
                    Years pass, and you have been labeled the hero 
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
                elif c1.upper() == "SPARE":
                    print("""\n
                    You find pity in the man’s last words to you. 
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
                    print("""\n
                    Years pass, and you have been the chosen 
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
                    #Now we reload the entire code, to allow for easier restarting of the program
                else:
                    print("INCORRECT! Type Kill or Spare!")
                    c1 = input()
                #Here it will re run the while loop if anything other then Stay or Leave is typed
        elif c1.upper() == 'BLOCK':
            time.sleep(2.5)
            print("""\n
            You raise your silver crest blocking Dracula Attack. 
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
            print("""\n
            Years pass, and you have been labeled the hero of the 
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
            #Now we reload the entire code, to allow for easier restarting of the program
        else:
            print("Wrong Input! Enter Attack or Block: ")
            c1 = input()
        #Here it will re run the while loop if anything other then Stay or Leave is typed.

def MageScene():
    time.sleep(2.5)
    print("""\n
    The Dragon looks down upon you, it chest bellowed up.
    "I AM ALAZATHOR, THE BREAKER OF CHAINS AND REDEEMER OF HUMANITY.
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
            print("""\n
            "Ahh, looking for the Arkenstone, a mighty artifact. 
            Only once has it been wielded by a mortal like yourself. An old 
            dwarf king, he became made with power, and the source of his 
            corruption was the stone its self. My internal question, 
            will you be able to strike off this corruption. I have but one 
            other question that you need to answer. For if one were to 
            answer this right, they will achieve the stone and bring 
            greatness to this world. If one were to answer wrong, the stone 
            they will receive. But they will spread a great darkness around 
            this world. A herald of pure chaos and death." 
            """)
            time.sleep(2.5)
            print("""\n
            "So now the Question. A long time ago, a farmer 
            worked hard to maintain a peaceful life for his family. He wasn't 
            rich, but that didn't matter to him. He had love and was loved by 
            those around him. But a king, made with power wanted his land. 
            It would be beneficial for him, so he sent his army and murdered 
            the family. The Farmer was out that night. He went to harvest 
            some herbs. He found his dead family, and was broken will grief 
            and rage." 

            "He spent the next years plotting his vengeance, and amassed a 
            mighty group of heroes and warriors that would fight for him. The 
            farmer slew the king, and took his throne." 

            "My question to you, was what he did the right course of action?"

            Answer his question, Yes or No: 
            """)
            c1 = input()
            time.sleep(2.5)
            ans = 'incorrect'
            while ans == 'incorrect':
                if c1.upper() == "YES":
                    print("""\n
                    "Ah, you truly understand the world. That 
                    ever action has a consequence. That no matter how lowly 
                    or mighty one is, that they will meet their fate with 
                    the force of justice. You have proved yourself to wield 
                    this stone with the might of a king. You will shepherd 
                    this world in its new age. Take flight and remember that 
                    you are a champion of Justice." 

                    Alazathor raises it right claw, and manifest this 
                    glowing ethereal stone, of blue and purple stars. He 
                    hands it to you, and with a bright flash, he disappears. 
                    But the stone speaks to you. And your able to learn all 
                    of its secrets. 
                    """)
                    time.sleep(2.5)
                    print("""\n
                    Years pass, and you have launched the world 
                    to the next age. You have become supreme emperor of the 
                    lands, and have amassed countless citadels to promote 
                    peace and tranquility. Everyone is happy, and you have 
                    made the world a better place. 
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
                    #Now we reload the entire code, to allow for easier restarting of the program
                elif c1.upper() == "NO":
                    print("""\n
                    "That saddens me. My your reign be ever 
                    short, and thou people be ever vigilant." 

                    Alazathor raises it right claw, and manifest this 
                    glowing ethereal stone, of blue and purple stars. He 
                    hands it to you, and with a bright flash, he disappears. 
                    But the stone speaks to you. And your able to learn all 
                    of its secrets. 
                    """)
                    time.sleep(2.5)
                    print("""\n
                    Years passed, and you have become the supreme 
                    tyrant of the lands. You have bent the knee, of anyone 
                    who has resisted your rule. becoming mad with power, 
                    those who were closet with you, have turned. Branding 
                    them traitors they fought against you. And in the end, 
                    you were the one who succumbed. 
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
                else:
                    print("INCORRECT! Type Yes or No!")
                    c1 = input()
                #Here it will re run the while loop if anything other then Stay or Leave is typed.
        elif c1.upper() == 'REFUSE':
            time.sleep(2.5)
            print("""\n
            "Interesting, I have not found a mortal to have gone 
            against my will. Justice is a fickle thing, I have long been 
            her champion for many millennia. You are free from her shackles i 
            sense. I will make you my champion, and together we will free 
            this world from Justice's prison. 
            """)
            time.sleep(2.5)
            print("""\n
            Alazathor raises it right claw, and manifest this 
            glowing ethereal stone, of blue and purple stars. He hands it to 
            you, and with a bright flash. The stone speaks to you.And your 
            able to learn all of its secrets. Alazathor takes you into his 
            wing, and the two of you, use the power of the Arkenstone for 
            the good of all humanity. 

            You have become a demigod, serving the champion of Justice. With 
            your powers you oversee the world, and step in when needed. You 
            become hope for children and many men alike. Your name is 
            whispered in the streets, as their silent savior. You have 
            became legend, and your stories will never die. 
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
        #Here it will re run the while loop if anything other then Stay or Leave is typed.


def RangerScene():
    time.sleep(2.5)
    print("""\n
    Pushing through the streets of the Reverly, your crew, 
    combined with some smart tactics from you and Ulysses, are managing the 
    efforts from the Plank King. Defending your self, you made it to the 
    court room of the Plank King. He is already awaiting you, with his 
    gnarly halberd in hand. 

    "So, Hugo is dead I presume. I know you will not believe me, but Hugo 
    was an evil needed to be destroyed. Was going beneath my nose, 
    and trying to usurp me. I took him out. I have regrets, but I did what 
    was needed to be done." 

    "You have impressed me though, along with your crew. I forgot this, 
    take my offer. Work under me, and Ill let you live, if you don't. Well, 
    you'll wish you did. So what is it? Be smart about this." 

    Ulysses looks over at you, gives you a nod; without words he lets you know
    he is on your side with whatever you choose.

    So, what will it be? (Type in "Accept" or "Refuse") 
    """)
    c1 = input()
    time.sleep(2.5)
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "REFUSE":
            time.sleep(2.5)
            print("""\n
            "Thank you, I haven't used old betsy in forever. Your 
            giving me a treat that ill savor for a thousand years." The 
            plank king stand up, and readies his blade. 

            He begins the attack against you two. It is a ruthless battle, 
            all three of you suffer wounds from each attacks. But in the 
            end, you and Ulysses manage, to get the Plank king down onto 
            his knees. He looks up at the two of you. 

            "If you don't, Ill make sure everything you ever loved, will come 
            crumbling down." 

            Do you kill or spare the plank king? 
            """)
            c1 = input()
            time.sleep(2.5)
            ans = 'incorrect'
            while ans == 'incorrect':
                if c1.upper() == "KILL":
                    print("""\n
                    You end the Plank Kings life. With the help 
                    of Ulysses. The two of you together in the chamber 
                    share glances with each other. Until the rumbling at the 
                    door breaks through, Its your crew along with the forces 
                    of the now dead plank king. 

                    Standing there you pick up the makeshift crown the Plank 
                    king had, and you declare yourself the New King of the 
                    Reverly. Some backlash comes from those who were aligned 
                    with the previous ruler. But Ulysses gave them the 
                    "Encouragement" they needed. 

                    You have become the new king of the Reverly.
                    """)
                    time.sleep(2.5)
                    print("""\n
                    For years, you have usurped the rule of the 
                    previous king. He ruled with chaos and anger. But you 
                    brought order and peace. People begin to follow you, 
                    not out of worry or fear; but now out of loyalty. 

                    The Reverly belongs to you, along side Ulysses, the two 
                    of you have changed the world of criminals, and now made 
                    it home to those who arent welcomed to their societies. 
                    You have sowed peace, and given hope to all. 
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
                elif c1.upper() == "SPARE":
                    print("""\n
                    You find pity in the man who once was king. You 
                    take his crown. And proclaim yourself the new leader of 
                    the Reverly. With backings from those around you, 
                    you rise yourself to the top. People started to believe 
                    in your leadership. They began to become loyal to you. 
                    You sentence the old King to imprisonment for the rest 
                    of his days. And he sat there, for years plotting his 
                    revenge against you. 
                    """)
                    time.sleep(2.5)
                    print("""\n
                    Its been years, but word has it that The 
                    Plank king has escaped his prison. You worried, begin to 
                    fortify the Reverly. But The Plank King came back and he 
                    brought with him the eldritch power, of an ancient evil, 
                    Uotakoa. With this power, he destroyed everything you 
                    knew. Ulysses fell last, until it was just you two 
                    together. 

                    Without hesitation, he ended your life, slowly. He 
                    allowed you to understand your surrounding, to take in 
                    the chaos and evil. Then the void takes you. Your eyes 
                    succumb to black, and nothingness fill everything you 
                    knew. 
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
                    #Now we reload the entire code, to allow for easier restarting of the program
                else:
                    print("INCORRECT! Type Kill or Spare!")
                    c1 = input()
                #Here it will re run the while loop if anything other then Stay or Leave is typed.
        elif c1.upper() == "ACCEPT":
            time.sleep(2.5)
            print("""\n
            "Well this is a surprise at least. Mighty well 
            gentlemen, welcome to the crew of the Plank King. First Go and 
            stop your old mates from wrecking to much havoc. Im in need 
            urgently of your Assistance." 

            You leave with Ulysses, and stop your crew from continuing their 
            rampage. Some gave resistance with joining the plank king. But it 
            didn't take long for the lot of them to get on board. You have 
            joined the Court of the Sea King, powerful members, who work 
            directly with the Plank King. 
            """)
            time.sleep(2.5)
            print("""\n
            Years pass, and you help the Plank King see his 
            errors in his ways. He begins to shape his ruler ship away from 
            Chaos, and begins to sow peace and harmony along the pirates and 
            thieves of the Reverly. 

            While the Plank King worked back at the Reverly, you and Ulysses 
            have sought out adventure when your desires arise. You own your 
            own ship, and become the captain of the "Squall Eater". For 
            years you become infamous, and a mortal enemy to the royal navy 
            of the empire. You've become legend, who never fails to make a 
            moment lively. 
            """)
            ans = 'correct'
            time.sleep(2.5)
            print("=================YOU GOT THE GOOD ENDING=================")
            time.sleep(2.5)
            print("==================THANK YOU FOR PLAYING=================")
            time.sleep(2.5)
            print("================RESTARTING FROM THE START===============")
            time.sleep(2.5)
            scene1()
        else:
            print("Wrong Input! Type in Accept or Refuse: ")
            c1 = input()
        #Here it will re run the while loop if anything other then Stay or Leave is typed.

scene1()
#We run the first scene wich will domino down into the ending.
