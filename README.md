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
The bot could listen and execute remote commands. In order to get started, please create a .yaml file
with the following structure:

```
# commands.yaml

commands:
  1:
    name: Git status
    description: Get status of git from current directory
    command: /gitstatus
    action: git status
  2:
    name: Linux list
    description: List all file under current directory
    command: /ls
    action: ls
```

The action field should be exactly the same as the command executed on the CLI, e.g.

```
action: ls - will list current directory
action: ls /etc - will list all files under /etc
```

Once created, register the commands via register_commands(...) method and start listening.
The specified interval, instructs the bot at what intervals to poll messages from telegram servers.
Defaults to 3 but could be overwritten.

```
bot.register_commands('example_commands.yaml')
bot.listen(interval=5)
```