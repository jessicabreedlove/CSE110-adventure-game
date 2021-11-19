
#Level One

passed_1 = True
passed_2 = True
is_winner = True

print('Welcome to the Halloween Adventure! If you complete the course in one piece you will get a great reward')
name = input('Enter your hero\'s name:')

step1 = input('Step #1:\nTRUTH or DARE?\nYour first encounter on the Halloween Adenture is a dark alley. As you creep forward you see a glimpse of a hunched form at the end. With shadows disguising most of it\'s form, a hobgobblin asks you your first question: TRUTH or DARE?')

if step1.upper() == 'TRUTH':
    truth = input('TRUTH! Quick! Type in your greatest fear! ')
    print(f'{truth.upper()}!? Scary!')
    passed_1
elif step1.upper() == 'DARE':
    worms = input('DARE! You think you are pretty fearless, huh? You now have to eat fried worms for dinner. Will you EAT them?')
    if worms.upper() == 'EAT':
        print('Good job! They were gross, but you made it!')
        passed_1
    else: 
        passed_1 = False
else:
    passed_1 = False

#Level Two
if passed_1:
    step2 = input('You passed the hobgobblin\'s test! Once past it you enter an abandonded building. There are two staircases, one leading UP and one leading DOWN. Which way do you choose?')
     
    
    if step2.upper() == 'UP':
        print(f'The creaky staircase leads you to the roof of the building. Floating right in front of you is a witch riding a broomstick! After cackaling for a long stretch the witch says,"Welcome {name.capitalize()}! I\'ve been waiting for you. Here is your final challenge: Ride my broomstick accross town to the cemetary without falling."')
        
        #Level 3
        witch = input('You can FLY or REFUSE. What do you choose?')
        if witch.upper() == 'FLY':
            print('You are so brave! Good work! You fly the broom accross town to the cemetary.')
            passed_2
        elif witch.upper() == 'REFUSE':
            print('Looks like you weren\'t up for the challenge. Return to the beginning of the adventure.')
            passed_2 = False
        else:
            passed_2 = False
   
            
    elif step2.upper() == 'DOWN':
        print(f'The creaky stairs lead you down deep into the basement. Once at the bottom you see a wrapped mummy approaching from the abyss. After a long moan the mummy says: "Welcome {name.capitalize()}! I\'ve been waiting for you. Here is your final challenge: Crawl through this underground tunnel to the cemetary."')
      
       #Level 3 Alternative
        mummy = input('You can CRAWL or REFUSE. What do you choose?')
        if mummy.upper() == 'CRAWL':
            print('You are so brave! Good work! You crawl through the dark tunnel to the cemetary.')
            passed_2
        elif mummy.upper() == 'REFUSE':
            print('Looks like you weren\'t up for the challenge. Return to the beginning of the adventure.')
            passed_2 = False
        else:
            passed_2 = False
    else: 
        passed_2 = False
else:
    is_winner = False

#Winner
if passed_1 and passed_2:
    is_winner
    print(f'Congratulations {name.capitalize()}! Once you arrive at the cemetary you see a truck full of candy. Best Halloween haul ever!')
else:
    print(f'Sorry {name.capitalize()}. You lost. Maybe give it another shot?')