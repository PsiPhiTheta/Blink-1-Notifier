# blink-1-notifier
Scripts used by the blink(1)mk2 device for USB-LED notifications (weather and cryptocurrency ticker).

## Installation
0. Clone this repository on your local machine
1. Download & install the latest version of Blink1Control2 from [todbot's repository](https://github.com/todbot/blink1).
2. Run Blink1Control2 & go to "Event Sources" and select "Add event source".
3. Select "Add File".
4. Point the program to the path of the "Blink1W.txt" .txt file of your local clone of this repository (step 0).
5. Set the check time to 15s.
6. Repeat step 4 for the "Blink1BTC.txt" .txt file.
7. Set the check time to 5min.
8. Run the UpdaterBTC.py and UpdaterW.py scripts continuously in the background (using pythonw.exe) to keep the .txt files updated with the correct values. You may use the .vbs and .bat files to automate this on startup by simply shortcutting the .vbs scripts and adding them to the Windows startup folder (shell:startup in the powershell). Alternatively, for macOS, the same can be achieved with the .sh shell scripts. 
