# Heavy Starrer Detector #

*Note: information about who starred a message, is now to longer passed in the web socket. This means that HeavyStarrerDetector cannot be used anymore to detect star trolls.*

Heavy Starrer Detector is a bot that lurks in Stack Exchange chat rooms and detects people who star many messages at a short time. If someone has 3 starring actions (= star or unstar) within 1 minute, they get a ping telling them that much starring can be inappropriate if they're starring trivial messages.

## Setup ##

It's a Python 2.7 bot that uses [ChatExchange](https://github.com/Manishearth/ChatExchange). You can run the file setup.sh after cloning the repository. If you are on Windows, you can rename to setup.bat or setup.cmd because the commands are still the same.

You might also want to change the message when a heavy starrer is detected; currently it sends messages which are specific to The SO Tavern; you can change them. The messages are in an array at the top of the file. You can use some variables in those messages: `$ping` gets evaluated to `@username`, and `$user` gets evaluated to `username`.

## Running the bot ##

When you run it, it will ask for the host of the chat room, the room number, and credentials for the bot to log on. When it's started, you'll see `<<` on your terminal and you can input commands. Currently, the commands are:

 - `stop`: stops the bot.
 - `disable`: disables the bot. It doesn't check for heavy starrers until you enable it again.
 - `enable`: enables the bot when it's disabled.
