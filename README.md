# DISCLAIMER DO NOT USE THIS TO SPAM / USE IN A DEDICATED DISCORD CHANNEL  

## discord link  
[click to add discord bot](https://discord.com/api/oauth2/authorize?client_id=955718572842287134&permissions=292057901056&scope=bot)  
discord bot link: https://discord.com/api/oauth2/authorize?client_id=955718572842287134&permissions=292057901056&scope=bot  
---
## about
discord bot to render videos in ascii / .txt format (sends each video frame as a discord message)  
`dimensions : w = 70 h = 22 characters 2.57 aspect ratio`  


## usage/commands:
`&frames <ur youtube video link>` -> starts render the video and messages ascii txt back  
`&stop` or `&end` to stop the bot  

## bugs/problems:
- the renderer outputs frames in batches of 5 and the correct framerate and then pauses for a moment (no idea why it does this)
it has something to do with openCV and the way videos are process have I B and P frames or delta frames from whats online  

- youtube-dl breaks with some links and &stop or &end has to be called to 'reset' the bot
somtimes the bot doesnt reset and just stays offline  

fix in progress :purple_heart:  
