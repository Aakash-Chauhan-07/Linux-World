import subprocess as sp

print('!! -- Welcome to the tool - - !!\n\n')

print('Press 1: Open Chrome browser')
print('Press 2: Open vlc player')
print('Press 3: Open notepad')
print('Press 4: Creating directory')

ch = int(input('Enter Your choice: '))

if ch == 1:
    sp.run('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"', shell = True)
elif ch == 2:
    sp.run("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", shell = True)
elif ch == 3:
    sp.run("notepad.exe", shell = True)
elif ch == 4:
    dir = input("Enter your directory name: ")
    path = input("Enter path at which you want put in or write current for current directory: ")
    if path == 'current':
        sp.run(f"mkdir {dir}", shell = True)
    else:
        sp.run(f"mkdir {path} {dir}", shell = True)
else:
    print("Invalid choice")