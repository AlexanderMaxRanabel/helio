import discord
from discord.ext import commands
import requests
import random
import time


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.typing = True
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)


@bot.command()
async def urban(ctx, term):
    url = f"https://api.urbandictionary.com/v0/define?term={term}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data['list']) > 0:
            top_definition = data['list'][0]['definition']
            await ctx.send(f"**{term}**: {top_definition}")
        else:
            await ctx.send(f"No definitions found for {term}.")
    else:
        await ctx.send("Error: Failed to fetch data from the Urban Dictionary API.")


@bot.command()
async def roll(ctx, maximum_number: int):
    try:
        result = random.randint(1, maximum_number)
        await ctx.send(f"You rolled a {result}!")
    except ValueError:
        await ctx.send("Invalid argument. Please enter a valid integer.")


@bot.command()
async def randomfact(ctx):
    url = 'https://uselessfacts.jsph.pl/random.json'
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json()['text']
        await ctx.send(fact)
    else:
        await ctx.send("Error: Failed to retrieve random fact")


@bot.command()
async def yomama(ctx, user: discord.Member):
    insult1 = "Yo mama so fat when she passed infront of the tv half of the seasons passed"
    insult2 = "Yo mama so dumb she studied for an eye test"
    insult3 = "Yo mama so slow she took 9 months to make a joke"

    joke = random.randint(1, 3)
    mention = user.mention
    if joke == 1:
        await ctx.send(f'{mention} {insult1}')
    elif joke == 2:
        await ctx.send(f'{mention} {insult2}')
    elif joke == 3:
        await ctx.send(f'{mention} {insult3}')


@bot.command()
async def ban(ctx, user: discord.Member):
    # Check if the user has the necessary permissions to ban members
    if ctx.author.guild_permissions.ban_members:
        await user.ban()
        await ctx.send(f"{user.name} has been banned.")
    else:
        await ctx.send(f"You don't have the permission to ban members.")


@bot.command()
async def unban(ctx, user: discord.Member):
    if ctx.author.guild_permissions.unban_members:
        await user.unban()
        await ctx.send(f"{user.name} has been unbanned")
    else:
        await ctx.send(f"You dont have permission to unban members")


@bot.command()
async def kick(ctx, user: discord.Member):
    # Check if the user has the necessary permissions to ban members
    if ctx.author.guild_permissions.kick_members:
        await user.kick()
        await ctx.send(f"{user.name} has been kicked.")
    else:
        await ctx.send(f"You don't have the permission to kick members.")


@bot.command()
async def rps(ctx, term):
    bot_choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(bot_choices)

    if term == bot_choice:
        await ctx.send(f"I choose {bot_choice}. You chose {term}. It's a tie!")
    elif term == "rock":
        if bot_choice == "paper":
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Paper beats rock. I win!")
        else:
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Rock beats scissors. You win!")
    elif term == "paper":
        if bot_choice == "rock":
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Paper beats rock. You win!")
        else:
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Scissors beat paper. I win!")
    elif term == "scissors":
        if bot_choice == "rock":
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Rock beats scissors. I win!")
        else:
            await ctx.send(f"I choose {bot_choice}. You chose {term}. Scissors beat paper. You win!")
    else:
        await ctx.send("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")


@bot.command()
async def http(ctx, url):
    if ctx.author.guild_permissions.ban_members:
        response = requests.get(url)
        if response.status_code == 200:
            resp = response.json()['text']
            await ctx.send(resp)
        else:
            await ctx.send("Failed to do HTTP request")


@bot.command()
async def remindme(ctx, times: int, remind_type: str, *, message: str):
    author_id = ctx.message.author.id
    user = await bot.fetch_user(author_id)

    if remind_type == "m":
        time.sleep(times * 60)
        await user.send(f"You wanted me to remind you: '{message}'")
    elif remind_type == "s":
        time.sleep(times)
        await user.send(f"You wanted me to remind you: '{message}'")
    elif remind_type == "h":
        time.sleep(times * 3600)
        await user.send(f"You wanted me to remind you: '{message}'")


@bot.command()
async def github(ctx):
    await ctx.send(f"https://github.com/AlexanderMaxRanabel/helio")


bot.run('MTEyMDYzNDM1MjM3MjU1MTc3Mw.GwUlvs.KfrNvpqduhKBfxHh44KpNSU4CgqhgOTt3SrCic')
