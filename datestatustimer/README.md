# Date Status Timer
Uses the bot's playing status as a countdown to an event.
## Syntax:
`[p]datestatus <month|day|name>` Commands for setting date for event

`[p]datestatus force_update` Forces an update to the status if it isn't working
properly.
### Notes:
Does not work with rndstatus Cog, so `<p>unload rndstatus` while using this
cog. Once you no longer need it, unload this one and load rndstatus again.

The status only changes when someone sends a message, so the status won't
change if there are no messages being sent in any guild channel that the bot
can read.
### Future Goals For This Cog:
- Not require a user to send message in order to update