import re
files = open('\\Users\wwx417681\Files\emails_2.txt','r') #change your file location
files = files.read()
file = files.split()
companys = []
for email in file:
    emails = str(email)
    company = re.findall('@([^ ]*)',emails)
    if company:
        company = str(company)
        company = company[2:-2]
        companys.append(company)
counts = dict()
for ema in companys:
    counts[ema] = counts.get(ema,0) + 1
c = list((v,k) for k,v in counts.items())
c.sort(reverse = True)
for em in c[:100]: #print top 100 email domain
    print(em)
