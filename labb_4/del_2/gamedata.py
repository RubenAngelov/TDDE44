ADVENTURE_TREE = {
    "Start" : ["Blue", "Red"],
    "Blue" : ["Chest", "Guard"],
    "Chest" : ["Take", "Leave"],
    "Take" : ["Sneak", "Talk"],
    "Leave" : ["Sneak", "Talk"],
    "Guard" : ["Sneak", "Talk"],
    "Sneak" : ["End"],
    "Talk" : ["Complement", "Joke"],
    "Complement" : ["End"],
    "Joke" : ["End"],
    "Red" : ["Flee", "Attack"],
    "Flee" : ["End"],
    "Attack" : ["End"]
}

DESCRIPTIONS = {
    "Start": """You enter a room, and you see a blue door to your left and a \
red door to your right.
Which door do you pick?""",
    "Blue": """You see a room with a wooden treasure chest on the left, and a \
sleeping guard on the right in front of the door.
What do you do?""",
    "Chest": """Let's see what's in here... /grins
The chest creaks open, and the guard is still sleeping. That's one heavy \
sleeper! You find some diamonds, a shiny sword, and lots of gold coins.
Do you take the treasure or leave it?""",
    "Take": """Woohoo! Bounty and a shiney new sword. /drops your crappy \
sword in the empty treasure chest.
Ooops! The noise has woken up the guard.
What do you do now?""",
    "Leave":
    """Leaving all the shinies behind hurts, but it feels safer for now.
Hopefully, it will still be here, right after you gets past this guard.
What do you do next?""",
    "Guard": """The guard seems to be deep in sleep, but he has a mean \
looking axe right beside him.
What do you do?""",
    "Sneak": """The guard jumps up and looks the other way, missing you \
entirely.
You just slipped through the door before the guard realised it.
You are now outside, home free! Huzzah!""",
    "Talk": """The guard approaches you, looking angry.""",
    "Complement": """You tell the guard that you like his armor and ask him how he got it that shiny.
He blushes and let's you past.""",
    "Joke": """You decide to tell the guard a joke and say the following:
'There are three types of people in the world: 
Those who can count and those who can’t.'
He looks at you with a blank face for a moment, and then swings his axe...""",
    "Red": """There you see the great evil Slathborg.
He, it, whatever stares at you and you go insane.
Do you flee for your life or attack it with your bare hands?""",
    "Flee": """You made it out alive, alas empty handed.""",
    "Attack": """You died. Well, at least the dragon thought you were tasty"""
}

OPTIONS = {
    "Blue": "Blue",
    "Red": "Red",
    "Chest": "Explore the chest",
    "Guard": "Advance toward the guard",
    "Take": "Grab all of the treasures",
    "Leave": "Leave them for another day",
    "Sneak": "Try to sneak past the guard",
    "Talk": "Talk to the guard",
    "Complement": "Complement the guard's armor",
    "Joke": "Tell a joke",
    "Flee": "Flee",
    "Attack": "Attack"
}