###IMPORTING###
import random

###FUNCTIONS###
def adjust_costs():
    total_common_dust_cost = single_common_dust_cost * len(playset_common_list)
    total_uncommon_dust_cost = single_uncommon_dust_cost * len(playset_uncommon_list)
    total_rare_dust_cost = single_rare_dust_cost * len(playset_rare_list)
    total_legendary_dust_cost = single_legendary_dust_cost * len(playset_legendary_list)
    total_set_dust_cost = total_common_dust_cost + total_uncommon_dust_cost + total_rare_dust_cost + total_legendary_dust_cost

def commons_per_pack():
    userInput = input("How many commons do you get per pack? If you're checking Eternal, you may type 'Eternal'. Otherwise, please type a number.")
    if userInput.lower() == 'eternal':
        return int(8)
    else:
        return int(userInput)
def uncommons_per_pack():
    userInput = input("How many uncommons do you get per pack? If you're checking Eternal, you may type 'Eternal'. Otherwise, please type a number.")
    if userInput.lower() == 'eternal':
        return int(3)
    else:
        return int(userInput)

def get_common():
    global dust_amount
    global playset_common_list
    card_got = random.randint(0,common_count)
    if card_got in playset_common_list:
        playset_common_list.remove(card_got)
        adjust_costs()
    else:
        dust_amount += common_dust_gain

def get_uncommon():
    global dust_amount
    global playset_uncommon_list
    card_got = random.randint(0,uncommon_count)
    if card_got in playset_uncommon_list:
        playset_uncommon_list.remove(card_got)
        adjust_costs()
    else:
        dust_amount += uncommon_dust_gain

def get_rare():
    global dust_amount
    global playset_rare_list
    card_got = random.randint(0,rare_count)
    if card_got in playset_rare_list:
        playset_rare_list.remove(card_got)
        adjust_costs()
    else:
        dust_amount += rare_dust_gain

def get_legendary():
    global dust_amount
    global playset_legendary_list1
    card_got = random.randint(0,legendary_count)
    if card_got in playset_legendary_list:
        playset_legendary_list.remove(card_got)
        adjust_costs()
    else:
        dust_amount += legendary_dust_gain


def open_a_pack():
    for i in range(0,commons_per_pack):
        get_common()
    for i in range(0,int(uncommons_per_pack)):
        get_uncommon()
    legendary_roll = random.randint(0,10)
    if legendary_roll != 9:
        get_rare()
    else:
        get_legendary()

###VARIABLES###
##COMMON VARIABLES##
common_count = int(input('How many commons are in the set?'))
common_list = list(range(0,common_count))
commons_per_pack = commons_per_pack()
playset_common_list = []
common_dust_gain = 1
single_common_dust_cost = 50
#defines playset_common_list#
for num in common_list:
    playset_common_list.append(num)
    playset_common_list.append(num)
    playset_common_list.append(num)
    playset_common_list.append(num)
total_common_dust_cost = single_common_dust_cost * len(playset_common_list)
##UNCOMMON VARIABLES##                                                                                            I AM THE START OF THE BLOCKED CODE, INCLUDE ME WHEN CTRL-/
uncommon_count = int(input('How many uncommons are in the set?'))
uncommon_list = list(range(0,uncommon_count))
uncommons_per_pack = uncommons_per_pack()
playset_uncommon_list = []
uncommon_dust_gain = 10
single_uncommon_dust_cost = 100
#defines playset_uncommon_list#
for num in uncommon_list:
    playset_uncommon_list.append(num)
    playset_uncommon_list.append(num)
    playset_uncommon_list.append(num)
    playset_uncommon_list.append(num)
total_uncommon_dust_cost = single_uncommon_dust_cost * len(playset_uncommon_list)
##RARE VARIABLES##
rare_count = int(input('How many rares are in the set?'))
rare_list = list(range(0,rare_count))
rares_per_pack = 'null'
playset_rare_list = []
rare_dust_gain = 200
single_rare_dust_cost = 800
#defines playset_rare_list#
for num in rare_list:
    playset_rare_list.append(num)
    playset_rare_list.append(num)
    playset_rare_list.append(num)
    playset_rare_list.append(num)
total_rare_dust_cost = single_rare_dust_cost * len(playset_rare_list)
##LEGENDARY VARIABLES##
legendary_count = int(input('How many legendaries are in the set?'))
legendary_list = list(range(0,legendary_count))
legendaries_per_pack = 'null'
playset_legendary_list = []
legendary_dust_gain = 800
single_legendary_dust_cost = 3200
#defines playset_legendary_list#
for num in legendary_list:
    playset_legendary_list.append(num)
    playset_legendary_list.append(num)
    playset_legendary_list.append(num)
    playset_legendary_list.append(num)
total_legendary_dust_cost = single_legendary_dust_cost * len(playset_legendary_list)                                ##I AM THE END OF THE BLOCKED CODE, INCLUDE ME WHEN CTRL-/
##MASTER VARIABLES##
current_game = str(input("Which game will you be testing today? Currently supported games are 'Eternal'."))
need_half_legendaries = ''
need_all_legendaries = True
if need_all_legendaries == False:
    need_half_legendaries = input("Do you feel you need half the legendaries? This would mean you could get half of every playset, or full playsets of half the legendaries, etc etc. Again, type True for yes, and False for no.")
else:
    pass
dust_amount = int(input('How much dust do you currently have?'))
if need_all_legendaries == True:
    total_set_dust_cost = total_common_dust_cost + total_uncommon_dust_cost + total_rare_dust_cost + total_legendary_dust_cost
elif need_half_legendaries == True:
    total_set_dust_cost = total_common_dust_cost + total_uncommon_dust_cost + total_rare_dust_cost + (total_legendary_dust_cost / 2)
else:
    total_set_dust_cost = total_common_dust_cost + total_uncommon_dust_cost + total_rare_dust_cost
opened_packs = int(0)
biggest_pack_count = int(input("What's the highest amount of packs that can be bought in one bulk purchase?"))
cost_of_packs = int(input("How much do you pay for that purchase? Only type numbers and periods; no special characters."))
cost_per_pack = float(cost_of_packs) / float(biggest_pack_count)


for i in range(0,1000):
    runs = []
    runs.append(opened_packs)
    opened_packs = 0
    dust_amount = 0
    if current_game.lower() == "eternal":
        while total_set_dust_cost > dust_amount:            ##checks that you don't have enough dust to craft remaining set
            open_a_pack()
            dust_amount += 100                                   ##checks whether user can craft remainder of set, then cracks a pack if you can't
            opened_packs += 1
    else:
        "I can't understand the game you typed for me. Please close and retry running this."

print(str(float(sum(runs)/len(runs))))
