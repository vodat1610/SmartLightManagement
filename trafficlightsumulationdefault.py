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
b=0
a=0
while True:
    if b<100:
        if actPreqLane[4]<act_preq_threshold:
            print("#",a)
            break

        if l2ac.lTime==0 and l2ac.lStatus=='Green':
            l2ac.lStatus="Red"
            l2ac.lTime=50
        if l2ca.lTime==0 and l2ca.lStatus=='Green':
            l2ca.lStatus="Red"
            l2ca.lTime=50
        if l2bd.lTime==0 and l2bd.lStatus=='Red':
            l2bd.lStatus="Green"
            l2bd.lTime=30 
        if l2db.lTime==0 and l2db.lStatus=='Red':
            l2db.lStatus="Green"
            l2db.lTime=30
        if l2ac.lTime==0 and l2ac.lStatus=='Red':
            l2ac.lStatus="Green"
            l2ac.lTime=30
        if l2ca.lTime==0 and l2ca.lStatus=='Red':
            l2ca.lStatus="Green"
            l2ca.lTime=30
        if l2bd.lTime==0 and l2bd.lStatus=='Green':
            l2bd.lStatus="Red"
            l2bd.lTime=50 
        if l2db.lTime==0 and l2db.lStatus=='Green':
            l2db.lStatus="Red"
            l2db.lTime=50
        if l2ac.lStatus=='Red':
            actPreqLane[4] +=2
        if l2ac.lStatus=='Green':
            actPreqLane[4] -=4
        if l2bd.lStatus=='Red':
            actPreqLane[5] +=2
        if l2bd.lStatus=='Green':
            actPreqLane[5] -=4
        if l2ca.lStatus=='Red':
            actPreqLane[6] +=2
        if l2ca.lStatus=='Green':
            actPreqLane[6] -=4
        if l2db.lStatus=='Red':
            actPreqLane[7] +=2
        if l2db.lStatus=='Green':
            actPreqLane[7] -=4
        print("                    Light 2db:",l2db.lStatus,l2db.lTime,actPreqLane[7])
        print("\r")
        print("Light 2ac:",l2ac.lStatus,l2ac.lTime,actPreqLane[4],"                    ","Light2ca: ",l2ca.lStatus,l2ca.lTime,actPreqLane[6])
        print("\r")
        print("                    Light 2bd:",l2bd.lStatus,l2bd.lTime,actPreqLane[5])
        l2db.lTime-=10
        l2ac.lTime-=10
        l2ca.lTime-=10
        l2bd.lTime-=10
        b +=1
        a +=1