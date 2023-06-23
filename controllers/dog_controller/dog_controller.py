from controller import Robot

robot=Robot()

timestep=320

flag= 0

leg1=robot.getDevice("front_left")
leg2=robot.getDevice("front_right")
leg3=robot.getDevice("back_left")
leg4=robot.getDevice("back_right")

rcvr = robot.getDevice("receiver")
rcvr.enable(timestep)
rcvd_data = 0

def walk(flag):

    if(flag%10==0):
        leg1.setPosition(-0.3)
    elif(flag%10==2):
        leg2.setPosition(-0.3)
    elif(flag%10==4):
        leg4.setPosition(-0.3)
    elif(flag%10==6):
        leg3.setPosition(-0.3)
        

    elif(flag%10==7):
        leg1.setPosition(0.2)
        leg2.setPosition(0.2)
        leg4.setPosition(0.2)
        leg3.setPosition(0.2)
        
def add_delay(num_timestep):
    timecounter = 0
    while robot.step(timestep)!=-1:
        if timeCounter>=num_timestep:
            break
        timeCounter+=1
         
def sit():
    leg_1.setPosition(0)
    leg_2.setPosition(0) 
    leg_3.setPosition(-0.37)    
    leg_4.setPosition(-0.37)     
    add_delay(3)

def stand():
    leg_1.setPosition(0)
    leg_2.setPosition(0)
    leg_3.setPosition(0)
    leg_4.setPosition(0)
    add_delay(3)

while (robot.step(timestep) !=-1):    
    if rcvr.getQueueLength()>0:
        rcvd_data = rcvr.getString()
        print(rcvd_data,type(rcvd_data))
        rcvr.nextPacket()
    
    if rcvd_data=="Sit":
        sit()
        rcvd_data=""
    elif rcvd_data=="Stand":
        stand()
        rcvd_data==""
    elif rcvd_data=="Walk":
        flag = flag+1
        while (flag%13!=0):
            walk(flag)
            flag = flag+1
            add_delay(3)
        rcvd_data = ""                