import vrep
import keyboard
from time import sleep
import sys, math
vrep.simxFinish(-1) 
clientID = vrep.simxStart("127.0.0.1", 19997, True, True, 5000, 5)  
KickBoV = 8000
L_KickBoV = (math.pi/180)*KickBoV
R_KickBoV = -(math.pi/180)*KickBoV
pushballv = 100
if clientID!= -1:  
    print('connect successfully')
else:
    print('connect failed')
    vrep.simxFinish(clientID)
print('program ended')

errorCode,Sphere_handle=vrep.simxGetObjectHandle(clientID,'Sphere',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,R3_handle=vrep.simxGetObjectHandle(clientID,'R3',vrep.simx_opmode_oneshot_wait)


if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    
    
     
def start():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
    while True:
        try:
            if keyboard.is_pressed('a'):
                    vrep.simxSetJointTargetVelocity(clientID,R3_handle,L_KickBoV,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('l'):
                    vrep.simxSetJointTargetVelocity(clientID,R2_handle,R_KickBoV,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('DOWN'):
                    vrep.simxSetJointTargetVelocity(clientID,R1_handle,L_KickBoV,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('UP'):
                    vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBoV,vrep.simx_opmode_oneshot_wait)
            else:
                    vrep.simxSetJointTargetVelocity(clientID,R2_handle,L_KickBoV,vrep.simx_opmode_oneshot_wait)
                    vrep.simxSetJointTargetVelocity(clientID,R3_handle,R_KickBoV,vrep.simx_opmode_oneshot_wait)
                    vrep.simxSetJointTargetVelocity(clientID,R1_handle,KickBoV,vrep.simx_opmode_oneshot_wait)
        except:
            break
        
start()