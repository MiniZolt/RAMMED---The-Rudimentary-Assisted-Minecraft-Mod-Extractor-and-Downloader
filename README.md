# RAMMED---The-Rudimentary-Assisted-Minecraft-Mod-Extractor-and-Downloader
**Very early alpha build, for offline LAN use only!
This is RAMMED, or Rudimentary Minecraft Mod Extractor and Downloader. 

This project was born out of an oddly niche need - multi-os Minecraft LAN parties. Since I started
attending university, I made a small friendgroup of fellow cybersecurity majors and computer science majors
of varying technical skill levels. We started to have the occasional Minecraft LAN party, using a little 
GLi.Net router on OpenWRT as our connection medium. We'd all connect to the wifi, and then share our mods
with a pen drive before joining whomever was hosting the server and playing. 

The issue however, was that we'd share mods by using a thumb drive - and there were a lot of mods.
So, we ran into the issue of half of us being on Linux, and the other half on Windows. See the issue?
In case you don't, whenever you read/write files on either Linux or Windows with thumbdrives, the data can 
get messed up between machines. It gets messy and difficult to share files via a thumbdrive when you have mixed
operating systems, so I devised this "solution".

A few quick notes:

This script uses a modified version of netutils tcp ping function. It has a modified timeout which accepts float
data types instead of int data types. Full credit for the ping function goes to the netutil creators for this.

This script has some fairly obvious security flaws. DO NOT EVER RUN THIS SCRIPT ON A PUBLIC NETWORK, AND DO NOT 
PORT FORWARD THE SERVER. Keep this for private, offline LAN use for the intended purposes of the script.
If this is used to abuse or damage systems in a non-authorized malicious manner, note I had no 
part of it, I do not authorize such behavior, and that any and all damages incurred are at the liability of the user.
You have been warned.

INSTALL INSTRUCTIONS: 

This program is in very, very early stages so it's a bit inefficient to install. First, download the py file 
and copy the path to where you saved it. Open your terminal and run:
python /The/Path/You/Copied/RAMMED.py
That's it!

RAMMED provides a few very, very simple functions. I'll go over how to use each one. 

USE INSTRUCTIONS FOR INSTALLER

In this version, 0.0.2, the modfolder is now found automatically. If you have multiple instances,
then it'll let you choose which one you want to install your mods to. Select one from the list,
and thats it! When you first run it, it will manually scan for whomever is serving their mod folder, 
and then save their address to a cache for when you go to download mods again. If they go offline, or 
aren't serving their folder, it will manually scan again and add that new host to the cache as well. 
Otherwise, this runs fairly quick after the first install! Be careful, if you run installer on a 
folder that already has mods in it, it will overwrite anything with the same name!

USE INSTRUCTIONS FOR LISTER

The list function... lists the files in your modfolder (well, actually only .jar/.zip/.disabled but whatever).
Same thing as the installer, just pick your insance (if you have multiple). This is somewhat useful to quickly compare 
folders with your lan mates while you already have the path copied. Is it redundant? Yeah. Is it kind of 
silly to have in here? Yeah. Did I still add it? Yeah, because it was fun and I'm learning. Womp womp. 

USE INSTRUCTIONS FOR DELETER

The delete function is a quick way to nuke your mod folder before downloading new ones. Again, same story as above.
If you have multiple instances, just pick the right one and double check it in the confirmation before you nuke
the folder. 

USE INSTRUCTIONS FOR SERVER

The server function also only requires you to pick your instance. It will let you share your mod folder
so that fellow LAN mates can download your mod folder. This shares your modfolder, and only your modfolder - you
won't have to worry about someone snooping around for your sensitive stuff. It also wont share resource packs or 
shaders however, since they're client side and aren't required to run. 

That's it! I will update it with random bits and bobs here and there. Enjoy.

