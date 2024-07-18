from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os
import replicate

load_dotenv()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    description="Runs models on Replicate!",
    intents=intents,
)

@bot.command(aliases=["sd"])
async def stable_diffusion(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={"prompt": prompt}
    )

    image_url = output[0]

    await ctx.send(image_url)

bot.run(os.environ["DISCORD_TOKEN"])
