# Yuzuru Desu RP Discord Bot

A private [Discord](https://discord.com/) bot that I, [Yuzurukyun](https://github.com/Yuzurukyun), am creating for the 
sake of automation and education.

## Introduction

This Discord bot is written in python using Discord's discord.py library. 
It is used for a private Discord server to aid in online RP-based activities, where RP stands for role-play. 
As of now, it can create and manage character data profiles for RP participants. 
In addition, it provides commands that allow GMs to manage discord DMs for an RP more efficiently, where GM stands for game master, and DM stands for direct message.

The bot is currently deployed on a server using [Docker](https://www.docker.com/) and [fly.io](https://fly.io/) BaaS (backend as a service).

### Discord Bot Documentation

- [Official documentation](https://discord.com/developers/docs/intro)
- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [How to create and invite a bot to a Discord server](https://discordpy.readthedocs.io/en/latest/discord.html)

## Notes

- The bot can be run locally using [Python 3.8](https://www.python.org/downloads/) or using Docker via the Dockerfile
- [PyCharm](https://www.jetbrains.com/pycharm/) is the Python IDE being used by the core developers of this bot
- Run `y!getbank` before shutting down the bot to retrieve the character's money data. The money data is not persistent on the live version. This problem does not occur if running the bot locally
- Only 1 bot needs to be deployed onto fly.io. Deploying more instances of the bot using the same Discord token will result in repeated bot messages for any `y!<command>` run on the Discord client
- Docker is required to use fly.io
- Whenever a new Python package is installed, run `pip freeze > requirements.txt` to update the requirements.txt file. This file is needed for the Dockerfile
- Whenever a new file is added to the repository that isn't needed for the program to run, add the filename to the .dockerignore file. This is to save space on the Docker image produced by the Dockerfile 
    
## Environment Setup

It is recommended to use a virtual environment to install the required Python packages into.
If you're using PyCharm, [setting up a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) is rather simple.

To install the Python package dependencies, run:

```
pip install -r requirements.txt
```

An .env file needs to be created in the root of this repository. 
Do not track this file with git, as it will contain the Discord token of the bot, which should never be shared.

Example .env:

```
DISCORD_TOKEN_YUZURU=<your discord token>
```

If testing the bot locally while another bot instance is running on a server, to prevent repeated messages, modify the bot to use the command syntax `dev!`, instead of `y!`.
Note that repeated bot messages may still be sent by the bot running on the server when using the same command syntax for the local bot running.
Another solution is to shut down or pause the bot on the server, and run it again once done testing the bot locally.
This second solution would remove the need to switch between the command syntax `dev!` and `y!`.

For `dev!`, this line should be active, and the `y!` commented out:

```
client = commands.Bot(command_prefix=commands.when_mentioned_or('dev!'), case_insensitive=True)
```

For `y!`, this line should be active, and the `dev!` commented out:

```
client = commands.Bot(command_prefix=commands.when_mentioned_or('yu!', 'y!', 'yuzuru!', 'yus!', 'yuyu!'), case_insensitive=True)
```

## Bot Command Summary

Run `y!<command>` in the Discord client and choose a command to run:

-  **bank**
    - Modify bank account of an RP participant
-  **check**
    - Check a RP participant's character profile
-  **getbank**
    - Get bank data of RP participants. Required before bot shutdown
-  **profile**
    - Show your character profile in the RP
-  **reply**  
    - Send a reply message to an RP participant
-  **search** 
    - Send a message to the GMs based on where you are in the RP

Run `y!help` to see all the commands of the bot.

Run `y!help <command>` to see help documentation for a specific command.

## Docker Deployment

If you're on Windows, you need the Windows Pro version, at the minimum, to run Docker.

To build the Dockerfile for local testing, run:

```
docker build -t yuzuru-desu/fly.io:v1 .
```

To run the bot, run:

```
docker run -d yuzuru-desu/fly.io:v1
```

To shut down the bot, create a new terminal window and run:

```
docker stop <container_id or container_name>
```

To check the container_id or container_name of the bot, create a new terminal window and run:

```
docker ps
```

### Docker Documentation

- [Official documentation](https://docs.docker.com/)
- [Dockerfile configuration](https://docs.docker.com/engine/reference/builder/)
- [Docker Hub](https://hub.docker.com/)

## fly.io Deployment

The bot is being hosted for free with fly.io BaaS (backend as a service). 
You can either create a fly.io account, or login with your Github account.

### fly.toml configuration

The default fly.toml generated by running the command `flyctl deploy` has to be modifed to work with the bot.
The fly.toml needs to be configured without healthchecks and without assigning any other ports to the bot application, except the standard `internal_port = 8080` for the [services](https://fly.io/docs/configuration/#the-services-section) option.
The options [services.ports](https://fly.io/docs/configuration/#services-ports) and [services.tcp_checks](https://fly.io/docs/configuration/#services-tcp_checks) should not be used in the fly.toml configuration.
This is because the bot is not configured to pass the healthchecks, and doesn't need to accept external web traffic.

### Dockerfile configuration

Make sure that the docker image is set to be exposed to port 8080, `EXPOSE 8080`, even if it's not used.
Port 8080 matches `internal_port = 8080` found in the fly.toml configuration, which allows the Docker container to connect and be used on the fly.io backend server instance.

### Using flyctl

flyctl is a command line program.
flyctl.exe is required when using fly.io. 
For Windows, the flyctl.exe should be placed in the same root directory as the repository.

To download flyctl.exe for Windows, run:

```
curl -LO https://getfly.fly.dev/windows-x86-64/flyctl.exe
```

To login to fly.io, run:

```
flyctl auth login
```

To check current app deployement status, based on the fly.toml configuration, run:

```
flyctl status
```

To deploy your app, based on the fly.toml configuration, run:

```
flyctl deploy
```

To see the help documentation, run:

```
flyctl --help
```

### fly.io Documentation

- [Official documentation](https://fly.io/docs/)
- [fly.toml configuration](https://fly.io/docs/configuration/)
- [Example deployment](https://fly.io/docs/speedrun/)
- [Pricing](https://fly.io/docs/pricing/)

## License

This Discord bot is licensed under the AGPLv3 license. 
In short, if you use a modified version of Yuzuru Desu, you *must* distribute its source licensed under the AGPLv3 as well, and notify your users where the modified source may be found.

See the [LICENSE](LICENSE.md) file for more information.
