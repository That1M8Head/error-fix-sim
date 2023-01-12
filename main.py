"""
Error Fixing Simulator - by Arsalan Kazmi
A small program that simulates a computer that can't start up.
"""

from time import sleep
from os import listdir
from os.path import isfile

def boot_main_system():
    """
    Load the VBOS (Very Broken Operating System) init script.
    In actuality this just breaks (on purpose ofc)
    """
    print("Loading main system.")
    sleep(4.5)
    if isfile("libmain.o"):
        print("System loaded successfully.")
    else:
        print("Could not find system library libmain.o.")
        print()
        print("ERROR! System drive mounted successfully, but the main system failed to start.")
        print("This could be due to a missing executable or a problem with the drive.")
sleep(1)
print("Loading VBOS...")
sleep(2)
print("Mounting drives and filesystems...")
sleep(2.5)
boot_main_system()
print("Dropping to recovery shell.")
print()
command = ""
while command != "exit":
    command = input("recovery ] ")
    if command in ("ls", "dir"):
        for x in listdir():
            print(x)
    elif command == "init":
        boot_main_system()
    elif command.split()[0] in ("sfc", "chkdsk", "scandisk"):
        print("This is not DOS!")
    elif command in ("", "exit"):
        pass
    elif command == "help":
        print("dir exit help init ls")
    elif ":q" in command:
        print("This is not vi!")
    else:
        print(f"{command.split()[0]} is an unknown command.")
print("Powering off system.")
