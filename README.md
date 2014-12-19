# Heavy Starrer Detector #

Heavy Starrer Detector is a bot that lurks in Stack Exchange chat rooms and detects people who star many messages at a short time. If someone has 3 starring actions (= star or unstar) within 1 minute, they get a ping telling them that much starring can be inappropriate if they're starring trivial messages.

## Setup ##

It's a Python 2.7 bot that uses [ChatExchange](https://github.com/Manishearth/ChatExchange). You can run the file setup.sh after cloning the repository. If you are on Windows, you can rename to setup.bat or setup.cmd because the commands are still the same.

You might also want to change the message when a heavy starrer is detected; currently it sends messages which are specific to The SO Tavern; you can change them. The messages are in an array at the top of the file. You can use some variables in those messages: `$ping` gets evaluated to `@username`, and `$user` gets evaluated to `username`.