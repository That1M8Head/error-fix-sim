# Error Fixing Simulator - by Arsalan Kazmi
# A small program that simulates a computer that can't start up.

from time import sleep
sleep(1)
print("Loading VBOS...")
sleep(2)
print("Mounting drives and filesystems...")
sleep(2.5)
print("Loading main system.")
sleep(7)
print()
print("ERROR! System drive mounted successfully, but the main system failed to start.")
print("This could be due to a missing executable or a problem with the drive.")
print("Dropping to recovery shell.")
print()
command = ""
while command != "exit":
    command = input("recovery ] ")
    if command in ("ls", "dir"):
        print("Filesystem is empty.")
    elif command == "init":
        print("Could not find system library libmain.o.")
    elif command.split()[0] in ("sfc", "chkdsk", "scandisk"):
        print("This is not DOS!")
    elif command in ("", "exit"):
        pass
    else:
        print(f"{command} is an unknown command.")
print("Powering off system.")
