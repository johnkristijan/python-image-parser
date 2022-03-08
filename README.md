# python-image-parser
Python parser to map an image into pixel xy locations for use in e.g. Minecraft build scripting

# setup
`python -m venv venv`
activate venv and install dependencies
`pip install Pillow`
run script
`python parser.py`

# example usage
The parser.py script will generate a set of buildcommands in the `buildcommands.txt` file
1. create a script on your minecraft server called `mcc.sh` with the following content:
```
#!/bin/sh
screen -S ranheim-minecraft-server -X stuff "$1^M"
```
NOTE: ranheim-minecraft-server must be replaced with the correct screen name

2. in the directory with the buildcommands.txt file, execute this command:
`ssh predator@84.210.210.61 'cd mc_scripts; bash -s' < buildcommands.txt`
NOTE: replace ssh login info with your username@server_ip and the cd mc_scripts part is to navigate to the mcc.sh script location on the server

3. enter your password and voila!
NOTE: save your ssh password so you dont need to add the password each time