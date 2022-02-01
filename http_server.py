# By Vinay Tajane on 1st Feb 2022

import os
import webbrowser

# opening cmd executing command and closing cmd
os.system("start /B start cmd.exe @cmd /c ipconfig & ipconfig>%userprofile%\HTTP-Server\ip.txt")

# Searching in file for Default gateway
file = open('ip.txt')
for line in file:
    line = line.strip()
    if line.startswith('Default'):
        gate = line

col = gate.find(':')
col = int(col)
pos = col + 2
ip = gate[pos:]
web = "http://" + ip + ":8080"
webbrowser.open(web)
