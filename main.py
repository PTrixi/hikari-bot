import discord
import random
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix='$')

punch_gifs = [
        'https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif',
        'https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif',
        'https://c.tenor.com/UH8Jnl1W3CYAAAAC/anime-punch-anime.gif',
        'https://c.tenor.com/wYyB8BBA8fIAAAAd/some-guy-getting-punch-anime-punching-some-guy-anime.gif',
        'https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif',
        'https://c.tenor.com/p_mMicg1pgUAAAAC/anya-forger-damian-spy-x-family.gif',
        'https://c.tenor.com/--80HfIQWT4AAAAd/punchy-one-punch-man.gif',
        'https://c.tenor.com/sgzZFnBVXCMAAAAd/one-punch-man-kick.gif',
        'https://tenor.com/view/jujutsu-kaisen-mahito-yuji-itadori-yuji-yuuji-gif-20475970',
        'https://c.tenor.com/laW-dCBdPUgAAAAC/dragon-ball-super-goku.gif'
        ]
punch_names = [
        'le dió un puñetazo a',
        'ha golpeado a',
        'le lanzó un fuerte golpe a',
        'le dió un golpe a',
        'le dió un debil puñetazo a',
        'le lanzó un puñetazo muy debil a',
        'golpeó con toda su fuerza a',
        'golpeó suavemente a',
        'golpeó con ganas a',
        'le lanzo un suave puñetazo a'
        ]

kiss_gifs = [
        'https://c.tenor.com/UQwgkQbdp48AAAAC/kiss-anime.gif',
        'https://c.tenor.com/bX5fwQMRiHQAAAAC/anime-love.gif',
        'https://c.tenor.com/3wE3JNW0fswAAAAC/anime-kiss-love.gif',
        'https://c.tenor.com/Fcc0laaEZ0gAAAAC/lip-lock-kiss.gif',
        'https://c.tenor.com/Fyq9izHlreQAAAAC/my-little-monster-haru-yoshida.gif',
        'https://c.tenor.com/Daj-Pn82PagAAAAC/gif-kiss.gif',
        'https://c.tenor.com/9jB6M6aoW0AAAAAC/val-ally-kiss.gif',
        'https://c.tenor.com/YKd-wOisWB0AAAAC/anime-kiss.gif',
        'https://c.tenor.com/Wc2RP6mAF_4AAAAC/volfeed-anime.gif',
        'https://c.tenor.com/Cpm-Ko_mU2gAAAAC/anime-kiss.gif'
        ]
kiss_names = [
        'le dió un beso a',
        'besó con ganas a',
        'le comió la boca a',
        'besó salvajemente a',
        'ha besado a',
        'le ha comido la boca a'
        ]

hug_gifs = [
        'https://c.tenor.com/3mr1aHrTXSsAAAAC/hug-anime.gif',
        'https://c.tenor.com/gyiM68xD1MQAAAAC/anime-cute.gif',
        'https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif',
        'https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif',
        'https://c.tenor.com/n0qIE_8B0JcAAAAC/gif-abrazo.gif',
        'https://c.tenor.com/wUQH5CF2DJ4AAAAC/horimiya-hug-anime.gif',
        'https://c.tenor.com/mM9XkpXjPwkAAAAC/hug-anime.gif',
        'https://c.tenor.com/hacbVpDut3sAAAAC/hug.gif',
        'https://c.tenor.com/8NnSbNaqB_0AAAAC/anime-hug.gif',
        'https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif'
        ]
hug_names = [
        'le dio un abrazo a',
        'ha abrazado a',
        'le dio un fuerte abrazo a',
        'abrazo fuertemente a',
        'ha abrazado fuertemente a',
        'le ha dado un abrazo a'
        ]

pat_gifs = [
        'https://c.tenor.com/8DaE6qzF0DwAAAAC/neet-anime.gif',
        'https://c.tenor.com/sX-K9XVf6KoAAAAC/catgirl-neko.gif',
        'https://c.tenor.com/2vFAxyl6cI8AAAAd/mai-headpats.gif',
        'https://c.tenor.com/E6fMkQRZBdIAAAAC/kanna-kamui-pat.gif',
        'https://c.tenor.com/N41zKEDABuUAAAAC/anime-head-pat-anime-pat.gif',
        'https://c.tenor.com/TDqVQaQWcFMAAAAC/anime-pat.gif',
        'https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif',
        'https://c.tenor.com/i7nXGbPLqTsAAAAC/anime-hug.gif',
        'https://c.tenor.com/o0re0DQzkd8AAAAC/anime-head-rub.gif',
        'https://c.tenor.com/nCuGm2jPW7UAAAAC/adachi-and-shimamura-head.gif'
        ]
pat_names = [
        '',
        '',
        '',
        '',
        ''
        ]

kill_gifs = [
        'https://c.tenor.com/G4SGjQE8wCEAAAAC/mikey-tokyo.gif',
        'https://c.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif',
        'https://c.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif',
        'https://c.tenor.com/t-0fYVPgg1YAAAAC/pink-hair-anime.gif',
        'https://c.tenor.com/EWhFGCTfmucAAAAC/akame-ga-kill-akame.gif',
        'https://c.tenor.com/Hpa1FyBhRusAAAAC/anime-zombies.gif',
        'https://c.tenor.com/wGgDECpN_eMAAAAC/akame-akame-ga-k-ill.gif',
        'https://c.tenor.com/YtRZgG_rRkwAAAAC/lubbock-akame-ga-kill.gif',
        'https://c.tenor.com/XXS9k7CT4YUAAAAd/ryuko-ryuko-matoi.gif',
        'https://c.tenor.com/dOUVztxZ9UAAAAAC/anime-explosion.gif'
        ]
kill_names = [
        '',
        '',
        '',
        '',
        ''
        ]

slap_gifs = [
        'https://c.tenor.com/pgq_YsVX7sEAAAAC/meliodas-seven-deadly-sins.gif',
        'https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif',
        'https://c.tenor.com/eU5H6GbVjrcAAAAC/slap-jjk.gif',
        'https://c.tenor.com/UDo0WPttiRsAAAAd/bunny-girl-slap.gif',
        'https://c.tenor.com/FJsjk_9b_XgAAAAC/anime-hit.gif',
        'https://c.tenor.com/XiYuU9h44-AAAAAC/anime-slap-mad.gif',
        'https://c.tenor.com/1-1M4PZpYcMAAAAd/tsuki-tsuki-ga.gif',
        'https://c.tenor.com/VlSXTbFcvDQAAAAC/naruto-anime.gif',
        'https://c.tenor.com/2R9-4O6jqEsAAAAC/slap-slapping.gif',
        'https://c.tenor.com/1lemb3ZmGf8AAAAC/anime-slap.gif'
        ]
slap_names = [
        '',
        '',
        '',
        '',
        ''
        ]

lick_gifs = [
        'https://c.tenor.com/o3BOAAiVcwMAAAAC/sono-hanabira-ni-kuchizuke-wo-anime.gif',
        'https://c.tenor.com/JgJeNlAhrN4AAAAC/lick-leg.gif',
        'https://c.tenor.com/aFig9dYnXooAAAAC/neko-anime.gif',
        'https://c.tenor.com/g1HYBQGPEVYAAAAC/anime-lick.gif',
        'https://c.tenor.com/jyv9sexi1fYAAAAC/anime-lick.gif',
        'https://c.tenor.com/t6cxb_yox3QAAAAC/lick-ear.gif',
        'https://c.tenor.com/dpp6H2ej1JYAAAAC/anime-kuzu-no-honkai.gif',
        'https://c.tenor.com/bgGMTIJhEvEAAAAC/anime-lick-lick.gif',
        'https://c.tenor.com/iPI6QifO4UYAAAAd/zero-two-and-hiro.gif',
        'https://c.tenor.com/qvFLVVUEWgIAAAAC/anime-golden.gif'
        ]
lick_names = [
        '',
        '',
        '',
        '',
        ''
        ]



@bot.command()
async def punch(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(punch_names))} {member.mention}"
    
    )
    embed.set_image(url=(random.choice(punch_gifs)))

    await ctx.send(embed = embed)


@bot.command()
async def kiss(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(kiss_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(kiss_gifs)))
    
    await ctx.send(embed = embed)


@bot.command()
async def hug(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(hug_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(hug_gifs)))
    
    await ctx.send(embed = embed)


@bot.command()
async def pat(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(pat_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(pat_gifs)))
    
    await ctx.send(embed = embed)


@bot.command()
async def kill(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(kill_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(kill_gifs)))
    
    await ctx.send(embed = embed)


@bot.command()
async def slap(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(slap_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(slap_gifs)))
    
    await ctx.send(embed = embed)


@bot.command()
async def lick(ctx, member: discord.Member = None):
    embed = discord.Embed(
        colour=(discord.Colour.random()),
        description = f"{ctx.author.mention} {(random.choice(lick_names))} {member.mention}"      
    )
    embed.set_image(url=(random.choice(lick_gifs)))
    
    await ctx.send(embed = embed)


bot.run(TOKEN)
