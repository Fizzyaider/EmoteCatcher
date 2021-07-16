import re
from urllib.request import Request, urlopen
import http.client
import string
import time

filename = input("Please input the filename of the saved audit log: ")
auditlogfile = open(filename, "r")

emotepattern = r"(?:\"target_id\". )(?P<emoteid>\"\d{18}\")"
namepattern = r"(?:\"old_value\". )(?P<nameid>\"\w+\".)"

websiteurl = "https://cdn.discordapp.com/emojis/"

storedIDs = []
storedNames = []

counter = 0

for line in auditlogfile:
    print(line)
    namematch = re.search(namepattern, line)
    match = re.search(emotepattern, line)
    if namematch:
        print("Succ")
    else:
        print("Not succ")
    if match:
        print("Success")
        print(match.group("emoteid"))
        print(namematch.group("nameid"))
        print(re.findall(emotepattern, line))
        print(re.findall(namepattern, line))
        emotecollection = re.findall(emotepattern, line)
        namecollection = re.findall(namepattern, line)
        newemoteid = r"\d{18}"
        newname = r"\w+"
        for eid in emotecollection:
            supermatch = re.search(newemoteid, eid)
            namesupermatch = re.search(newname, namecollection[counter])
            if supermatch:
                print("Success")
                print(supermatch.group())
                print(namesupermatch.group())
                storedIDs.append(str(supermatch.group()))
                storedNames.append(str(namesupermatch.group()))
                try:
                    connect = websiteurl + storedIDs[counter] + ".gif"
                    req = Request(connect, headers={'User-Agent': 'Mozilla/5.0'})
                    test = urlopen(req)
                    demifile = open(storedNames[counter] + ".gif", "wb")
                    demifile.write(test.read())
                    demifile.close()
                    test.close()
                    time.sleep(2)
                    counter = counter + 1
                except:
                    connect = websiteurl + storedIDs[counter] + ".png"
                    req = Request(connect, headers={'User-Agent': 'Mozilla/5.0'})
                    test = urlopen(req)
                    demifile = open(storedNames[counter] + ".png", "wb")
                    demifile.write(test.read())
                    demifile.close()
                    test.close()
                    time.sleep(2)
                    counter = counter + 1
                    continue
            else:
                print("fail")
                continue
    else:
        continue

auditlogfile.close()
