import queries
import api
import os
import xml.etree.ElementTree as Et
from timer import *

game_timer: RepeatedTimer


def main():
    global game_timer
    conf_tree = Et.parse('config')
    conf_root = conf_tree.getroot()
    conf_settings = conf_root.find('settings')
    conf_timer = int(conf_settings.find('timer').text)

    if not os.path.exists('openToW.sqlite'):
        queries.setup(conf_root)

    reset()
    game_timer = RepeatedTimer(conf_timer, reset)
    menu_loop()


def reset():
    api.stop()
    queries.update_sectors()
    api.start()
    
    
def shutdown():
    game_timer.stop()
    api.stop()
    raise SystemExit
    

def menu_loop():
    while True:
        print_menu()
        response = input()
        menu_handler(response)


def menu_handler(response):
    try:
        menu_options[response]()
    except KeyError:
        pass


def print_menu():
    print("MAIN MENU:")
    print('0: Quit openTow')
        
        
menu_options = {
    '0': shutdown
}
    

if __name__ == "__main__":
    main()
