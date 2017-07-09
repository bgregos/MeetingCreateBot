#!/usr/bin/env python3
"""
Autocreates new meetings weekly on the VTLUUG wiki, when used with cron; and also updates
related calendar pages.

Use -d <YYYY-MM-DD> to use a non-today date for the meeting to be created
or -h for help

Change what gets posted to the meeting and the calendar in
meetingtemplate.txt and calendartemplate.txt
Note: these files are to be written in mediawiki syntax
Also, these files will replace $l (last meeting's date in ISO format),
$d (the meeting being made's date, in ISO format), and
$c (today's date, in ISO format).

Created by Brendan Gregos for VTLUUG
"""

import datetime
from datetime import date
import sys
import getopt

def main(argv):
    mtgdatestr = ''
    try:
        opts, arg = getopt.getopt(argv, "hi:o:", ["mtgdate="])
    except getopt.GetoptError:
        print('./luugmeeting.py -h -d <YYYY-MM-DD>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('./luugmeeting.py (-d <YYYY-MM-DD>)')
            sys.exit()
        elif opt in ("-d", "--mtgdate"):
            mtgdatestr = arg
    if mtgdatestr == '':
        mtgdate = date.today()
    else:
        mtgdate = datetime.datetime.strptime(mtgdatestr, "%Y-%m-%d")

    sys.argv.append('-dir:conf/')
    import pywikibot

    site = pywikibot.Site('VTLUUG', 'VTLUUG')
    print("Updating the VTLUUG wiki")

    #find previous meeting
    prevmeeting = date.today()
    flag = False
    while flag is not True:
        page = pywikibot.Page(site, 'VTLUUG:'+str(prevmeeting))
        if page.exists():
            flag = True #found the previous meeting
        else:
            prevmeeting = prevmeeting - datetime.timedelta(days=1)

    #make new meeting
    page = pywikibot.Page(site, 'VTLUUG:'+date.today().isoformat())
    file = open('conf/meetingtemplate.txt', 'r')
    page.text = file.read()
    page.text = page.text.replace("$d", mtgdate.isoformat())
    page.text = page.text.replace("$l", prevmeeting.isoformat())
    page.text = page.text.replace("$c", date.today().isoformat())
    page.save("Edited by the VTLUUG wikibot.")

    #update calendar page
    page = pywikibot.Page(site, 'Calendar') #set to calendar later
    file = open('conf/calendartemplate.txt', 'r')
    page.text = file.read()
    page.text = page.text.replace("$d", mtgdate.isoformat())
    page.text = page.text.replace("$l", prevmeeting.isoformat())
    page.text = page.text.replace("$c", date.today().isoformat())
    page.save("Edited by the VTLUUG wikibot.")



if __name__ == "__main__":
   main(sys.argv[1:])
