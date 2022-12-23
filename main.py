import time
from time import sleep
from os import path as p
from sys import platform

import pyautogui
from pyautogui import hotkey, press, hold
from pyperclip import copy

print("注意事項:")
print("1. 要發文件的話要先把你要發的文件移到跟這個exe同個文件夾\n"
      "   或是用絕對路徑 like:C:\\..\\..\\example.txt")
print("2. 手動輸入多行一樣會一行一行發，輸入結束則最後再單獨輸入一次 ok")
print("2. 輸入完發送次數會有兩秒的緩衝時間，請在此兩秒內點擊你要發送的窗口")
print("3. 支持Windows，可能支持macOS，可以試試看，為什麼是可能去問賈勃斯")
print("4. 不想玩了直接關掉就好，想看源碼我有上傳到YT：https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("6. 雖然程式很簡單 但我還是想署名一下 因為感覺很屌\n"
      "\t\t\t\t\t\t\t\t\t\t--Lun")

choice = input("1. 發文件\n2. 自己輸入\n請輸入 1 or 2 :")
retry = 0
while(choice != '1' and choice != '2'):
    choice = input("輸入無效！請輸入 1 or 2 :")
    retry += 1
    if(retry > 2):
        print("叫你輸 1 or 2")
        time.sleep(1)
        print("聽不懂是不是？？")
        time.sleep(1)
        print("聽不懂不要玩了")
        time.sleep(1)
        exit(0)

if(choice == '1'):
    content = ""
    path = input("請輸入文件路徑(記得末尾要加副檔名.txt):")
    while (not p.exists(path)):
        path = input("文件不存在！請重新輸入:")

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
        times = int(input("請輸入你要重複發送的次數(輸入n代表整個文件內容發送n次)"))
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
        print("請輸入(結束記得再單獨輸入一次 ok)：")
        tmp = str(input())
        while(tmp != "ok"):
            content.append(tmp)
            tmp = input()
        times = int(input("請輸入你要重複發送的次數(輸入n代表整個文件內容發送n次)"))
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