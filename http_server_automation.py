# By Vinay Tajane on 1st Feb 2022
import os
import subprocess
import webbrowser

# Execute ipconfig command and save output to file
with open('ip.txt', 'w') as file:
    try:
        subprocess.run(['ipconfig'], stdout=file, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute ipconfig command: {str(e)}")

# Check if file exists before opening
file_path = 'ip.txt'
if os.path.exists(file_path):
    try:
        with open(file_path) as file:
            # Search for Default gateway
            for line in file:
                line = line.strip()
                if line.startswith('Default'):
                    gate = line
                    break
            else:
                print("Default gateway not found.")
                exit()
        
        # Extract IP address from the gateway line
        col = gate.find(':')
        if col != -1:
            pos = col + 2
            ip = gate[pos:]
            web = "http://" + ip + ":8080"
            
            # Open web browser with error handling
            try:
                webbrowser.open(web)
            except Exception as e:
                print(f"Failed to open web browser: {str(e)}")
        else:
            print("Invalid gateway format.")
    except IOError as e:
        print(f"Failed to read file '{file_path}': {str(e)}")
else:
    print(f"File '{file_path}' does not exist.")
