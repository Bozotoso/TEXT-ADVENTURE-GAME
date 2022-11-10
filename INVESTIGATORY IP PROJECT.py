import time
from sys import exit
import random

def ts():
    time.sleep(1.1)
    print()
     
def tl():
    time.sleep(1.9)
    print()
     
def welcome() : 
    print()
    print('   MENU : ') 
    print()
    print('Start or Quit')
    wels =input()
    if wels.upper() == 'START':
        intro()
    else : 
        exit()

def intro() :
   
    print('You wake up in a cave thinking to yourself how you got here')
    tl()
    print('You find a dimmly lit torch not so far from you.. ')
    tl()
    print('You\'re scared of the dark, you pick it up')
    tl()
    print('You want to get out as soon as possible')
    tl()
    print('           Whats your next move : ')
    tl()
    print('1.Scream  2.Call out for help  3.Explore the cave')
    intr = input('')
    if intr.upper() == 'SCREAM':
       
        print('You scream and let it all out, You feel a lot better now')
        tl()
        print('You go further into the cave')
        scene1()
    elif intr.upper() == 'CALL OUT FOR HELP' :
       
        print('You shout \"IS ANYONE THERE?? HELLOOO\" but no one answers')
        tl()
        print('You couldn\'t bear the loneliness')
        tl()
        print('You die from the fear of being alone')
        print('           THE END')
        exit()
    elif intr.upper() == 'EXPLORE THE CAVE':
        
        print('You bravely decide to explore the cave with nothing but your dim torch')
        scene1()
                
def scene1():
    tl()
    print('As You\'re going further and further into the cave ')
    tl()
    print('you feel the light getting closer')
    tl()
    print('But you also hear faint sounds of dancing and chanting')
    tl()
    print('You come across a tribal ritual')    
    tl()
    print('They\'re dancing around a fire')
    tl()
    print('Finally you\'ve found humans... more or less')
    tl()
    print('   Whats your next move :')
    tl()
    print('1.Ignore  2.Greet  3.Fight')
    scn1 = input()
    if scn1.upper() == 'IGNORE':
       
        print('You decide to ignore them')
        tl()
        print('You\'re way too for them anyways')
        tl()
        print('You go further into the cave only to find that...')
        tl()
        print('You\'ve been going in circles all this time')
        tl()
        print('You go crazy')
        tl()
        print('You find yourself joining the Tribals\' dancing ritual')
        tl()
        print('You decide to stay with them forever...')
        tl()
        print('             THE END')
        
    elif scn1.upper() == 'GREET':
        
        print('You decide to say hello')
        tl()
        print('Surprisingly they\'re very friendly')
        tl()
        print('You meet their leader')
        tl()
        print('His name is tum tum luck luck')
        tl()
        print('        What do u say to him :')
        tl()
        print('\"weird nose\"  \"How do i get out of here\"')
        tumtumluckluck()
        
    elif scn1.upper() == 'FIGHT':
        print('You decided to fight the tribe')
        tl()
        print('It\'s 1 Vs 30 but you\'re still confident you\'ll win')
        tl()
        print('You were wrong, very wrong')
        tl()
        print('They knocked you out and tied u with a rope in a matter of seconds')
        tl()
        print('They take you to their leader')
        tl()
        print('His name is tum tum luck luck')
        tl()
        print('        What do u say to him :')
        tl()
        print('\"weird nose\"  \"I just want to get out of here\"')
        tumtumluckluck()
        

def tumtumluckluck() : 
    tl()
    ttll = input()
    if ttll.upper() == 'WEIRD NOSE':
        
        print('They all look at you funny')
        tl()
        print('They kill you for disrespecting their leader')
        tl()
        print('...But it was worth it')
        tl()
        print('        THE END')
    elif (ttll.upper() == 'HOW DO I GET OUT OF HERE' or ttll.upper() == 'I JUST WANT TO GET OUT OF HERE') :
       
        print('he says,')
        tl()
        print('  \"Very well i will tell u how to get out of the cave\"')
        tl()
        print('  \"On one condition...\"')
        tl()
        print('  \"You have to kill the... RED GHOST!\"')
        tl()
        print('You in desperation, accept it')
        tl()
        print('  \"THE RED GHOST is a dangerous cannibal\"')
        tl()
        print('  \"You must kill him\"')
        findRG()

def findRG() :
    tl()
    print('You set out to find the RED GHOST')
    tl()
    print('You\'ve been walking for the past 3 days')
    tl()
    print('He\'s no where to be seen')
    tl()
    print('but wait!')
    tl()
    print('You look down... and see BLOODY FOOTPRINTS!')
    tl()
    print('He\'s near')
    tl()
    print('You follow the bloody footprints')
    tl()
    print('You\'ve come across what seems is the RED GHOST\'s hideout')
    tl()
    print('What\'s your move :')
    tl()
    print('1.Runaway  2.Call him names  3.Surprise attack')
    frg = input('')
    if frg.upper() == 'RUNAWAY' :
        
        print('You\'ve decided to runaway')
        tl()
        print('like a coward')
        tl()
        print('Tum Tum Luck Luck never tells u the exit of the cave')
        tl()
        print('You live your whole life in the cave')
        tl()
        print('            THE END')
    elif frg.upper() == 'CALL HIM NAMES' :
       
        print('You call him mean names like...')
        ts()
        print('Fatty')
        ts()
        print('And Dumb Dumb')
        tl()
        print('This makes him very sad')
        tl()
        print('He approaches to fight you!')
        fight()
    elif frg.upper() == 'SURPRISE ATTACK' :
        print('You hit him in the head with the torch')
        tl()
        print('It barely affects him, as he\'s wearing a helmet')
        tl()
        print('He approaches to fight you!')
        fight()
    
def fight() :
    
    sleep = time.sleep


    
    critchance = random.randint(0,10)
    
    crit = 2
    
    defended = random.randint(0,6)
    
    maxhealth= 35
    
    bhealthmax = 50


    def menu():

    	
    	
    	print("Your Health: {}".format(hp))
    	sleep(1)
    	print("THE RED GHOST\'s Health: {}".format(bosshp))
    	sleep(1)
    	print("\n[Attack] - Damages THE RED GHOST.\n[Defend] - Chance to block enemies attack.\n[Heal] - Regain some of your health.\n\n")

   
    def attack():

    	
    	sleep(.2)
    	print("You attack THE RED GHOST. \n")
    	
    	
    	critdmg = 1
    	
    	sleep(1)
    	
    	
    	if critchance == 10:
    		
    		
    		critdmg = damagedealt * crit
    		
    		
    	print("You dealt {} damage.\n".format(damagedealt * critdmg))

    	
    	return damagedealt * critdmg
   
    def defend():
    	
    	sleep(.2)
    	
    	print("You prepare your defences. \n")

    def heal():
    	
    	sleep(.2)
    	print("You wrap yourself in bandages. \n")
    	sleep(1)

    	
    	print("You gained {} health. \n".format(plushp))

    def battack():
    	
    	sleep(.2)
    	print("THE RED GHOST attacks you. \n")
    	sleep(1)

    	

    	if prompt == "DEFEND":
    		
    			print("You deflected the attack. \n")

    	else:
    		
    		print("You take {} damage. \n".format(damagetaken))

    def bdefend():
    	
    	
    	sleep(.2)

    	
    	if prompt == "ATTACK":
    		
    			print("THE RED GHOST deflected your attack. \n")
    	else:
    		
    		print("THE RED GHOST tried to deflect you attack...\n")
    		sleep(1)
    		
    		print("... but it failed")

    def bheal():
    	
    	
    	sleep(.2)
    	
    	print("THE RED GHOST regained {} health. \n".format(plusbhp))

   
    play = True
    hp = 20
    bosshp = 50
    while play == True:
    	
    	bturn = random.randint(1,6)

    	
    	damagedealt = random.randint(2,10)

    	
    	plushp = random.randint(5,12)

    	
    	plusbhp = random.randint(3,7)

    	
    	damagetaken = random.randint(1,8)

    	
    	if hp > 0 or bosshp > 0:

    		
    		if hp > 0:
    			menu()
    			
    			
    			prompt = input().upper()

    			
    			if prompt == "ATTACK":
    				if bturn != 5:
    					
    					bosshp = bosshp - attack()
    				sleep(1)

    			
    			elif prompt == "DEFEND":
    				
    				defend()
    				sleep(1)

    			
    			elif prompt == "HEAL":
    				
    				
    				heal()
    				
    				hp = hp + plushp
    				
    				if hp > maxhealth:
    					
    					hp = maxhealth
    				sleep(1)

    		
    		else:
    			break

    		
    		if bosshp > 0:
    			
    			if bturn < 5:
    				
    				battack()

    			
    				if prompt != "DEFEND":
    					
    					hp = hp - damagetaken
    					
    				sleep(1)
    				

    			
    			elif bturn == 5:
    				bdefend()
    				sleep(1)

    			
    			elif bturn == 6:
    				
    				bheal()

    				
    				bosshp = bosshp + plusbhp

    				if bosshp > bhealthmax:
    					bosshp = bhealthmax
    				sleep(1)

    		else:
    			break

    	
    	else:
    		play = False
    		break

    print("Your Health: {}".format(hp))
    print("THE RED GHOST\'s Health: {}".format(bosshp))


    if bosshp <= 0:
    	print("You Win!, YOU GET TO ESCAPE THE CAVE")

    elif hp <= 0:
    	print("You Lose!, YOU DIE")     
    print('THE END')

       
        

        
welcome()

    
        
      
      
      



