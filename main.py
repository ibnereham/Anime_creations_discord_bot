import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from dotenv import load_dotenv
import os
from typing import Literal
# yada yada here
intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.streaming , name="ANIME CREATIONS")
status = discord.Status.idle

bot = commands.Bot(command_prefix="/", intents=intents, status=status, activity=activity)
bot.remove_command("help")

#Importing all crap from env
load_dotenv()
discord_token = os.getenv('TOKEN')

@bot.event
async def on_ready():
    print("bot is on")
    try:
        synced = await bot.tree.sync()
        print(f"SYNCED{len(synced)} command(s) ")
    except Exception as e:
        print(e)
async def logup(client,user,type,desc):
    channel = await bot.fetch_channel("1133684290652217406") #1132283982084575272
    embed = discord.Embed(title=f"ORDER FOR {user} by {client}",
                      url="https://discord.gg/Bt4racbC9h",
                      description=f"**{client} has ordered a {type} from {user}\nThanks for ordering**\n\nHere is the description client provided:\n{desc}",
                      colour=0x00b0f4)
    await channel.send(embed=embed)

#zys = await bot.fetch_user('859014645360885760')
#jupi = await bot.fetch_user('954127073759354940')
#rxin = await bot.fetch_user('1114817994565111829')


@bot.tree.command(name="order", description="Makes a order")
async def order(interaction: discord.Interaction, user: Literal['ZYS',"RXIN","JUPI"],type: Literal["PFP","THUMBNAIL","BANNER"], desc: str):
    await interaction.response.defer()
    zys = await bot.fetch_user('859014645360885760')
    jupi = await bot.fetch_user('954127073759354940')
    rxin = await bot.fetch_user('1114817994565111829')
    if len(desc) <= 30:
        await interaction.followup.send("Please give a description longer than 30 characters")
    else:
        try:
            await logup(client=interaction.user.mention,user=user,type=type,desc=desc ) 
        except:
            await interaction.channel.send("dont have perm to log at <#1132283982084575272>")       
        match user:
            case "ZYS":
                xd = discord.Embed(title=f"ORDER FOR {user}",
                        url="https://discord.gg/Bt4racbC9h",
                        description=f"**{interaction.user.display_name} has ordered a {type} from you. **\n\nHERE IS THE DESCRIPTION:\n{desc}",
                        colour=0x00f549)
                try:
                    await zys.send(embed=xd)
                    await interaction.followup.send("Order successful")
                except:
                    await interaction.followup.send("something went wrong")
            case "RXIN":
                xd = discord.Embed(title=f"ORDER FOR {user}",
                        url="https://discord.gg/Bt4racbC9h",
                        description=f"**{interaction.user.display_name} has ordered a {type} from you. **\n\nHERE IS THE DESCRIPTION:\n{desc}",
                        colour=0x00f549)
                try:
                    await rxin.send(embed=xd)
                    await interaction.followup.send("Order successful")
                except:
                    await interaction.followup.send("something went wrong")
            case "JUPI":
                xd = discord.Embed(title=f"ORDER FOR {user}",
                        url="https://discord.gg/Bt4racbC9h",
                        description=f"**{interaction.user.display_name} has ordered a {type} from you. **\n\nHERE IS THE DESCRIPTION:\n{desc}",
                        colour=0x00f549)
                try:
                    await jupi.send(embed=xd)
                    await interaction.followup.send("Order successful")
                except:
                    await interaction.followup.send("something went wrong")


#    question = discord.Embed(title="CHECK UR DM")
#    await interaction.response.send_message(embed=question, ephemeral=True)
#    await interaction.user.send(f'HELLO {interaction.user.display_name}.')
#    await interaction.user.send('https://media.tenor.com/Vant9OGye9gAAAAC/rainbow-bar-divider.gif')
#    questions = [
#    'Whom do u want it from ?\n\n\n1. ZYS\n2. RXIN\n3. JUBI\n(REPLY WITH NUMBER eg. 1 )'
#    'what do u want to order?\n1. PFP\n2. BANNER\n3. THUMBNAIL\n(REPLY WITH NUMBER eg. 1 ) ',
#]
#    answers = {}
#    data = ["whom", "what"]
#
#
 #   for i in range(len(questions)):
  #      await interaction.user.send(questions[i])
#
 #       def check(message):
  #          return message.author == interaction.user and isinstance(message.channel, discord.DMChannel)
   #     try:
    #        response = await bot.wait_for('message', timeout=90.0, check=check)
     #       answers[data[i]] = response.content
      #  except TimeoutError:
       #     await interaction.user.send('You did not provide a response in time.')
        #    break

#    match answers['whom']:
#        case "1":
#            match answers['what']:
#                case "1":
#                    zys.send(f'{interaction.user.display_name} wants a ')
            
    




bot.run(discord_token)
