import time
global Pizza

def start():
    Name = input("Hola Senor! Oh wait... you don't speak spanish. Hello, my name is cody the computer. What's your name?")
    Pizza=""
    print("Hello "+Name+" I like Pizza, do you like pizza too? ")
    while Pizza!="yes" and Pizza!="no":
        Pizza = input("yes/no: ")
    if Pizza == "yes":
        print("I guess you arent so bad after all...")
        time.sleep(1)
    else:
        print("booo")
        time.sleep(1)
    bye()
    if Pizza == "yes":
        Win()
    else:
        Lose()

def bye():
    print("I guess I'll send you on your way then old friend.")
    time.sleep(1)

    path()

def path():
    Path = input("You start going down a rickedy old path. You see a village in the distance. Setup camp('camp') or Keep Walking ('walk')")
    if Path == "camp":
        camp()

    else:
        walk()

def camp():
    print("You set up camp but can't get a fire started.")
    time.sleep(1)
    run()

def walk():
    print("The village is farther away than you think but you keep walking.")
    time.sleep(1)
    fight()

def fight():
    fight = input("you are just about to the village when... a horde of zombies attack! Run 'run' or fight 'fight'")
    if fight == "run":
        flee()
    else:
        bad()
        
def run():
    run =  input("you are almost all set up when... a horde of zombies attack! Run 'run' or fight 'fight'")
    if run == "run":
        flee()
    else:
        bad()
        
def bad():
    print("You manage to kill one zombie but the rest swarm you")
    time.sleep(1)
    print("Game Over. 'Restart code to retry'")
          
def flee():
    print("You manage to get away and make it to the village.")
    time.sleep(1)
    print("You find a nice person and they let you have some food and sleep for the night.")
    time.sleep(1)
    print("When you wake up the village is abandoned. You wonder whats going on and run outside.")
    time.sleep(1)
    go = input("You start to enter a cave but don't know if it is a good idea. Go down 'go' or Don't go down 'dont'")
    if go == "go":
        down()
    else:
        dont()

def dont():
    print("As you are leaving a creeper comes behind you and blows you up.")
    time.sleep(1)
    print("Game Over. 'Restart code to retry'")
        
def down():
    print("You find a chest and decide to loot it. A sword! Could be helpful later.")
    time.sleep(1)
    cave = input("You suddenly are attacked by behind. Fight 'fight' or Run 'run'")
    if cave == "fight":
        lucky()
    else:
        ded()

def ded():
    print("You try to blend into the cave but the spider has good eye sight and spots you.")
    time.sleep(1)
    print("Game Over. 'Restart code to retry'")

def lucky():
    print("You slay the spider and grab the string he drops.")
    time.sleep(1)
    print("Hey the sword came in handy!")
    time.sleep(1)
    print("You here a voice in the distance, it sounds like someone you know...")
    time.sleep(1)
    print("Cody comes around the corner and sees you.")
    time.sleep(1)
    print("Oh hello! I thought I might find you here")
    
    
def Lose():
    print("Remember the Pizza question in the beginning? Yeah that kinda decides if you win or not, sorry f or not telling you!")
    time.sleep(1)
    print("But we're still friends, right?")
    time.sleep(1)
    print("Well then I will see you in the end old friend!")
    time.sleep(1)
    print("Game Over. 'Restart code to retry'")

def Win():
    print("Remember the Pizza question in the beginning? Yeah that kinda decides if you win or not, sorry for not telling you!")
    time.sleep(1)
    print("But because you entered yes you WIN!... a free back massage!")
    time.sleep(1)
    print("Yeah... That kinda sounded better in my head...")
    time.sleep(1)
    print("Well I will see you in the next game!")
    time.sleep(1)
    print("You WIN! Play my next game when it comes out!")
    
start()

