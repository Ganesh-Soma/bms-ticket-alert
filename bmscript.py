from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import smtplib
import time
from collections import OrderedDict
import datetime

venue = {'SPPZ':'Pallazo', 'JACM':'Luxe Cinemas', 'PVVL':'Grand Mall Velachery', 'VRCM':'VR Mall', 'ESMR':'Escape EA', 'TCHT':'S2 Thiruvanmyur', 'STHM':'Satyam'}

site= "https://in.bookmyshow.com/buytickets/doctor-strange-in-the-multiverse-of-madness-chennai/movie-chen-ET00326386-MT/"
date="20220506"

site=site+date
delay=300

email = "bookmyshowbot@gmail.com"
password = "bookmyshowbot12345"

while(True):
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    soup = BeautifulSoup(page, "html.parser")
    soup2=soup.find_all('div', {'data-online': 'Y'})
    line = str(soup2)
    soup3= BeautifulSoup(line, "html.parser")
    soup4=soup3.find_all('a', {'data-venue-code': venue.keys()})
    line1=str(soup4)

    final = []
    for i in venue.keys():
        venue_string = 'data-venue-code="'+i+'"'
        result=re.findall(venue_string,line1)
        if(len(result)>0):
            temp = list(OrderedDict.fromkeys(result))
            result = temp[0][17:21]
            final.append(venue.get(result))
        
    if(len(final)>0):
        print("Bookings Open!!! Page Visited On:" + str(datetime.datetime.now()))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email, password)

        message = "From: BookmyShow <bookmyshowbot@gmail.com>" + "\n" + "To: BookmyShow <bookmyshowbot@gmail.com>" + "\n" + "Subject: Book!! Tickets Available!!!" + "\n"
        
        """From: BookmyShow <bookmyshowbot@gmail.com>
        To: BookmyShow <bookmyshowbot@gmail.com>
        Subject: Book!! Tickets Available!!!
        """
        message = message + "\n" + 'Tickets available for Doctor Strange on May 06, 2022 in theaters: ' + str(final) + '\n'
        s.sendmail(email, email, message)
        print("Email Sent: "+str(datetime.datetime.now()))
        s.quit()
    else:
        print("No Luck. Page Visited On:" + str(datetime.datetime.now()))
    
    time.sleep(delay)
