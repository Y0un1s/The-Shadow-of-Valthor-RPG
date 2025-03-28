import random as r

print("🌟 Welcome to The Shadow of Valthor! Let your adventure begin! 🎮\n")

#Choosing the class

while True:
    try:
        class_ = int(input('''Please select your class: 
1) Warrior
2) Mage
3) Assassin
4) Paladin
5) Not Sure
Choose: '''))
    except ValueError:
        print("Speak now thy number, and let it be whole")
        continue
    if class_ in (1,2,3,4,5):
        w = 0
        m = 0
        h = 0
        a = 0
        match class_:
            case 5:
                print('let\'s figure out together, please answer the following questions')
                print('\n')
                try:
                    q1 = int(input('''You find yourself in a dense, enchanted forest, the moonlight barely piercing through the canopy. Suddenly, a shadow moves in the distance. What is your first instinct?
1)🌳 Stand your ground, preparing to fight whatever lurks ahead.
            
2)🔮 Whisper an incantation, ready to control or deceive the unknown.
            
3)🌿 Blend into your surroundings, watching silently.
            
4)💖 Step cautiously forward, offering a gesture of peace. 
'''))
                    if q1 not in (1,2,3,4):
                        raise ValueError
                except ValueError:
                    print("State your number promptly, ensuring it is whole, complete, and between 1 and 4.\n")
                match q1:
                    case 1:
                        print("Fear is for the weak. You are the shield, the sword, the unshakable force. Let them come.")
                        w += 2
                    case 2:
                        print("Knowledge is your power, and power bends reality. Whatever lurks in the dark… you will master it.")
                        m += 2
                    case 3:
                        print("To be seen is to be vulnerable. To be patient is to strike at the perfect moment. The night is your ally.")
                        a += 2
                    case 4:
                        print("Darkness and fear consume the reckless, but kindness is a force unseen. Even shadows can be calmed.")
                        h += 2
                print('\n')
                try:
                    q2 = int(input('''A mysterious traveler hands you a locked, ancient chest and vanishes. The key is nowhere to be found. What do you do?
1)⚔️ Smash it open with brute force—nothing hides from me!
            
2)🔥 Whisper a spell, attempting to unlock its secrets through magic. 
            
3)🗡️ Examine it carefully, searching for hidden mechanisms or traps.
            
4)💫 Take it with you, believing it will reveal its purpose when the time is right.
'''))
                    if q1 not in (1,2,3,4):
                        raise ValueError
                except ValueError:
                    print("State your number promptly, ensuring it is whole, complete, and between 1 and 4.\n")

                match q2:
                    case 1:
                        print("Secrets are for the cunning. Strength is truth. The chest will yield to your might or be nothing at all.")
                        w += 2
                    case 2:
                        print("No lock is beyond knowledge, no mystery beyond magic. The chest will open… if it dares to resist, it will burn.")
                        m += 2
                    case 3:
                        print("A fool rushes. A ghost waits. There is no door that cannot be slipped through, no secret safe from silent hands.")
                        a += 2
                    case 4:
                        print("All things unfold as they must. Some doors are meant to remain closed… until their time has come.")
                        h += 2
                print('\n')
                try:
                    q3 = int(input('''You hear a voice echoing in your mind: "Choose your path." Before you appear four shimmering doors, each pulsing with strange energy. Which do you enter?
1)🚪 A towering iron gate, battered by years of battle and glory.
            
2)🔮 An arched doorway of swirling stars and arcane symbols.
            
3)🌿 A hidden passageway, only visible when the light hits just right.
            
4)🌸 A glowing entryway, humming with warmth and renewal.
'''))
                    if q1 not in (1,2,3,4):
                        raise ValueError
                except ValueError:
                    print("State your number promptly, ensuring it is whole, complete, and between 1 and 4.\n")

                match q3:
                    case 1:
                        print("Only those who have faced the storm can claim the throne. This path leads to war… and to legends.")
                        w += 3
                    case 2:
                        print("This is not just a path—it is knowledge, eternity, and power beyond mortal hands. Only the wise may enter.")
                        m += 3
                    case 3:
                        print("If you see this door, you were meant to. If others do not, they were not. Step carefully, and the world will never know your name.")
                        a += 3
                    case 4:
                        print("Some walk paths of destruction, but yours is of restoration. To walk through this door is to choose life itself.")
                        h += 3
                print('\n')
                c = {"Warrior": w,"Mage" : m ,"Assassin": a ,"Paladin": h}
                his_class = max(c, key = c.get)
                print("You are the", his_class)
                match his_class:
                    case "Warrior":
                        he = 100
                        fp = 50
                        ad = 7
                        ap = 1
                        hp = 0
                    case "Mage":
                        he = 60
                        fp = 100
                        ad = 1
                        ap = 10
                        hp = 3
                    case "Paladin":
                        he = 80
                        fp = 80
                        ad = 7
                        ap = 8
                        hp = 10
                    case "Assassin":
                        he = 20
                        fp = 50
                        ad = 10
                        ap = 0
                        hp = 0
            case 1:
                he = 100
                fp = 50
                ad = 7
                ap = 1
                hp = 0

            case 2:
                he = 60
                fp = 100
                ad = 1
                ap = 10
                hp = 5

            case 3:
                he = 20
                fp = 60
                ad = 10
                ap = 0
                hp = 0

            case 4:
                he = 80
                fp = 80
                ad = 7
                ap = 8
                hp = 10
        break
    else:
        print("Let thy choice be numbered between one and five, and stray not from the path set before thee.\n")
initial_he = he
initial_fp = fp
initial_ad = ad
initial_ap = ap
initial_hp = hp


#The beginning of the game


print("""# The Shadow of Valthor # 
And lo, the heavens wept, and the stars did tremble, for darkness had taken root in the heart of men. Valthor the Betrayer, he who once walked among the righteous, did cast aside his oaths and embraced the abyss. He bound the souls of the fallen unto his will, and from the ruins of Eldoria, he did forge a kingdom of the damned
But from the ashes of despair rose one chosen by fate, whom the stars had marked, and the winds did whisper of their coming. He who beareth the weight of destiny must now tread the path of trial, for the hour of reckoning is at hand.\n""")

print('''Thou dost stand at the threshold of fate, where the bones of the fallen whisper unto thee. The Monastery of the Fallen, once a sanctuary, now lieth in ruin, and within its broken halls, the shadows stir. The Hollowborn, cursed souls bound to eternal torment, rise from the dust, their lifeless eyes set upon thee.
Two Hollowborn Scouts emerge, their rusted blades glinting in the moon’s sorrowful light. The air is thick with the scent of death. The first trial is upon thee.\n''')
counter1 = 0
while True:
    can_survive = input("Thy journey beginneth. would thou chose to fight? (y/n): \n").lower()

    if can_survive == "y" or can_survive == "yes":
        print("Lift thine hand, grasp thy steel, and let not fear find a place in thy heart! For the wicked shall know terror when the chosen doth not waver. Strike, and let the heavens bear witness to thy wrath!\n")
        break
    elif can_survive == "n" or can_survive == "no":
        print("Peace is a tongue unknown unto the dead, and mercy findeth no home in their hollow hearts. They draw near, for no voice may turn back the tide of darkness, YOU WILL FIGHT!\n")
        break
    else:
        counter1 += 1
        if counter1 > 1:
            print("Nay, thou canst not turn back, for the path behind is lost to thee. He who forsaketh the trial is but chaff upon the wind, to be scattered and forgotten. Stand, or be naught but dust upon the earth.\n")
        else:
            print("Let thy words be true, and enter but 'yes' or 'no', lest thou be counted among the faithless who flee from fate.\n")


print("""The air is thick with the scent of damp earth and decay. The heavens are veiled in darkness, and the trees whisper with unseen voices. From the abyss of silence steps forth thy first foe—Morrak, the Forsaken Squire.
Once a loyal warrior, now but a wretched soul cast from grace, his armor is rusted, and his blade is dulled, yet the malice in his eyes is sharp as any steel. He raises his cracked longsword, eager to spill thy blood....

Foul soul,

Emboldened by the flame of ambition.

Hrah!

Someone must extinguish thy flame.

Let it be Morrak the Fell!

\n""")
morrak_he = 50
morrak_fp = 20
morrak_ad = 5
morrak_ap = 3
morrak_hp = 2
print("Morrak is a", morrak_he, "hit point")
print('\n')

#The First Encounter with an enemy

while morrak_he > 0 and he > 0:
    try:
        print("""#######################
#### ⚔ YOUR TURN ⚔ ####
#######################
Your health =""",he)
        action = int(input("\nWill thou:\n1) ⚔ Strike with thy blade\n2) 🧙 Cast a spell\n3) 🗡 Sneak attack\n4) 💖 Heal thy wounds\nChoose: "))
    except ValueError:
        print("Speak thy number with haste, ensuring it is whole and unwavering!\n")
        continue
    if action in (1,2,3,4):
        match action:
            case 1:
                print("Thy steel cleaveth the air as thunder, and the heavens bear witness to thy might. Let thine enemy taste cold iron, and may his bones tremble!\n")
                if ad >= 7 or r.randint(1, 30)+ad > 20:
                    print("Morrak staggers, crimson spilling upon the earth, his strength waning like the dying light of dusk.!\n")
                    morrak_he -= 1.5*ad
                else:
                    print("Thy strike findeth naught but the empty wind, and Morrak mocketh thee with a wicked grin, his fangs bared in defiance!\n")

            case 2:
                print("Lo, the elements hearken to thee! With words unuttered since the dawn of time, thou summoneth ruin upon thine enemy!\n")
                if (ap >= 8 or r.randint(1, 30)+ap > 20) and fp > 0:
                    print("Morrak shrieketh as eldritch fire consumeth him, his wretched form writhing as the unseen forces do thy bidding!\n")
                    morrak_he -= (ap + 5)
                else:
                    print("The heavens heed thee not. The incantation withereth on thy tongue, and Morrak’s cruel laughter ringeth in thine ears.\n")
                fp -= 10
            case 3:
                print("Like the serpent in the garden, thou moveth unseen, thy dagger thirsting for blood. Let the deceiver be deceived!\n")
                if ad > 8 or r.randint(1, 40)+ad > 20:
                    print("Steel sinketh into flesh ere the wretch draweth breath. His eyes widen in terror, for his folly was to believe thou wert but a mortal.\n")
                    morrak_he -= 3*ad
                else:
                    print("Thy foot betrayeth thee, a whisper upon the stone! Morrak turneth, his wicked blade seeking thy heart, and the hunter becometh the hunted!\n")
                    fp -= 5
            case 4:
                print("Raise thy hands to the heavens, and let the light of creation mend what is broken! May thy flesh be restored, lest darkness claim thee!\n")
                if he == 100:
                    print("Thy body is whole—why dost thou seek to mend what is unbroken?\n")
                elif (hp == 10 or r.randint(1, 30)+hp > 20) and fp > 0:
                    print("A warmth unseen filleth thy veins, and thy wounds seal as if the hand of providence hath touched thee. Strength returneth, and the battle is not yet lost!\n")
                    he = min(100, he + 1.3 * he)
                else:
                    print("The prayer falleth upon deaf ears. The heavens are silent, and thy wounds remain, a cruel jest upon thy suffering.\n")
                    fp -= 10
    else:
        print("Thou hesitateth, squandering precious moments! Speak now thy number between one and four, let it be whole—but alas, thy indecision hath cost thee thy turn.")



    if morrak_he > 0:
        print("""########################
#### ⚔ ENEMY TURN ⚔ ####
########################
Enemy health =""",morrak_he,)
        print('\n')
        morrak_action = r.randint(1, 3)
        if morrak_action == 1:
            print("Thou thinkest thy steel fierce? Nay, weakling, thou art but a trembling leaf before the storm!\n")
            if morrak_ad >=5:
                print("Morrak’s blade cleaveth flesh, and pain danceth through thy veins! Blood spillest from thy wound, a crimson tribute to his might!\n")
                he -= 1.5 * morrak_ad
            else:
                print("Thy reflex is quick, and fate doth spare thee! Morrak’s blade meeteth naught but the whispering wind, his fury mounting!\n")
        elif morrak_action == 2:
            print("The shadows bow to me, the very air trembleth at my call! Now, taste the might of the abyss!\n")
            if morrak_fp > 0 and r.randint(1, 30)+morrak_ap > 20:
                print("A searing darkness lurches forth! Pain wracketh thy form as unseen hands claw at thy very soul!\n")
                he -= morrak_ap * 1.5
            else:
                print("The void stirs… yet dost not obey! Morrak’s fury riseth as his own magic betrayeth him!\n")
            morrak_fp -= 10

        elif morrak_action == 3:
            print("Didst thou truly think me bested? Nay… the shadows hide my wrath, and from darkness, I shall end thee!\n")
            if r.randint(1, 30)+morrak_ad > 17:
                print("From the blackness, a dagger slippeth between thy ribs! The cold embrace of treachery stealeth thy breath—Morrak’s laughter echoeth in thy ears!\n")
                he -= 3 * morrak_ad
            else:
                print("Thy senses doth not betray thou dost twist away, and Morrak’s blade meeteth naught but emptiness!\n")


if he > 0:
    print("""#############################################################\n
💀 With a final cry, Morrak falleth to his knees. His soul fadeth into the abyss, and the path before thee is now clear.\n
#############################################################\n""")
else:
    print("""#############################################################\n
Put these foolish ambitions to rest said Morrak... 
Thy body collapseth, and the tale of thy journey endeth here.\n
#############################################################\n""")
    exit()

#resetting the character stats

he = initial_he
fp = initial_fp
ad = initial_ad
ap = initial_ap
hp = initial_hp

#the progression system

print("""
Through the mist-laden woods, thou dost tread, the echoes of battle still whispering in the wind. The scent of damp earth and the hush of ancient trees bear witness to thy passage.
Lo, upon the path, a box doth rest, untouched by time, its surface veiled in the dust of forgotten years. A presence lingers about it—neither menacing nor kind, but watching, waiting. The choice is thine, and the fate of thy power shall be shaped by thy will.
""")

while True:
    try:
        open_box = int(input("How dost thou open the box?\n Will thou: \n1) 💪 Pry the lid asunder with brute force. \n2) 🎭 Unfasten it, deft hands moving like the wind. \n3) 📖 Weave sigils upon its surface.\n4) 🙏 place thy hand upon it, seeking balance. \nChoose: "))
    except ValueError:
        print("Declare thy number without delay, ensuring it be whole and resolute!\n")
        continue
    if open_box in (1, 2, 3, 4):

        match open_box:
            case 1:
                ad += 3
                break
            case 2:
                ad += 2
                he += 10
                break
            case 3:
                fp += 20
                ap += 2
                break
            case 4:
                ap += 1
                ad += 1
                fp += 10
                he += 10
                break
    else:
        print("Why doth thou tarry, letting precious moments slip away? Declare thy whole number, chosen from one to four, and let it be whole!\n")

print("""A choice is made, and the heavens break asunder! A blinding light doth surge forth, wrapping thee in its embrace. The world doth fade, and for but a breath, thou art lost within the abyss of radiance.
Then, as shadows yield, thou dost stand anew. Strength unfelt courses through thy veins, the weight of newfound power settling upon thy soul.\n""")

#The choice affecting the ending of the game

print("""Yet ere the moment stills, a cry doth pierce the air—a woman’s voice, wrenched from the depths of peril.
Before thee, the path doth split, and choice be thine to make:\n""")

while True:

    try:
        rescue_women = int(input("Will thou:\n1) Harden thy heart, walk forth, and heed her not.\n2) Turn fleet of foot, hasten toward the cry, and face what fate may bring.\n3) Shun the unknown, flee ere the dark entwines thee. \nChoose: "))
    except ValueError:
        print("Proclaim thy number boldly, whole and steadfast, with no delay!\n")
        continue
    if rescue_women in (1, 2, 3):
        match rescue_women:

            case 1:
                rescued = False
                print('''He walks away, pushing forward. The world is full of suffering; he cannot answer every cry.
    
Yet, some minutes later, the woman is in front of him. Impossible. She watches him with unreadable eyes.
    
"You heard me. You left. But you are still here, aren’t you?" She steps closer, voice soft. "That means something."
    
She raises a hand and points.
    
"It was a wolf. It saw me. It sees you now. Go on, then. If you wish to leave, do so. But you will find your path leads back to it, no matter what you choose."
    
A strange, unsettling truth coils around him. The wolf awaits.''')
                break

            case 2:
                rescued = True
                print('''He bursts through the trees, blade drawn, breath ragged. The woman stands in a clearing, trembling.
    
"You came so fast… why?" she asks, her voice barely above a whisper.
    
Before he can answer, she looks past him, eyes flickering with something unreadable.
    
"I saw it. The wolf. It watched me from the trees. Its eyes… hollow, endless. Tell me, stranger… would you have come if you knew it was only fear? Not danger?"
    
Her words are strange, yet something inside him stirs. A need. A pull. The wolf. He must find it.\n''')
                break

            case 3:
                rescued = False
                print('''Moving like a shadow, he hears the scream—but does not go to it. Something about it feels… wrong. His instincts, honed by survival, whisper danger. And so, he turns away.
    
Yet, no matter how far he walks, the feeling lingers. The trees press in, their branches twisting like grasping hands. The air is heavy, suffocating. He is being watched.
    
Then, she is there.
    
Not behind him. Not calling for help. But standing ahead, waiting, as if she had always been there.
    
Seated on a moss-covered rock, she looks at him with knowing eyes. A slow, deliberate smile tugs at her lips.
    
"You ran," she murmurs. "You always run, don’t you?"
    
He does not answer. His grip tightens on his weapon.
    
"Tell me, stranger… is that wisdom, or fear?"
    
The question lingers in the cold night air, wrapping around him like unseen chains.
    
Then she tilts her head, looking past him, as if seeing something just over his shoulder.
    
"It was just a wolf," she says at last. "But it saw me. And when it did… it did not run."
    
The weight of her words settles deep in his bones. A presence stirs on the edge of his senses.
    
He needs to find it. He cannot turn away now.\n''')
                break
    else:
        print("Why dost thou linger, squandering fleeting time? Declare thy whole number betwixt one and three, and let it be done without delay!\n")

print('''

################################################################################
******************************** One hour later ********************************
################################################################################

🌲 The forest is quiet. Too quiet. He moves with purpose now, tracking the signs—paw prints pressed into soft mud, broken branches, the lingering scent of something ancient.

Then, he sees it. 🐺

A lone wolf, standing beneath a dying tree. Its fur is silver, but its eyes are… wrong. Deep, endless pools of darkness. It watches him, still and knowing.

Then, it turns and runs.

He pursues. The chase is relentless, twisting through trees, leaping over fallen logs, cutting through the cold night like a blade through flesh. The closer he gets, the stronger the feeling inside him grows—he must stop this creature. 

At last, the wolf stops at the edge of a ruined temple. It turns to face him.

Without thinking, he raises his weapon. The need to strike is overwhelming. 🗡️

He attacks.

And in that instant, the wolf is no more.

A golden-red flame erupts, engulfing its body. The ground trembles. From within the fire, a figure emerges—tall, armored, wrapped in power. A voice like a dying star echoes through the air.\n''')

print('''
******************************************

"Thou, who approacheth Destined Deat...

I will not have it stolen from me again."

Valthor steps forward, his presence swallowing the very light around them.

"Why wouldst thou…" His voice falters, then hardens. "Why..."

He lifts his blade, a weapon pulsing with the weight of a thousand forgotten lives.

"Tis no matter. I hereby vow...
That Destined Death shall not be stolen again."

A cold wind sweeps through the battlefield.

Valthor raises his free hand to the sky. Shadows coil around him, forming a jagged, deathly aura. His fingers tighten into a fist.

"O, Death..."

The sky darkens. The land trembles. The weight of fate itself presses down upon them.

"Become my blade, once more."

******************************************

The time for words is over.

🔥 The battlefield is set.
⚔️ The fight begins.

The warrior raises his sword. The rogue vanishes into the mist. The mage calls upon forgotten powers. The paladin stands firm, light shining in his grasp.

Valthor’s blade descends.\n''')

#The Valthor Encounter

valthor_he = 100
valthor_fp = 60
valthor_ad = 6
valthor_ap = 6
valthor_hp = 3

print("Valthor is a", valthor_he, "hit point\n")

while valthor_he > 0 and he > 0:
    try:
        print("""#######################
#### ⚔ YOUR TURN ⚔ ####
#######################
Your health =""",he)
        action = int(input(
            "\nHow shalt thou shape the tide of fate?\n"
            "1) ⚔ Unleash thy steel, let the clash of blades sing in battle!\n"
            "2) 🔥 Call upon the forbidden arts, weaving ruin with sorcery!\n"
            "3) 🗡 Become the shadow, strike swift and unseen, a whisper of death!\n"
            "4) 💖 Defy the abyss, mend thy wounds, and rise anew!\n"
            "Choose thy path, warrior: "))
    except ValueError:
        print("Thy words falter, unfit for the tongue of warriors! Speak again with clarity, lest fate forsake thee!\n")
        continue
    if action in (1, 2, 3, 4):
        match action:
            case 1:
                print(
                    "With the wrath of the storm and the fury of the ancients, thou dost cleave the air! Let the earth quake beneath thy strike, and let thine enemy tremble ere the clash of steel!\n")
                if ad >= 7 or r.randint(1, 30) + ad > 20:
                    print(
                        "Valthor staggers, his lifeblood spilt upon the sacred ground, his might waning like the setting sun, yet still he stands, defiant!\n")
                    valthor_he -= 1.5 * ad
                else:
                    print(
                        "The winds betray thee, and thy blade findeth naught but the mocking void! Valthor’s laughter is a hymn of derision, his fangs bared in cruel amusement!\n")

            case 2:
                print(
                    "Thou dost beckon to the primordial forces, thy voice a whisper upon the void! The heavens crack and the abyss stirs as thou summoneth ruin upon thine adversary!\n")
                if (ap >= 8 or r.randint(1, 30) + ap > 20) and fp > 0:
                    print(
                        "A wail of agony rendeth the air as eldritch flame devoureth Valthor! He writhes in torment, his form sundered by powers unseen, yet still he doth endure!\n")
                    valthor_he -= (ap + 5)
                else:
                    print(
                        "The ancient tongues fail upon thy lips, and the forces of destruction heed thee not! Valthor’s eyes gleam with cruel mirth as thy spell falters into silence!\n")
                fp -= 10

            case 3:
                print(
                    "Silent as the specter of death, thou dost weave through the battlefield, a shadow given form! The blade in thy grasp thirsts for the crimson of thine enemy!\n")
                if ad > 8 or r.randint(1, 40) + ad > 20:
                    print(
                        "Steel kisseth flesh ere the fiend draweth breath! His eyes widen, for in his folly he hath underestimated the phantom that stalketh him!\n")
                    valthor_he -= 3 * ad
                else:
                    print(
                        "A treacherous whisper upon the stone betrayeth thee! Valthor turns, his wicked blade a streak of midnight, and lo—the hunter becometh the hunted!\n")
                    fp -= 5

            case 4:
                print(
                    "Thy hands rise heavenward, and lo! The light of creation doth descend! The old wounds mend, the breath of life is renewed, and the battle is not yet lost!\n")
                if he == 100:
                    print("Thy form is whole—why dost thou call upon the divine for what needeth not repair?\n")
                elif (hp == 10 or r.randint(1, 30) + hp > 20) and fp > 0:
                    print(
                        "A golden warmth floodeth thy being, and where there was weakness, strength returneth! Thy wounds are but echoes of a past pain, cast aside by the grace of the heavens!\n")
                    he = min(100, he + 1.3 * he)
                else:
                    print(
                        "Thine invocation is met with silence, the stars weep not for thee! The wounds remain, cruel testimony to a fate unwilled!\n")
                    fp -= 10
    else:
        print(
            "Time slips through thy grasp like sand upon the wind! Speak now, warrior, lest hesitation be thy undoing! A number between one and four, whole and true, or suffer the folly of indecision!")

    if valthor_he > 0:
        print("""########################
#### ⚔ ENEMY TURN ⚔ ####
########################""")
        print("Valthor's health remaineth:", valthor_he, "\n")

        valthor_action = r.randint(1, 4)

        if valthor_action == 1:
            print("Fool! Didst thou think thy steel could match mine? Nay! Thou art but a reed before the tempest!\n")
            if valthor_ad >= 5:
                print(
                    "Valthor's blade descendeth as the wrath of the heavens! Agony surgeth through thy veins, and thy blood staineth the earth, a sacrifice to his might!\n")
                he -= 1.5 * valthor_ad
            else:
                print(
                    "Swift as the wind, thou dost evade! Valthor’s strike cleaveth naught but the void, his rage kindled by thy defiance!\n")

        elif valthor_action == 2:
            print(
                "The abyss knoweth my name, and its whispers doth heed my call! Now, mortal, gaze into the maw of oblivion!\n")
            if valthor_fp > 0 and r.randint(1, 30) + valthor_ap > 20:
                print(
                    "A maelstrom of dark sorcery erupts forth! The air burneth, unseen talons rend thy flesh, and the void itself seeketh to consume thy soul!\n")
                he -= valthor_ap * 1.5
            else:
                print(
                    "The abyss stirreth… yet it heareth not! Valthor’s incantation faileth, and frustration darkeneth his countenance!\n")
            valthor_fp -= 10

        elif valthor_action == 3:
            print(
                "Didst thou truly believe I had fallen? Nay, wretch! The shadows cradle me, and from their depths, I strike!\n")
            if r.randint(1, 30) + valthor_ad > 17:
                print(
                    "A blade, unseen as the serpent, pierceth thy flesh! Cold and cruel is the kiss of treachery, and Valthor’s laughter is the hymn of thy suffering!\n")
                he -= 3 * valthor_ad
            else:
                print(
                    "Thine instincts scream, and thou dost twist away! Valthor’s dagger cutteth naught but the empty air, his fury a storm unchecked!\n")


        elif valthor_action == 4:
            print("Didst thou think me spent? Fool! I am eternal! The abyss doth not forsake its own!\n")
            if valthor_hp < 100 and valthor_fp > 0:
                print(
                    "Valthor spreadeth his arms, and the darkness gathereth. His wounds mend as if kissed by the void, and the shadows themselves strengthen his resolve!\n")
                valthor_hp = min(100, valthor_hp + valthor_ap * 1.3)
            else:
                print(
                    "The void remaineth silent. Valthor’s call goeth unanswered, and the wound upon his flesh remaineth! A flicker of doubt darkeneth his gaze.\n")
            valthor_fp -= 10
#The game ending 

if he > 0 and rescued == True:
    print("""#############################################################\n
    
The battle raged like a tempest upon the heavens, steel clashing with steel, the very air thick with the scent of blood and embers. 

The warrior’s breath was ragged, his limbs heavy, yet his resolve burned brighter than ever. Valthor staggered, the once-mighty shadow now reduced to a figure of ruin. His form, twisted with power long since corrupted, faltered as he fell to one knee.

The warrior stood over him, blade poised, the echoes of their battle still trembling through the land.

Valthor coughed, a cruel smirk still haunting his lips as his crimson-stained fingers clutched at the wound upon his chest. Yet his eyes, once alight with malice, now held something deeper—acceptance, perhaps, or revelation.

He exhaled, a whisper of a laugh escaping his lips.

"I have lingered in the darkness, waiting, watching. Bound to the fate of a throne that shall never be mine. And now, the hour is come. Thou hast triumphed. But tell me, wanderer… What dost thou seek, truly?"

His voice wavered, but the weight of it remained.

"Wilt thou claim the light, radiant and blinding, that burneth away all shadows? Or the dark, that cradleth secrets yet untold? Or dost thou seek something else, a path uncarved, unknown?"

The warrior did not answer. The silence was its own response.

Valthor’s smirk faded. His body wavered, his form shifting like mist in the morning sun. The curse that bound him unraveled at last.

"Then go, and see where thy choice leadeth thee… Perhaps one day, we shall meet again, beyond light and shadow alike."

With those final words, his body faded into nothingness, scattered upon the wind. The land grew silent. The battle was won.

The battlefield was still. The air, thick with echoes of the clash, now settled into silence. But the warrior had no time to linger. The woman—he had run to save her.

He turned, feet moving before his mind, driven by the call that had first led him astray. The path was steep, the woods dark, but he pressed on. 

The place where he had first heard her scream now lay in eerie quiet. And then, she stepped from the shadows.

************************

She was unscathed. No fear lingered in her eyes, only quiet amusement.

"So, thou didst come for me, even after all that hath passed. A noble fool thou art, or perhaps something more."

Her voice was calm, unreadable. The warrior narrowed his gaze, searching her face for some trace of the terror that had once filled the night.

She tilted her head, a knowing smile playing upon her lips.

"I told thee… It was but a wolf."

Her words hung in the air, twisting like a cruel jest. The warrior stiffened. A test. She had tested him from the very beginning.

She stepped closer, her gaze piercing, studying him.

"And tell me, now that thy battle is won, dost thou feel fulfilled? Did slaying the beast grant thee peace?"

Her words were light, yet they bore weight. The warrior clenched his fists. He had fought not for peace, nor glory, but because something deep within him had demanded it. And yet, even now, the hunger in his soul remained.

She let out a soft breath, almost like a sigh.

"Then perhaps thy war is not yet ended."

The wind howled through the trees, a whisper upon the earth. The warrior turned his gaze to the horizon, where the land stretched far beyond his sight. He had slain Valthor. He had followed the call of a woman who had never truly needed saving.

And yet, his journey had only begun.
    
#############################################################\n""")
elif he > 0 and rescued == False:
    print("""#############################################################\n

Valthor fell to his knees, the weight of his defeat pressing upon his fading form. His breath was ragged, his once-mighty presence reduced to nothing but flickering embers in the night. Yet, in his final moments, there was no anger, no wrath—only knowing.

"I lost all, yet I remained. Patiently. The throne shall take thee, as it would have taken me… But tell me, warrior—what dost thou truly seek? Light? Dark? Or dost thou yearn for something beyond?"

His body crumbled like ash in the wind, vanishing as though he had never been. The air was silent, save for the whispers of fate shifting around the warrior. He had triumphed. And yet… something lingered, something unresolved.

He turned, stepping over the remnants of battle, moving toward the place where he had first heard the woman’s cries. But this time, he did not run. He had chosen the path of battle, not rescue. 

And so he returned, not as a savior, but as one who had claimed his own victory.

************************

She stood there, waiting.

Her expression was different now—not amused, not warm, but unreadable. She watched him as one watches a puzzle, measuring the weight of his choice.

"So, thou didst not come for me."

There was no accusation in her tone, nor was there kindness. Only the simple truth of his decision.

"Didst thou think I needed saving? Or was it simply that the cry did not stir thee enough?"

Her gaze was sharp, cutting deeper than any blade. She took a step closer, studying him as if searching for something beneath his flesh, beneath his steel.

"Then tell me, warrior. Now that the beast is slain, now that thy blade hath tasted victory… dost thou stand fulfilled?"

The words hung in the air, twisting like an unseen chain wrapping around his soul. He did not answer—perhaps because he did not know.

She let out a quiet breath, tilting her head slightly, as if disappointed, or perhaps merely expectant.

"I told thee… It was but a wolf."

Silence stretched between them, as deep and unfathomable as the night itself. Then she turned, her footsteps light upon the earth, leaving him with the weight of what had passed.

He had chosen battle over rescue. He had proven his strength. And yet, as she vanished into the shadows, he could not help but wonder…

Had he won anything at all?
    
#############################################################\n""")
else:
    print("""#############################################################\n

The battle had raged like a storm, steel clashing against steel, fire against shadow. But fate had not favored the warrior this night. His strength waned, his breath came ragged, and his vision blurred as crimson ran from his wounds like a river feeding the abyss.

Valthor loomed over him, his form a silhouette against the cold moonlight, his presence like a storm on the edge of breaking. He did not gloat, nor did he strike the final blow in haste. Instead, he simply gazed upon the fallen warrior, as if peering through his very soul.

"Thou fought well, yet here thou liest, broken. And still… thou dost not understand."

His voice was neither cruel nor triumphant, but steeped in something deeper—something ancient.

"I lost all, yet I remained. Patiently. The throne would take thee, as it would have taken me. But tell me, broken warrior… what was it thou sought? Was it light? Darkness? Or didst thou chase a dream that was never thine to claim?"

The world tilted. The warrior tried to rise, but his limbs failed him. The strength that had once carried him through countless battles was gone, spent like a candle’s final flicker.

And then—footsteps.

************************

Soft, deliberate.

The woman stepped into view, her expression shrouded in shadow. She looked down at him—not with pity, nor sorrow, but with something colder.

Disappointment.

"So, this is the fate thou didst carve for thyself?"

Her voice did not waver, nor did she move to help him. There was no outstretched hand, no warmth in her gaze. Only the weight of judgment.

"When I first called, thou didst hesitate. And then thou didst run—not to me, but to the fight, seeking thy purpose in battle. Tell me, warrior… where doth it lie now?"

Valthor let out a low chuckle, stepping back, allowing her words to pierce deeper than any blade.

"He hath no answer," he mused. "For in truth, he never knew."

The woman exhaled, turning from the fallen warrior, her voice barely above a whisper.

"It was but a wolf."

With that, she was gone, her figure swallowed by the darkness, as if she had never been.

Valthor, too, turned away, leaving the warrior alone with his failure, his unanswered questions sinking into the blood-soaked earth.

And as his vision faded, as the night claimed him, one final thought echoed in his mind.

Had he ever truly known why he fought?
    
#############################################################\n""")
    exit()









