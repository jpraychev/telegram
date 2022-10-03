# Simplest telegram bot
The simplest telegram bot out there that could be embedded into your apps as a notification service
and could listen and execute remote commands.

# Installation
```
pip install pytele
```

# Introduction
The simplest telegram bot out there that could be embedded into your apps as a notification service and can listen and execute remote commands.

```
from telegram import Bot

bot = Bot() # takens the BOT's token from environment variables - TELEGRAM_BOT_TOKEN
bot.send_msg(to='chait_id', msg='your message')
```