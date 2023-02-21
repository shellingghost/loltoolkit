import curses


def home_screen(window,option_sel):
    selection = ['Champion Lookup','Item Lookup','Player Lookup']
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

        # try to nest the home screen into it's own block (press enter to get to home screen idea -> better for app as a whole?)

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
            player_sel = 0

            if option_sel ==0:
                champ_screen(window,champ_sel)

            elif option_sel ==1:
                item_screen(window,item_sel)

            elif option_sel ==2:
                player_screen(window,player_sel)


            window.refresh()
            window.getch()
        
        home_screen(window, option_sel)
        window.refresh()
    



def champ_screen(window,champ_sel):
    champion_options = ["Champion name","Return"]
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2


    window.addstr(0,0,'Welcome to the champion lookup screen')
    window.addstr(1,0,'Please enter a chamption name to get details on them')

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
                window.addstr(0,0, f"Welcome to the enter champ screen")    

            elif champ_sel ==1:
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
    window.addstr(1,0,'Please enter a item name to gather information:')

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
                window.addstr(0,0, f"Welcome to the item enter screen")    

            elif item_sel ==1:
                home_screen(window, 0) 

            window.refresh()
            window.getch()

        item_screen(window,item_sel)

def player_screen(window,player_sel):
    player_options = ["Player name","Return"]
    window.clear()
    # getting dimensions
    h, w = window.getmaxyx()
    mainH = (h+3)//2


    window.addstr(0,0,'Welcome to the item lookup screen')
    window.addstr(1,0,'Please enter a item name to gather information:')

    for index,textString in enumerate(player_options):
        
        y = mainH//2 + index

        # paint to screen selected match from main
        if index == player_sel:
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


        if press == curses.KEY_UP and player_sel != 0:
            player_sel -= 1
            
        elif press == curses.KEY_DOWN and player_sel != len(player_options)-1:
            player_sel += 1

        # Add to champion select, note home_screen at bottom
        # if enter was pressed
        elif press == press in [10]:
            if player_sel == 0:
                window.addstr(0,0, f"Welcome to the player search enter screen")    

            elif player_sel ==1:
                home_screen(window, 0) 


            window.refresh()
            window.getch()

        player_screen(window,player_sel)


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











#I want to make a helper function for selecting
# feed in object (list)
def selector(object):
    pass

curses.wrapper(main)
