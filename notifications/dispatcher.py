from notifications.discord import send_discord
import os

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
def notify(message: str):
    if DISCORD_WEBHOOK:
        send_discord(message, DISCORD_WEBHOOK)