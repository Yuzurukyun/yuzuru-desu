# Yuzuru Desu RP Discord Bot
A private [Discord](https://discord.com/) bot that I, [Yuzurukyun](https://github.com/Yuzurukyun), am creating for the 
sake of automation and education.

## Introduction
This Discord bot is written in python using Discord's discord.py library. 
It is used for a private Discord server to aid in online RP-based activities, where RP stands for role-play. 
As of now, it can create and manage character data profiles for RP participants. In addition, it provides commands 
that allow GM's to manage discord DM's for an RP more efficiently, where GM stands for game master, and DM stands 
for direct message.

### Discord Documentation
- [Official documentation](https://discord.com/developers/docs/intro)
- [discord.py](https://discordpy.readthedocs.io/en/latest/)

## Notes
- The bot can be run locally using [Python 3.8](https://www.python.org/downloads/), or using 
[Docker](https://www.docker.com/) via the Dockerfile
- [PyCharm](https://www.jetbrains.com/pycharm/) is the Python IDE being used by the core developers of this bot
- Run `y!getbank` before shutting down the bot to retrieve the character's money data. The money data is not persistent on
the live version. This problem does not occur if running the bot locally
- Only 1 bot needs to be deployed onto fly.io. Deploying more instances of the bot using the same Discord token will
result in repeated bot messages for any `y!<command>` run on the Discord client

## Docker Deployment
If you're on Windows, you need the Windows Pro version, at the minimum, to run Docker.

To build the Dockerfile for local testing, run:

```docker build -t yuzuru-desu/fly.io:v1 .```

To run the bot, run:

```docker run -d yuzuru-desu/fly.io:v1```

To shut down the bot, create a new terminal window and run:

```docker stop <container_id or container_name>```

To check the container_id or container_name of the bot, create a new terminal window and run:

```docker ps```

### Docker Documentation
- [Official documentation](https://docs.docker.com/)
- [Dockerfile configuration](https://docs.docker.com/engine/reference/builder/)
- [Docker Hub](https://hub.docker.com/)

## fly.io
The bot is being hosted for free with [fly.io](https://fly.io/). The fly.toml needs to be configured without healthchecks 
and without assigning ports to the bot application.

The flyctl.exe is required when using fly.io. For Windows, the flyctl.exe should be placed in the same 
directory as the repository.

To download flyctl.exe for Windows, run:

```curl -LO https://getfly.fly.dev/windows-x86-64/flyctl.exe```

### fly.io Documentation
- [Official documentation](https://fly.io/docs/)
- [fly.toml configuration](https://fly.io/docs/configuration/)
- [Example deployment](https://fly.io/docs/speedrun/)
- [Pricing](https://fly.io/docs/pricing/)