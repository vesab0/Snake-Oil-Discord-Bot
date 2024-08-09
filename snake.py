
from discord.ext import commands
import discord
import random 
 #2.3.2

bot_token = "YOURBOTTOKEN"
channelid = YOURCHANNELID

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

profesione = ["Actor", "Alien Abductee", "Alien", "Amputee" "Astronaut", "Amputee","Astronaut","Babysitter","Bartender"
"Bank Robber","Biker","Billionaire", "Beggar","Big Foot", "Bridesmaid", "Bull Fighter","Camper","Bungee Jumper", 
"Caveman", "Cheerleader", "chef", "Class Clown", "Coach","Clown", "Coal Mĺner", "Cowboy" "Comedian", "Cupid", "Dad", "Dictator",
"Dumpster Diver", "Doctor", "executioner", "Dog", "Fire Fighter", "Fashion Model", "Fortune Teller", "Fisherman", "Geek", "Gladiator"
"Gambler", "Grandma", "Gangster", "High School Dropout", "Ghost", "Hippie", "Girl Scout", "Hitch Hiker", "Haunted House Actor",
"Immigrant", "High School Student", "Insomniac", "Hostage", "Kindergartener", "Hunter", "Life Guard", "Janitor", "Life Guard", 
"Last Person On Earth", "Lovers", "Lawyer", "Lumberjack", "Lottery Winner", "Mad Scientist","Magician" , "Ninja", "Nurse",
"Olympic Athlete", "Pirate","paparazzi", "Pizza Delivery", "Police Officer", "Police Officer", "Pop Singer", "Politician",
"Prisoner of War", "Pregnant Woman", "Prison Guard", "Priest", "pro Wrestler","Princess","protester", "Robot", "Queen", "Rock star",
"Rapper", "Roommate", "Referee", "School Bus Driver", "Rock Climber", "Soldier",  "Santa", "Sports Fan", "Senior Citizen","Spy",
"Snowman", "substitute Teacher", "Stewardess", "Tarzan", "Super Hero", "Taxi Driver", "Surfer","teenager", "Teacher", "Tourist",
"The President", "Vampire", "Therapist", "Villain", "Toddler", "Waitress", "Witch ", "Zombie"]

words = "axe baby bacon bacteria bag bait ball balloon banana bandana banner bar barricade basket bath battle bazooka beach beads beard bed bell belly belt berry bib bicycle bikini biscuit bladder blanket blender blimp blizzard blood board boat body bomb bone bonfire booger book boomerang boots bottle bowl box boy bra bracelet brain brick bridge broom brush bubble bucket buckle buddy bullet bunny burp bus bush butt butter butterfly button buzzer cactus caffine cage camera candle candy cane cannon canoe canteen cap cape car card carpet carrot case catapult cave chain chair chalk charm cheese chest chicken chili chip chocolate circus clamp claw cliff cloak clock closet cloud club coat coffin coin collar compass computer concert cone cookie corpse costume couch coupon courage cream crowd crown crystal cuddle cup curse curtain cushion dagger dance danger dare dart death debt decoy desire desk detector diamond diaper diary Dinosaur dirt discipline disease dispenser doll dolphin donkey doom door doubt dragon dream dress drill drone drool drum dumpster dung dungeon dust ear egg elephant emergency energy envelope envy eraser escape excuse exercise eye face fact factory failure fairy faith family fan fanny fantasy farm fart fate faucet fear feather fence fever film finger fire fish fitness flag flame flesh floss flower fluid flute foam fog food foot forest fork fountain freedom friend friendship fruit fuel funeral fur future fuzz galaxy game garbage garden gas gem germ geyser ghost giggle glasses glitter glory glove glue goggles gorilla gossip gown grass grave gravity gravy grease greed grenade grief grill guilt gum gun hair hammer hammock hamster hand handcuffs handle harmonica harmony harness hat hatchet head heart heaven hell helmet hole honey hood hoodie hook hoop hope hormone horn horse hose house hug hurricane ice idiot ink insect island jacket Jar jello jelly jewel jewelry joke joy juice jungle junk karate key kiss kit kite kitten knife lace ladder lady lake lamp lantern lasso laugh lava leaf leash leg light lightning lip lock locker lotion love machine magic magnet man map marker marriage marshmallow mask massage mattress maze meat medicine memory message milk mint miracle mirror missile mist mistake mitten money monkey monster mood moon mop mosquito motor mountain mouth movie mud mug murder muscle music musket mustache mystery nap napkin needle nest net news night nightmare noise noodle nose ocean odor oil oven oxygen pad paddle pail pain paint pajamas panda pants paper parachute parade parrot party passion paste patch paw peace pearl pen penalty pepper perfume permit pet phone photo pickle picnic picture pill pillow pimple pin pinata pipe pit pity plate pleasure plug plunger pocket poison pole poncho pool poop popcorn popsicle poster potion potty pouch powder prank prayer pregnancy pride prize probe promise protein pudding puddle puke pump pumpkin puppet puppy purse putty puzzle radar radiation radio raft rag rage rain rake razor reality recipe regret remote rescue revenge ribbon ring riot river road robe robot rock rocket rodeo romance rope rubber rug rumor sack saddle safety salad sand Sandwich satellite sauce sauna sausage saw scarf school scoop scooter scream sculpture seat secret security seed sensor shadow shame shampoo sheet shell shield shirt shoes shovel shower shrine signal silence siren skeleton skin skirt skull skunk sky sled sleep slide slime slipper smile smoke smoothie snake snore snot snow soap socks sofa song soup souvenir space spaghetti spear spider spike spirit spit sponge spray spring stage stain star statue steroid stew stick sticker stool storm story stove strap straw street stress string sugar suit sun surgery surprise sushi swamp sweat sweater swing switch sword syrup table taco tail tambourine tank tape tar tarp taser tattoo tax team tear telephone telescope tent test therapy thorn throat throne ticket tickle tie tiger time toe tofu toilet tomb tongue tooth torch tornado torpedo towel tower toy traffic trail training trampoline trap trash tray treadmill treasure tree trick trigger trophy truck trumpet trust truth tsunami tub tube tummy tumor tunnel turtle tutu tuxedo tv umbrella underwear unicorn uniform urge urinal vacation vaccine vacuum vapor vault velcro vest victory video vine virus vision vitamin voice volcano vomit wagon wall wand war water wax web wheel whip whistle wig wind window wings wire wisdom wish work worm yarn yawn zit"
letrat = words.split (" ")

profesione_discard = []
letrat_discard = []
global hand

@bot.event
async def on_ready():
    print('hii')
    channel = bot.get_channel(channelid)
    #await channel.send("ollla")

@bot.event
async def on_member_join(member):
    await member.send("E bon !play ti jep letrat kur i kqyr letrat edhe vendos cilat mi perdor e bon !use x y DMTH x y jon numrat e letrave qe don mi perdor ky ti ndrron nese je judge e bon !judge ti jep 2 opcione komandat te channel PER komanda sdi a punon ndyjat ama po pritoj me provu")

@bot.command()
async def judge(ctx):
    prof1 = random.choice(profesione)
    prof2 = random.choice(profesione)

    while prof1 == prof2:
        prof1 = random.choice(profesione)

    while prof1 in profesione_discard:
        prof1 = random.choice(profesione)
    
    while prof2 in profesione_discard:
        prof2 = random.choice(profesione)
    
    profesione_discard.append(prof1)
    profesione_discard.append(prof2)

    #channel = bot.get_channel(channelid)
    await ctx.send(prof1)
    await ctx.send(prof2)

@bot.command()
async def play(ctx):
    l1 = random.choice(letrat)
    l2 = random.choice(letrat)
    l3 = random.choice(letrat)
    l4 = random.choice(letrat)
    l5 = random.choice(letrat)
    l6 = random.choice(letrat)

    while l1 in letrat_discard:
        l1 = random.choice(letrat)
    while l2 in letrat_discard:
        l2 = random.choice(letrat)
    while l3 in letrat_discard:
        l3 = random.choice(letrat)
    while l4 in letrat_discard:
        l4 = random.choice(letrat)
    while l5 in letrat_discard:
        l5 = random.choice(letrat)
    while l6 in letrat_discard:
        l6 = random.choice(letrat)
    
    while l1 == l2 or l1 == l3 or l1 == l4 or l1 == l5 or l1 == l6:
        l1 = random.choice(letrat)
    while l2 == l1 or l2 == l3 or l2 == l4 or l2 == l5 or l2 == l6:
        l2 = random.choice(letrat)
    while l3 == l2 or l3 == l1 or l3 == l4 or l3 == l5 or l3 == l6:
        l3 = random.choice(letrat)
    while l4 == l2 or l4 == l3 or l4 == l1 or l4 == l5 or l4 == l6:
        l4 = random.choice(letrat)
    while l5 == l2 or l5 == l3 or l5 == l4 or l5 == l1 or l5 == l6:
        l5 = random.choice(letrat)
    while l6 == l2 or l6 == l3 or l6 == l4 or l6 == l5 or l6 == l1:
        l6 = random.choice(letrat)
    
    letrat_discard.append(l1)
    letrat_discard.append(l2)
    letrat_discard.append(l3)
    letrat_discard.append(l4)
    letrat_discard.append(l5)
    letrat_discard.append(l6)

    global hand
    hand = [l1,l2,l3,l4,l5,l6]

    await ctx.message.author.send("1. "+l1+" 2. "+l2+" 3. "+l3+" 4. "+l4+" 5. "+l5+" 6. "+l6)

@bot.command()
async def use(ctx,x,y):
    l1_new = random.choice(letrat)
    l2_new = random.choice(letrat)
    while l1_new in letrat_discard:
        l1_new = random.choice(letrat)
    while l2_new in letrat_discard:
        l2_new = random.choice(letrat)
    letrat_discard.append(l1_new)
    letrat_discard.append(l2_new)

    global hand
    hand[int(x) - 1] = l1_new
    hand[int(y) - 1] = l2_new

    await ctx.message.author.send("1. "+hand[0]+" 2. "+hand[1]+" 3. "+hand[2]+" 4. "+hand[3]+" 5. "+hand[4]+" 6. "+hand[5])

@bot.command()
async def clear(ctx):
    letrat_discard.clear()
    profesione_discard.clear() 
    print(letrat_discard)
    print(profesione_discard)

bot.run(bot_token)
