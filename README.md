## AltBot
A Discord bot for interfacing with a VirtualBox VM.
```
- Created by nicl83.
- Modded by Avanpost.
```

## Pre-Setup
1. Install Python 3.8. (If you're able to use `discord.py` with your version of Python 3.9, feel free to use 3.9.)
2. Install VirtualBox.
3. Install `discord.py`, `pystyle`, `colorama` and `pywin32` (or your COM library of choice for your platform)
4. Install `virtualbox` by following the instructions at [pypi](https://pypi.org/project/virtualbox/).

## Setup
1. Run `main.py` once. It should generate a new file, `altbot.ini`.
2. Open VirtualBox and create a VM with the same name you used for `vm_name` (if it doesn't already exist.)
3. Start the VM through VirtualBox.
4. Start the bot by running `main.py`.

## Commands
```
  help   Shows this message
  keys   Get a list of keys you can use with press
  mouse  Move mouse
  ping   Ping Pong!
  press  Send special keys to the VM
  screen Get a screenshot of the VM
  type   Sends a long string of text to the VM, followed by a newline
  upload Upload file (Beta)
  reload Reload the bot config files (Owner only)
  reset  Reset the VM (Owner only)
```
