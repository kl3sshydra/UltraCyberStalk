# UltraCyberStalk
customizable python OSINT tool for information gathering

# Setting up
```
git clone https://github.com/kl3sshydra/UltraCyberStalk
cd UltraCyberStalk
pip3 install -r requirements.txt
python3 main.py
```

# Customizing existing modules
All module customization can be done by editing the files inside of the CONFIG folder.<br>
Customizing dorks:<br>
Open the dorks.txt file and add your personal dorks,<br>
Replacing the target name with {target}<br><br>
![alt-text](https://github.com/kl3sshydra/UltraCyberStalk/raw/main/dorkscreenshot.png)
<br><br>
Customizing the usernamesearch module:<br>
The usernamesearch.txt file contains all urls where UltraCyberStalk will search the target on,<br>
Remember to replace your target with {target}.<br><br>
![alt-text](https://github.com/kl3sshydra/UltraCyberStalk/raw/main/usernamesearchscreenshot.png)
<br>When adding your urls, make sure to add the proper syntax in the usernamesearchresults.txt file,<br>
Otherwise UltraCyberStalk will not recognize an existing username.<br>
Status code example:<br>
```www.yoursite.com :: STATUSCODE :: 404```
<br>
This tells the program that on yoursite.com a non-existing user will be recognized via a 404 status code in the response.<br>
Content example:<br>
```www.yoursite.com :: CONTENT :: unregistered```
<br>
This tells the program that on yoursite.com a non-existing user will be recognized via the word unregistered in the response.<br>
![alt-text](https://github.com/kl3sshydra/UltraCyberStalk/raw/main/usernamesearchresultsscreenshot.png)

# Adding your custom modules
Adding your custom module on UltraCyberStalk is simpler to do than to explain, with the following steps:<br>
Go on the modules.py file and write your module:
```
class myepicmodule:
  def main(self):
     print("hello from my custom module!")
```
Once you finish writing your module its time to actually add it:<br>
Go on the commands.json file, you will find the other commands there.<br>
![alt-text](https://github.com/kl3sshydra/UltraCyberStalk/raw/main/commandscreenshot.png)<br>
You will notice that the commands here are stored following this syntax:
```
"mycommand": [
        "this is the descriptin of my cool command",
        "utils.myepicmodule()"
],
```
Once you finish adding the command you created, you will be able to see it in the 'help' menu of the program and to use it (even with the 'all' function)<br>
