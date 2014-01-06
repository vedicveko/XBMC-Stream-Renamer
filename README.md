This is a collection of scripts to massage HDHomeRun and USTVNOW streams into a format I find appealing.

Website: <a href=></a>

What you see here is the act of a desperate man who got sick of trying to make XBMC's PVR support work.

When all setup XBMC will have a directory full or playlist files representing your channels/streams. The playlist files will be named after the channel they represent along with the current and next show that is going to play.

Here is a video to show what I mean:

_VIDEO_

Installation is a crazy mess. I didn't expect to release this but I figured at the least the USTVNOW streams will be useful to someone.

I did all of this under openElec. XBMCbuntu works. Other Linux based installs should work. Windows will probably work if you install Python and something similar to CRON.

<b>Prerequisites:</b>
For USTV: Just make sure you have the USTVNOW plugin working. <a href=http://www.xbmchub.com/blog/2013/10/07/how-to-get-started-with-ustvnow-for-xbmc/>XBMC HUB Article About It</a>
For HD Home Run: Make sure its connected to your network and can view some channels. Have hdhomerun_config working. (Part of libhdhomerun: <a href=http://www.silicondust.com/forum2/viewtopic.php?t=1924>Download It</a>

<b>Installation:</b>

<ul>
<li> <a href=https://github.com/vedicveko/XBMC-Stream-Renamer/archive/master.zip>Download this repo.</a> 
<li> Unzip it and copy everything into /storage/dean. If you're the picky sort this is where you begin to change pathnames. For narcissistic reasons I'm going to assume you've put everything in /storage/dean 
<li> Make a directory: /storage/Streams. This is where all your stream files will go. Add that directory as video source in XBMC.
</ul>

<b>USTVNOW Streams</b>
<ul>
<li> Edit /storage/dean/ustvnow_stream_grabber.py and change the email and password variables to your USTVNOW credentials.
<li> Move /storage/dean/ustvnow_stream_grabber.py to the directory your USTVNOW addon resides in. For me its /storage/.xbmc/addons/ustvnow/
<li> Make sure it works by running /storage/dean/ustvnow.sh. After that your should see a bunch of stream files in /storage/Streams. Each file should represent one of your USTVNOW channels.
<li> Add a cron job so that /storage/dean/ustvnow.sh is ran every thirty minutes. Example is /storage/crontab.
</ul>

Go to your stream video source in XBMC. You should be able to play each file in there.  

<b>HD Home Run Streams</b>

