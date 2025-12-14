# anti-ok

A Discord bot that tells users off for saying "ok" and tracks how many times they've said it.

## Features

- Detects the word "ok" (case-insensitive, by itself).
- Tracks counts per user per server.
- Has a 25% chance to reply with a scolding message and the user's total count.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure the bot:
   Open `config.json` and replace `YOUR_TOKEN_HERE` with your actual Discord Bot Token.
   ```json
   {
       "token": "YOUR_ACTUAL_DISCORD_TOKEN",
       "target_word": "ok"
   }
   ```
   You can also change the `target_word` if you want to forbid a different word.

3. Run the bot:
   ```bash
   python bot.py
   ```
