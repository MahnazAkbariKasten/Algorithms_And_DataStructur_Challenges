from bs4 import BeautifulSoup
import urllib.request
import codecs
webpage = urllib.request.urlopen('https://appexchange.salesforce.com/results?keywords=consultant')
soup = BeautifulSoup(webpage)

# table
table=soup.find('table')

records = [] # store all of the records in this list
for row in table.findAll('tr'):
    col = row.findAll('td')
    if len(col) == 10:
        contestant = row.th.a.string.strip()
        age = col[1].string.strip()
        hometown = col[2].string.strip()[:col[2].string.strip().find(",")]
        state = col[2].string.strip()[col[2].string.strip().find(",")+1:].strip()
        season = col[3].a.string.strip()
        finish = col[4].string.strip()
        tribalChallangeWins = col[5].string.strip()
        indidviduslChallangeWins = col[6].string.strip()
        totalwins = col[7].string.strip()
        daysLasted = col[8].string.strip()
        votesAgainst = col[9].string.strip()
        record = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (contestant,age,hometown,state,season,finish,tribalChallangeWins,indidviduslChallangeWins,totalwins,daysLasted,votesAgainst)
        records.append(record)

f1 = codecs.open('partners.csv','wb','utf8')
#line = ';'.join(records)
#f1.write(line+u'\r\n')

title = 'contestant,age,hometown,state,season,finish,tribal'
f1.write(title+u'\r\n')
for rec in records:
    f1.write(rec+u'\r\n')
f1.close()
