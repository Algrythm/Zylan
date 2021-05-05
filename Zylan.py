import os
import time

import ctypes
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


print("Welcome to ZyLan Console! V3.5.1")
mapver = "V3.5.1"



while (True):
    code = input("root@Zylan>: ")
    if (code):
        if (code == " " or ""):
            print("Not a valid command.")

    if (code == "payam"):
        state = input("What to print: ")
        print(state)

    if (code == "cls"):
        os.system("cls")

    if (code == "exit"):
        exit()

    if (code == "help"):
        what = input("With what? instl, args, or cmds?: ")
        if (what == "cmds"):
            print("Commands are: payam, cls, exit, shutdown, pause, spam, color, files, sendkey, help, PNINSTL, start, vol, mkdir, taskkill, date, update, mapyter, cmd, time, diskpart, cd, tasklist, compressed, certreq, getmac, host, klist, mountvol, msinfo, rdc, qwinsta, sxstrace, vssadmin, cipher")

        if (what == "instl"):
            print("Download PYTHON off python.org to use this coding language.")
        if (what == "args"):
            print("Args List: Shutdown(s,r,i), Color(r,g,b,w,k), zylan(--version, --uninstall, --info, --owner), cipher(-e)")


    if (code == "pause"):
        input("Press any key to continue")
        os.system("cls")

    if (code == "shutdown"):
        que = input("Args: ")
        if (que == "r"):
            os.system("shutdown -r")
        if (que == "s"):
            os.system("shutdown -s")

        if (que == "i"):
            os.syetem("shutdown -i")
    
    if (code == "files"):
        print(os.system("tree"))

    if (code == "color"):
        arg = input("Args: ")
        if (arg == "r"):
            os.system("color 0c")

        if (arg == "g"):
            os.system("color 2")
        if (arg == "b"):
            os.system("color 1")
        if (arg == "w"):
            os.system("color 7")
        if (arg == "k"):
            os.system("color E")

    if (code == "spam"):
        waaaa = input("Spam what?: ")
        while (True):
            print(waaaa)

    if (code == "sendkey"):
        print("WARNING! THIS ONLY WORKS IF YOU HAVE PYNPUT INSTALLED! IF YOU DO NOT, USE THE COMMAND PNINSTL")
        key = input("What would you like to type: ")
        if (key):
            from pynput.keyboard import Key, Controller
            keyb = Controller()

            keyb.press(key)
            keyb.release(key)

    if (code == "PNINSTL"):
        os.system("pip install pynput")

    if (code == "start"):
        dirr = input("File location: ")
        os.system("start " + dirr)

    if (code == "vol"):
        print(os.system("vol"))

    if (code == "taskkill"):
        task = input("Task name: ")
        os.system("taskkill /f /IM " + task)
    
    if (code == "mkdir"):
        os.system("mkdir")

    if (code == "date"):
        os.system("date")

    if (code == "update"):
        browser = input("Enter your browser name! (chrome or msedge): ")
        if (browser == "chrome"):
            os.system("start chrome.exe https://github.com/Algrythm/MaDos")

        if (browser == "msedge"):
            os.system("start msedge.exe https://github.com/Algrythm/MaDos")

    if (code == "zylan"):
        print("Insufficient arguments provided!")

    if (code == "zylan --version"):
        print("Current Installed Zylan version is: " + mapver)

    if (code == "zylan --uninstall"):
        print("Uninstalling Zylan! Close program to cancel!")
        time.sleep(15)
        Mbox('Uninstalled!', "We're sorry to see you go! ):", 1)
        time.sleep(2)
        os.remove("Zylan.py")
        exit()

    if (code == "zylan --info"):
        print("Mapyter is a coding language coded my Marsden Cannon in Python.")

    if (code == "zylan --owner"):
        os.system("start chrome.exe https://www.youtube.com/channel/UC5yR6zakk5yEXmJ3iwKdiRQ")
    
    if (code == "cmd"):
        os.system("cmd")

    if (code == "time"):
        os.system("time")

    if (code == "tasklist"):
        os.system("tasklist")

    if (code == "diskpart"):
        os.system("diskpart")
    if (code == "cd"):
        os.system("cd")
    if (code == "compressed"):
        os.system("compact")
    if (code == "certreq"):
        os.system("certreq")
    if (code == "getmac"):
        os.system("getmac")
    if (code == "host"):
        os.system("hostname")
    if (code == "klist"):
        os.system("klist")
    
    if (code == "mountvol"):
        os.system("mountvol")
    
    if (code == "msinfo"):
        os.system("msinfo32")
    if (code == "rdc"):
        os.system("mstsc")
    if (code == "qwinsta"):
        os.system("qwinsta")
    if (code == "sxstrace"):
        os.system("sxstrace")
    if (code == "vssadmin"):
        os.system("vssadmin")
    
    if (code == "cipher"):
        argumentals = input("Args: ")
        if (argumentals == "-e"):
            os.system("cipher -e")
            print("Successfully ciphered all files in: C:")
        else:
            print("Invalid Arguments. Returning to C:")
            

    

   

    
        
        

    

    
