# Configure Ubuntu Subsystem for Windows

## Query Ubuntu version
- lsb_release -a
- be sure, that it's the newest version of Ubuntu:
```
No LSB modules are available.                                                                            
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal 
```

Caution. It may be that different versions are installed 
and you open the wrong bash. The best solution is to open 
Ubuntu 20.04 via the Microsoft Store and then pin the 
application to the taskbar. Otherwise, you will probably 
open the older version via the search function.

## Update system
```
$ sudo apt-get update
```
```
$ sudo apt-get upgrade
```
## Create user

1. First switch to root user if you're not already
Open cmd and type command:
```
$ ubuntu2004.exe config --default-user root
```

Go back to Ubuntu shell and create a new user
```
$ adduser username
```
give sudo rights to your new user
```
$ usermod -G sudo username
```

## Set path for home directory

current home directory path: 
```
/home/username
```
path you want to set as home directory 
```
/mnt/c/Users/username
```
1. First switch to root user if you're not already
open cmd and type command:
```
$ ubuntu2004.exe config --default-user root
```

2. Open Ubuntu shell as root
- set new home directory:
```
$ usermod -d /mnt/c/Users/username username
```

3. When done switch back to your user typing following command on cmd:
```
$ ubuntu2004.exe config --default-user username
```
4. Restart Ubuntu shell
- now your home directory is set new

### Error when opening shell after setting new home directory

- when starting ubuntu this error occurs:
```
: No such file or directoryr/bin/win-sudo/s/aliases   
```

#### SOLUTION 
Path is in 
```
/mnt/c/Users/username/bin/win-sudo/s/aliases
```
change path in .bashrc
```
$ sudo nano .bashrc
```
replace 
```
~/bin/win-sudo/s/path.sh 
```
with 
```
/mnt/c/Users/username/bin/win-sudo/s/path.sh
```
Error should now be fix

#### Prompt highlighting is gone after setting new home directory

- First shell was hightlighted with green username@PC and blue path
- after fixing home directory this is gone

#### Solution

- copy content from 
```
/home/username/.bashrc
```
go to 
```
/mnt/c/Users/username/.bashrc and paste content in there
```
Prompt Highlighting should work again

Note: Maybe copying content can be difficult in commandline editors 
for the workshop participants because the indentation is not transferred 
by pasting and you don't want to overwrite the lines that are already in ~/.bashrc.
Consider to let them copy first into a file:
```
$ cp /home/username/.bashrc bashskript.txt
```
and paste it manually through texteditor in their fileexplorer.
Be are that hidden folders must be seen then. You can make them visable 
by "Ansicht / [x] Ausgeblendete Elemente"

## Tips / To consider

### Copy / Paste
- copy with CTRL C
- Paste also with right click
- otherwise change properties to 
SHIFT+STRG+C/V

### Execute Python
$ ~/Anaconda3/python.exe script.py

- try set path as alias in .bashrc
```
alias python="~/Anaconda3/python.exe"
```- does not work so far
