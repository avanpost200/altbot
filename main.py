import virtualbox, discord, sys, asyncio, traceback
from discord.ext import commands
from configparser import ConfigParser as configparser
import pystyle
from colorama import Fore
import os
import platform
import logging

def logo():
    print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_cyan, """
░█████╗░██╗░░░░░████████╗██████╗░░█████╗░████████╗
██╔══██╗██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
███████║██║░░░░░░░░██║░░░██████╦╝██║░░██║░░░██║░░░
██╔══██║██║░░░░░░░░██║░░░██╔══██╗██║░░██║░░░██║░░░
██║░░██║███████╗░░░██║░░░██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░"""))

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def config_creator(config_file_name):
    config = configparser()
    config_check = True

    while config_check:
        alt_token = input(f"{Fore.BLUE}[1/5] Enter bot token: ")
        alt_prefix = input(f"{Fore.BLUE}[2/5] Enter bot prefix (You can leave this field blank to enter the value \"alt!\"): ")
        alt_vm_name = input(f"{Fore.BLUE}[3/5] Enter the name of the virtual machine: ")
        alt_owner_id = input(f"{Fore.BLUE}[4/5] Enter the virtual machine owner ID: ")
        alt_channel_id = input(f"{Fore.BLUE}[5/5] Enter the channel ID for sending logs (You can skip this step): ")

        if alt_prefix == "":
            alt_prefix = "alt!"

        config['altbot'] = {}
        config['altbot']['token'] = alt_token
        config['altbot']['prefix'] = alt_prefix
        config['altbot']['vm_name'] = alt_vm_name
        config['altbot']['owner_id'] = alt_owner_id
        config['altbot']['channel_id'] = alt_channel_id
        with open(config_file_name, 'w') as f:
            config.write(f)
        print(f"{Fore.GREEN}[+] Setup completed successfully!")

        clear_console()
        return

def load_config(config_file_name):
    logo()
    config_check = True

    while config_check:
        config = configparser()

        try:
            with open(config_file_name, 'r') as w:
                config.read(config_file_name)
            print(f"{Fore.GREEN}[+] Config loaded succesfully!")
        except:
            config_creator(config_file_name)
            logo()
            break

        if len(config['altbot']['token']) < 8:
            print(f"{Fore.RED}[!] altbot.ini contains invalid data. Altbot will now terminate.")
            sys.exit(1)
        else:
            return_config = []
            return_config.append(config['altbot']['token'])
            return_config.append(config['altbot']['prefix'])
            return_config.append(config['altbot']['vm_name'])
            return_config.append(int(config['altbot']['owner_id']))

            if config['altbot']['channel_id'] != "":
                return_config.append(int(config['altbot']['channel_id']))
            return return_config

config_file = "altbot.ini"
try:
    token, prefix, vm_name, owner_id, channel_id = load_config(config_file)
except:
    token, prefix, vm_name, owner_id = load_config(config_file)
    channel_id = None

print(f"{Fore.YELLOW}[*] Modded by {Fore.LIGHTCYAN_EX}Avanpost (GitHub: avanpost200)")
print(f"{Fore.YELLOW}[*] Prefix: {Fore.BLUE}{prefix}")
print(f"{Fore.YELLOW}[*] VM name: {Fore.BLUE}{vm_name}")
print(f"{Fore.YELLOW}[*] Owner ID: {Fore.BLUE}{owner_id}")
if channel_id != None:
    print(f"{Fore.YELLOW}[*] Channel ID: {Fore.BLUE}{channel_id}")

keycodes = {
    'esc': (0x01, 0x81),
    '1': (0x02, 0x82),
    '2': (0x03, 0x83),
    '3': (0x04, 0x84),
    '4': (0x05, 0x85),
    '5': (0x06, 0x86),
    '6': (0x07, 0x87),
    '7': (0x08, 0x88),
    '8': (0x09, 0x89),
    '9': (0x0A, 0x8A),
    '0': (0x0B, 0x8B),
    '-': (0x0C, 0x8C),
    '+': (0x0D, 0x8D),
    'backspace': (0x0E, 0x8E),
    'tab': (0x0F, 0x8F),
    'q': (0x10, 0x90),
    'w': (0x11, 0x91),
    'e': (0x12, 0x92),
    'r': (0x13, 0x93),
    't': (0x14, 0x94),
    'y': (0x15, 0x95),
    'u': (0x16, 0x96),
    'i': (0x17, 0x97),
    'o': (0x18, 0x98),
    'p': (0x19, 0x99),
    '[': (0x1A, 0x9A),
    ']': (0x1B, 0x9B),
    'enter': (0x1C, 0x9C),
    'ctrl': (0x1D),
    'a': (0x1E, 0x9E),
    's': (0x1F, 0x9F),
    'd': (0x20, 0xA0),
    'f': (0x21, 0xA1),
    'g': (0x22, 0xA2),
    'h': (0x23, 0xA3),
    'j': (0x24, 0xA4),
    'k': (0x25, 0xA5),
    'l': (0x26, 0xA6),
    ';': (0x27, 0xA7),
    "'": (0x28, 0xA8),
    '~': (0x29, 0xA9),
    'shift': (0x2A),
    '\\': (0x2B, 0xAB),
    'z': (0x2C, 0xAC),
    'x': (0x2D, 0xAD),
    'c': (0x2E, 0xAE),
    'v': (0x2F, 0xAF),
    'b': (0x30, 0xB0),
    'n': (0x31, 0xB1),
    'm': (0x32, 0xB2),
    ',': (0x33, 0xB3),
    '.': (0x34, 0xB4),
    '/': (0x35, 0xB5),
    'rshift': (0x36),
    'numpad*': (0x37, 0xB7),
    'alt': (0x38),
    'space': (0x39, 0xB9),
    'caps': (0x3A, 0xBA),
    'f1': (0x3B, 0xBB),
    'f2': (0x3C, 0xBC),
    'f3': (0x3D, 0xBD),
    'f4': (0x3E, 0xBE),
    'f5': (0x3F, 0xBF),
    'f6': (0x40, 0xC0),
    'f7': (0x41, 0xC1),
    'f8': (0x42, 0xC2),
    'f9': (0x43, 0xC3),
    'f10': (0x44, 0xC4),
    'f11': (0x57, 0xD7),
    'f12': (0x58, 0xD8),
    'numlock': (0x45),
    'scrolllock': (0x46),
    'numpad1': (0x4F, 0xCF),
    'numpad2': (0x50, 0xD0),
    'numpad3': (0x51, 0xD1),
    'numpad4': (0x4B, 0xCB),
    'numpad5': (0x4C, 0xCC),
    'numpad6': (0x4D, 0xCD),
    'numpad7': (0x47, 0xC7),
    'numpad8': (0x48, 0xC8),
    'numpad9': (0x49, 0xC9),
    'numpad0': (0x52, 0xD2),
    'numpad+': (0x4E, 0xCE),
    'numpad.': (0x53, 0xD3),
    'keypad-': (0x4A, 0xCA),
    'up': (0xE0, 0x48, 0xE0, 0xC8),
    'left': (0xE0, 0x4B, 0xE0, 0xCB),
    'right': (0xE0, 0x4D, 0xE0, 0xCD),
    'down': (0xE0, 0x50, 0xE0, 0xD0),
    'pgup': (0xE0, 0x49, 0xE0, 0xC9),
    'pgdown': (0xE0, 0x51, 0xE0, 0xD1),
    'win': (0xE0, 0x5B, 0xE0, 0xDB),
    'а': (0x91),
    'б': (0x92),
    'в': (0x93),
    'г': (0x94),
    'д': (0x95),
    'е': (0x96),
    'ё': (0xA1, 0x8A),
    'ж': (0x97),
    'з': (0x98),
    'и': (0x99),
    'й': (0x9A),
    'к': (0x9B),
    'л': (0x9C),
    'м': (0x9D),
    'н': (0x9E),
    'о': (0x9F),
    'п': (0xA0),
    'р': (0xA1),
    'с': (0xA2),
    'т': (0xA3),
    'у': (0xA4),
    'ф': (0xA5),
    'х': (0xA6),
    'ц': (0xA7),
    'ч': (0xA8),
    'ш': (0xA9),
    'щ': (0xAA),
    'ъ': (0xAB),
    'ы': (0xAC),
    'ь': (0xAD),
    'э': (0xAE),
    'ю': (0xAF),
    'я': (0xB0)
}

bot = commands.Bot(command_prefix = prefix, intents=discord.Intents.all())
bot.remove_command("help") # Removing the standard help message
bot.owner_id = owner_id
bot.channel_id = channel_id
bot.mouse_state = 0

bot.vbox = virtualbox.VirtualBox()
bot.vm = bot.vbox.find_machine(vm_name)
bot.session = bot.vm.create_session()

@bot.event
async def on_ready():
    print(f"{Fore.YELLOW}[*] Total servser: {Fore.BLUE}{len(bot.guilds)}")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"AltBot - VM: {vm_name} - Help command: {prefix}help - Created by Avanpost (GitHub: avanpost200)"))
    if channel_id != None:
        get_vm_screenshot(bot.session, 'temp.png')
        channel = bot.get_channel(bot.channel_id)
        await channel.send('[+] Altbot has started!\n[*] Current VM state:', file=discord.File('temp.png'))
        os.remove('temp.png')

@bot.event
async def on_command_error(ctx, exception):
    tb_data = ''.join(traceback.format_tb(exception.__traceback__))
    await ctx.send(f"[-] Sorry, an error occurred.\n```\n{repr(exception)}\n{tb_data}\n```")

@bot.event
async def on_guild_join(guild):
    print(f"{Fore.GREEN}[+] The bot has been added to the server \"{guild}\"")
    print(f"{Fore.YELLOW}[*] Total servser: {Fore.BLUE}{len(bot.guilds)}")

@bot.event
async def on_guild_remove(guild):
    print(f"{Fore.RED}[-] The bot has been removed to the server \"{guild}\"")
    print(f"{Fore.YELLOW}[*] Total servser: {Fore.BLUE}{len(bot.guilds)}")


#Help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="AltBot - Commands", description=f"{prefix}help - Shows this message\n{prefix}keys - Get a list of keys you can use with press\n{prefix}mouse - Move mouse\n{prefix}ping - Ping pong\n{prefix}press - Send special keys to the VM\n{prefix}screen - Get a screenshot of the VM\n{prefix}type - Sends a long string of text to the VM, followed by a newline\n{prefix}upload - Upload file (Beta)\n{prefix}reload - Reload the bot config files (Owner only)\n{prefix}reset - Reset the VM (Owner only)")
    embed.set_footer(text="Created by Avanpost (GitHub: avanpost200)")
    await ctx.send(embed=embed)

#Ping pong!
@bot.command()
async def ping(ctx):
    """Ping Pong!
    
    If the bot is alive, it will reply with "Pong!\""""
    await ctx.send('[+] Pong!')

#Get image of VM
def get_vm_screenshot(vm_sesh, file_name):
    h, w, _, _, _, _ = vm_sesh.console.display.get_screen_resolution(0)
    png = vm_sesh.console.display.take_screen_shot_to_array(0, h, w, virtualbox.library.BitmapFormat.png)
    with open(file_name, 'wb') as file:
        file.write(png)

@bot.command()
async def screen(ctx):
    """Get a screenshot of the VM."""
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

@bot.command()
async def upload(ctx):
    """Uploads a file to the VM."""
    if file_path is None and len(ctx.message.attachments) == 0:
        await ctx.send("[-] Please specify a file path or attach a file to the command.")
        return

    attachment = ctx.message.attachments[0]
    file_name = attachment.filename
    file_path = f"temp/{file_name}"
    await attachment.save(file_path)

    with open(file_path, 'rb') as file:
        content = file.read()
    bot.session.put_file(file_name, content)
    await ctx.send(f'[+] File "{file_name}" uploaded successfully!')

    if os.path.exists(file_path):
        os.remove(file_path)


#Send long string or normal chars to VM
@bot.command()
async def type(ctx, *, arg):
    """Sends a long string of text to the VM, followed by a newline."""
    bot.session.console.keyboard.put_keys(arg + '\n')
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Send special buttons to the VM
def release_special_keys(key_session):
    release_codes = [0x9d, 0xaa, 0xb8, 0xb6]
    key_session.console.keyboard.put_scancodes(release_codes)

@bot.command()
async def press(ctx, *args):
    """Send special keys to the VM.
    
    Get a list of valid keys with vb!keys. Also accepts a sequence of keys."""
    try:
        temp_scancodes = []
        for key in args:
            if isinstance(keycodes[key], int):
                temp_scancodes.append(keycodes[key])
            else:
                temp_scancodes = [*temp_scancodes, *keycodes[key]]
        bot.session.console.keyboard.put_scancodes(temp_scancodes)
        release_special_keys(bot.session)
        await asyncio.sleep(0.5)
        get_vm_screenshot(bot.session, 'temp.png')
        await ctx.send('[+] Done!', file=discord.File('temp.png'))
        bot.session.console.keyboard.release_keys()
        os.remove('temp.png')
    except Exception as e:
        print(repr(e))
        await ctx.send("[-] Something went wrong whilst doing that, try again or check the log!")

#Send a mouse command
@bot.group()
async def mouse(ctx):       
    if ctx.invoked_subcommand is None:
        await ctx.send(f"[-] Unknown mouse command, do {prefix}help mouse for valid commands!")

#Click the mouse
@mouse.command()
async def click(ctx, *args):
    bot.mouse_state = 0x01
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    bot.mouse_state = 0x00
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Click and hold the mouse
@mouse.command()
async def clickhold(ctx, *args):
    bot.mouse_state = 0x01
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Right click the mouse.
@mouse.command()    
async def rclick(ctx, *args):
    bot.mouse_state = 0x02
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    bot.mouse_state = 0x00
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Right click and hold the mouse.
@mouse.command()
async def rclickhold(ctx, *args):
    bot.mouse_state = 0x02
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Stop holding any mouse buttons (reset state to 0).
@mouse.command()
async def release(ctx, *args):
    bot.mouse_state = 0x00
    bot.session.console.mouse.put_mouse_event(0, 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Move the mouse right (+X).
@mouse.command()
async def right(ctx, pixels):
    bot.session.console.mouse.put_mouse_event(int(pixels), 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Move the mouse left (-X).
@mouse.command()
async def left(ctx, pixels):
    bot.session.console.mouse.put_mouse_event(0-int(pixels), 0, 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Move the mouse down (+Y).
@mouse.command()
async def down(ctx, pixels):
    bot.session.console.mouse.put_mouse_event(0, int(pixels), 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Move the mouse up (-Y).
@mouse.command()
async def up(ctx, pixels):
    bot.session.console.mouse.put_mouse_event(0, 0-int(pixels), 0, 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Scroll the mouse wheel.
@mouse.command()
async def scroll(ctx, pixels):
    bot.session.console.mouse.put_mouse_event(0, 0, int(pixels), 0, bot.mouse_state)
    await asyncio.sleep(0.5)
    get_vm_screenshot(bot.session, 'temp.png')
    await ctx.send('[+] Done!', file=discord.File('temp.png'))
    os.remove('temp.png')

#Send a raw put_mouse_event command.
@mouse.command()
async def rawcommand(ctx, *args):
        if len(args) == 5:
            bot.session.console.mouse.put_mouse_event(int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            await asyncio.sleep(0.5)
            get_vm_screenshot(bot.session, 'temp.png')
            await ctx.send('[+] Done!', file=discord.File('temp.png'))
            os.remove('temp.png')
        else:
            await ctx.send("[-] You didn't provide some arguments")



#List available keys
@bot.command()
async def keys(ctx):
    """Get a list of keys you can use with vb!press"""
    keys = list(keycodes.keys())
    keys.sort()
    await ctx.send(f"`{keys}`")

#Reset the VM
@bot.command()
async def reset(ctx):
    """Reset the VM. Owner only."""
    if ctx.author.id == owner_id:
        bot.session.console.reset()
        await asyncio.sleep(0.5)
        get_vm_screenshot(bot.session, 'temp.png')
        await ctx.send('[+] Done!', file=discord.File('temp.png'))
        os.remove('temp.png')
    else:
        await ctx.send("[-] You are not the owner.")

#Reload some bot config paramaters, but not all of them
@bot.command()
async def reload(ctx):
    """Reload the bot config files.
    
    Will also reload other config files, when added."""
    if ctx.author.id == bot.owner_id:
        logo()
        _, _, vm_name, bot.owner_id, bot.channel_id = load_config(config_file)
        print(f"{Fore.YELLOW}[*] Modded by {Fore.LIGHTCYAN_EX}Avanpost (GitHub: avanpost200)")
        print(f"{Fore.YELLOW}[*] Prefix: {Fore.BLUE}{prefix}")
        print(f"{Fore.YELLOW}[*] VM name: {Fore.BLUE}{vm_name}")
        print(f"{Fore.YELLOW}[*] Owner ID: {Fore.BLUE}{owner_id}")
        if channel_id != None:
            print(f"{Fore.YELLOW}[*] Channel ID: {Fore.BLUE}{channel_id}")
        try:
            bot.session.unlock_machine()
        except:
            print(f"{Fore.LIGHTYELLOW_EX}[*] Warning: session not unlocked. You probably don't need to worry about this.")
        bot.vm = bot.vbox.find_machine(vm_name)
        bot.session = bot.vm.create_session()
        await ctx.send("[+] Config reloaded!")
    else:
        await ctx.send("[-] You are not the owner.")
bot.run(token=token, log_level=logging.ERROR)
