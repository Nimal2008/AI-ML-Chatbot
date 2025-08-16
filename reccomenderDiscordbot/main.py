import json
import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
from recommender import search, add_user, recommend,rate

load_dotenv()

#create global var

DISCORD_BOT_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

intents.message_content = True

with open("config.json","r") as config_file:
    config = json.load(config_file)

command_prefix = config['prefix']

#intents are permissions allowed for the bot
bot = commands.Bot(command_prefix=command_prefix, intents = intents)
bot.add_command(search)
bot.add_command(add_user)
bot.add_command(rate)
bot.add_command(recommend)
#bot.add_command(add_user)
# decorators change the functionality of functions
# this one marks it as a handler for the ready event
# this function will trigger exactly once, when the bot starts up
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("hi")

@bot.command(name="howareyou")
async def howareyou(ctx):
    await ctx.send("Good how about you")


@bot.command(name="rps")
async def rock_paper_scissors(ctx, user_choice: str):
    choices = ["rock", "paper", "scissors"]
    user_choice = user_choice.lower()

    if user_choice not in choices:
        await ctx.send("Please choose rock, paper, or scissors.")
        return

    bot_choice = random.choice(choices)

    result = ""
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "scissors" and bot_choice == "paper") or
        (user_choice == "paper" and bot_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    await ctx.send(f"You chose **{user_choice}**.\nI chose **{bot_choice}**.\n{result}")
def main():
    bot.run(DISCORD_BOT_TOKEN)

# If this script is run (instead of imported), start the bot.
if __name__ == '__main__':
    main()