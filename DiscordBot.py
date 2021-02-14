import random
import discord
from discord.ext import commands


urls = {"php": "https://www.php.net/docs.php",
        "bash": "https://ryanstutorials.net/bash-scripting-tutorial/\nhttps://www.youtube.com/watch?v=oxuRxtrO2Ag\nhttps://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html\nhttps://devhints.io/bash\nhttps://www.shellscript.sh/",
        "mySQL":"https://dev.mysql.com/doc/refman/8.0/en/language-structure.html",
        "python":"https://docs.python.org/3/",
        "discord":"https://discordpy.readthedocs.io/en/latest/#manuals\nhttps://github.com/Rapptz/discord.py/tree/master/examples\nhttps://discord.com/invite/r3sSKJJ\nhttps://www.techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/",
        "c":"First link is to Lib Gen\nhttp://libgen.is/book/index.php?md5=556E6BEE561B776C95C6872C441BAAD1\nSecond link is a link directly to Steph's message with a download\nhttps://discord.com/channels/751791015630995496/751791015630995499/802322088894660629",
        "commands":"-bash\n-c\n-commands\n-disc\n-linux\n-php\n-python\n-playlist\n-njit\n-receipt\n-libgen",
        "linux":"https://ubuntu.com/download \nhttps://getfedora.org/",
        "Playlist":"https://open.spotify.com/playlist/576j38Yts0TeQGzOpPHvTm?si=ugUeJNk3T26mYJLmCznP6g",
        "njit":"Fuck NJIT.\nhttps://twitter.com/NJIT/status/971122883815763968",
        "receipt":"Don't let any of the school administration victimize you for things you didn't do. Hold everyone in the same position accountable for the things they say - keep the fucking receipts and save the fucking recordings. Above all else, never forget that the issues at NJIT are not just a result of the student population\nhttps://discord.com/channels/751791015630995496/751791015630995499/791839370440343562",
        "LibGen":"Here's a link to Steph's message explaing how to use Lib Gen to get your books for free. Don't ever overpay for something that's free.\nMake sure you select the right format\nhttps://discord.com/channels/751791015630995496/751791015630995499/801991957068513310"}#dict of all the links

cdPhrases=['Fuck off.',
           'My dude chill out',
           'I *JUST* posted those links.',
           'Listen it aint hardwork but it is honest work.',
           'I am going to delete canvas if you bug me again.',
           'That is it you will not like me when I am angry.',
           'Hail Hydra! You prick!',
           'Heil BASSEL! OUR LORD AND SAVIOR!',
           'Somebody get this guy a body bag for when I am done with him.'] #Spam phrases for those dickheads trying to abuse the bot

client=commands.Bot(command_prefix='-',case_insensitive=True)#this is what the bot will be called ie bot or client,also not case sensitivity
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Thinking about putting grades in."))#Sets the game being played to this custom message, bot status is Online always
    print('My guy I am busy deleting Canvas.')

#Gives the links for the command "!php"
@client.command(name='php')
@commands.cooldown(1, 60, commands.BucketType.user)
async def php(ctx):
    if (ctx.author.bot): return
    response=urls["php"]
    await ctx.send(response)
#Cooldown error handling
@php.error
async def php_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!mySQL"
@client.command(name='mySQL')
@commands.cooldown(1, 60, commands.BucketType.user)
async def mySQL(ctx):
    if (ctx.author.bot): return
    response=urls["mySQL"]
    await ctx.send(response)
#Cooldown error handling
@mySQL.error
async def mySQL_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!python"
@client.command(name='python')
@commands.cooldown(1, 60, commands.BucketType.user)
async def python(ctx):
    if (ctx.author.bot): return
    response=urls["python"]
    await ctx.send(response)
#Cooldown error handling
@python.error
async def python_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!bash"
@client.command(name='bash')
@commands.cooldown(1, 60, commands.BucketType.user)
async def bash(ctx):
    if (ctx.author.bot): return
    response=urls["bash"]
    await ctx.send(response)
#Cooldown error handling
@bash.error
async def bash_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!c"
@client.command(name='c')
@commands.cooldown(1, 60, commands.BucketType.user)
async def c(ctx):
    if (ctx.author.bot): return
    response=urls["c"]
    await ctx.send(response)
#Cooldown error handling
@c.error
async def c_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!disc"
@client.command(name='disc')
@commands.cooldown(1, 60, commands.BucketType.user)
async def disc(ctx):
    if (ctx.author.bot): return
    response=urls["discord"] #This gives a ton of resources for discord.py
    await ctx.send(response)
#Cooldown error handling
@disc.error
async def disc_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!linux"
@client.command(name='linux')
@commands.cooldown(1, 60, commands.BucketType.user)
async def linux(ctx):
    if (ctx.author.bot): return
    response=urls["linux"]
    await ctx.send(response)
#Cooldown error handling
@linux.error
async def linux_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!playlist"
@client.command(name='playlist')
@commands.cooldown(1, 60, commands.BucketType.user)
async def linux(ctx):
    if (ctx.author.bot): return
    response=urls["Playlist"]
    await ctx.send(response)
#Cooldown error handling
@linux.error
async def linux_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!njit"
@client.command(name='NJIT')
@commands.cooldown(1, 60, commands.BucketType.user)
async def njit(ctx):
    if (ctx.author.bot): return
    response=urls["njit"]
    await ctx.send(response)
#Cooldown error handling
@njit.error
async def njit_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!receipt"
@client.command(name='receipt')
@commands.cooldown(1, 60, commands.BucketType.user)
async def receipt(ctx):
    if (ctx.author.bot): return
    response=urls["receipt"]
    await ctx.send(response)
#Cooldown error handling
@receipt.error
async def recepit_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Gives the links for the command "!libgen"
@client.command(name='libgen')
@commands.cooldown(1, 60, commands.BucketType.user)
async def receipt(ctx):
    if (ctx.author.bot): return
    response=urls["LibGen"]
    await ctx.send(response)
#Cooldown error handling
@receipt.error
async def libgen_error(ctx, error):
    pharses=random.choice(cdPhrases)
    await ctx.send(pharses)

#Dm's user a list of commands to use
@client.command(name='commands')
async def on_message(ctx):
    if (ctx.author.bot): return
    houseKeeping='Each command has resources for that language or topic,the following are a list of commands avaible to you:\n '
    response=urls["commands"]#Dict entry for all the commands
    await ctx.author.send(houseKeeping+response)

@client.event #Error handling for invalid commands,Sends the message below to tell them how to get the list of valid commands
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is invalid. Please use -commands to recieve a dm telling you the vaild commands.')

client.run('Bot Token removed for public viewing')#Bot token goes here