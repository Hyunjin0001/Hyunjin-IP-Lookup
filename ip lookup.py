import os , json    
os.system("color E")
from urllib.request import urlopen
from colorama import Fore

Choix = True
while Choix == True:
    ip = input(""" 

                                $$\   $$\                                   $$\           
                                $$ |  $$ |                                  \__|          
                                $$ |  $$ |$$\   $$\ $$\   $$\ $$$$$$$\  $$\ $$\ $$$$$$$\  
                                $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$  __$$\ \__|$$ |$$  __$$\ 
                                $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\ $$ |$$ |  $$ |
                                $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
                                $$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ |  $$ |$$ |$$ |$$ |  $$ |
                                \__|  \__| \____$$ | \______/ \__|  \__|$$ |\__|\__|  \__|
                                        $$\   $$ |              $$\   $$ |              
                                        \$$$$$$  |              \$$$$$$  |              
                                        \______/                \______/                                                          


Enter Ip > """)                             
    os.system('color B')
    os.system('color A')
    os.system('color C')
    os.system('color D')
    os.system('color E')
    os.system('color F')
    os.system('color B')
    os.system('color A')
    os.system('color C')
    os.system('color D')
    os.system('color F')
    os.system('color E')
    os.system('color A')
    os.system('color F')
    os.system('color D')
    os.system('color C')
    os.system('color A')
    os.system('color D')
    print(f'''

________  _______    ______   _______         ________  ______   _______   ________ 
/        |/       \  /      \ /       \       /        |/      \ /       \ /        |
$$$$$$$$/ $$$$$$$  |/$$$$$$  |$$$$$$$  |      $$$$$$$$//$$$$$$  |$$$$$$$  |$$$$$$$$/ 
   $$ |   $$ |__$$ |$$ |  $$ |$$ |__$$ |      $$ |__   $$ |  $$ |$$ |__$$ |   $$ |   
   $$ |   $$    $$< $$ |  $$ |$$    $$/       $$    |  $$ |  $$ |$$    $$<    $$ |   
   $$ |   $$$$$$$  |$$ |  $$ |$$$$$$$/        $$$$$/   $$ |  $$ |$$$$$$$  |   $$ |   
   $$ |   $$ |  $$ |$$ \__$$ |$$ |            $$ |     $$ \__$$ |$$ |  $$ |   $$ |   
   $$ |   $$ |  $$ |$$    $$/ $$ |            $$ |     $$    $$/ $$ |  $$ |   $$ |   
   $$/    $$/   $$/  $$$$$$/  $$/             $$/       $$$$$$/  $$/   $$/    $$/    

                         ps: j'adore quand tu m'utilise :)
''')

    
    
    url = urlopen('https://ipinfo.io/'+ ip)
    info = json.loads(url.read())
    try:
        ip = info['ip']
    except:
        ip = "Introuvable"

    try:
        country = info['country']
    except:
        country = "Introuvable"

    try:
        city = info['city']
    except:
        city = "Introuvable"

    try:
        region = info['region']
    except:
        region = "Introuvable"

    try:
        postal = info['postal']
    except:
        postal = "Introuvable"

    try:
        orga = info['org']
    except:
        orga = "Introuvable"

    try:
        timezone = info['timezone']
    except:
        timezone = "Introuvable"

    print(f"""
┣━━━━━━━━━━━━━━━━━━━━━━━
┃ Bien jouer le h4xor 
┃ Ip: {ip}
┃ Pays: {country}
┃ Ville: {city}
┃ Region: {region}
┃ Code Postal {postal}
┃ Operateur: {orga}   
┃ TimeZone {timezone}""")
    
    choix = input("┣━━━━━━━━━━━━━━━━━━━━━━━\n┃ Veux tu réessayer ? [Y/N] > ")

    if choix == "Y" or choix == "y":
        Choix = True
        
    else:
        Choix = False
    os.system('color F')    
        
