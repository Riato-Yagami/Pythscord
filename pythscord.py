import discord
import pkg_resources
from discord.ext import commands
import asyncio

from IPython.utils.capture import capture_output
from discord import Game
from discord.ext.commands import Bot




BOT_PREFIX = ("?","!")
TOKEN = 'YOUR TOKEN'                                                              #put your dicsord token right here

client = Bot(command_prefix=BOT_PREFIX) 


@client.event
async def on_message(message):
    if message.content.startswith('>'):
        pyth_w = open("pythscord_code.py","w+")
        pyth_r = open("pythscord_code.py","r")
        pyth_a = open("pythscord_code.py","a+")
       
        msg = await client.wait_for_message(author=message.author)
        
        while msg.content != 'stop':
            if msg.content.startswith ('tab'):                                    #you can identent by tapping tab
                count = msg.content.count('tab')
                pyth_a.write('  '*count+str(msg.content)[3*count:]+ '\n')
                print(str(msg.content))
                msg = await client.wait_for_message(author=message.author)
                
            #elif msg.content.startswith ('del'):                                 #i'm not sure of how to do that
                
            else :
                pyth_a.write(str(msg.content)+ '\n') 
                print(str(msg.content))
                msg = await client.wait_for_message(author=message.author)
            
        
        pyth_a.close()
        
        with capture_output() as c:
            code = str(exec(open("pythscord_code.py").read()))
            await client.send_message(message.channel, c.stdout+ '\n---------------- \n         end \n----------------')
            
        
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='with python'))
    print('Logged in as '+ client.user.name)
    print('In:')
    for server in client.servers:
        print(server.name)

client.run(TOKEN)