import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}')












from model import get_class

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./images/{attachment.filename}')
            await ctx.send(f'Image saved: {file_name}')
            await ctx.send(get_class(model_path='./keras_model.h5',
                                     labels_path='./labels.txt',
                                     image_path=f'./images/{attachment.filename}'))
    else:
        await ctx.send('No images attached')
















import os
@bot.command()
async def get_images(ctx):
    for file in os.listdir('./images'):
        await ctx.send(file)


@bot.command()
async def delete_images(ctx):
    for file in os.listdir('./images'):
        os.remove(f'./images/{file}')
        await ctx.send(f'Deleted {file}')


@bot.command()
async def get_image_index(ctx, index: int):
    if index < 0 or index >= len(os.listdir('./images')):
        await ctx.send('Invalid index')
    else:
        await ctx.send(os.listdir('./images')[index])




bot.run('xxxxxxxxxxx')
