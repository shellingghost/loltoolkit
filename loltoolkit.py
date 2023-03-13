import curses
import socket
import json
from textParse import textParse
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 65432
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = "utf-8"

championLocation = 'C:/CS361/loltoolkit/ddragonData/dragontail-12.6.1/12.6.1/data/en_US/championFull.json'
summonerLocation = 'C:/CS361/loltoolkit/ddragonData/dragontail-12.6.1/12.6.1/data/en_US/summoner.json'

# --champion json object code
# opens data for champion info
jsonfile = open(championLocation,'r', encoding = "utf8")

champData = jsonfile.read()

# parse json data into data object
championObject = json.loads(champData)


# loop once and make a new dictionary with # and item name, keys and values respectively and use key to access json information
# build to check if valid item
championDict = {}
for k,v in championObject['data'].items():
    for key in v.keys():
        if key == 'name':
            championDict[v[key]] = k

# dictionary for sanitized input, case & "'" indifferent
championSanDict = {}
for k,v in championObject['data'].items():
    for key in v.keys():
        if key == 'name':
            sanKey = ''
            lowerKey = v[key].lower()
            for char in range(0,len(lowerKey)):
                if lowerKey[char] != "'":
                    sanKey += lowerKey[char]
            championSanDict[sanKey] = k

# --summonerability json object code
# opens data for sumAbility info
jsonfile = open(summonerLocation,'r', encoding = "utf8")
sumData = jsonfile.read()

# parse json data into data object
summonerObject = json.loads(sumData)

# build to check if valid item
summonerDict = {}
for k,v in summonerObject['data'].items():
    for key in v.keys():
        if key == 'name':
            lowerKey = v[key].lower()
            summonerDict[lowerKey] = k

def championCall(champion_name):
    sanName = ''
    for char in range(0,len(champion_name)):
        if champion_name[char] != "'":
            sanName += champion_name[char]
    san_champ_name = sanName.lower()

    if san_champ_name in championSanDict:
        # Start building string
        # to screen aspects of items
        # parsing func for description text
        champId = championSanDict[san_champ_name]
        name = championObject['data'][champId]['name']
        title = championObject['data'][champId]['title']

        champType = ''
        for type in range(len(championObject['data'][champId]['tags'])):
            champType += championObject['data'][champId]['tags'][type] + ' '

        stringReturn = 'Name: '
        stringReturn += name + '\n'
        stringReturn += 'Title: ' + title + '\n'
        stringReturn += champType + '\n \n' 

        # ability parser
        passive = 'Passive: ' + championObject['data'][champId]['passive']['name'] + '\n'
        passive += textParse(championObject['data'][champId]['passive']['description']) + '\n'
        stringReturn += passive + '\n'

        # build abilities
        abilityQ = championObject['data'][champId]['spells'][0]['name'] + '\n'
        abilityQ += textParse(championObject['data'][champId]['spells'][0]['description'])
        stringReturn += abilityQ + '\n'

        abilityW = championObject['data'][champId]['spells'][1]['name'] + '\n'
        abilityW += textParse(championObject['data'][champId]['spells'][1]['description'])
        stringReturn += abilityW + '\n'

        abilityE = championObject['data'][champId]['spells'][2]['name'] + '\n'
        abilityE += textParse(championObject['data'][champId]['spells'][2]['description'])
        stringReturn += abilityE + '\n'

        abilityR = championObject['data'][champId]['spells'][3]['name'] + '\n'
        abilityR += textParse(championObject['data'][champId]['spells'][3]['description'])
        stringReturn += abilityR + '\n'

        return(stringReturn)
    
    elif san_champ_name == 'random':
        champKeys = list(championSanDict.keys())
        san_champ_name = random.choice(champKeys)

        # to screen aspects of items
        champId = championSanDict[san_champ_name]
        name = championObject['data'][champId]['name']
        title = championObject['data'][champId]['title']

        champType = ''
        for type in range(len(championObject['data'][champId]['tags'])):
            champType += championObject['data'][champId]['tags'][type] + ' '

        stringReturn = 'Name: '
        stringReturn += name + '\n'
        stringReturn += 'Title: ' + title + '\n'
        stringReturn += champType + '\n \n' 

        # ability parser
        passive = 'Passive: ' + championObject['data'][champId]['passive']['name'] + '\n'
        passive += textParse(championObject['data'][champId]['passive']['description']) + '\n'

        stringReturn += passive + '\n'

        # build abilities
        abilityQ = championObject['data'][champId]['spells'][0]['name'] + '\n'
        abilityQ += textParse(championObject['data'][champId]['spells'][0]['description'])
        stringReturn += abilityQ + '\n'

        abilityW = championObject['data'][champId]['spells'][1]['name'] + '\n'
        abilityW += textParse(championObject['data'][champId]['spells'][1]['description'])
        stringReturn += abilityW + '\n'

        abilityE = championObject['data'][champId]['spells'][2]['name'] + '\n'
        abilityE += textParse(championObject['data'][champId]['spells'][2]['description'])
        stringReturn += abilityE + '\n'

        abilityR = championObject['data'][champId]['spells'][3]['name'] + '\n'
        abilityR += textParse(championObject['data'][champId]['spells'][3]['description'])
        stringReturn += abilityR + '\n'
        return(stringReturn)

    else:
        return('There is no champion by that name. Please hit "Enter" key to return to the menu.')



def summoner_call(sum_name):
    sum_name = sum_name.lower()
    if sum_name in summonerDict:
        summId = summonerDict[sum_name]
        name = summonerObject['data'][summId]['name']
        description = summonerObject['data'][summId]['description']
        range = str(summonerObject['data'][summId]['range'][0])
        cooldown = str(summonerObject['data'][summId]['cooldown'][0])
        resource = summonerObject['data'][summId]['resource']

        stringReturn = 'Name: '
        stringReturn += name + '\n'
        stringReturn += 'Description: ' + '\n'
        stringReturn += description + '\n'
        stringReturn += 'Range: ' + '\n'
        stringReturn += range + '\n'
        stringReturn += 'Cooldown: ' + '\n'
        stringReturn += cooldown + '\n'
        stringReturn += 'Resource:' + '\n'
        stringReturn += resource

        return stringReturn
    else:
        return('There is no summoner ability by that name. Please hit "Enter" key to return to the menu.')


def home_screen(window,option_sel):
    selection = ['Champion Lookup','Item Lookup','Summoner ability Lookup']
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2

    window.addstr(0,0,'Welcome to LoL Tool!')
    window.addstr(1,0,'From this screen you may search up information about League of Legends!')
    window.addstr(5,0,'Please choose from these functionalities:')


    for index,textString in enumerate(selection):
        y = mainH//2 + index
        # paint to screen selected match from main
        if index == option_sel:
            window.attron(curses.color_pair(1))
            window.addstr(y,0, textString)
            window.attroff(curses.color_pair(1))
        else:
            # if not selected, paint normal
            window.addstr(y,0, textString)
    window.refresh()

    press_check = True
    while press_check == True:
        press = window.getch()
        window.clear()

        if press == curses.KEY_UP and option_sel != 0:
            option_sel -= 1

        elif press == curses.KEY_DOWN and option_sel != len(selection)-1:
            option_sel += 1

        # Add to champion select, note home_screen at bottom
        # if enter was pressed
        elif press == press in [10]:
            press_check == False
            champ_sel = 0
            item_sel = 0
            summoner_sel = 0

            if option_sel ==0:
                champ_screen(window,champ_sel)

            elif option_sel ==1:
                item_screen(window,item_sel)

            elif option_sel ==2:
                summoner_screen(window,summoner_sel)

            window.refresh()
            window.getch()

        home_screen(window, option_sel)
        window.refresh()



def champ_screen(window,champ_sel):
    champion_options = ["Champion name","Random Champion","Return"]
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2
    window.addstr(0,0,'Welcome to the champion lookup screen')
    window.addstr(1,0,'Please enter a chamption name to get details on them or use the "Random Champion" function')

    for index,textString in enumerate(champion_options):
        y = mainH//2 + index
        # paint to screen selected match from main
        if index == champ_sel:
            window.attron(curses.color_pair(1))
            window.addstr(y,0, textString)
            window.attroff(curses.color_pair(1))
        else:
            # if not selected, paint normal
            window.addstr(y,0, textString)
    window.refresh()

    while True:
        press = window.getch()
        window.clear()
        if press == curses.KEY_UP and champ_sel != 0:
            champ_sel -= 1

        elif press == curses.KEY_DOWN and champ_sel != len(champion_options)-1:
            champ_sel += 1

        # Add to champion select, note home_screen at bottom
        # if enter was pressed
        elif press == press in [10]:
            if champ_sel == 0:
                window.addstr(0,0, f"Please enter a champion name: ")
                curses.echo()
                # Champion input
                champion_input = window.getstr(0,30)

                # function call for string of information
                # decode required as input turns it into bytes type
                returnString = championCall(champion_input.decode())
                window.addstr(0,0, returnString)

            elif champ_sel == 1:
                returnString = championCall('random')
                window.addstr(0,0, returnString)

            elif champ_sel == 2:
                home_screen(window, 0)

            window.refresh()
            window.getch()

        champ_screen(window,champ_sel)



def item_screen(window,item_sel):
    item_options = ["Item name","Return"]
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2

    window.addstr(0,0,'Welcome to the item lookup screen')
    window.addstr(1,0,'Please enter a item name to gather information or use the Return key to go back to the main menu:')

    for index,textString in enumerate(item_options):
        y = mainH//2 + index
        # paint to screen selected match from main
        if index == item_sel:
            window.attron(curses.color_pair(1))
            window.addstr(y,0, textString)
            window.attroff(curses.color_pair(1))
        else:
            # if not selected, paint normal
            window.addstr(y,0, textString)
    window.refresh()

    while True:
        press = window.getch()
        window.clear()
        if press == curses.KEY_UP and item_sel != 0:
            item_sel -= 1

        elif press == curses.KEY_DOWN and item_sel != len(item_options)-1:
            item_sel += 1

        # Add to champion select, note home_screen at bottom
        # if enter was pressed
        elif press == press in [10]:
            if item_sel == 0:
                window.addstr(0,0, "Please enter an item name: ")
                curses.echo()
                # USER INPUT****
                user_input = window.getstr(0,27)

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(ADDR)
                connected = True
                while connected:
                    client.send(user_input)
                    msg = client.recv(SIZE).decode(FORMAT)
                    connected = False
                # window add str, here
                window.addstr(3,0, msg)

            elif item_sel ==1:
                home_screen(window, 0)

            window.refresh()
            window.getch()

        item_screen(window,item_sel)

def summoner_screen(window,summoner_sel):
    summoner_options = ["Summoner ability name","Return"]
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2


    window.addstr(0,0,'Welcome to the item lookup screen')
    window.addstr(1,0,'Please enter a summoner ability to gather information:')

    for index,textString in enumerate(summoner_options):
        y = mainH//2 + index
        # paint to screen selected match from main
        if index == summoner_sel:
            window.attron(curses.color_pair(1))
            window.addstr(y,0, textString)
            window.attroff(curses.color_pair(1))
        else:
            # if not selected, paint normal
            window.addstr(y,0, textString)
    window.refresh()

    while True:
        press = window.getch()
        window.clear()

        if press == curses.KEY_UP and summoner_sel != 0:
            summoner_sel -= 1

        elif press == curses.KEY_DOWN and summoner_sel != len(summoner_options)-1:
            summoner_sel += 1

        # Add to champion select, note home_screen at bottom
        # if enter was pressed
        elif press == press in [10]:
            if summoner_sel == 0:
                window.addstr(0,0, f"Please enter a summoner ability: ")
                curses.echo()
                # Champion input
                summoner_input = window.getstr(0,33)
                returnString = summoner_call(summoner_input.decode())
                window.addstr(0,0, returnString)

            elif summoner_sel ==1:
                home_screen(window, 0)

            window.refresh()
            window.getch()

        summoner_screen(window,summoner_sel)

def main(window):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    window.addstr(0,0, f"Welcome!")
    window.addstr(3,0, f"On LoL Tool, you are able to look up information from the game 'League of Legends'")
    window.addstr(4,0, f"Using your Up, Down, and Enter keys, select what functionality you would like to use")
    window.addstr(5,0, f"If you would like to return to the home screen, please select the Return option on each tool page")
    window.addstr(6,0, f"Otherwise, when you are finished using LoL Tool, please push the Ctrl+C buttons together to exit the application")
    window.addstr(7,0, f"Press enter to go to the Home Screen")

    press = window.getch()
    if press == press in [10]:
        option_sel = 0
        home_screen(window,option_sel)

curses.wrapper(main)
