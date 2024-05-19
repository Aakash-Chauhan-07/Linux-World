import subprocess as sp
import webbrowser

# Options
print("\n",
    'Press 1: To Start Notepad', '\n',
    'Press 2: To Start Chrome', '\n',
    'Press 3: To Start Vlc player', '\n',
    'Press 4: Type the url or website link to open in Web Browser', '\n\n',
)

ch = int(input('Press the appropriate key for desired task: '))


if ch == 1:
    sp.run('notepad', shell = True)

elif ch == 2: 
    sp.run('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"', shell = True)

elif ch == 3:
    sp.run('"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"', shell = True)

elif ch == 4:
    url = input("-- Type the URL or website link to open in Web Browser -- \n")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    webbrowser.open(url)
