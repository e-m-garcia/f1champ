from random import *

hCount = 0
bCount = 0
vCount = 0

hPointC = 0
bPointC = 0
vPointC = 0

def lP():
    r = random()
    if r <= 0.35:
        return 12
    elif r <= 0.6:
        return 10
    elif r <= 0.75:
        return 8
    elif r <= 0.85:
        return 6
    elif r <= 0.925:
        return 4
    elif r <= 0.975:
        return 2
    else:
        return 1

for x in range(10000):
    hPoint = 63
    bPoint = 58
    vPoint = 33
    for t in range(14):

        h1 = False
        b1 = False
        v1 = False
        h2 = False
        b2 = False
        v2 = False
        h3 = False
        b3 = False
        v3 = False
        hD = False
        bD = False
        vD = False

        hDProb = random()
        if hDProb <=0.2:
            hD = True
        
        bDProb = random()
        if bDProb <= 0.2:
            bD = True

        vDProb = random()
        if vDProb <= 0.2:
            vD = True
        
        if hD and bD and not vD:
            v1 = True
        
        if hD and vD and not bD:
            b1 = True

        if vD and bD and not hD:
            h1 = True
        
        if hD and not bD and not vD:
            fProb = random()
            if fProb <= (0.35/0.55):
                b1 = True
                v2 = True
            else:
                v1 = True
                b2 = True
        
        if bD and not hD and not vD:
            fProb = random()
            if fProb <= (0.45/0.65):
                h1 = True
                v2 = True
            else:
                v1 = True
                h2 = True

        if vD and not hD and not bD:
            fProb = random()
            if fProb <= (0.45/0.8):
                h1 = True
                b2 = True
            else:
                b1 = True
                h2 = True
        
        if not hD and not bD and not vD:
            fProb = random()
            if fProb <= 0.45:
                h1 = True
            elif fProb <= 0.8:
                b1 = True
            else:
                v1 = True
            if h1:
                sProb = random()
                if sProb <= (0.35/0.55):
                    b2 = True
                else:
                    v2 = True
                if b2:
                    v3 = True
                if v2:
                    b3 = True
            if b1:
                sProb = random()
                if sProb <= (0.45/0.65):
                    h2 = True
                else:
                    v2 = True
                if h2:
                    v3 = True
                if v2:
                    h3 = True
            if v1:
                sProb = random()
                if sProb <= (0.45/0.8):
                    h2 = True
                else:
                    b2 = True
                if h2:
                    b3 = True
                if b2:
                    h3 = True
        #print("Race:", t+4)
        if h1:
            hPoint += 25
            #print("HAM: P1")
        if b1:
            bPoint += 25
            #print("BOT: P1")
        if v1:
            vPoint += 25
            #print("VER: P1")
        if h2:
            hPoint += 18
            #print("HAM: P2")
        if b2:
            bPoint += 18
            #print("BOT: P2")
        if v2:
            vPoint += 18
            #print("VER: P2")
        if h3:
            hPoint += 15
            #print("HAM: P3")
        if b3:
            bPoint += 15
            #print("BOT: P3")
        if v3:
            vPoint += 15
            #print("VER: P3")

        point_table = {12:4,10:5,8:6,6:7,4:8,2:9,1:10}
        point_record = []
        if hD:
            r = random()
            if r <= 0.5:
                add = lP()
                point_record.append(add)
                hPoint += add
                #print("HAM: P", point_table[add])
        
        if bD:
            r = random()
            if r <= 0.5:
                add = lP()
                while add in point_record:
                    add = lP()
                point_record.append(add)
                bPoint += add
                #print("BOT: P", point_table[add])
        if vD:
            r = random()
            if r <= 0.5:
                add = lP()
                while add in point_record:
                    add = lP()
                point_record.append(add)
                vPoint += add
                #print("VER: P", point_table[add])
        
        lapProb = random()
        if lapProb <= 0.25 and not hD:
            hPoint += 1
        elif lapProb <= 0.5 and not bD:
            bPoint += 1
        elif lapProb <= 0.7 and not vD:
            vPoint += 1
        #print()
        #print("HAM:", hPoint)
        #print("BOT:", bPoint)
        #print("VER:", vPoint)
        #print()


    if hPoint > bPoint and hPoint > vPoint:
        hCount += 1
    if vPoint > hPoint and vPoint > bPoint:
        vCount += 1
    if bPoint > hPoint and bPoint > vPoint:
        bCount += 1
    
    hPointC += hPoint
    bPointC += bPoint
    vPointC += vPoint

print("HAM:", hCount/100.0)
print("BOT:", bCount/100.0)
print("VER:", vCount/100.0)
print()
print("HAM avg.:", hPointC/10000.0)
print("BOT avg.:", bPointC/10000.0)
print("VER avg.:", vPointC/10000.0)




    

    
