import os
import requests
import time
import phpfetch
srvip = "127.0.0.1:8080"
def disconnect():
    os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=0'")
os.system("curl 'http://" + srvip + "/setinfo.php?turn=1'")
counts = 0
def algor(placeholder, people):
    count = 0
    people = str(people)
    count = str(count)
    print("algor")
    while count <= people:
        #print("0", count)
        count = int(count)
        count = count+1
        count = str(count)
        #print("uno", count)
        #print("people", people)
        people = str(people)
        count = str(count)
        #x = int(x)
        #x = x-1
        #x = str(x)
        #print("dos", count)
        if count > people:
            break
        ba1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a1")
        ba2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a2")
        ba3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a3")
        ba4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a4")
        ba5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a5")
        ba6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a6")
        ba7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a7")
        ba8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a8")
        ba9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a9")
        ba10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/a10")

        bb1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b1")
        bb2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b2")
        bb3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b3")
        bb4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b4")
        bb5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b5")
        bb6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b6")
        bb7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b7")
        bb8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b8")
        bb9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b9")
        bb10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/b10")

        bc1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c1")
        bc2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c2")
        bc3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c3")
        bc4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c4")
        bc5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c5")
        bc6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c6")
        bc7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c7")
        bc8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c8")
        bc9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c9")
        bc10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/c10")

        bd1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d1")
        bd2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d2")
        bd3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d3")
        bd4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d4")
        bd5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d5")
        bd6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d6")
        bd7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d7")
        bd8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d8")
        bd9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d9")
        bd10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/d10")

        be1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e1")
        be2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e2")
        be3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e3")
        be4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e4")
        be5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e5")
        be6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e6")
        be7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e7")
        be8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e8")
        be9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e9")
        be10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/e10")

        bf1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f1")
        bf2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f2")
        bf3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f3")
        bf4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f4")
        bf5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f5")
        bf6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f6")
        bf7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f7")
        bf8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f8")
        bf9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f9")
        bf10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/f10")

        bg1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g1")
        bg2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g2")
        bg3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g3")
        bg4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g4")
        bg5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g5")
        bg6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g6")
        bg7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g7")
        bg8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g8")
        bg9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g9")
        bg10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/g10")

        bh1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h1")
        bh2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h2")
        bh3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h3")
        bh4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h4")
        bh5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h5")
        bh6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h6")
        bh7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h7")
        bh8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h8")
        bh9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h9")
        bh10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/h10")

        bi1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i1")
        bi2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i2")
        bi3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i3")
        bi4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i4")
        bi5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i5")
        bi6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i6")
        bi7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i7")
        bi8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i8")
        bi9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i9")
        bi10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/i10")

        bj1 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j1")
        bj2 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j2")
        bj3 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j3")
        bj4 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j4")
        bj5 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j5")
        bj6 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j6")
        bj7 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j7")
        bj8 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j8")
        bj9 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j9")
        bj10 = phpfetch.getval(srvip, "info/pinfo" + count + "/boardbot/j10")
        iswin = 0

        #a

        if ba1 == "%":
            print("player x is alive a1")
        if ba1 == "X":
            iswin = iswin+1
        if ba2 == "%":
            print("player x is alive a2")
        if ba2 == "X":
            iswin = iswin+1
        if ba3 == "%":
            print("player x is alive a3")
        if ba3 == "X":
            iswin = iswin+1
        if ba4 == "%":
            print("player x is alive a4")
        if ba4 == "X":
            iswin = iswin+1
        if ba5 == "%":
            print("player x is alive a5")
        if ba5 == "X":
            iswin = iswin+1
        if ba6 == "%":
            print("player x is alive a6")
        if ba6 == "X":
            iswin = iswin+1
        if ba7 == "%":
            print("player x is alive a7")
        if ba7 == "X":
            iswin = iswin+1
        if ba8 == "%":
            print("player x is alive a8")
        if ba8 == "X":
            iswin = iswin+1
        if ba9 == "%":
            print("player x is alive a9")
        if ba9 == "X":
            iswin = iswin+1
        if ba10 == "%":
            print("player x is alive a10")
        if ba10 == "X":
            iswin = iswin+1
            
            #a

            #b

        if bb1 == "%":
            print("player x is alive")
        if bb1 == "X":
            iswin = iswin+1
        if bb2 == "%":
            print("player x is alive")
        if bb2 == "X":
            iswin = iswin+1
        if bb3 == "%":
            print("player x is alive")
        if bb3 == "X":
            iswin = iswin+1
        if bb4 == "%":
            print("player x is alive")
        if bb4 == "X":
            iswin = iswin+1
        if bb5 == "%":
            print("player x is alive")
        if bb5 == "X":
            iswin = iswin+1
        if bb6 == "%":
            print("player x is alive")
        if bb6 == "X":
            iswin = iswin+1
        if bb7 == "%":
            print("player x is alive")
        if bb7 == "X":
            iswin = iswin+1
        if bb8 == "%":
            print("player x is alive")
        if bb8 == "X":
            iswin = iswin+1
        if bb9 == "%":
            print("player x is alive")
        if bb9 == "X":
            iswin = iswin+1
        if bb10 == "%":
            print("player x is alive")
        if bb10 == "X":
            iswin = iswin+1
            
            #b

            #c

        if bc1 == "%":
            print("player x is alive")
        if bc1 == "X":
            iswin = iswin+1
        if bc2 == "%":
            print("player x is alive")
        if bc2 == "X":
            iswin = iswin+1
        if bc3 == "%":
            print("player x is alive")
        if bc3 == "X":
            iswin = iswin+1
        if bc4 == "%":
            print("player x is alive")
        if bc4 == "X":
            iswin = iswin+1
        if bc5 == "%":
            print("player x is alive")
        if bc5 == "X":
            iswin = iswin+1
        if bc6 == "%":
            print("player x is alive")
        if bc6 == "X":
            iswin = iswin+1
        if bc7 == "%":
            print("player x is alive")
        if bc7 == "X":
            iswin = iswin+1
        if bc8 == "%":
            print("player x is alive")
        if bc8 == "X":
            iswin = iswin+1
        if bc9 == "%":
            print("player x is alive")
        if bc9 == "X":
            iswin = iswin+1
        if bc10 == "%":
            print("player x is alive")
        if bc10 == "X":
            iswin = iswin+1
            
            #c

            #d

        if bd1 == "%":
            print("player x is alive")
        if bd1 == "X":
            iswin = iswin+1
        if bd2 == "%":
            print("player x is alive")
        if bd2 == "X":
            iswin = iswin+1
        if bd3 == "%":
            print("player x is alive")
        if bd3 == "X":
            iswin = iswin+1
        if bd4 == "%":
            print("player x is alive")
        if bd4 == "X":
            iswin = iswin+1
        if bd5 == "%":
            print("player x is alive")
        if bd5 == "X":
            iswin = iswin+1
        if bd6 == "%":
            print("player x is alive")
        if bd6 == "X":
            iswin = iswin+1
        if bd7 == "%":
            print("player x is alive")
        if bd7 == "X":
            iswin = iswin+1
        if bd8 == "%":
            print("player x is alive")
        if bd8 == "X":
            iswin = iswin+1
        if bd9 == "%":
            print("player x is alive")
        if bd9 == "X":
            iswin = iswin+1
        if bd10 == "%":
            print("player x is alive")
        if bd10 == "X":
            iswin = iswin+1

            #d

            #e

        if be1 == "%":
            print("player x is alive")
        if be1 == "X":
            iswin = iswin+1
        if be2 == "%":
            print("player x is alive")
        if be2 == "X":
            iswin = iswin+1
        if be3 == "%":
            print("player x is alive")
        if be3 == "X":
            iswin = iswin+1
        if be4 == "%":
            print("player x is alive")
        if be4 == "X":
            iswin = iswin+1
        if be5 == "%":
            print("player x is alive")
        if be5 == "X":
            iswin = iswin+1
        if be6 == "%":
            print("player x is alive")
        if be6 == "X":
            iswin = iswin+1
        if be7 == "%":
            print("player x is alive")
        if be7 == "X":
            iswin = iswin+1
        if be8 == "%":
            print("player x is alive")
        if be8 == "X":
            iswin = iswin+1
        if be9 == "%":
            print("player x is alive")
        if be9 == "X":
            iswin = iswin+1
        if be10 == "%":
            print("player x is alive")
        if be10 == "X":
            iswin = iswin+1
         
            #e

            #f

        if bf1 == "%":
            print("player x is alive")
        if bf1 == "X":
            iswin = iswin+1
        if bf2 == "%":
            print("player x is alive")
        if bf2 == "X":
            iswin = iswin+1
        if bf3 == "%":
            print("player x is alive")
        if bf3 == "X":
            iswin = iswin+1
        if bf4 == "%":
            print("player x is alive")
        if bf4 == "X":
            iswin = iswin+1
        if bf5 == "%":
            print("player x is alive")
        if bf5 == "X":
            iswin = iswin+1
        if bf6 == "%":
            print("player x is alive")
        if bf6 == "X":
            iswin = iswin+1
        if bf7 == "%":
            print("player x is alive")
        if bf7 == "X":
            iswin = iswin+1
        if bf8 == "%":
            print("player x is alive")
        if bf8 == "X":
            iswin = iswin+1
        if bf9 == "%":
            print("player x is alive")
        if bf9 == "X":
            iswin = iswin+1
        if bf10 == "%":
            print("player x is alive")
        if bf10 == "X":
            iswin = iswin+1
            
            #f

            #g

        if bg1 == "%":
            print("player x is alive")
        if bg1 == "X":
            iswin = iswin+1
        if bg2 == "%":
            print("player x is alive")
        if bg2 == "X":
            iswin = iswin+1
        if bg3 == "%":
            print("player x is alive")
        if bg3 == "X":
            iswin = iswin+1
        if bg4 == "%":
            print("player x is alive")
        if bg4 == "X":
            iswin = iswin+1
        if bg5 == "%":
            print("player x is alive")
        if bg5 == "X":
            iswin = iswin+1
        if bg6 == "%":
            print("player x is alive")
        if bg6 == "X":
            iswin = iswin+1
        if bg7 == "%":
            print("player x is alive")
        if bg7 == "X":
            iswin = iswin+1
        if bg8 == "%":
            print("player x is alive")
        if bg8 == "X":
            iswin = iswin+1
        if bg9 == "%":
            print("player x is alive")
        if bg9 == "X":
            iswin = iswin+1
        if bg10 == "%":
            print("player x is alive")
        if bg10 == "X":
            iswin = iswin+1
            
            #g

            #h

        if bh1 == "%":
            print("player x is alive")
        if bh1 == "X":
            iswin = iswin+1
        if bh2 == "%":
            print("player x is alive")
        if bh2 == "X":
            iswin = iswin+1
        if bh3 == "%":
            print("player x is alive")
        if bh3 == "X":
            iswin = iswin+1
        if bh4 == "%":
            print("player x is alive")
        if bh4 == "X":
            iswin = iswin+1
        if bh5 == "%":
            print("player x is alive")
        if bh5 == "X":
            iswin = iswin+1
        if bh6 == "%":
            print("player x is alive")
        if bh6 == "X":
            iswin = iswin+1
        if bh7 == "%":
            print("player x is alive")
        if bh7 == "X":
            iswin = iswin+1
        if bh8 == "%":
            print("player x is alive")
        if bh8 == "X":
            iswin = iswin+1
        if bh9 == "%":
            print("player x is alive")
        if bh9 == "X":
            iswin = iswin+1
        if bh10 == "%":
            print("player x is alive")
        if bh10 == "X":
            iswin = iswin+1
            
            #h

            #i

        if bi1 == "%":
            print("player x is alive")
        if bi1 == "X":
            iswin = iswin+1
        if bi2 == "%":
            print("player x is alive")
        if bi2 == "X":
            iswin = iswin+1
        if bi3 == "%":
            print("player x is alive")
        if bi3 == "X":
            iswin = iswin+1
        if bi4 == "%":
            print("player x is alive")
        if bi4 == "X":
            iswin = iswin+1
        if bi5 == "%":
            print("player x is alive")
        if bi5 == "X":
            iswin = iswin+1
        if bi6 == "%":
            print("player x is alive")
        if bi6 == "X":
            iswin = iswin+1
        if bi7 == "%":
            print("player x is alive")
        if bi7 == "X":
            iswin = iswin+1
        if bi8 == "%":
            print("player x is alive")
        if bi8 == "X":
            iswin = iswin+1
        if bi9 == "%":
            print("player x is alive")
        if bi9 == "X":
            iswin = iswin+1
        if bi10 == "%":
            print("player x is alive")
        if bi10 == "X":
            iswin = iswin+1
            
            #i

            #j

        if bj1 == "%":
            print("player x is alive")
        if bj1 == "X":
            iswin = iswin+1
        if bj2 == "%":
            print("player x is alive")
        if bj2 == "X":
            iswin = iswin+1
        if bj3 == "%":
            print("player x is alive")
        if bj3 == "X":
            iswin = iswin+1
        if bj4 == "%":
            print("player x is alive")
        if bj4 == "X":
            iswin = iswin+1
        if bj5 == "%":
            print("player x is alive")
        if bj5 == "X":
            iswin = iswin+1
        if bj6 == "%":
            print("player x is alive")
        if bj6 == "X":
            iswin = iswin+1
        if bj7 == "%":
            print("player x is alive")
        if bj7 == "X":
            iswin = iswin+1
        if bj8 == "%":
            print("player x is alive")
        if bj8 == "X":
            iswin = iswin+1
        if bj9 == "%":
            print("player x is alive")
        if bj9 == "X":
            iswin = iswin+1
        if bj10 == "%":
            print("player x is alive")
        if bj10 == "X":
            iswin = iswin+1

            #j
        print(iswin)
        if iswin == 17:
            phpfetch.setval(srvip, "setinfo.php?trdy=0&client=" + count)
            print("Player " + count + "is ded")
            phpfetch.setval(srvip, "setinfo.php?ded=1&client=" + count)
        if iswin != 17:
            phpfetch.setval(srvip, "setinfo.php?trdy=1&client=" + count)
            print("Player " + count + "is alive")
        win = phpfetch.getval(srvip, "info/pinfo" + count + "/win")
        if win == 0:
            phpfetch.setval(srvip, "setinfo.php?ded=1&client=" + count)
os.system("curl 'http://" + srvip + "/addclient.php?client=1&connect=1'")
people = int(input("How many people are there:"))
count = 0
peoplelst = []
listgo = 0
while listgo == 0:
    count = count+1
    peoplelst.append(count)
    if count == people:
        listgo = 1
people = str(people)
phpfetch.setval(srvip, "addclient.php?ammountofclients='" + people + "'")
for x in peoplelst:
    xp = x+1
    print(x)
    x = str(x)
    if xp != people:
        cl2con = "0"
        while cl2con == "0":
            time.sleep(1)
            res = requests.get("http://" + srvip + "/connect/p" + x)
            if res.status_code == 200:
                p2 = int(res.text)
                if p2 == 1:
                    cl2con = "1"
phpfetch.setval(srvip, "setinfo.php?all=1")
phpfetch.setval(srvip, "addclient.php?clientdatafoldernumber=1")
peoplestr = phpfetch.listToString(peoplelst)
phpfetch.setval(srvip, "setinfo.php?in=" + peoplestr)
phpfetch.setval(srvip, "setinfo.php?out=_")
clients = phpfetch.getval(srvip, "connect/clients")
clients = int(clients)
waow = 200*clients
print("Hold on while I set ", waow, " variabels in the server this may take a while...")
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=top&pos=j" + countstr)

##

count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=a" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=b" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=c" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=d" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=e" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=f" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=g" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=h" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=i" + countstr)
count = 0
while count != 10:
    count = count+1
    countstr = str(count)
    phpfetch.setval(srvip, "setinfo.php?val=.&client=1&board=bot&pos=j" + countstr)

print("Done!")

print("Time to set your ships! Here is the current board. Give me a minute i need to get all those variables again....")

ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#Destroyer

Destroyerstr = str(input("Where would you like your 'Destroyer' ship? It takes up 2 spaces.  "))
Destroyerlst = phpfetch.convert(Destroyerstr)
Destroyerlet = Destroyerlst[0]
Destroyernum = Destroyerlst[1]
phpfetch.setval(srvip, "setinfo.php?shpded=0&client=1&shpnm=destroy&shprnm=destroy")
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + Destroyerlet + Destroyernum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + Destroyerlet + Destroyernum + "&client=1&shpnm=pos1&shprnm=destroy")
Destroyernum = int(Destroyernum)
Destroyernum = Destroyernum-1
Destroyernum = str(Destroyernum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + Destroyerlet + Destroyernum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + Destroyerlet + Destroyernum + "&client=1&shpnm=pos2&shprnm=destroy")

ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#Destroyer

#sub

substr = str(input("Where would you like your 'Submarine' ship? It takes up 3 spaces.  "))
sublst = phpfetch.convert(substr)
sublet = sublst[0]
subnum = sublst[1]
phpfetch.setval(srvip, "setinfo.php?shpded=0&client=1&shpnm=sub&shprnm=sub")
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + sublet + subnum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + sublet + subnum + "&client=1&shpnm=pos1&shprnm=sub")
subnum = int(subnum)
subnum = subnum-1
subnum = str(subnum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + sublet + subnum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + sublet + subnum + "&client=1&shpnm=pos2&shprnm=sub")
subnum = int(subnum)
subnum = subnum-1
subnum = str(subnum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + sublet + subnum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + sublet + subnum + "&client=1&shpnm=pos3&shprnm=sub")

ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#sub

#battle

battlestr = str(input("Where would you like your 'Battleship' ship? It takes up 4 spaces.  "))
battlelst = phpfetch.convert(battlestr)
battlelet = battlelst[0]
battlenum = battlelst[1]
phpfetch.setval(srvip, "setinfo.php?shpded=0&client=1&shpnm=battle&shprnm=battle")
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + battlelet + battlenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + battlelet + battlenum + "&client=1&shpnm=pos1&shprnm=battle")
battlenum = int(battlenum)
battlenum = battlenum-1
battlenum = str(battlenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + battlelet + battlenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + battlelet + battlenum + "&client=1&shpnm=pos2&shprnm=battle")
battlenum = int(battlenum)
battlenum = battlenum-1
battlenum = str(battlenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + battlelet + battlenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + battlelet + battlenum + "&client=1&shpnm=pos3&shprnm=battle")
battlenum = int(battlenum)
battlenum = battlenum-1
battlenum = str(battlenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + battlelet + battlenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + battlelet + battlenum + "&client=1&shpnm=pos4&shprnm=battle")

ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#battle

#care

carestr = str(input("Where would you like your 'Carrier' ship? It takes up 5 spaces.  "))
carelst = phpfetch.convert(carestr)
carelet = carelst[0]
carenum = carelst[1]
phpfetch.setval(srvip, "setinfo.php?shpded=0&client=1&shpnm=care&shprnm=care")
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + carelet + carenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + carelet + carenum + "&client=1&shpnm=pos1&shprnm=care")
carenum = int(carenum)
carenum = carenum-1
carenum = str(carenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + carelet + carenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + carelet + carenum + "&client=1&shpnm=pos1&shprnm=care")
carenum = int(carenum)
carenum = carenum-1
carenum = str(carenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + carelet + carenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + carelet + carenum + "&client=1&shpnm=pos1&shprnm=care")
carenum = int(carenum)
carenum = carenum-1
carenum = str(carenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + carelet + carenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + carelet + carenum + "&client=1&shpnm=pos1&shprnm=care")
carenum = int(carenum)
carenum = carenum-1
carenum = str(carenum)
carenum = str(carenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + carelet + carenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + carelet + carenum + "&client=1&shpnm=pos1&shprnm=care")

ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#care



crusestr = str(input("Where would you like your 'Cruser' ship? It takes up 3 spaces.  "))
cruselst = phpfetch.convert(crusestr)
cruselet = cruselst[0]
crusenum = cruselst[1]
phpfetch.setval(srvip, "setinfo.php?shpded=0&client=1&shpnm=cruse&shprnm=cruse")
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + cruselet + crusenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + cruselet + crusenum + "&client=1&shpnm=pos1&shprnm=cruse")
crusenum = int(crusenum)
crusenum = crusenum-1
crusenum = str(crusenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + cruselet + crusenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + cruselet + crusenum + "&client=1&shpnm=pos2&shprnm=cruse")
crusenum = int(crusenum)
crusenum = crusenum-1
crusenum = str(crusenum)
phpfetch.setval(srvip, "setinfo.php?val=%&client=1&board=bot&pos=" + cruselet + crusenum)
phpfetch.setval(srvip, "setinfo.php?shpded=" + cruselet + crusenum + "&client=1&shpnm=pos3&shprnm=cruse")


ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

########

ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


print("Done! Here is the current top board...")
topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
print(topboard)
print("The bottom board")
print(botboard)

#care


game = 1
turn = 2
os.system("clear")
phpfetch.setval(srvip, "setinfo.php?ded=0&client=1")
while game == 1:
    ta1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a1")
    ta2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a2")
    ta3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a3")
    ta4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a4")
    ta5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a5")
    ta6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a6")
    ta7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a7")
    ta8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a8")
    ta9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a9")
    ta10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/a10")

    tb1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b1")
    tb2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b2")
    tb3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b3")
    tb4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b4")
    tb5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b5")
    tb6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b6")
    tb7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b7")
    tb8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b8")
    tb9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b9")
    tb10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/b10")

    tc1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c1")
    tc2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c2")
    tc3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c3")
    tc4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c4")
    tc5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c5")
    tc6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c6")
    tc7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c7")
    tc8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c8")
    tc9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c9")
    tc10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/c10")

    td1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d1")
    td2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d2")
    td3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d3")
    td4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d4")
    td5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d5")
    td6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d6")
    td7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d7")
    td8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d8")
    td9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d9")
    td10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/d10")

    te1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e1")
    te2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e2")
    te3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e3")
    te4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e4")
    te5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e5")
    te6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e6")
    te7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e7")
    te8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e8")
    te9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e9")
    te10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/e10")

    tf1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f1")
    tf2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f2")
    tf3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f3")
    tf4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f4")
    tf5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f5")
    tf6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f6")
    tf7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f7")
    tf8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f8")
    tf9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f9")
    tf10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/f10")

    tg1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g1")
    tg2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g2")
    tg3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g3")
    tg4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g4")
    tg5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g5")
    tg6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g6")
    tg7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g7")
    tg8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g8")
    tg9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g9")
    tg10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/g10")

    th1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h1")
    th2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h2")
    th3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h3")
    th4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h4")
    th5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h5")
    th6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h6")
    th7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h7")
    th8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h8")
    th9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h9")
    th10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/h10")

    ti1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i1")
    ti2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i2")
    ti3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i3")
    ti4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i4")
    ti5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i5")
    ti6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i6")
    ti7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i7")
    ti8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i8")
    ti9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i9")
    ti10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/i10")

    tj1 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j1")
    tj2 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j2")
    tj3 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j3")
    tj4 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j4")
    tj5 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j5")
    tj6 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j6")
    tj7 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j7")
    tj8 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j8")
    tj9 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j9")
    tj10 = phpfetch.getval(srvip, "info/pinfo1/boardtop/j10")

    ########

    ba1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a1")
    ba2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a2")
    ba3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a3")
    ba4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a4")
    ba5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a5")
    ba6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a6")
    ba7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a7")
    ba8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a8")
    ba9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a9")
    ba10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/a10")

    bb1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b1")
    bb2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b2")
    bb3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b3")
    bb4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b4")
    bb5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b5")
    bb6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b6")
    bb7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b7")
    bb8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b8")
    bb9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b9")
    bb10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/b10")

    bc1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c1")
    bc2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c2")
    bc3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c3")
    bc4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c4")
    bc5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c5")
    bc6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c6")
    bc7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c7")
    bc8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c8")
    bc9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c9")
    bc10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/c10")

    bd1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d1")
    bd2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d2")
    bd3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d3")
    bd4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d4")
    bd5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d5")
    bd6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d6")
    bd7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d7")
    bd8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d8")
    bd9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d9")
    bd10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/d10")

    be1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e1")
    be2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e2")
    be3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e3")
    be4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e4")
    be5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e5")
    be6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e6")
    be7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e7")
    be8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e8")
    be9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e9")
    be10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/e10")

    bf1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f1")
    bf2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f2")
    bf3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f3")
    bf4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f4")
    bf5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f5")
    bf6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f6")
    bf7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f7")
    bf8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f8")
    bf9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f9")
    bf10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/f10")

    bg1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g1")
    bg2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g2")
    bg3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g3")
    bg4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g4")
    bg5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g5")
    bg6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g6")
    bg7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g7")
    bg8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g8")
    bg9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g9")
    bg10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/g10")

    bh1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h1")
    bh2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h2")
    bh3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h3")
    bh4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h4")
    bh5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h5")
    bh6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h6")
    bh7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h7")
    bh8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h8")
    bh9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h9")
    bh10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/h10")

    bi1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i1")
    bi2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i2")
    bi3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i3")
    bi4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i4")
    bi5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i5")
    bi6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i6")
    bi7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i7")
    bi8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i8")
    bi9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i9")
    bi10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/i10")

    bj1 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j1")
    bj2 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j2")
    bj3 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j3")
    bj4 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j4")
    bj5 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j5")
    bj6 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j6")
    bj7 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j7")
    bj8 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j8")
    bj9 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j9")
    bj10 = phpfetch.getval(srvip, "info/pinfo1/boardbot/j10")


    print("Done! Here is the current top board...")
    topboard = phpfetch.getboard(ta1, ta2, ta3, ta4, ta5, ta6, ta7, ta8, ta9, ta10, tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, td1, td2, td3, td4, td5, td6, td7, td8, td9, td10, te1, te2, te3, te4, te5, te6, te7, te8, te9, te10, tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tg1, tg2, tg3, tg4, tg5, tg6, tg7, tg8, tg9, tg10, th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, ti1, ti2, ti3, ti4, ti5, ti6, ti7, ti8, ti9, ti10, tj1, tj2, tj3, tj4, tj5, tj6, tj7, tj8, tj9, tj10, )
    botboard = phpfetch.getboard(ba1, ba2, ba3, ba4, ba5, ba6, ba7, ba8, ba9, ba10, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, bb10, bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, be1, be2, be3, be4, be5, be6, be7, be8, be9, be10, bf1, bf2, bf3, bf4, bf5, bf6, bf7, bf8, bf9, bf10, bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bh1, bh2, bh3, bh4, bh5, bh6, bh7, bh8, bh9, bh10, bi1, bi2, bi3, bi4, bi5, bi6, bi7, bi8, bi9, bi10, bj1, bj2, bj3, bj4, bj5, bj6, bj7, bj8, bj9, bj10, )
    print(topboard)
    print("The bottom board")
    print(botboard)
    ded = phpfetch.getval(srvip, "info/pinfo1/ded")
    turnstr = phpfetch.getval(srvip, "connect/in")
    turnlst = phpfetch.convert(turnstr)
    if ded == 1:
        game = 0
        turnlst.remove(1)
        break
    time.sleep(2)
    print("Clients connected!")
    while turn != 1:

        time.sleep(1)
        res = requests.get("http://" + srvip + "/info/turn")
        if res.status_code == 200:
            turn = int(res.text)
            if turn == 1:
                print("Your turn!")
    choicestr = str(input("Where would you like to attempt a hit?"))
    choicestr.lower()
    choicelst = phpfetch.convert(choicestr)
    choicelet = choicelst[0]
    choicenum = choicelst[1]
    doihit = 0
    while doihit != 1:
        for x in peoplelst:
            xp = x+1
            print("x" ,x)
            print("xp", xp)
            x = str(x)
            xp = str(xp)
            people = str(people)
            if xp == "1":
                print("no")
            else:
                if xp != people:
                    choicestr = str(choicestr)
                    xp = str(xp)
                    doihitpeople = phpfetch.getval(srvip, "info/pinfo" + x + "/boardbot/" + choicestr + "")
                    if doihitpeople == "%":
                        doihit = 1
                        personhit = x
                        personhit = str(personhit)
                        phpfetch.setval(srvip, "setinfo.php?val=X&client=" + personhit + "&pos=" + choicestr + "&board=bot")
            if xp == people:
                doihit = 1
    #os.system("curl 'http://" + srvip + "/setinfo.php?client=1&move=" + p1mv + "'")
    algor(counts, people)
    turnstr = phpfetch.getval(srvip, "connect/in")
    turnlst = phpfetch.convert(turnstr)
    goturn = turnlst[1]
    phpfetch.setval(srvip, "setinfo.php?turn=" + goturn)
    #os.system("curl 'http://" + srvip + "/index.php?clean=2'")
    #os.system("clear")
    turn = 2