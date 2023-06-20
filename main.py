import discord
from discord.ext import commands
import requests
import random
import wikipedia


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.typing = True
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.command()
async def filesay(ctx, pastebin_link):
    response = requests.get(pastebin_link)
    if response.status_code == 200:
        await ctx.send(response.text)
    else:
        await ctx.send("Error: Failed to fetch data from the provided Pastebin link.")


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
async def wiki(ctx, *, query: str):
    try:
        summary = wikipedia.summary(query)
        response_str = f"Here's what I found on Wikipedia:\n{summary}"
        await ctx.send(response_str)
    except wikipedia.exceptions.PageError:
        await ctx.send("Error: Page not found on Wikipedia.")
        #try:
            #summary = wikipedia.summary(query)
            #response_str = f""

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


#@bot.command()
#async def levget(ctx):

bot.run('token')
