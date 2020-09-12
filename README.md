# mlb-broadcast

Requirements to use: 
1. A streaming service (HDHomeRun, IPTV service, or other) that requires no authentication outside of the URL path
2. A network stream that can play in VLC

This is a script that can be set to auto-run on boot. It will parse the MLB API broadcast schedule for the network that your team is on and then automatically tune into the link you provide. This would require something like an HDHomeRun or IPTV service where you can enter a direct play link per network.

This built for the 2019 World Series Champion Washington Nationals, but it can be used for any team, provided that you change your team name in the script, you provide the network name for your service, and that you can provide the links.

This proof of concepts works well on a Raspberry Pi 3 and higher with a systemd service to start the program on boot.
