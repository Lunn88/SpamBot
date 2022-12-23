import time
from time import sleep
from os import path as p
from sys import platform

from pyautogui import hotkey, press, hold
from pyperclip import copy

print("Notice:")
print("1. If you want to send file like txt, please move that file to the folder where your exe at.\n"
      "   Or use absolute path like:C:\\..\\..\\example.txt")
print("2. Manual input will send line by line, type a single 'ok' for ending your input.")
print("3. There's gonna be two seconds after entering how many times you to send.\n"
      "   click the window where you want to spam at within these two seconds.")
print("4. Works on Windows, probably works on mac, you can give it a shot."
      "   As for why, go ask Steve Jobs why don't just ust ctrl instead of command, control or some shits.")
print("5. Close the console window directly when you're done."
      "   I've uploaded the source code to Youtube：https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("6. I would love to have some foreign friends, so follow my instagram: lunlun_0805")

choice = input("1. send file\n2. Manual input\nplease input 1 or 2 :")
retry = 0
while(choice != '1' and choice != '2'):
    choice = input("Invalid input！please input 1 or 2 :")
    retry += 1
    if(retry > 2):
        print("Told you to input 1 or 2")
        time.sleep(1)
        print("Wut? can't read?")
        time.sleep(1)
        print("Then bye bye buddy.")
        time.sleep(1)
        exit(0)

if(choice == '1'):
    content = ""
    path = input("Please input the path(don't forget the '.txt' by the end of your file):")
    while (not p.exists(path)):
        path = input("No such file！Input again:")

    text = open(path, 'r',encoding='utf-8')
    while True:
        tmp = text.readline()
        content += tmp
        if (not tmp):
            if(content[-1]== '\n'):
                break
            else:
                content += '\n'
                break
    text.close()

    line = ""
    while True:
        times = int(input("How many times you want to send:(input n for sending the whole file for n times)"))
        sleep(2)
        for i in range(times):
            for word in content:
                if(word != '\n'):
                    line += word
                else:
                    copy(line)
                    if(platform == "win32"):
                        hotkey('ctrl', 'v')
                    elif(platform == "darwin"):
                        with hold('command'):
                            press('v')
                    press('enter')
                    line = ""
else:
    while(True):
        content = []
        print("Please input:(remember to enter a single ok by the end of your input)：")
        tmp = str(input())
        while(tmp != "ok"):
            content.append(tmp)
            tmp = input()
        times = int(input("How many times you want to send:(input n for sending the whole file for n times)"))
        sleep(2)
        while(times > 0):
            for line in content:
                copy(line)
                if (platform == "win32"):
                    hotkey('ctrl', 'v')
                elif (platform == "darwin"):
                    with hold('command'):
                        press('v')
                press('enter')
            times -= 1