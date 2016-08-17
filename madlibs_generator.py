# A list of replacement words to be passed in to the play game function. 
parts_of_speech1  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]

# The following are some test strings to pass in to the play_game function.
test_string1 = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered 
OCCUPATION could VERB them."""
test_string3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."
import easygui
# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
def censorship (keys,text):
    c=0
    for key in keys:
        text=text.replace(key,blanks[c])
        c=c+1
    return text
def replacer(key,text,blank):
    text=text.replace(key,blank)
    return text

def filltheblank(tries,text,keys):
    i=0
    for i in range(0,len(keys)):
        while tries>0:
            user_input = raw_input("Type in a replacement for " + blanks[i] + ": ")
            if user_input in keys:
                print 'Good Job!:)'
                text=replacer(blanks[i],text,user_input)
                print text
                break
            else:
                tries=tries-1
                if tries >1:
                    print 'Try again,you only have '+str(tries)+' tries left'
                elif tries==1:
                    print 'Try again,you only have '+str(tries)+' try left'
                else:
                    print "You lost, looser2456"
                    return None
#        replaced = " ".join(replaced)
    print 'CONGRADULATIONS YOU ARE NOW ELIGIBLE FOR A FREE ICE-CREAM CONE FROM DAIRY QUEEN'
    print text
    return None

#def difficulty():
#    msg = "What difficulty do you choose"
#    choices = ["Easy","Medium","Hard"]
 #   reply = buttonbox(msg, image=image, choices=choices)
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.

blanks=['__1___','__2___','__3___','__4___','__5___','__6___','__7___']

Rope_text1='A rope is a group of yarns, plies, or strands that are twisted or braided together into a larger and stronger form. Ropes have tensile strength and so can be used for dragging and lifting, but are too flexible to provide compressive strength. As a result, they cannot be used for pushing or similar compressive applications. Rope is thicker and stronger than similarly constructed cord ,line, string, and twine. Ropes made from metal strands are called wire rope.'

Rope_text2='The use of ropes for hunting, pulling, fastening, attaching, carrying, lifting, and climbing dates back to prehistoric times. It is likely that the earliest "ropes" were naturally occurring lengths of plant fibre, such as vines, followed soon by the first attempts at twisting and braiding these strands together to form the first proper ropes in the modern sense of the word. Impressions of cordage found on fired clay provide evidence of string and rope-making technology in Europe dating back 28,000 years.[2] Fossilized fragments of "probably two-ply laid rope of about 7 mm diameter" were found in one of the caves at Lascaux, dating to approximately 15,000 BC.[3]'

Rope_text3='The modern sport of rock climbing uses so-called "dynamic" rope, which stretches under load in an elastic manner to absorb the energy required to arrest a person in free fall without generating forces high enough to injure them. Such ropes normally use a kernmantle construction, as described below. "Static" ropes, used for example in caving, rappelling, and rescue applications, are designed for minimal stretch; they are not designed to arrest free falls. The UIAA, in concert with the CEN, sets climbing-rope standards and oversees testing. Any rope bearing a GUIANA or CE certification tag is suitable for climbing. Despite the hundreds of thousands of falls climbers suffer every year, there are few recorded instances of a climbing rope breaking in a fall; the cases that do are often attributable to previous damage to, or contamination of, the rope. Climbing ropes, however, do cut easily when under load. Keeping them away from sharp rock edges is imperative.'

def play_game():
    user_difficulty=raw_input("What is your ideal difficulty. Choose easy, medium or hard: ")
    print("You have chosen " + user_difficulty)
    if user_difficulty=='easy':
        key1=['rope','tensile','compressive','wire']
        rope_challange1=censorship(key1,Rope_text1)
        print rope_challange1
        return filltheblank(4,rope_challange1,key1)
    elif user_difficulty=='medium':
        key2=['prehistoric','twisting','braiding','Fossilized']
        rope_challange2=censorship(key2,Rope_text2)
        return filltheblank(3,rope_challange2,key2)
    elif user_difficulty=='hard':
        key3=['elastic','stretch','falls','cut','sharp']
        rope_challange3=censorship(key3,Rope_text3)
        return filltheblank(2,rope_challange3,key3)
    else:
        return('Please enter a valid difficulty and try again.')
play_game()

'''  
def l_replacer(keys,text,blank):
    return map(lambda key : replacer(key,text,blank),keys)
def ll_replacer(keys,text,blanks):
    return map(lambda blank : l_replacer(keys,text,blank),blanks) 
                word = word.replace(replacement, user_input)
                replaced.append(word)

        for word in text:
            replacement = word_in_pos(word, keys)
            if replacement != None:
                
            else:
                replaced.append(word)
'''