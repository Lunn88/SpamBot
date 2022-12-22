from time import sleep
from os import path as p
from sys import platform
from pyautogui import hotkey, press, hold
from pyperclip import copy

print("注意事項:")
print("1. 要先把你要發的文件移到跟這個exe同個文件夾\n"
      "   或是用絕對路徑 like:C:\\..\\..\\example.txt")
print("2. 輸入完發送次數會有兩秒的緩衝時間，請在此兩秒內點擊你要發送的窗口")
print("3. 支持Windows，可能支持macOS，可以試試看，為什麼是可能去問賈勃斯")
print("4. 我不希望半夜聽到我手機狂響 所以不要搞我 不想玩了直接關掉就好")
print("5. 想看源碼我有上傳到YT：https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("6. 雖然程式很簡單 但我還是想署名一下 因為感覺很屌\n"
      "\t\t\t\t\t\t\t\t\t\t--Lun")

path = input("請輸入文件路徑(記得末尾要加副檔名.txt):")
while (not p.exists(path)):
    path = input("文件不存在！請重新輸入:")

content = ""
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

