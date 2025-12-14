import discord
import json
import random
import os

# Load configuration
if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
else:
    print("Error: config.json not found.")
    exit(1)

TOKEN = config.get('token')
TARGET_WORD = config.get('target_word', 'ok')

class AntiOkClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counts = self.load_counts()

    def load_counts(self):
        if os.path.exists('counts.json'):
            try:
                with open('counts.json', 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_counts(self):
        with open('counts.json', 'w') as f:
            json.dump(self.counts, f)

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Check for target word (exact match, case insensitive)
        if not message.content:
            return
            
        content = message.content.strip().lower()
        
        if content == TARGET_WORD:
            user_id = str(message.author.id)
            guild_id = str(message.guild.id) if message.guild else "dm"
            
            # Update counts
            if guild_id not in self.counts:
                self.counts[guild_id] = {}
            if user_id not in self.counts[guild_id]:
                self.counts[guild_id][user_id] = 0
            
            self.counts[guild_id][user_id] += 1
            self.save_counts()
            
            count = self.counts[guild_id][user_id]

            # 25% chance to reply
            if random.random() < 0.25:
                await message.reply(f"STOP! You've said {TARGET_WORD} {count} times in this guild n*a.")

intents = discord.Intents.default()
intents.message_content = True

client = AntiOkClient(intents=intents)

if __name__ == "__main__":
    if not TOKEN or TOKEN == "YOUR_TOKEN_HERE":
        print("Error: Please set your Discord token in config.json")
    else:
        client.run(TOKEN)
