import discord
import logging
import os
from datetime import datetime
from discord.ext import commands

# Konfiguration
TOKEN = 'Token_Hier'
LOG_CHANNEL_ID = ID_Hier
LOG_DIRECTORY = "logs"
os.makedirs(LOG_DIRECTORY, exist_ok=True)

# Logging einrichten
logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_to_file(log_type, message):
    timestamped_message = f"[{get_timestamp()}] {message}"
    with open(f"{LOG_DIRECTORY}/{log_type}.log", "a", encoding="utf-8") as file:
        file.write(timestamped_message + "\n")

def log_chat_to_file(channel_name, message):
    safe_channel_name = channel_name.replace(" ", "_").replace("/", "_")
    timestamped_message = f"[{get_timestamp()}] {message}"
    with open(f"{LOG_DIRECTORY}/chat_{safe_channel_name}.log", "a", encoding="utf-8") as file:
        file.write(timestamped_message + "\n")

async def log_event(log_type, message):
    log_to_file(log_type, message)

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    log_message = f"{message.author} ({message.author.id}): {message.content}"
    log_chat_to_file(message.channel.name, log_message)
    await log_event("chat", log_message)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    log_message = f"Nachricht gelöscht von {message.author} ({message.author.id}) in #{message.channel.name}: {message.content}"
    await log_event("deleted_messages", log_message)

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if before.channel != after.channel:
        if before.channel is None:
            log_message = f"{member} ist dem Sprachkanal {after.channel} beigetreten"
        elif after.channel is None:
            log_message = f"{member} hat den Sprachkanal {before.channel} verlassen"
        else:
            log_message = f"{member} wechselte von {before.channel} zu {after.channel}"
        await log_event("voice", log_message)

@bot.event
async def on_member_update(before, after):
    if after.bot:
        return
    added_roles = [r.name for r in after.roles if r not in before.roles]
    removed_roles = [r.name for r in before.roles if r not in after.roles]
    if added_roles:
        await log_event("roles", f"{after} erhielt Rollen: {', '.join(added_roles)}")
    if removed_roles:
        await log_event("roles", f"{after} verlor Rollen: {', '.join(removed_roles)}")

@bot.event
async def on_member_join(member):
    if member.bot:
        return
    await log_event("user", f"{member} ist dem Server beigetreten")

@bot.event
async def on_member_remove(member):
    if member.bot:
        return
    await log_event("user", f"{member} hat den Server verlassen")

@bot.event
async def on_member_ban(guild, user):
    await log_event("user", f"{user} wurde gebannt")

@bot.event
async def on_member_unban(guild, user):
    await log_event("user", f"{user} wurde entbannt")

bot.run(TOKEN)
