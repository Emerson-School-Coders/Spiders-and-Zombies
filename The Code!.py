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
        time.sleep(5)
    else:
        print("booo")
        time.sleep(5)
    bye()

def bye():
    print("I guess I'll send you on your way then old friend.")
    time.sleep(4)

    path()

def path():
    Path = input("You start going down a rickedy old path. You see a village in the distance. Setup camp('camp') or Keep Walking ('walk')")
    if Path == "camp":
        camp()

    else:
        walk()

def camp():
    print("You set up camp but can't get a fire started.")
    time.sleep(5)
    run()

def walk():
    print("The village is farther away than you think but you keep walking.")
    time.sleep(5)
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
    time.sleep(2)
    print("Game Over. 'Restart code to retry'")
          
def flee():
    print("You manage to get away and make it to the village.")
    time.sleep(3)
    print("You find a nice person and they let you have some food and time.sleep for the night.")
    time.sleep(5)
    print("When you wake up the village is abandoned. You wonder whats going on and run outside.")
    time.sleep(3)
    go = input("You start to enter a cave but don't know if it is a good idea. Go down 'go' or Don't go down 'dont'")
    if go == "go":
        down()
    else:
        dont()

def dont():
    print("As you are leaving a creeper comes behind you and blows you up.")
    time.sleep(2)
    print("Game Over. 'Restart code to retry'")
        
def down():
    print("You find an empty chest and decide to take it. Could be helpful later.")
    time.sleep(3)
    cave = input("You suddenly are attacked by behind. Fight 'fight' or Run 'run'")
    if cave == "fight":
        lucky()
    else:
        ded()

def ded():
    print("You try to blend into the cave but the spider has good eye sight and spots you.")
    time.sleep(3)
    print("Game Over. 'Restart code to retry'")

def lucky():
    print("You slay the spider and grab the string he drops.")
    time.sleep(4)
    print("You here a voice in the distance, it sounds like someone you know...")
    time.sleep(4)
    print("Cody comes around the corner and sees you.")
    time.sleep(3)
    print("Oh hello! I thought I might find you here")
    
    if Pizza == "yes":
        Win()
    else:
        Lose()

def Lose():
    print("Remember the Pizza question in the beginning? Yeah that kinda decides if you win or not, sorry f or not telling you!")
    time.sleep(4)
    print("But we're still friends, right?")
    time.sleep(3)
    print("Well then I will see you in the end old friend!")
    time.sleep(4)
    print("Game Over. 'Restart code to retry'")

def Win():
    print("Remember the Pizza question in the beginning? Yeah that kinda decides if you win or not, sorry for not telling you!")
    time.sleep(4)
    print("But because you entered yes you WIN!... a free back massage!")
    time.sleep(2)
    print("Yeah... That kinda sounded better in my head...")
    time.sleep(3)
    print("Well I will see you in the next game!")
    time.sleep(3)
    print("You WIN! Play my next game when it comes out!")
    
start()

