import random
import array as arr
from telnetlib import theNULL
import time


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
Y_time=3
class lightTime:
    
        def __init__(self,status,a):
            self.lStatus = status
            self.lTime=a
l=["l1ac","l1bd","l1ca","l1db","l2ac","l2bd","l2ca","l2db","l3ac","l3bd","l3ca","l3db"]         
l1ac=lightTime("Green",30)
l1bd=lightTime("Red",50)     
l1ca=lightTime("Green",30)     
l1db=lightTime("Red",50)             
l2ac=lightTime("Green",30)     
l2bd=lightTime("Red",50)     
l2ca=lightTime("Green",30)     
l2db=lightTime("Red",50)     
l3ac=lightTime("Green",30)     
l3bd=lightTime("Red",50)     
l3ca=lightTime("Green",30)     
l3db=lightTime("Red",50)     

actL = random.randint(0,15)
actM = random.randint(16,25)
actH = random.randint(26,50)
act_preq_threshold = 30


actPreqLane=arr.array('d',[actL,actL,actL,actL,45,10,25,10,actL,actL,actL,actL])
lane=arr.array('i',[0,0,0,0,0,0,0,0,0,0,0,0])
for d in range (0,12):
    print(actPreqLane[d], end=" ")
print("\r")
for i in range(0,12):
    if actPreqLane[i]>act_preq_threshold:
        lane[i]=1
 
    else:
        lane[i]=0
    print(l[i],'=', lane[i], end =" ")
print("\r")
if lane[4]==1 and lane[5]==1 and lane[6]==1 and lane[7]==1:

    if actPreqLane[1]<act_preq_threshold and actPreqLane[3]<act_preq_threshold:
        if l1bd.lStatus == 'Green':
            l1bd.lStatus="Red"
            l1bd.lTime = 50

        if l1db.lStatus == 'Green':
            l1db.lStatus="Red"
            l1bd.lTime = 50

        if l1ac.lStatus == 'Red':
            l1ac.lStatus="Green"
            l1ac.lTime = 30

        if l1ca.lStatus == 'Red':
            l1ca.lStatus="Green"
            l1ca.lTime = 30
        l1ac.lTime=0
        l1ca.lTime=0 
        l1bd.lTime=20
        l1db.lTime=20
        print("luu luong thong khi xay ra tac nghen:")
        print ("lane1ac",actPreqLane[0])
        print ("lane1bd",actPreqLane[1])
        print ("lane1ca",actPreqLane[2])
        print ("lane1db",actPreqLane[3])
        print ("lane2ca",actPreqLane[6])

        if l1ac.lTime==0:
            actPreqLane[0] -=6
            actPreqLane[1] +=6
            actPreqLane[6] -=12
            actPreqLane[3] +=6
        print("Luu luong giao thong sau 30s:")
        print ("lane1ac",actPreqLane[0])
        print ("lane1bd",actPreqLane[1])
        print ("lane1ca",actPreqLane[2])
        print ("lane1db",actPreqLane[3])
        print ("lane2ca",actPreqLane[6])
        a=0
        b=1

        while a < 3 and  actPreqLane[1]<act_preq_threshold and actPreqLane[3]<act_preq_threshold:
            
            if actPreqLane[6]>act_preq_threshold or actPreqLane[6]<25:
                
                l1ac.lTime +=10
                l1ca.lTime +=10
                l1bd.lTime +=10
                l1db.lTime +=10
                print ("l1ac:",l1ac.lStatus,"+",l1ac.lTime,"#",b)               
                b+=1     
                l1ac.lTime -=10
                l1ca.lTime -=10
                l1bd.lTime -=10
                l1db.lTime -=10       
                actPreqLane[0] +=2
                actPreqLane[6] -=4
                actPreqLane[1] +=2
                actPreqLane[3] +=2
                print ("lane1ac",actPreqLane[0])
                print ("lane1bd",actPreqLane[1])
                print ("lane1ca",actPreqLane[2])
                print ("lane1db",actPreqLane[3])
                print ("lane2ca",actPreqLane[6])

            else:
                l1ac.lStatus="Red"
                l1ac.lTime=50
                l1ca.lStatus="Red"
                l1ca.lTime=50
                l1bd.lStatus="Green"
                l1bd.lTime=30
                l1db.lStatus="Green"
                l1db.lTime=30
                print("Sau khi tac duong duoc giai quyet, 2 den tin hieu l2ac va l2ca se chuyen qua mau vang")
                print("Sau khi tin hieu den vang ket thuc, cac tin hieu den cua nga tu nay se tro ve theo cai dat mac dinh")
                print("                  Light 1db:",l1db.lStatus,l1db.lTime)
                print("Light 1ac:",l1ac.lStatus,l1ac.lTime,"                    ","Light1ca: ",l1ca.lStatus,l1ca.lTime)
                print("                  Light 1bd:",l1bd.lStatus,l1bd.lTime)
                break            
            a+=1
##
    if actPreqLane[9]<act_preq_threshold and actPreqLane[11]<act_preq_threshold:
        if l3bd.lStatus == 'Green':
            l3bd.lStatus="Red"
            l3bd.lTime = 50

        if l3db.lStatus == 'Green':
            l3db.lStatus="Red"
            l3bd.lTime = 50

        if l3ac.lStatus == 'Red':
            l3ac.lStatus="Green"
            l3ac.lTime = 30

        if l3ca.lStatus == 'Red':
            l3ca.lStatus="Green"
            l3ca.lTime = 30
        l3ac.lTime=0
        l3ca.lTime=0 
        l3bd.lTime=20
        l3db.lTime=20
        print("luu luong thong khi xay ra tac nghen:")
        print ("lane3ac",actPreqLane[8])
        print ("lane3bd",actPreqLane[9])
        print ("lane3ca",actPreqLane[10])
        print ("lane3db",actPreqLane[11])
        print ("lane2ac",actPreqLane[4])

        if l3ac.lTime==0:
            actPreqLane[4] -=9
            actPreqLane[9] +=3
            actPreqLane[10] -=3
            actPreqLane[11] +=3
        print("Luu luong giao thong sau 30s:")
        print ("lane3ac",actPreqLane[8])
        print ("lane3bd",actPreqLane[9])
        print ("lane3ca",actPreqLane[10])
        print ("lane3db",actPreqLane[11])
        print ("lane2ac",actPreqLane[4])
        a=0
        b=1

        while a < 3 and  actPreqLane[9]<act_preq_threshold and actPreqLane[11]<act_preq_threshold:
            
            if actPreqLane[4]>act_preq_threshold or actPreqLane[4]<25:                
                l3ac.lTime +=10
                l3ca.lTime +=10
                l3bd.lTime +=10
                l3db.lTime +=10
                print ("l3ac:",l3ac.lStatus,"+",l3ac.lTime,"#",b)               
                b+=1     
                l3ac.lTime -=10
                l3ca.lTime -=10
                l3bd.lTime -=10
                l3db.lTime -=10       
                actPreqLane[4] -=4
                actPreqLane[9] +=2
                actPreqLane[10] -=2
                actPreqLane[11] +=2
                print ("lane3ac",actPreqLane[8])
                print ("lane3bd",actPreqLane[9])
                print ("lane3ca",actPreqLane[10])
                print ("lane3db",actPreqLane[11])
                print ("lane2ac",actPreqLane[4])

            else:
                l3ac.lStatus="Red"
                l3ac.lTime=50
                l3ca.lStatus="Red"
                l3ca.lTime=50
                l3bd.lStatus="Green"
                l3bd.lTime=30
                l3db.lStatus="Green"
                l3db.lTime=30
                print("Sau khi tac duong duoc giai quyet, 2 den tin hieu l2ac va l2ca se chuyen qua mau vang")
                print("Sau khi tin hieu den vang ket thuc, cac tin hieu den cua nga tu nay se tro ve theo cai dat mac dinh")
                print("                  Light 3db:",l3db.lStatus,l3db.lTime)
                print("Light 1ac:",l1ac.lStatus,l1ac.lTime,"                    ","Light3ca: ",l3ca.lStatus,l3ca.lTime)
                print("                  Light 3bd:",l3bd.lStatus,l3bd.lTime)
                break            
            a+=1


if lane[0]==1 and lane[4]==1:

    if actPreqLane[5]<act_preq_threshold and actPreqLane[7]<act_preq_threshold:
        if l2bd.lStatus == 'Green':
            l2bd.lStatus="Red"
            l2bd.lTime = 50

        if l2db.lStatus == 'Green':
            l2db.lStatus="Red"
            l2bd.lTime = 50

        if l2ac.lStatus == 'Red':
            l2db.lStatus="Green"
            l2bd.lTime = 30

        if l2ca.lStatus == 'Red':
            l2ca.lStatus="Green"
            l2ca.lTime = 30
        l2ac.lTime=0
        l2ca.lTime=20
        l2bd.lTime=20
        l2db.lTime=20
        print("luu luong thong khi xay ra tac nghen:")
        print ("lane2ac",actPreqLane[4])
        print ("lane2bd",actPreqLane[5])
        print ("lane2ca",actPreqLane[6])
        print ("lane2db",actPreqLane[7])

        if l2ac.lTime==0:
            actPreqLane[4] -=12
            actPreqLane[5] +=6
            actPreqLane[6] -=6
            actPreqLane[7] +=6
        print("Luu luong giao thong sau 30s:")
        print ("lane2ac",actPreqLane[4])
        print ("lane2bd",actPreqLane[5])
        print ("lane2ca",actPreqLane[6])
        print ("lane2db",actPreqLane[7])
        a=0
        b=1

        while a < 3 and  actPreqLane[5]<act_preq_threshold and actPreqLane[7]<act_preq_threshold:
            
            if actPreqLane[4]>act_preq_threshold and actPreqLane[4]<25 :
                
                l2ac.lTime +=10
                l2ca.lTime +=10
                l2bd.lTime +=10
                l2db.lTime +=10
                print ("l2ac:",l2ac.lStatus,"+",l2ac.lTime,"#",b)               
                b+=1     
                l2ac.lTime -=10
                l2ca.lTime -=10
                l2bd.lTime -=10
                l2db.lTime -=10       
                actPreqLane[4] -=4
                actPreqLane[5] +=2
                actPreqLane[6] -=4
                actPreqLane[7] +=2
                print ("lane2ac",actPreqLane[4])
                print ("lane2bd",actPreqLane[5])
                print ("lane2ca",actPreqLane[6])
                print ("lane2db",actPreqLane[7])

            else:
                l2ac.lStatus="Red"
                l2ac.lTime=50
                l2ca.lStatus="Red"
                l2ca.lTime=50
                l2bd.lStatus="Green"
                l2bd.lTime=30
                l2db.lStatus="Green"
                l2db.lTime=30
                print("Sau khi tac duong duoc giai quyet, 2 den tin hieu l2ac va l2ca se chuyen qua mau vang")
                print("Sau khi tin hieu den vang ket thuc, cac tin hieu den cua nga tu nay se tro ve theo cai dat mac dinh")
                print("                  Light 2db:",l2db.lStatus,l2db.lTime)
                print("Light 2ac:",l2ac.lStatus,l2ac.lTime,"                    ","Light2ca: ",l2ca.lStatus,l2ca.lTime)
                print("                  Light 2bd:",l2bd.lStatus,l2bd.lTime)
                break            
            a+=1

###
    if actPreqLane[1]<act_preq_threshold and actPreqLane[3]<act_preq_threshold:
        if l1bd.lStatus == 'Green':
            l1bd.lStatus="Red"
            l1bd.lTime = 50

        if l1db.lStatus == 'Green':
            l1db.lStatus="Red"
            l1bd.lTime = 50

        if l1ac.lStatus == 'Red':
            l1ac.lStatus="Green"
            l1ac.lTime = 30

        if l1ca.lStatus == 'Red':
            l1ca.lStatus="Green"
            l1ca.lTime = 30
        l1ac.lTime=0
        l1ca.lTime=0 
        l1bd.lTime=20
        l1db.lTime=20
        print("luu luong thong khi xay ra tac nghen:")
        print ("lane1ac",actPreqLane[0])
        print ("lane1bd",actPreqLane[1])
        print ("lane1ca",actPreqLane[2])
        print ("lane1db",actPreqLane[3])

        if l1ac.lTime==0:
            actPreqLane[0] -=12
            actPreqLane[1] +=6
            actPreqLane[2] -=6
            actPreqLane[3] +=6
        print("Luu luong giao thong sau 30s:")
        print ("lane1ac",actPreqLane[0])
        print ("lane1bd",actPreqLane[1])
        print ("lane1ca",actPreqLane[2])
        print ("lane1db",actPreqLane[3])
        a=0
        b=1

        while a < 6 and  actPreqLane[1]<act_preq_threshold and actPreqLane[3]<act_preq_threshold:
            
            if actPreqLane[0]>act_preq_threshold or actPreqLane<25:
                
                l1ac.lTime +=10
                l1ca.lTime +=10
                l1bd.lTime +=10
                l1db.lTime +=10
                print ("l1ac:",l1ac.lStatus,"+",l1ac.lTime,"#",b)               
                b+=1     
                l1ac.lTime -=10
                l1ca.lTime -=10
                l1bd.lTime -=10
                l1db.lTime -=10       
                actPreqLane[0] -=4
                actPreqLane[1] +=2
                actPreqLane[2] -=4
                actPreqLane[3] +=2
                print ("lane1ac",actPreqLane[0])
                print ("lane1bd",actPreqLane[1])
                print ("lane1ca",actPreqLane[2])
                print ("lane1db",actPreqLane[3])

            else:
                l1ac.lStatus="Red"
                l1ac.lTime=50
                l1ca.lStatus="Red"
                l1ca.lTime=50
                l1bd.lStatus="Green"
                l1bd.lTime=30
                l1db.lStatus="Green"
                l1db.lTime=30
                print("Sau khi tac duong duoc giai quyet, 2 den tin hieu l2ac va l2ca se chuyen qua mau vang")
                print("Sau khi tin hieu den vang ket thuc, cac tin hieu den cua nga tu nay se tro ve theo cai dat mac dinh")
                print("                  Light 1db:",l1db.lStatus,l1db.lTime)
                print("Light 1ac:",l1ac.lStatus,l1ac.lTime,"                    ","Light1ca: ",l1ca.lStatus,l1ca.lTime)
                print("                  Light 1bd:",l1bd.lStatus,l1bd.lTime)
                break            
            a+=1
       
if lane[4]==1 and lane[0]==0:

    if actPreqLane[5]<act_preq_threshold and actPreqLane[7]<act_preq_threshold:
        if l2bd.lStatus == 'Green':
            l2bd.lStatus="Red"
            l2bd.lTime = 50

        if l2db.lStatus == 'Green':
            l2db.lStatus="Red"
            l2bd.lTime = 50

        if l2ac.lStatus == 'Red':
            l2db.lStatus="Green"
            l2bd.lTime = 30

        if l2ca.lStatus == 'Red':
            l2ca.lStatus="Green"
            l2ca.lTime = 30
        l2ac.lTime=0
        l2ca.lTime=20
        l2bd.lTime=20
        l2db.lTime=20
        print("luu luong thong khi xay ra tac nghen:")
        print ("lane2ac",actPreqLane[4])
        print ("lane2bd",actPreqLane[5])
        print ("lane2ca",actPreqLane[6])
        print ("lane2db",actPreqLane[7])

        if l2ac.lTime==0:
            actPreqLane[4] -=12
            actPreqLane[5] +=6
            actPreqLane[6] -=12
            actPreqLane[7] +=6
        print("Luu luong giao thong sau 30s:")
        print ("lane2ac",actPreqLane[4])
        print ("lane2bd",actPreqLane[5])
        print ("lane2ca",actPreqLane[6])
        print ("lane2db",actPreqLane[7])
        a=0
        b=1

        while a < 6 and  actPreqLane[5]<act_preq_threshold and actPreqLane[7]<act_preq_threshold:
            
            if actPreqLane[4]>act_preq_threshold or actPreqLane[4]>25:
                
                l2ac.lTime +=10
                l2ca.lTime +=10
                l2bd.lTime +=10
                l2db.lTime +=10
                print ("l2ac:",l2ac.lStatus,"+",l2ac.lTime,"#",b)               
                b+=1     
                l2ac.lTime -=10
                l2ca.lTime -=10
                l2bd.lTime -=10
                l2db.lTime -=10       
                actPreqLane[4] -=4
                actPreqLane[5] +=2
                actPreqLane[6] -=4
                actPreqLane[7] +=2
                print ("lane2ac",actPreqLane[4])
                print ("lane2bd",actPreqLane[5])
                print ("lane2ca",actPreqLane[6])
                print ("lane2db",actPreqLane[7])

            else:
                l2ac.lStatus="Red"
                l2ac.lTime=50
                l2ca.lStatus="Red"
                l2ca.lTime=50
                l2bd.lStatus="Green"
                l2bd.lTime=30
                l2db.lStatus="Green"
                l2db.lTime=30
                print("Sau khi tac duong duoc giai quyet, 2 den tin hieu l2ac va l2ca se chuyen qua mau vang")
                print("Sau khi tin hieu den vang ket thuc, cac tin hieu den cua nga tu nay se tro ve theo cai dat mac dinh")
                print("                  Light 2db:",l2db.lStatus,l2db.lTime)
                print("Light 2ac:",l2ac.lStatus,l2ac.lTime,"                    ","Light2ca: ",l2ca.lStatus,l2ca.lTime)
                print("                  Light 2bd:",l2bd.lStatus,l2bd.lTime)
                break            
            a+=1

  



#print (l2bd.lStatus)
#print (l2db.lStatus)
'''b=0
while True:
    if b<20:

        print("                  Light 1db:",l1db.lStatus,l1db.lTime)
        print("Light 1ac:",l1ac.lStatus,l1ac.lTime,"                    ","Light1ca: ",l1ca.lStatus,l1ca.lTime)
        print("                  Light 1bd:",l1bd.lStatus,l1bd.lTime)
        if l1ac.lTime==0 and l1ac.lStatus=='Green':
            l1ac.lStatus="Red"
            l1ac.lTime=50
        if l1ca.lTime==0 and l1ca.lStatus=='Green':
            l1ca.lStatus="Red"
            l1ca.lTime=50
        if l1bd.lTime==0 and l1bd.lStatus=='Red':
            l1bd.lStatus="Green"
            l1bd.lTime=30 
        if l1db.lTime==0 and l1db.lStatus=='Red':
            l1db.lStatus="Green"
            l1db.lTime=30      
        l1db.lTime-=5
        l1ac.lTime-=5
        l1ca.lTime-=5
        l1bd.lTime-=5
        countdown(3)
        b +=1
'''

