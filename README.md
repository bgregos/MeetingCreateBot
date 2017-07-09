# MeetingCreateBot
Creates meetings automatically in the VTLUUG wiki.

Written by Brendan Gregos (bgregos) for the Linux and Unix Users Group at Virginia Tech (VTLUUG).

## Installation
1. Download pywikibot if you haven't done so already.
2. You'll also need to download your OS's version of Python 3.
3. Get pywikibot by running `pip3 install pywikibot` or similar.

## Configuration
* `conf/credentials.txt`: Place the password for the wikibot user on the wiki here. I'm not going to include that in the public code for obvious reasons. =) You can also specify a different user to use here, but you must change the name in `user-config.py` as well.
* `conf/meetingtemplate.txt`: This is the template that the bot places into each new meeting. It's formatted in mediawiki syntax, with the exception of the autoreplace symbols defined below.
* `conf/calendartemplate.txt`: This is the template that the bot places into the calendar when it runs. It's formatted in mediawiki syntax, with the exception of the autoreplace symbols defined below.
* `conf/user-config.py`: You shouldn't have to mess with this, but it contains settings for pywikibot. This file will be interesting if you're hacking this to run on a different user or different wiki altogether; the first few settings define username and wiki location.
* Note: If you want this script to run at certain time intervals (ex: making a meeting every week), you must have cron run this script every week. Running this script once will create one meeting.

## Autoreplace Symbols
The following symbols are recognized and replaced in the template files:
* `$c` is replaced by today's date, in ISO format
* `$d` is replaced by the meeting being created's date, in ISO format
* `$l` is replaced by last meeting's date, in ISO format. Note that this value is whenever the most recent meeting found was, it is NOT a one week prior symbol.

## Running
Launch the script with `./luugmeeting.py`. No drama necessary!

You can supply `-d YYYY-MM-DD` when running the script to supply a date to create the meeting, otherwise, today is assumed.

## Contributions/Forking
MeetingCreateBot uses the MIT License. If you want to submit pull requests with features/fixes, you're definitely welcome. Also, feel free to modify this code to suit your needs. The current code shouldn't be too hard to modify to work with your own wiki.
