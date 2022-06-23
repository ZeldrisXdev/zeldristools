import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.commun import *

def search_for_updates():
    clear()
    setTitle("@@Zeldris Checking For Updates...")
    r = requests.get("https://github.com/ZeldrisXdev/zeldristools/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("@Zeldris New Update Found!")
        print(f'''\n\n                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝\n'''.replace('█', f'{b}█{y}'))
        discserver()
        print(f'''{y}[{Fore.RED}!{y}]{w}Looks like this @Zeldris {THIS_VERSION} is outdated...''')
        soup = BeautifulSoup(requests.get("https://github.com/ZeldrisXdev/zeldristools/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(f'{y}[{b}#{y}]{w} Update to the latest version (Y/N) ? ')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n{y}[{b}#{y}]{w} Updating...")
            setTitle(f'@Zeldris Updating...')

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("zeldristool-main.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("zeldristool-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("zeldristool-main.zip")
                cwd = os.getcwd()+'\\zeldristool\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), '@TIO.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('zeldris')
                setTitle('@Zeldris Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!", end="")
                os.startfile("@zeldris.py")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/ZeldrisXdev/zeldristools/archive/refs/heads/main.zip")
                with open("zeldristool-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("zeldristool-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("zeldristool-main.zip")
                cwd = os.getcwd()+'\\zeldristool-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                setTitle('@Zeldris Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!")
                if os.path.exists(os.getcwd()+'setup_tool.bat'):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd()+'start_tool.bat'):
                    os.startfile("start_tool.bat")
                os._exit(0)
