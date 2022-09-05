import os , json
from urllib.request import urlopen
from colorama import Fore

Choix = True
while Choix == True:


    ip = input("""
┣━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┫  
┃                      ┃                         ┃
┃ IP Look Up Basique   ┃ Crédit : ┃✦ Hyunjin ✧#0001┃
┃                      ┃                         ┃
┣━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ For [Hiruma]:   https://discord.gg/hiruma    ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Enter Ip > """)                               

    url = urlopen('https://ipinfo.io/'+ ip)
    info = json.loads(url.read())

    try:
        ip = info['ip']
    except:
        ip = "Not found"

    try:
        country = info['country']
    except:
        country = "Not found"

    try:
        city = info['city']
    except:
        city = "Not found"

    try:
        region = info['region']
    except:
        region = "Not found"

    try:
        postal = info['postal']
    except:
        postal = "Not found"

    try:
        orga = info['org']
    except:
        orga = "Not found"

    try:
        timezone = info['timezone']
    except:
        timezone = "Not found"

    print(f"""
┣━━━━━━━━━━━━━━━━━━━━━━━
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
